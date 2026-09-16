# Botanical Assets, Product Shapes and Motion — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the hand-generated botanicals with botanically accurate, AI-generated white silhouettes (one object per product, plus background motifs), derive the photo masks from those real outlines, attach leaves to the vines, and add scroll-driven motion so the Phase 1 specimen reads as an award-level page.

**Architecture:** Recraft V4.1 (vector mode) generates white silhouettes with gold interior lines on a gold background and returns real SVG; a Python post-processor strips metadata and the background, snaps fills to exactly white and gold, and derives a normalised `clipPath` (outer outline) for photo masks by rasterising the silhouette and tracing it with potrace. The specimen consumes the sprite; a small motion script drives reveals, parallax, stroke-draw and vine-leaf attachment from scroll with `prefers-reduced-motion` honoured. Nothing touches `assets/site.css`, `assets/site.js` or `scripts/` until the owner's "go" (Phase 3 ports it).

**Tech Stack:** Higgsfield MCP (`recraft_v4_1`, `model_type=vector`), Python 3 + Pillow + numpy + potrace (`/opt/homebrew/bin/potrace`), vanilla JS + CSS scroll-driven animations with IntersectionObserver fallback, headless Chrome for captures.

**Spec:** `docs/design/01-brand-identity.md` (rev. 3, §5 imagery and §7 components) and `docs/design/00-reference-analysis.md` (rev. 3, §5 imagery treatment, §9 checklist), plus the owner's feedback of 2026-09-16 evening: shapes must outline the real plants; vanilkový puding = vanilla flower **with leaves** as one object; kakao = cocoa pod **with leaves**; vanilínový cukr = **sugarcane stalk, leaves and flower**; leaves must attach to the vine; add motion and scroll effects.

## Global Constraints

- Three colours only: gold `#D4AF37`, white `#FFFFFF`, ink `#1A1A1A`; greys only for form chrome. No brown, no cream.
- White text on gold is never used (2.10:1). Headings on gold are ink.
- Product photos stay whole; the product must be fully visible and centred inside its mask.
- Botanicals are solid white silhouettes with thin gold interior lines; no thin outline drawings.
- Fonts: Fraunces (display, numerals at 500) and Geologica; no Inter, Space Grotesk, Playfair Display.
- Motion ≥ 600 ms, ease-out, nothing bouncy; every animation has a `prefers-reduced-motion` alternative; content is visible without JS.
- No changes to `assets/`, `scripts/` or generated HTML before the owner's "go". Deliverables live under `docs/design/` and `assets/botanicals/` (image files only, as the brief specifies).
- Higgsfield: one test image first, then the batch. Record model, prompts and credits in `docs/design/01b-botanical-assets.md`.
- Repo: `~/Juzlova-site/juzlova-rebuild-status`. Local server for renders: `python3 -m http.server 8765 --bind 127.0.0.1` from the repo root. Headless Chrome hangs after writing a PNG: wrap with `perl -e 'alarm 80; exec @ARGV'`.

---

## File structure

| Path | Responsibility |
|---|---|
| `docs/design/samples/generate_botanicals.md` | The exact prompts and parameters used (copy of what was sent to Higgsfield) |
| `docs/design/samples/process_botanicals.py` | PNG → alpha-white PNG, potrace SVG, normalised clipPath sprite |
| `assets/botanicals/src/*.png` | Raw Higgsfield downloads (black on white) |
| `assets/botanicals/*.png` | White silhouettes with alpha, veins transparent |
| `assets/botanicals/*.svg` | Traced vector silhouettes |
| `docs/design/samples/botanicals-sprite.svg` | `<symbol>`s (white fill) + `<clipPath>`s (objectBoundingBox) for the specimen |
| `docs/design/samples/01-specimen.html` | The page; consumes the sprite |
| `docs/design/samples/01-specimen.js` | Motion: reveals, parallax, stroke-draw, vine leaf attachment |
| `docs/design/01b-botanical-assets.md` | Model choice, prompts, credits, what was kept or re-rolled |
| `docs/design/01-brand-identity.md` | §5.1 and §5.3 updated to the new object set |

---

### Task 1: The five product objects and five motifs (definition, no generation)

**Files:**
- Create: `docs/design/samples/generate_botanicals.md`

**Interfaces:**
- Produces: the canonical object list and prompt strings used by Task 2 and documented in Task 7. Object ids: `potato`, `wheat`, `vanilla`, `cocoa`, `sugarcane`, `leaf-banana`, `leaf-cocoa`, `vine-vanilla`, `beans`, `sugarcane-leaves`.

- [x] **Step 1: Write the object table and prompts**

```markdown
# Botanical generation brief · Recraft V4.1 (vector)

Common parameters: `model=recraft_v4_1`, `model_type=vector`, `resolution=2k`,
`colors=["#FFFFFF","#D4AF37"]`, `background_color="#D4AF37"`. One object per image.
**Owner rule (2026-09-16 evening): every generated asset must already be on-brand,
white silhouette on gold with gold interior lines. No black or grey sources.**
Recraft vector mode returns real SVG, so no bitmap tracing is needed for the
silhouettes; masks are derived from the SVG outline.

Common prompt tail (verbatim on every prompt):
"Pure white flat vector silhouette on a plain solid gold background, thin gold
interior lines only where noted, one centred object filling about 80 percent of
the frame, botanically accurate proportions, smooth clean curves, only two
colours white and gold, no gradients, no shadow, no outline stroke, no text."

| id | product / role | aspect | prompt head |
|---|---|---|---|
| potato | Bramborové knedlíky (product object + mask) | 4:3 | "Two potato tubers side by side with a short potato-plant sprig of three compound leaves rising from behind them; tubers slightly irregular ovals with a few eye dimples as small white dots" |
| wheat | Chlupaté knedlíky (flour from the family mill) | 4:3 | "A bundle of three wheat ears on curving stems with two long narrow leaves, grains clearly articulated as overlapping scales, awns fine; the ears lean to one side" |
| vanilla | Vanilkový puding (product object + mask) | 4:3 | "A Vanilla planifolia orchid flower seen from the front, three slender pointed sepals and two narrower petals, a tubular frilled lip in the centre, on a short vine section with two thick oval leaves and a coiled tendril; thin white lines mark the petal midlines and leaf midribs" |
| cocoa | Kakao holandského typu (product object + mask) | 4:3 | "A ripe Theobroma cacao pod hanging from a short branch beside two large elliptic cacao leaves with drip tips; pod oblong, blunt at the stem end, tapered tip, five deep longitudinal furrows drawn as thin white lines" |
| sugarcane | Vanilínový cukr (product object + mask) | 3:4 | "A section of sugarcane stalk with visible nodes, a fan of four long arching sugarcane leaves and a feathery flowering plume at the top; thin white lines mark the leaf midribs" |
| leaf-banana | background motif | 16:9 | "A single large banana leaf seen flat, oblong with a rounded base and blunt tip, strong midrib and closely spaced parallel oblique ribs drawn as thin white lines, two natural tears along the ribs" |
| leaf-cocoa | background motif | 3:2 | "A spray of three cacao leaves on one twig, elliptic with drip tips, midribs and pinnate veins as thin white lines" |
| vine-vanilla | background motif (wave ornaments) | 16:9 | "A horizontal Vanilla planifolia vine with alternating thick oval leaves, two small orchid flowers and one coiled tendril, leaves attached to the vine by short petioles" |
| beans | background motif | 3:2 | "A fan of four long slender vanilla beans tied at the base with a twist of string, tips gently hooked" |
| sugarcane-leaves | background motif | 16:9 | "A cluster of long arching sugarcane leaves with midribs as thin white lines, no stalk" |
```

- [x] **Step 2: Save the file and commit nothing yet** (the repo is uncommitted by owner's instruction; leave `git status` as is).

---

### Task 2: Anchor test image, then the batch

**Files:**
- Create: `assets/botanicals/src/cocoa.png` (test), then the other nine `assets/botanicals/src/<id>.png`

**Interfaces:**
- Consumes: prompts from Task 1.
- Produces: ten black-on-white PNGs at 2k, plus job ids recorded in `docs/design/01b-botanical-assets.md`.

- [x] **Step 1: Generate the anchor (`cocoa`) with `generate_image`**

```json
{"model":"recraft_v4_1","model_type":"vector","resolution":"2k","aspect_ratio":"4:3",
 "colors":["#000000"],"background_color":"#FFFFFF",
 "prompt":"<cocoa prompt head>. <common tail>"}
```

- [x] **Step 2: Judge the anchor against four checks**: (1) reads as a cacao pod with leaves at thumbnail size, (2) pod proportions oblong not lemon-like, (3) furrows are thin white lines, (4) background pure white, no stroke. Re-roll once with a tightened prompt if any fails; otherwise continue.

- [x] **Step 3: Download the result**

```bash
curl -sL "<result_url>" -o assets/botanicals/src/cocoa.png && sips -g pixelWidth -g pixelHeight assets/botanicals/src/cocoa.png
```

- [x] **Step 4: Batch the remaining nine with `generate_image_batch`** (indices 1–9 in the table order), poll with `jobs_wait` in one group, present with one `show_generation_by_ids`, download each to `assets/botanicals/src/<id>.png`.

- [x] **Step 5: Record credits**: read `balance` before and after; write the delta into `docs/design/01b-botanical-assets.md` (Task 7).

---

### Task 3: Post-processor — alpha silhouettes, traced SVG, mask sprite

**Files:**
- Create: `docs/design/samples/process_botanicals.py`
- Create: `assets/botanicals/<id>.png`, `assets/botanicals/<id>.svg`, `docs/design/samples/botanicals-sprite.svg`

**Interfaces:**
- Consumes: `assets/botanicals/src/<id>.png`.
- Produces: `<symbol id="sil-<id>" viewBox="0 0 W H">` (white fill, holes preserved) and `<clipPath id="m-<id>" clipPathUnits="objectBoundingBox">` (outer outline only, holes filled) for each id.

- [x] **Step 1: Write the test**

```python
# docs/design/samples/test_process_botanicals.py
import subprocess, sys, os, re
from PIL import Image
def test_alpha_and_sprite():
    subprocess.check_call([sys.executable, "docs/design/samples/process_botanicals.py", "cocoa"])
    im = Image.open("assets/botanicals/cocoa.png").convert("RGBA")
    a = im.getchannel("A"); assert a.getextrema() == (0, 255)          # real transparency
    assert im.getpixel((im.width//2, im.height//2))[:3] == (255,255,255)  # white fill
    s = open("docs/design/samples/botanicals-sprite.svg").read()
    assert '<symbol id="sil-cocoa"' in s and '<clipPath id="m-cocoa"' in s
    m = re.search(r'id="m-cocoa"[^>]*>\s*<path d="([^"]+)"', s)
    nums = [float(x) for x in re.findall(r"-?\d*\.?\d+", m.group(1))]
    assert max(nums) <= 1.001 and min(nums) >= -0.001                   # normalised
```

- [x] **Step 2: Run it, expect failure** (`process_botanicals.py` missing).

- [x] **Step 3: Implement**

```python
# docs/design/samples/process_botanicals.py
"""Turn Recraft black-on-white silhouettes into brand assets.
usage: process_botanicals.py <id> [<id> ...]   (ids = filenames in assets/botanicals/src)"""
import sys, subprocess, re, pathlib, xml.etree.ElementTree as ET
import numpy as np
from PIL import Image, ImageFilter

ROOT = pathlib.Path(__file__).resolve().parents[3]
SRC, OUT, SPRITE = ROOT/"assets/botanicals/src", ROOT/"assets/botanicals", ROOT/"docs/design/samples/botanicals-sprite.svg"

def alpha_white(src: pathlib.Path, dst: pathlib.Path) -> Image.Image:
    g = np.asarray(Image.open(src).convert("L"), dtype=np.float32)
    a = np.clip((200 - g) / 120, 0, 1) * 255            # dark -> opaque, white -> clear, soft edge
    rgba = np.zeros((*g.shape, 4), dtype=np.uint8); rgba[..., :3] = 255; rgba[..., 3] = a.astype(np.uint8)
    im = Image.fromarray(rgba, "RGBA"); im.save(dst, optimize=True); return im

def trace(src: pathlib.Path, fill_holes: bool) -> tuple[str, int, int]:
    """potrace -> single path d attribute in pixel space. fill_holes keeps only outer contours."""
    im = Image.open(src).convert("L").point(lambda v: 0 if v < 200 else 255)   # threshold; veins stay white
    w, h = im.size
    if fill_holes:
        from PIL import ImageDraw
        mask = Image.new("L", im.size, 0)
        # flood the outside from the four corners, everything not reached is "object"
        outside = im.copy(); ImageDraw.floodfill(outside, (0, 0), 128); ImageDraw.floodfill(outside, (w-1, h-1), 128)
        ImageDraw.floodfill(outside, (w-1, 0), 128); ImageDraw.floodfill(outside, (0, h-1), 128)
        im = outside.point(lambda v: 255 if v == 128 else 0)
    pbm = src.with_suffix(".pbm"); im.save(pbm)
    svg = subprocess.run(["potrace", str(pbm), "-s", "-o", "-", "--flat", "-t", "12", "-a", "1.2", "-O", "0.6"],
                         check=True, capture_output=True, text=True).stdout
    pbm.unlink()
    root = ET.fromstring(svg); ns = {"s": "http://www.w3.org/2000/svg"}
    d = " ".join(p.get("d") for p in root.iter("{http://www.w3.org/2000/svg}path"))
    tf = root.find(".//s:g", ns).get("transform", "")          # potrace emits translate+scale
    return d, w, h, tf

def to_objectbbox(d: str, tf: str, w: int, h: int) -> str:
    """Bake potrace's transform and normalise to 0..1 (objectBoundingBox)."""
    sx = sy = 1.0; tx = ty = 0.0
    m = re.search(r"translate\(([-\d.]+),([-\d.]+)\)", tf);  tx, ty = (float(m[1]), float(m[2])) if m else (0, 0)
    m = re.search(r"scale\(([-\d.]+),([-\d.]+)\)", tf);      sx, sy = (float(m[1]), float(m[2])) if m else (1, 1)
    nums = iter(re.findall(r"-?\d*\.?\d+", d)); out = []
    for tok in re.findall(r"[MmLlHhVvCcSsQqTtAaZz]|-?\d*\.?\d+", d):
        out.append(tok)
    # potrace uses absolute M and relative c/l; convert by walking the path
    return _normalise_path(d, tx, ty, sx, sy, w, h)

def _normalise_path(d, tx, ty, sx, sy, w, h):
    toks = re.findall(r"[MmLlHhVvCcSsQqTtAaZz]|-?\d*\.?\d+", d); i = 0; cmd = None; x = y = 0; out = []
    def P(px, py): return f"{(tx + px * sx) / w:.4f},{(ty + py * sy) / h:.4f}"
    while i < len(toks):
        t = toks[i]
        if re.match(r"[A-Za-z]", t): cmd = t; i += 1; 
        if cmd in "Mm":
            nx, ny = float(toks[i]), float(toks[i+1]); i += 2
            if cmd == "m": nx += x; ny += y
            x, y = nx, ny; out.append("M" + P(x, y)); cmd = "L" if cmd == "M" else "l"
        elif cmd in "Ll":
            nx, ny = float(toks[i]), float(toks[i+1]); i += 2
            if cmd == "l": nx += x; ny += y
            x, y = nx, ny; out.append("L" + P(x, y))
        elif cmd in "Cc":
            c = [float(toks[i+k]) for k in range(6)]; i += 6
            if cmd == "c": c = [c[0]+x, c[1]+y, c[2]+x, c[3]+y, c[4]+x, c[5]+y]
            out.append("C" + P(c[0], c[1]) + " " + P(c[2], c[3]) + " " + P(c[4], c[5])); x, y = c[4], c[5]
        elif cmd in "Zz": out.append("Z"); i += 0 if not re.match(r"[A-Za-z]", toks[i-1]) else 0; 
        else: i += 1
        if cmd in "Zz" and i < len(toks) and not re.match(r"[A-Za-z]", toks[i]): cmd = "l"
    return "".join(out)

def build_sprite(ids):
    syms, clips = [], []
    for i in ids:
        src = SRC/f"{i}.png"; alpha_white(src, OUT/f"{i}.png")
        d, w, h, tf = trace(src, fill_holes=False)
        (OUT/f"{i}.svg").write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}"><g transform="{tf}" fill="#fff" fill-rule="evenodd"><path d="{d}"/></g></svg>')
        syms.append(f'<symbol id="sil-{i}" viewBox="0 0 {w} {h}"><g transform="{tf}" fill="#fff" fill-rule="evenodd"><path d="{d}"/></g></symbol>')
        d2, _, _, tf2 = trace(src, fill_holes=True)
        clips.append(f'<clipPath id="m-{i}" clipPathUnits="objectBoundingBox"><path d="{_normalise_path(d2, *_tf(tf2), w, h)}"/></clipPath>')
    SPRITE.write_text("\n".join(syms + clips))

def _tf(tf):
    m1 = re.search(r"translate\(([-\d.]+),([-\d.]+)\)", tf); m2 = re.search(r"scale\(([-\d.]+),([-\d.]+)\)", tf)
    return (float(m1[1]), float(m1[2])) if m1 else (0.0, 0.0)) + ((float(m2[1]), float(m2[2])) if m2 else (1.0, 1.0))

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True); build_sprite(sys.argv[1:])
```

- [x] **Step 4: Run the test, expect pass.** Open `assets/botanicals/cocoa.png` and `cocoa.svg` in the browser pane on a gold background and confirm: white fill, furrows show gold through, outline smooth.

- [x] **Step 5: Run for all ten ids** and inspect the sprite size (target < 120 KB; if larger raise potrace `-t` to 20).

---

### Task 4: Product masks, objects and the footer in the specimen

Owner notes (2026-09-16 evening) folded in here: the footer keeps the reference's
feel: hairline-split centred wordmark, nav with gold active underline, phone and
mail, a row of **grey watermark-style marks** (pick-up places set like the
reference's greyed payment logos, plus a faint grey J mark behind the column),
and a **minimalist light form**: rounded 14 px fields, `#F6F6F6` fill, 1 px
`#E4E4E4` border, grey placeholder, ink focus ring, gold button. Improve the form
where it helps: `autocomplete="name"` / `"tel"`, `inputmode="tel"`, an inline
success line ("Zavoláme vám zpět.") and an error line in `--error`, both AA.

**Files:**
- Modify: `docs/design/samples/01-specimen.html` (the `<defs>` block, `.shape` rules, hero/stats/recipes markup)

**Interfaces:**
- Consumes: `#m-potato #m-wheat #m-vanilla #m-cocoa #m-sugarcane` clipPaths and `#sil-*` symbols from the sprite.
- Produces: `.shape.<id>` classes with per-photo `background-size/position` so the product stays fully visible.

- [x] **Step 1: Replace the five hand-drawn clipPaths and the generated symbols with the sprite contents** (inline the file; keep the `<svg width="0" height="0">` wrapper).

- [x] **Step 2: Map products to masks**

```css
.shape.potato   {clip-path:url(#m-potato);   aspect-ratio:4/3}
.shape.wheat    {clip-path:url(#m-wheat);    aspect-ratio:4/3}
.shape.vanilla  {clip-path:url(#m-vanilla);  aspect-ratio:4/3}
.shape.cocoa    {clip-path:url(#m-cocoa);    aspect-ratio:4/3}
.shape.sugarcane{clip-path:url(#m-sugarcane);aspect-ratio:3/4;background-size:cover}
```

Assign: knedlíky photo → `potato`; chlupaté → `wheat`; puding → `vanilla`; kakao → `cocoa`; cukr → `sugarcane`. For each, set `background-size`/`background-position` so bag and bowl sit inside the object's largest mass (check by screenshot; adjust in 2 % steps).

- [x] **Step 3: Pair every masked photo with its white object silhouette** behind it on gold bands (`<svg class="art"><use href="#sil-cocoa"/></svg>` at 1.3× the photo width, opacity .55, offset up-left by 6 %), so the real outline is read even where the mask crops.

- [x] **Step 4: Update the "Pět tvarů, pět směsí" legend** to show the five `#sil-*` objects in gold tiles with the five masks beneath.

- [x] **Step 5: Render desktop and mobile; check no product part is cut and no silhouette crosses text.**

---

### Task 4b: Photoreal cut-out objects with a hand-cut white outline

Owner note (2026-09-16 evening): besides the white silhouettes, add minimalist
**real** objects (cocoa pod and beans, vanilla flower, banana leaf, cocoa leaf,
sugarcane, wheat) as cut-outs with a white outline "like hand drawn", exactly
where the reference floats its cut-outs (hero, stats column, journey right).

**Files:**
- Create: `assets/botanicals/cutouts/src/<id>.png` (gpt_image_2_5 on white), `assets/botanicals/cutouts/<id>.png` (alpha, via `remove_background`)
- Modify: `01-specimen.html` (`.cutout` class, sticker filter)

**Interfaces:**
- Produces: `.cutout` = `<img>` with alpha + SVG filter `#sticker` (feMorphology dilate 6 px → white flood → merge) and the soft shadow; fallback: eight 5 px `drop-shadow(#fff)` offsets.

- [x] **Step 1: Generate one test** (`gpt_image_2_5`, 1:1, 1 credit): "Studio product photograph of a single ripe cacao pod split open lengthwise, revealing the white pulp and dark cocoa beans inside, with three loose roasted cocoa beans beside it. Isolated on a pure white background, soft warm natural daylight from the upper left, high detail, realistic texture, no shadow on the background, no other objects, no text." Judge: warm light matching the farmhouse photos, clean white background, one object.
- [x] **Step 2: `remove_background` on the job id**; download the PNG; verify alpha with Pillow (`getextrema` on A = (0, 255)).
- [x] **Step 3: Batch the other five** with the same tail: vanilla flower on a vine with two beans (3:4); single fresh banana leaf (16:9); spray of three cacao leaves on a twig (3:2); sugarcane stalk section with leaves (3:4); bundle of three wheat ears (3:4). Remove backgrounds, download.
- [x] **Step 4: Sticker filter in the sprite**

```html
<filter id="sticker" x="-10%" y="-10%" width="120%" height="120%">
  <feMorphology in="SourceAlpha" operator="dilate" radius="6" result="d"/>
  <feFlood flood-color="#fff" result="w"/><feComposite in="w" in2="d" operator="in" result="o"/>
  <feMerge><feMergeNode in="o"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
```
`.cutout{filter:url(#sticker) drop-shadow(0 28px 28px rgba(26,26,26,.18))}`

- [x] **Step 5: Place**: hero right of the headline (cocoa pod, bridging the band edge, `plx data-speed="25"`); stats centre column (three small cut-outs replacing the masked stack: cocoa, vanilla, wheat) with the masked product photos moving to the product cards; journey right (vanilla plant, tall, bridging up); why band (banana leaf cut-out low right, small). Masked product photos keep the recipes row and the product section.

---

### Task 4c: Price ticker → brand marquee

Owner note (2026-09-16 evening): the live site's dark price ticker under the hero is basic. Rebuild it on-brand.

**Files:** Modify `01-specimen.html` (new `<div class="marquee">` under the hero), `01-specimen.js`.

- [x] **Step 1: Markup**: a gold band 3.2rem tall with 1 px white hairlines top and bottom; items = product name (Geologica 400) + price (Fraunces 500, `tnum`) separated by a small white silhouette (`<svg><use href="#sil-leaf-cocoa"/></svg>` at 1.4rem, alternating with `sil-beans`), duplicated twice for a seamless loop.
- [x] **Step 2: Motion**: `@keyframes marquee{to{transform:translateX(-50%)}}` on the track, 38 s linear infinite, `animation-play-state:paused` on hover/focus-within; reduced motion → `animation:none` and the track wraps as a static two-line list. Text is ink on gold (8.28:1).
- [x] **Step 3: Verify** the loop has no seam (track width = 2 × content) at 1440 and 390.

---

### Task 5: Vines with attached leaves

**Files:**
- Create: `docs/design/samples/01-specimen.js`
- Modify: `01-specimen.html` (wave and why-band vines get `data-vine` with `data-leaves="n"`)

**Interfaces:**
- Produces: `attachLeaves(pathEl, count, symbolId)` which places `<use>` leaves whose base sits on the path and whose rotation follows the tangent.

- [x] **Step 1: Write the function**

```js
// 01-specimen.js
export function attachLeaves(path, count, symbolId = 'sil-leaf-cocoa', size = 110) {
  const svg = path.ownerSVGElement, L = path.getTotalLength();
  for (let i = 1; i <= count; i++) {
    const t = (i / (count + 1)) * L, p = path.getPointAtLength(t), q = path.getPointAtLength(t + 1);
    const ang = Math.atan2(q.y - p.y, q.x - p.x) * 180 / Math.PI + (i % 2 ? -55 : 55);   // alternate sides
    const use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
    use.setAttribute('href', '#' + symbolId);
    use.setAttribute('width', size); use.setAttribute('height', size * 0.45);
    use.setAttribute('transform', `translate(${p.x} ${p.y}) rotate(${ang}) translate(0 ${-size * 0.225})`); // base on the line
    use.setAttribute('class', 'vine-leaf'); svg.appendChild(use);
  }
}
document.querySelectorAll('[data-vine]').forEach(el => attachLeaves(el, +el.dataset.leaves || 4, el.dataset.leaf || 'sil-leaf-cocoa'));
```

- [x] **Step 2: Remove the hand-placed `.art` leaf `<svg>`s on the wave and the why-band vines; add `data-vine data-leaves="4"` to those `<path>`s and give the wave `<svg>` `preserveAspectRatio="xMidYMid meet"` so tangents are not distorted.

- [x] **Step 3: Render and confirm every leaf's base touches the stroke and leaves alternate sides.**

---

### Task 6: Motion and scroll effects

**Files:**
- Modify: `01-specimen.js`, `01-specimen.html` (classes `rv`, `plx`, `draw`)

**Interfaces:**
- Produces: `.rv` reveal (fade-up 700 ms, stagger 80 ms), `.plx[data-speed]` parallax on botanicals and bridging photos, `.draw` stroke-draw on vines and the wave driven by scroll progress, hover micro-interactions, all disabled under `prefers-reduced-motion`.

- [x] **Step 1: CSS (content visible by default; JS only adds `is-in`)**

```css
.rv{transition:opacity .7s cubic-bezier(.22,1,.36,1),transform .7s cubic-bezier(.22,1,.36,1)}
.js .rv{opacity:0;transform:translateY(28px)} .js .rv.is-in{opacity:1;transform:none}
.draw path{stroke-dasharray:var(--len,2000);stroke-dashoffset:var(--len,2000);transition:stroke-dashoffset 1.6s cubic-bezier(.22,1,.36,1)}
.draw.is-in path{stroke-dashoffset:0}
.more svg{transition:transform .35s cubic-bezier(.22,1,.36,1)} .more:hover svg{transform:translateX(6px)}
nav.demo a{position:relative} nav.demo a::after{content:"";position:absolute;left:0;right:0;bottom:-.35rem;height:3px;background:var(--gold);transform:scaleX(0);transform-origin:left;transition:transform .35s cubic-bezier(.22,1,.36,1)} nav.demo a:hover::after,nav.demo a.on::after{transform:scaleX(1)}
@media (prefers-reduced-motion:reduce){.rv,.draw path,.more svg,nav.demo a::after{transition:none} .js .rv{opacity:1;transform:none} .draw path{stroke-dashoffset:0} .plx{transform:none!important}}
```

- [x] **Step 2: JS**

```js
document.documentElement.classList.add('js');
const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
// reveals with stagger among siblings
const io = new IntersectionObserver(es => es.forEach(e => { if (!e.isIntersecting) return;
  const sibs = [...e.target.parentElement.querySelectorAll(':scope > .rv')];
  e.target.style.transitionDelay = reduced ? '0s' : (Math.max(sibs.indexOf(e.target), 0) * 80) + 'ms';
  e.target.classList.add('is-in'); io.unobserve(e.target); }), { threshold: .15 });
document.querySelectorAll('.rv,.draw').forEach(el => io.observe(el));
// stroke lengths
document.querySelectorAll('.draw path').forEach(p => p.style.setProperty('--len', p.getTotalLength()));
// parallax: botanicals and bridging photos drift at data-speed × scroll delta, rAF-throttled
if (!reduced) { const els = [...document.querySelectorAll('.plx')]; let raf = 0;
  const tick = () => { raf = 0; const vh = innerHeight; els.forEach(el => { const r = el.getBoundingClientRect(); const c = (r.top + r.height / 2 - vh / 2) / vh;
    el.style.transform = `translate3d(0, ${(-c * (parseFloat(el.dataset.speed) || 40)).toFixed(1)}px, 0)`; }); };
  addEventListener('scroll', () => { if (!raf) raf = requestAnimationFrame(tick); }, { passive: true }); tick(); }
```

- [x] **Step 3: Apply classes**: `rv` on H1, tagline, stats, steps, recipe figures, form; `plx data-speed="60"` on big botanicals, `data-speed="25"` on bridging photos, `data-speed="-30"` on small leaves; `draw` on the wave and the why-band vines.

- [x] **Step 4: Verify in the browser pane**: scroll the page, screenshot mid-reveal and after; confirm the wave draws in, leaves stay attached during parallax (leaves are children of the path's svg, so they move with it), and with `prefers-reduced-motion` emulated everything is static and visible.

---

### Task 7: Documentation and captures

**Files:**
- Create: `docs/design/01b-botanical-assets.md`
- Modify: `docs/design/01-brand-identity.md` §5.1, §5.3, §8
- Update: `docs/design/samples/01-specimen-desktop.png`, `01-specimen-mobile.png`

- [x] **Step 1: Write `01b-botanical-assets.md`**: model and why (Recraft V4.1 vector: SVG-like illustration, palette lock, flat background; 10 credits per 2k image), the ten prompts, job ids, credits before/after, re-rolls and why, processing steps, licence note (Higgsfield output, owner's account).
- [x] **Step 2: Update §5.1** with the five objects (potato plant, wheat ears, vanilla flower with leaves, cocoa pod with leaves, sugarcane stalk with leaves and plume) and §5.3 with the motif set and the vine-attachment rule; add the motion principles to §7.
- [x] **Step 3: Re-render desktop (1440) and mobile (390 via iframe) captures; review every band; fix and re-render until no product is cropped and no silhouette crosses text.**
- [x] **Step 4: Update memory** (`juzlova-redesign-2026-09.md`) with the object set and asset locations.

---

### Task 6b: Fourth colour proposal and white-on-gold verdict (documentation only)

- Petrol teal `#094853` proposed as the single vibrant companion to gold: text on white 10.18 (AAA), white text on it 10.18 (AAA), as text on gold 4.84 (AA), gold on it 4.84 (AA). Uses: focus rings, link hover, the "bez lepku" badge, one accent stroke in the botanicals when a second tone is wanted. Never as a surface larger than a badge or button. Record in `01-brand-identity.md` §3 as *proposed, awaiting owner's decision*.
- White text on gold: 2.10:1, fails WCAG 2.0 and 2.1 at AA for normal text (4.5) and for large text (3.0). Verdict: ink text on gold; white reserved for silhouettes, cut-out outlines, hairlines and the wave. Record the numbers in §3.2.

## Status 2026-09-17

Tasks 1–7 executed inline (owner set autopilot). Rev. 5 specimen, assets, sprite, i18n and the check report `02b` are in place; Phase 3 ports them into `assets/` and `scripts/` after the owner's "go".

## Self-review

- Spec coverage: real outlines (T2–T4), vanilla flower with leaves (T1/T2), cocoa pod with leaves (T1/T2), sugarcane for sugar (T1/T2), leaves attached to vines (T5), motion and scroll (T6), Higgsfield with a named model and prompts (T1/T2/T7). Product visibility rule kept (T4 step 2). Colour and contrast constraints unchanged.
- Placeholders: none; every step carries its code or exact parameters.
- Names: `sil-<id>` / `m-<id>` used consistently in T3, T4, T5; `attachLeaves` signature consistent in T5.
