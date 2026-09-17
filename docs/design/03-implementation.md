# 03 · Phase 3 — the rev. 5 design in the real site

Implemented 2026-09-17. The specimen (`samples/01-specimen.html`) was ported
into the generator and the two shipped assets; nothing on the site is hand-edited.

## What changed, where

| File | Change |
|---|---|
| `assets/site.css` | Rewritten to the brand system: tokens (gold `#D4AF37`, white, ink `#1A1A1A`, grey `#767676`, teal focus ring `#094853`), Fraunces + Geologica via `@font-face`, root type scale 16/17/19/22/30 px by viewport, buttons with the fill sweep (gold / white-on-gold / outline-on-gold / ink ghost), bands, silhouettes, masks, cut-outs, wind keyframes, reference footer, and the restyle of every existing component (forms, price board, reviews, team, B2B tiles, cocoa radar, ratings, consent). Every class the generator emits kept its name. No side-stripe borders, no cream tints. |
| `assets/site.js` | Inertial scroll and the scroll-film are gone. Added: reveals with sibling stagger, count-up numerals, leaves attached along vine paths, per-element wind timing, stroke-draw, parallax (fine pointers only), marquee with hover/focus pause and a pause button. Kept: phone menu, product accordion, contact/newsletter/call-back form posting, cocoa animation, recipe ratings, carousel, Google Analytics consent. `?static=1` freezes motion for captures; `prefers-reduced-motion` switches it all off. |
| `assets/fonts/` | `fraunces-var.woff2` (82 KB), `geologica-var.woff2` (29 KB), OFL licences. Preloaded from `shell()`. |
| `assets/botanicals/sprite.svg` | One cached external sprite with the twelve white silhouettes. Pages reference symbols with `<use href="…sprite.svg#sil-…">`. |
| `scripts/build_site.py` | `PRODUCT_OBJECT` (product → potato / wheat / vanilla / cocoa / sugarcane), `MASKS` parsed from the sprite and inlined per page through `defs_html()` (home: cocoa, vanilla, potato; product pages: their own), `sil()`, `shape_html()`, `cutout_html()`, header CTA in `nav()`, new `footer()` with the call-back form, new `build_home()`, product object panel + cocoa origin capsule and FAQ in `build_product()`, cocoa origin line in `llms-full.txt`. `TODAY` 2026-09-17, `ASSET_VER` 20260917a, `theme-color` gold. |
| `scripts/cocoa_origin.py` | Capsule, three FAQ pairs, flower caption and llms line in cs/en/de/sk (from `docs/messaging/07`). No supplier names. |
| `scripts/content_{cs,en,de,sk}.py` | Appended rev. 5 strings: split H1 (`h1_main` + `h1_sub`), six stat labels, journey heading and five steps, footer marks, call-back form (`cb_*`), short header CTA, marquee labels, cut-out alt texts. |
| `nginx.conf` | `charset utf-8`, `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`, HSTS; fonts cached one year immutable; woff2 in gzip types. |

## Decisions worth knowing

- **Photos inside the masks are real `<img>` elements** (not CSS backgrounds), so they keep `alt`, `width`/`height` (no layout shift) and stay indexable. The mask (`clip-path`) sits on a wrapper span; zoom and focal point are `--zoom` / `--pos` custom properties; the drop shadow sits on a second wrapper because a filter and a clip on the same element would clip the shadow.
- **Silhouettes are external, masks are inline.** Browsers do not resolve `clip-path` to another document reliably, so each page inlines only the 3–20 KB of masks it uses. Symbols are shared through the cached sprite.
- **Rotated art carries `data-rotate`.** The parallax script rewrites `transform`; without the attribute the rotation was lost after the first scroll tick (a specimen bug that static captures hid).
- **Call-back form reuses `/api/contact`** with `type=contact`, a required name and phone (≥ 9 digits client-side), a hidden message and `buyer=household`. No server change.
- **Marquee** is a `<nav>` of product links; the second copy is `aria-hidden` and untabbable; a pause button satisfies WCAG 2.2.2 for touch and keyboard users. 
- **Header**: drawer below 1200 px with the short CTA ("Zavolat") always visible; inline nav from 1200 px; the long CTA from 1440 px. Language switcher is text (cs en de sk), flags hidden.
- **Home structure**: gold hero → white stats with product outlines and product links → gold journey → white recipes → gold why band → white delivery + reviews → newsletter → footer with call-back. The carousel, B2B/EU teaser bands and the closing CTA band were folded into these (each fact once; the why band's buttons lead to "Pro kuchyně" and "Kde nás najdete", the delivery block links to EU shipping).
- **Buttons on gold** follow the owner's instruction (white fill + gold text; white outline + white text) and are recorded as the AA exception in `01-brand-identity.md` §3.2d.

## Regenerate

```bash
python3 scripts/build_site.py && python3 scripts/verify_refs.py
```

## QA

See section "QA record" below (filled in after the build and again after the production deploy).

## QA record

**Local build, 2026-09-17** (`python3 scripts/build_site.py` → 279 pages, `verify_refs.py` 0 broken references).
Captures in `qa/` (headless Chrome, `?static=1`, halved for the repo):

| Check | Result |
|---|---|
| Home cs 1440 | Hero, split H1, white/outline buttons, cocoa-pod cut-out, marquee with icons and pause button, stats with three masked product photos, product links, journey wave with attached leaves and vanilla cut-out, recipes row, why band with vines, leaves, cocoa silhouette and banana-leaf cut-out, delivery + reviews, newsletter, reference footer with call-back form |
| Home de 1440 | Longest language: two-line H1, nav fits, long header CTA |
| Home cs 1280 | Inline nav with the short CTA ("Zavolat") |
| Home cs 390 | Drawer header with CTA + toggle, stacked buttons, cut-out below, single-column stats, stacked shapes; hero accents hidden on phones |
| Kakao 1440 | Gold object panel: cocoa silhouette backdrop + masked photo; price card; flower cut-out with caption; origin capsule; six FAQ entries |
| Structure | No duplicate ids, every image has alt, one H1 per page, heading order h1 → h2 → h3 |
| Sitemaps, redirects, robots | Changed only by `lastmod`; redirect rules identical |

Defects found and fixed before the commit: the external sprite lacked an `<svg>` root (every `<use>` failed silently); article heading rules outranked component headings (fixed with `:where()`); rotated art lost its rotation under parallax (`data-rotate`); phone hero accents collided with the tagline and the pause button (hidden below 700 px).

**Production, 2026-09-17** — commit `6eb67df` pushed to GitHub (build-check green) and deployed by hand to Cloud Run `juzlova-web`, europe-west4, revision `juzlova-web-00045-kgn` (the GitHub deploy job still skips: `GCP_SA_KEY` / `GCP_PROJECT` are not set).

| Live check | Result |
|---|---|
| Statuses | `/`, `/en/`, `/de/`, `/sk/`, price list, product, recipe index, FAQ, sitemaps, robots, llms.txt, llms-full.txt, CSS, JS, sprite, fonts, cut-outs, product photos: all 200 with `charset=utf-8` |
| Redirects | `/en/bramborove_knedliky/` → 301 → `/en/potato-dumpling-mix/`; `/bramborove_knedliky/` → 301 → `/bramborove-knedliky-v-prasku/` |
| Headers | `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`, HSTS on every response; fonts `max-age=31536000, immutable` |
| Home HTML | `site.css?v=20260917a`; hreflang cs-CZ, sk-SK, de-DE, de-AT, en, x-default; JSON-LD Organization/LocalBusiness/FoodManufacturer, WebSite, WebPage, ItemList with five Products and Offers; three inline masks; 12 marquee links; none of the banned words |
| Cocoa page | Six FAQ entries, origin capsule, flower figure; `llms-full.txt` carries the origin line |
| Rendering | Real Chrome on the live host: Fraunces and Geologica loaded, all sprite `<use>` elements have a bounding box, 11 leaves attached to vines; captures `qa/2026-09-17-live-*.png` |
| Lighthouse (home, `qa/2026-09-17-lighthouse-*.json`) | Desktop 98 / 100 / 100 / 100, LCP 1.0 s, CLS 0. Mobile 90 / 100 / 100 / 100, LCP 3.7 s, CLS 0.014 (performance, accessibility, best practices, SEO) |

Follow-ups, not blocking: a lighter phone-size variant of the hero cut-out would pull the mobile LCP under 2.5 s; `http://juzlova.cz/` still takes two hops (Cloudflare 302 to https, then nginx 301 to www), which is a Cloudflare rule the owner controls; the language switcher's `aria-label` (full language name) differs from its visible text (code), flagged by Lighthouse as informative.
