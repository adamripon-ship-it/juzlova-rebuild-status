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
    "produkt-bramborove-knedliky": 1200,
    "produkt-chlupate-knedliky": 1200,
    "produkt-vanilkovy-puding": 1200,
    "produkt-kakao": 1200,
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


def main():
    if not IMG.exists():
        return
    for stem, width in sorted(TARGETS.items()):
        out = IMG / f"{stem}.webp"
        srcs = [p for p in IMG.glob(f"{stem}.*") if p != out]
        if out.exists() and not srcs:
            continue
        src = srcs[0] if srcs else out
        before = src.stat().st_size
        out = optimize(src, width)
        print(f"  {out.name}: {before // 1024} kB -> {out.stat().st_size // 1024} kB")
        for p in srcs:  # drop the oversized original
            p.unlink()


if __name__ == "__main__":
    sys.exit(main())
