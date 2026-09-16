"""Turn Recraft V4.1 vector output (white silhouette + gold lines on a gold background)
into brand assets.

usage: process_botanicals.py <id> [<id> ...]      ids = files in assets/botanicals/src/<id>.svg

For each id:
  assets/botanicals/<id>.svg                 cleaned silhouette: no metadata, no background,
                                             fills snapped to #fff / #D4AF37, gold lines kept
  docs/design/samples/botanicals-sprite.svg  <symbol id="sil-<id>"> for every id and
                                             <clipPath id="m-<id>" clipPathUnits="objectBoundingBox">
                                             built from the OUTER outline (holes filled) so photos
                                             can be masked to the real object shape
Outline extraction: the cleaned SVG is rasterised by headless Chrome, thresholded, flood-filled
from the corners, traced with potrace, and the path normalised to 0..1.
No XML parser is used on the untrusted SVG text; everything is regex over known Recraft output.
"""
import os, re, sys, pathlib, subprocess, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = pathlib.Path(__file__).resolve().parents[3]
SRC, OUT = ROOT / "assets/botanicals/src", ROOT / "assets/botanicals"
SPRITE = ROOT / "docs/design/samples/botanicals-sprite.svg"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
GOLD, WHITE = "#D4AF37", "#ffffff"

def rgb_to_hex(m):
    r, g, b = (int(v) for v in m.groups())
    return f'fill="{WHITE}"' if (r + g + b) / 3 > 200 else f'fill="{GOLD}"'

def clean(svg: str):
    """Return (cleaned svg text, width, height). Drops metadata and the full-frame background."""
    svg = re.sub(r"<metadata>.*?</metadata>", "", svg, flags=re.S)
    svg = re.sub(r'\s+xmlns:c2pa="[^"]*"', "", svg)
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg); w, h = float(m[1]), float(m[2])
    # background = a path/rect whose bbox covers the whole frame; Recraft emits it first
    def is_bg(tag):
        d = re.search(r'\sd="([^"]+)"', tag)
        if d:
            nums = [float(x) for x in re.findall(r"-?\d*\.?\d+", d[1])]
            xs, ys = nums[0::2], nums[1::2]
            return xs and ys and min(xs) <= 1 and min(ys) <= 1 and max(xs) >= w - 1 and max(ys) >= h - 1
        return bool(re.search(r"<rect", tag))
    svg = re.sub(r"<(?:path|rect)\b[^>]*/>", lambda t: "" if is_bg(t.group(0)) else t.group(0), svg)
    svg = re.sub(r'fill="rgb\((\d+),\s*(\d+),\s*(\d+)\)"', rgb_to_hex, svg)
    svg = re.sub(r'\s(?:style|width|height|preserveAspectRatio)="[^"]*"', "", svg, count=4)
    return svg, w, h

def inner(svg: str) -> str:
    return re.sub(r"^.*?<svg[^>]*>|</svg>\s*$", "", svg, flags=re.S).strip()

def rasterise(svg_path: pathlib.Path, w: float, h: float, px=1600) -> Image.Image:
    scale = px / w; W, H = int(round(w * scale)), int(round(h * scale))
    html = f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:#000}}svg{{display:block;width:{W}px;height:{H}px}}</style>{svg_path.read_text(encoding="utf8")}'
    with tempfile.TemporaryDirectory() as td:
        hp = pathlib.Path(td) / "r.html"; hp.write_text(html, encoding="utf8"); png = pathlib.Path(td) / "r.png"
        subprocess.run(["perl", "-e", "alarm 25; exec @ARGV", CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
                        f"--user-data-dir={td}/p", "--virtual-time-budget=1500", f"--window-size={W},{H}", f"--screenshot={png}", hp.as_uri()],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["pkill", "-f", "Google Chrome.*--headless"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return Image.open(png).convert("L").copy()

def outer_outline(img: Image.Image) -> str:
    """Threshold the raster (object is white or gold on black), fill interior holes, trace with potrace."""
    a = np.asarray(img); obj = (a > 40).astype(np.uint8) * 255          # anything not black = object
    im = Image.fromarray(obj).filter(ImageFilter.MaxFilter(11)).filter(ImageFilter.MinFilter(11))   # closing: seal vein slits that reach the margin
    filled = im.copy(); ImageDraw.floodfill(filled, (0, 0), 128)
    for xy in ((im.width - 1, 0), (0, im.height - 1), (im.width - 1, im.height - 1)):
        if filled.getpixel(xy) == 0: ImageDraw.floodfill(filled, xy, 128)
    obj2 = filled.point(lambda v: 0 if v == 128 else 255)              # everything not reachable from outside
    with tempfile.TemporaryDirectory() as td:
        pbm = pathlib.Path(td) / "o.pbm"; obj2.point(lambda v: 255 - v).convert("1").save(pbm)   # potrace traces black
        svg = subprocess.run(["potrace", str(pbm), "-s", "-o", "-", "--flat", "-t", "40", "-a", "1.2", "-O", "0.5"],
                             check=True, capture_output=True, text=True).stdout
    tf = re.search(r'transform="([^"]+)"', svg); d = " ".join(re.findall(r'<path d="([^"]+)"', svg, flags=re.S))
    return normalise(d, tf[1] if tf else "", im.width, im.height)

def normalise(d, tf, w, h):
    tx, ty, sx, sy = 0.0, 0.0, 1.0, 1.0
    if m := re.search(r"translate\(([-\d.]+),([-\d.]+)\)", tf): tx, ty = float(m[1]), float(m[2])
    if m := re.search(r"scale\(([-\d.]+),([-\d.]+)\)", tf): sx, sy = float(m[1]), float(m[2])
    toks = re.findall(r"[MmLlCcZz]|-?\d*\.?\d+", d); out = []; i = 0; cmd = None; x = y = 0.0
    P = lambda px, py: f"{(tx + px * sx) / w:.4f},{(ty + py * sy) / h:.4f}"
    while i < len(toks):
        t = toks[i]
        if t.isalpha():
            cmd = t; i += 1
            if cmd in "Zz": out.append("Z"); cmd = None
            continue
        if cmd is None: cmd = "l"
        if cmd in "Mm":
            nx, ny = float(toks[i]), float(toks[i + 1]); i += 2
            if cmd == "m": nx, ny = x + nx, y + ny
            x, y = nx, ny; out.append("M" + P(x, y)); cmd = "l" if cmd == "m" else "L"
        elif cmd in "Ll":
            nx, ny = float(toks[i]), float(toks[i + 1]); i += 2
            if cmd == "l": nx, ny = x + nx, y + ny
            x, y = nx, ny; out.append("L" + P(x, y))
        elif cmd in "Cc":
            c = [float(toks[i + k]) for k in range(6)]; i += 6
            if cmd == "c": c = [c[0] + x, c[1] + y, c[2] + x, c[3] + y, c[4] + x, c[5] + y]
            out.append("C" + P(c[0], c[1]) + " " + P(c[2], c[3]) + " " + P(c[4], c[5])); x, y = c[4], c[5]
        else: i += 1
    return "".join(out)

def main(ids):
    OUT.mkdir(parents=True, exist_ok=True)
    existing = SPRITE.read_text(encoding="utf8") if SPRITE.exists() else ""
    blocks = dict(re.findall(r'<(?:symbol|clipPath) id="((?:sil|m)-[^"]+)".*?</(?:symbol|clipPath)>', existing, flags=re.S) and
                  [(m.group(1), m.group(0)) for m in re.finditer(r'<(?:symbol|clipPath) id="((?:sil|m)-[^"]+)".*?</(?:symbol|clipPath)>', existing, flags=re.S)])
    for i in ids:
        svg, w, h = clean((SRC / f"{i}.svg").read_text(encoding="utf8"))
        cleaned = OUT / f"{i}.svg"; cleaned.write_text(svg, encoding="utf8")
        blocks[f"sil-{i}"] = f'<symbol id="sil-{i}" viewBox="0 0 {w:g} {h:g}">{inner(svg)}</symbol>'
        d = outer_outline(rasterise(cleaned, w, h))
        blocks[f"m-{i}"] = f'<clipPath id="m-{i}" clipPathUnits="objectBoundingBox"><path d="{d}"/></clipPath>'
        print(f"{i}: {w:g}x{h:g}, cleaned {cleaned.stat().st_size} B, mask path {len(d)} chars")
    SPRITE.write_text("\n".join(blocks[k] for k in sorted(blocks)), encoding="utf8")
    print("sprite", SPRITE.stat().st_size, "bytes,", len(blocks), "blocks")

if __name__ == "__main__":
    main(sys.argv[1:] or [p.stem for p in SRC.glob("*.svg")])
