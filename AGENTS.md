# Working on juzlova.cz

Entry point for coding agents (Cursor, Claude Code, and friends). Read this
before touching anything. `docs/HANDOFF.md` has the longer history.

## What this is

A static site for Jůzlová, a Czech family food-mix workshop in Kochánov,
Vysočina — potato and "chlupaté" dumpling mixes, gluten-free puddings,
Dutch-process cocoa, vanilla sugar. The original WordPress/Shopify site went
down; everything here was recovered from the Wayback Machine and rebuilt as a
generated static site in four languages.

**It is live.** `https://www.juzlova.cz` serves this build — Czech at the root,
plus `/en/`, `/de/`, `/sk/`. Treat changes as production changes.

## The rule that matters most

**Never hand-edit the HTML.** Every `index.html` in the repo root and under
`en/ de/ sk/` is generated output, committed because the host serves the repo
directly. Editing it is wasted work — the next `build_site.py` run overwrites
it, and CI (`build-check.yml`) fails the build when committed output is stale.

Change the source, then rebuild:

| To change | Edit |
|---|---|
| Page copy, product text, UI strings | `scripts/content_{cs,en,de,sk}.py` |
| Recipes | `scripts/recipes_{cs,en,de,sk}.py` |
| Label data: composition, allergens, nutrition, preparation | `scripts/product_spec.py` |
| Layout, SEO tags, JSON-LD, nav, sitemap, llms.txt, redirects | `scripts/build_site.py` |
| Styling | `assets/site.css` |
| Scroll and motion behaviour | `assets/site.js` |

Czech is the source of truth; the other three languages are translations of it.
A copy change in one language usually needs the same change in all four.

## Build and verify

```sh
python3 scripts/build_site.py       # regenerates every page; commit the output
python3 scripts/verify_refs.py      # every local src/href/url() must resolve
python3 scripts/wayback_archive.py --check   # archive intact, exit 0 = fine
python3 scripts/optimize_images.py  # resize oversized artwork to WebP
```

No dependencies outside the standard library, except Pillow for the two image
scripts. Cursor Cloud Agents get an nginx preview on port 8080 via
`.cursor/environment.json`; locally, `scripts/dev_server.sh` does the same.

Always finish with a clean `git status` after `build_site.py` — a diff there
means the committed HTML had drifted from the sources.

Render changes in a real browser before calling them done. Two rendering bugs
in this codebase were invisible in the markup and only showed up on screen: the
hero headline sat at opacity 0 on load, and an invisible scroll-film act was
swallowing clicks meant for the button beneath it.

## SITE_BASE

`build_site.py` builds every absolute URL from `SITE_BASE`, which defaults to
`https://juzlova.cz`. It feeds canonical links, hreflang alternates,
`x-default`, `sitemap.xml`, `llms.txt`, `llms-full.txt`, `site.webmanifest`,
JSON-LD `url` fields, **and the legacy redirect stubs** — which are
`<meta http-equiv="refresh">` pages carrying hardcoded absolute URLs. Get it
wrong and every old WordPress link bounces visitors off the site.

```sh
SITE_BASE=https://example.test python3 scripts/build_site.py   # for a preview host
```

## Layout

```
scripts/
  build_site.py            the generator — all pages, sitemap, llms.txt, redirects
  content_{cs,en,de,sk}.py page copy and UI strings per language
  recipes_{cs,en,de,sk}.py recipe content per language
  verify_refs.py           fails when a local reference does not resolve
  wayback_archive.py       Wayback mirror crawler; `--check` reports completeness
  make_brand_assets.py     brand/ sources -> favicons and wordmarks in img/
  optimize_images.py       resizes oversized artwork to WebP
  dev_server.sh            local nginx preview with production-like clean URLs
  cloudflare_dns.sh        DNS cutover; refuses to run without I_MEAN_IT=yes
  gcp_domain_mapping.sh    Cloud Run domain mapping + Google site verification
assets/site.css            design system, motion, brand contrast rules
assets/site.js             inertial scroll, scroll-film hero, parallax, reveals
assets/style.css           UNUSED leftover — nothing references it
img/                       web assets (see provenance below)
brand/                     the owner's four supplied source files
archive/                   full Wayback mirror: 40 pages, 56 images, CDX index
docs/HANDOFF.md            history, decisions, what is still open
index.html, en/, de/, sk/  GENERATED — do not edit
status.html                old recovery status board, unrelated to the site
```

Directories like `kakao/`, `kdo-jsme/`, `vanilkovy_puding/`, `jirina-juzlova/`
and `recepty-index/` are legacy-URL redirect stubs generated from
`LEGACY_REDIRECTS` in `build_site.py`. They keep old WordPress links working.
Do not delete them by hand.

## Images

Provenance is mixed, and it matters when deciding whether an image can be
replaced.

**The workshop's own, recovered from the Wayback mirror:**

- `kochanov-letecky.webp` — aerial of Kochánov at golden hour, the shot the old
  site ran as its background video. The scroll-film's opening frame.
- `dilna-panorama.webp` — their real production room: flour sacks, the scale,
  the bagging line. On the "Kdo jsme" page.
- `vanilkovy-cukr-pytliky.webp` — their 2012 photograph of labelled vanilla
  sugar packets, warm-toned to sit in the page palette. The `.png` beside it is
  the untoned original.
- `sisky-s-makem.png`, `strapacky.jpg`, `bebe-rezy.gif` — recipe thumbnails.

**Generated, because no usable original survived.** The recovered "product"
files turned out to show the wrong products — the file the 2012 site named
`Chlupaté-knedlíky` is a photograph of vanilla sugar, and `Vanilkový-puding` is
a bag-sealing machine — so accurate ones were made:

- `produkt-{bramborove-knedliky,chlupate-knedliky,vanilkovy-puding,kakao}.webp`
- `hruskovy-kolac.webp`, `slehackova-rolada.webp`, `domaci-pernik.webp`,
  `bramborovo-tvarohove-knedliky.webp` — four recipes the Wayback Machine has
  no working capture for.
- `hero.webp`, `workshop.webp`, `film-blizko.webp`, `film-makro.webp` — scroll
  film frames.

**Brand, from the owner's files in `brand/`:** `logo-wordmark-{black,white}.png`
swapped by contrast (black on cream pages, white over the film hero), the
navy/white favicon set, `favicon.ico`, `apple-touch-icon.png`, and
`mark-white.png` for the footer watermark. Regenerate with
`python3 scripts/make_brand_assets.py`.

Image sources arrive as multi-megabyte PNGs. Run `optimize_images.py` before
committing anything new — the four recipe photos were 36 MB before it, 315 kB
after.

## Hosting and DNS — be careful here

`www.juzlova.cz` is production, served from a Google host. The apex
`juzlova.cz` 301s to it. `docs/HANDOFF.md` carries the current records and the
history of how it got there.

- Capture the Cloudflare zone before any DNS edit. Rollback is **not** "put the
  old Shopify records back" — those are long gone.
- There is exactly one supported cutover mechanism,
  `.github/workflows/cutover-pages-dns.yml`. Do not add a competing one; two
  earlier attempts were closed as duplicates.
- Do not deploy to the Cloud Run service named `juzlova-web` — that is
  production. `deploy-cloudrun-preview.yml` exists for previews and uses a
  different service name.
- `PR #3` carries a whole parallel site — its own `assets/`, fonts, stylesheet,
  `404.html`. Do not merge it; it would collide across most of the tree.

## Ask before

DNS changes, deleting a bucket or Cloud Run service, force-pushing `main`, or
anything that changes what visitors see without a way back.
