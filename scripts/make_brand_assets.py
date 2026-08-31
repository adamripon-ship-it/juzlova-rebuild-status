#!/usr/bin/env python3
"""Turn the brand source files in brand/ into the web assets in img/.

Sources (2000x2000 PNGs supplied by the owner):
  brand/wordmark-black.png   black "Jůzlová" script, transparent
  brand/wordmark-white.png   white  "Jůzlová" script, transparent
  brand/mark-navy-source.png navy "J" monogram on a white background (no alpha)
  brand/mark-white.png       white "J" monogram, transparent

Produces trimmed, right-sized files: the two wordmarks for the header and
footer (picked by contrast), and the monogram as favicons in both navy and
white so the tab icon stays legible in light and dark browser chrome.
"""
import pathlib

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "brand"
OUT = ROOT / "img"
NAVY = (2, 21, 54)


def trim(im, pad_ratio=0.0):
    """Crop to the visible pixels, optionally leaving proportional padding."""
    box = im.getchannel("A").getbbox()
    im = im.crop(box)
    if pad_ratio:
        pad = int(max(im.size) * pad_ratio)
        canvas = Image.new("RGBA", (im.width + pad * 2, im.height + pad * 2), (0, 0, 0, 0))
        canvas.paste(im, (pad, pad))
        im = canvas
    return im


def to_height(im, height):
    w = round(im.width * height / im.height)
    return im.resize((w, height), Image.LANCZOS)


def square(im, size):
    """Fit the artwork inside a transparent square canvas."""
    im = to_height(im, size) if im.height >= im.width else im.resize(
        (size, round(im.height * size / im.width)), Image.LANCZOS)
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    canvas.paste(im, ((size - im.width) // 2, (size - im.height) // 2), im)
    return canvas


def keyed_from_white(path, colour):
    """Rebuild a dark-on-white scan as clean transparent artwork.

    Alpha comes from how dark each pixel is, so the anti-aliased edges stay
    smooth instead of picking up a white fringe.
    """
    grey = Image.open(path).convert("L")
    alpha = grey.point(lambda v: 255 - v)
    art = Image.new("RGBA", grey.size, colour + (255,))
    art.putalpha(alpha)
    return art


def main():
    OUT.mkdir(exist_ok=True)

    # ── wordmarks: header (34px tall) and footer, exported at 3x for retina ──
    for name, src in (("black", "wordmark-black.png"), ("white", "wordmark-white.png")):
        im = trim(Image.open(SRC / src).convert("RGBA"))
        to_height(im, 200).save(OUT / f"logo-wordmark-{name}.png", optimize=True)
        print(f"  logo-wordmark-{name}.png", to_height(im, 200).size)

    # ── monogram ──
    navy = trim(keyed_from_white(SRC / "mark-navy-source.png", NAVY), pad_ratio=0.04)
    white = trim(Image.open(SRC / "mark-white.png").convert("RGBA"), pad_ratio=0.04)

    for size in (32, 192, 512):
        square(navy, size).save(OUT / f"icon-{size}.png", optimize=True)
        square(white, size).save(OUT / f"icon-white-{size}.png", optimize=True)
    print("  icon-{32,192,512}.png + white variants")

    # multi-size .ico for legacy browser chrome
    square(navy, 64).save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

    # Apple composites touch icons onto black, so give it a solid cream tile
    tile = Image.new("RGBA", (180, 180), (250, 246, 239, 255))
    mark = square(navy, 148)
    tile.paste(mark, (16, 16), mark)
    tile.convert("RGB").save(OUT / "apple-touch-icon.png", optimize=True)

    # large white monogram for the footer watermark
    square(white, 640).save(OUT / "mark-white.png", optimize=True)
    print("  favicon.ico, apple-touch-icon.png, mark-white.png")


if __name__ == "__main__":
    main()
