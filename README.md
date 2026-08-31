# Jůzlová.cz — rebuilt site

Static rebuild of **juzlova.cz**, the Czech food-mix workshop in Kochánov,
Vysočina, recovered from the Wayback Machine after the original WordPress site
went down.

**Start here if you are picking this up: [`docs/HANDOFF.md`](docs/HANDOFF.md).**
It covers what is deployed where, how the live domain differs from this repo,
and what is left to do.

## Building

```sh
python scripts/build_site.py
```

No dependencies outside the standard library. Output is written into the repo
root — `index.html` plus one directory per original URL slug, so old links keep
working — and committed, because GitHub Pages serves the repo directly.

Pass the production domain at cutover, since every canonical URL, hreflang
alternate, sitemap entry and JSON-LD `url` is built from it:

```sh
SITE_BASE=https://juzlova.cz python scripts/build_site.py
```

## What is here

- **Four languages.** Czech at the root, `en/`, `de/`, `sk/`, with a language
  selector, hreflang plus `x-default`, and localised metadata. 68 pages.
- **Content** in `scripts/content_{cs,en,de,sk}.py` and
  `scripts/recipes_{cs,en,de,sk}.py`. Czech is the source of truth.
- **Search and LLM visibility:** `sitemap.xml`, `robots.txt`, `llms.txt`,
  `llms-full.txt`, and JSON-LD for Organization, Product, Recipe, FAQPage and
  BreadcrumbList.
- **`archive/`** — the full Wayback mirror the rebuild came from: 40 pages, 56
  images, 16 other files, plus the CDX index. Verify with
  `python scripts/wayback_archive.py --check`.
- **`brand/`** — the owner's wordmark and monogram sources.
  `scripts/make_brand_assets.py` turns them into the icons in `img/`.
- **`status.html`** — the original recovery status board.

## Scripts

| Script | Does |
|---|---|
| `build_site.py` | Builds every page in all four languages |
| `wayback_archive.py` | Mirrors juzlova.cz from the Wayback Machine; `--check` reports completeness |
| `make_brand_assets.py` | Wordmarks, favicons and the footer monogram from `brand/` |
| `optimize_images.py` | Resizes oversized artwork to web-sized WebP |
