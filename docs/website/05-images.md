# 5. Images

[← Back to the handbook](README.md)

---

All images are stored in this repository:

| Folder | Contents |
|---|---|
| [`img/`](../../img/) | Every image used on the site (photos, product shots, icons, logos) |
| [`assets/botanicals/`](../../assets/botanicals/) | Decorative illustrations: cocoa leaves, beans, flowers |
| [`assets/video/`](../../assets/video/) | Short background video clips |
| [`brand/`](../../brand/) | The owner's four original logo files |
| [`archive/images/`](../../archive/) | Every image recovered from the original WordPress site |

👉 **See them all in the [image gallery](generated/images.md)**, with previews,
file sizes, and the pages each image appears on.

## Where the images came from

Knowing the origin matters when deciding whether an image may be replaced.

### 📷 The workshop's own photographs

Recovered from the old website via the Wayback Machine.

| File | Shows |
|---|---|
| `kochanov-letecky.webp` | Aerial view of Kochánov at golden hour. The old site's background video |
| `dilna-panorama.webp` | The real production room: flour sacks, scale, bagging line ("About us" page) |
| `sisky-s-makem.png`, `strapacky.jpg`, `bebe-rezy.gif` | Original recipe photos |

### 🎨 Newly created images

Made because no usable original survived. Several old "product" photos showed
the wrong product: the file named *chlupaté knedlíky* is actually vanilla
sugar, and *vanilkový puding* is a bag-sealing machine.

| Files | Use |
|---|---|
| `produkt-*.webp` | The four product photos |
| `hruskovy-kolac.webp`, `slehackova-rolada.webp`, `domaci-pernik.webp`, `bramborovo-tvarohove-knedliky.webp` | Recipes with no surviving photo |
| `hero.webp`, `workshop.webp`, `film-*.webp` | Frames for the scrolling "film" at the top of the home page (some kept as spares) |
| `vanilkovy-cukr-kilo.webp` | The vanilla-sugar kilo bag. It replaced the old sachet photo, because the workshop sells kilo bags only |

### 👪 Family portraits

`img/team/`: portraits for the "About us" page. Family members without a
real photo yet have a placeholder drawing (`.svg`).

### 🏷️ Brand

Generated from the owner's files in `brand/` by `scripts/make_brand_assets.py`:
black and white wordmarks, the navy favicon set, `apple-touch-icon.png`, and the
footer monogram.

## Adding a new image

1. Put the file in `img/`.
2. Run `python3 scripts/optimize_images.py`. It shrinks oversized files to web
   WebP (the recipe photos went from 36 MB to 315 kB).
3. Reference it from the page source, rebuild, and check it on screen.
