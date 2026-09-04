#!/usr/bin/env python3
"""Shrink oversized images in img/ to web-sized WebP, in place.

Generated artwork arrives from the image service at full resolution — several
megabytes each — which is fine as a source and hopeless as a page asset. This
resizes anything larger than its role needs and re-encodes it as WebP, then
drops the oversized original so the workflow does not keep re-fetching it.

Roles and their widths are declared in TARGETS; anything not listed is left
alone. Run it after the fetch step, or by hand after adding a new image.
"""
import pathlib
import sys

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMG = ROOT / "img"

# stem -> max width in CSS pixels, doubled here for retina
TARGETS = {
    "hruskovy-kolac": 1200,
    "slehackova-rolada": 1200,
    "domaci-pernik": 1200,
    "bramborovo-tvarohove-knedliky": 1200,
    "strapacky": 1200,
    "bebe-rezy": 1200,
    "vanilkovy-cukr": 1200,
    "sisky-s-makem": 1200,
    "produkt-bramborove-knedliky": 1200,
    "produkt-chlupate-knedliky": 1200,
    "produkt-vanilkovy-puding": 1200,
    "produkt-kakao": 1200,
    "pytel-bramborove-knedliky": 1200,
    "pytel-chlupate-knedliky": 1200,
}

# Hero stills also get narrow copies, so a phone is not sent a 2200px file for a
# 400px screen. build_site.py picks these up automatically via srcset when they
# exist, and ships the full image alone when they do not.
VARIANTS = {
    "kochanov-letecky": (900, 1400),
}


def optimize(src, width, quality=82):
    """Resize to at most `width` and write a sibling .webp. Returns its path."""
    im = Image.open(src)
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    out = src.with_suffix(".webp")
    im.save(out, "WEBP", quality=quality, method=6)
    return out


def warm(src, out, width=1200):
    """Tone a grey archive photo into the site's cream palette.

    The one genuine product photograph we have — their own packets of vanilla
    sugar — is a grainy 2012 greyscale snap, and sitting next to four warm
    colour shots it reads as a mistake rather than as the real thing. Mapping
    its greys onto the page's own ink-to-paper ramp keeps the photograph
    honest while letting the product grid read as one set.
    """
    im = Image.open(src).convert("L")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    ramp = []
    for v in range(256):
        t = v / 255
        ramp.append((
            round(36 + t * (250 - 36)),
            round(31 + t * (246 - 31)),
            round(26 + t * (239 - 26)),
        ))
    toned = Image.new("RGB", im.size)
    toned.putdata([ramp[p] for p in im.getdata()])
    toned.save(out, "WEBP", quality=86, method=6)
    return out


def variants(stem, widths):
    """Write narrow copies of img/<stem>.webp beside it, skipping any upscale."""
    src = IMG / f"{stem}.webp"
    if not src.exists():
        return
    with Image.open(src) as im:
        base = im.convert("RGB")
        for w in widths:
            if base.width <= w:
                continue
            out = IMG / f"{stem}-{w}.webp"
            if out.exists():
                continue
            base.resize((w, round(base.height * w / base.width)),
                        Image.LANCZOS).save(out, "WEBP", quality=82, method=6)
            print(f"  {out.name}: {out.stat().st_size // 1024} kB")


def main():
    if not IMG.exists():
        return
    for stem, widths in sorted(VARIANTS.items()):
        variants(stem, widths)
    packets = IMG / "vanilkovy-cukr-pytliky.png"
    if packets.exists():
        out = warm(packets, IMG / "vanilkovy-cukr-pytliky.webp")
        print(f"  {out.name}: warm-toned from the greyscale original")
    for stem, width in sorted(TARGETS.items()):
        out = IMG / f"{stem}.webp"
        srcs = [p for p in IMG.glob(f"{stem}.*") if p != out]

        # A finished .webp is left alone unless it is genuinely too big. Without
        # this the script re-derives it from whatever sibling it finds — which,
        # once the huge originals are gone, means the small recovered archive
        # file — and replaces a good 1200px asset with a 300px one before
        # deleting the archive file it came from. Re-encoding a webp from a
        # webp also loses quality on every run.
        if out.exists():
            with Image.open(out) as done:
                if done.width <= width:
                    continue
            src, drop = out, []
        else:
            if not srcs:
                continue
            src, drop = srcs[0], srcs

        before = src.stat().st_size
        out = optimize(src, width)
        print(f"  {out.name}: {before // 1024} kB -> {out.stat().st_size // 1024} kB")
        for p in drop:  # the oversized original we just replaced
            p.unlink()


if __name__ == "__main__":
    sys.exit(main())
