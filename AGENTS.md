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
| Layout, SEO tags, JSON-LD, nav, sitemap, llms.txt, redirects | `scripts/build_site.py` |
| Styling | `assets/site.css` |
| Scroll and motion behaviour | `assets/site.js` |

Czech is the source of truth; the other three languages are translations of it.
A copy change in one language usually needs the same change in all four.

## Editorial bans (owner)

- **Never** name ingredient suppliers (cocoa or otherwise), and **never** add
  FAQ/copy that says we refuse to name them (“Do you name the cocoa supplier?”
  / “Uvádíme jen typ…”). Stay silent on suppliers; describe product type and
  specs only.

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

## How a change goes live

GitHub is the whole workflow. Nobody needs Google Cloud, Cloudflare or server
access to change the site.

1. Branch off `main`, edit the sources, run `build_site.py`, commit the
   sources **and** the regenerated HTML together.
2. Open a pull request. `build-check.yml` rebuilds from scratch and fails if
   the committed HTML is stale or a local reference is broken.
3. Merge to `main`. `deploy-cloudrun.yml` rebuilds with
   `SITE_BASE=https://www.juzlova.cz`, deploys Cloud Run `juzlova-web`
   (europe-west4) and smoke-tests it. Live in about two minutes.
4. Check the live page. The run summary shows a `Not deployed` warning if the
   repository variables `GCP_PROJECT`, `GCP_WIF_PROVIDER` and `GCP_DEPLOY_SA`
   were ever removed; it can still look green in that case.

Live HTML differs from the repo by exactly one line: the server injects the
Cloudflare analytics `<script>` at container start
(`server/inject-analytics.py`). Everything else is byte-identical to `main`.

Bump `ASSET_VER` in `build_site.py` whenever `site.css` or `site.js` changes,
or returning visitors keep the cached old file.

### What is not in the repository

Only runtime secrets, held as environment variables on the Cloud Run service
and never committed. `.env.example` lists every name. Site edits need none of
them; locally the contact and ratings API fall back to a directory and the
optional extras switch themselves off.

| Variable | Feeds |
|---|---|
| `ZAPIER_WEBHOOK_URL`, `SMTP_*` or `FORMSPREE_*` | delivery of contact-form messages to `CONTACT_TO` |
| `TURNSTILE_SITE_KEY` | optional captcha on the contact form |
| `CLOUDFLARE_WEB_ANALYTICS_TOKEN`, `GOOGLE_ANALYTICS_MEASUREMENT_ID` | visitor analytics |
| `DATA_BUCKET` | GCS bucket for ratings and the contact inbox |

The owner manages those in Google Cloud; changing them is not a code change.

## URLs, slugs and redirects (2026-09-16)

- Every page has a stable **page id** (`kdo_jsme`, `bramborove_knedliky`, a
  recipe's historical Czech slug…). The public slug is looked up per language in
  `SLUGS` in `scripts/build_site.py` — exact keyword translations, hyphens only,
  no brand or personal names (`/de/kartoffelknoedel-mischung/`,
  `/en/potato-dumpling-mix/`, `/sk/zemiakove-knedle-v-prasku/`).
- hreflang uses region codes (`cs-CZ`, `sk-SK`, `de-DE` + `de-AT` on the same
  URL, `en`, `x-default` → Czech). Canonical, hreflang and sitemap URLs are the
  same string by construction (`url_of(lang, pid)`).
- Local landing pages (`vysocina`, `humpolec`, `velkoobchod-*`…) are **Czech
  only**: not built for en/de/sk, no hreflang set, not in the foreign sitemaps.
- Renaming a slug: change `SLUGS`, add the old slug to `LEGACY_REDIRECTS`,
  rebuild. The build writes meta-refresh stubs at every old path plus
  `redirects.conf` (nginx `rewrite … permanent`, included by `nginx.conf`) and
  `_redirects` (Netlify). Never delete an old directory by hand.
- WordPress-era URLs that never had a localized page go in `WP_REDIRECTS`
  (root only, nginx + Netlify rules, no stubs). Dead WordPress machinery, theme
  demo posts, feeds, `/archive/` and `status.html` are in `GONE_PREFIXES` /
  `GONE_PATHS` and answer **410**. Do not add them back to robots.txt as
  `Disallow` — Google would stop seeing the 410 and list them as "Blocked by
  robots.txt" forever. `WORDPRESS/feed/` of any page 301s to that page.
- Messaging rules and the copy rationale live in `docs/messaging/`. Keep one
  H1 per page, one primary CTA (call Jiřina), each fact once per page, no
  taste claims ("k nerozeznání"), no supermarket multipliers, no invented
  scores. Each page owns its own FAQ; the home page has none.

## SITE_BASE

`build_site.py` builds every absolute URL from `SITE_BASE`, which defaults to
`https://www.juzlova.cz`, the production host (the apex 301s there). It feeds canonical links, hreflang alternates,
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
docs/messaging/            copy rules and page-by-page copy rationale
index.html, en/, de/, sk/  GENERATED — do not edit
redirects.conf, _redirects GENERATED — nginx and Netlify redirect rules
server/                    contact + ratings API and analytics injection (Cloud Run)
data/                      ratings seed and review data for the API
Dockerfile, nginx.conf     the production image deployed by deploy-cloudrun.yml
netlify/, netlify.toml     unused Netlify fallback; not what serves the domain
status.html                old recovery status board; answers 410 in production
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
- The 2012 photograph of labelled vanilla-sugar sachets is retired: the
  workshop sells kilo bags only, so `vanilkovy-cukr-kilo.webp` replaced it and
  nginx 301s the old `vanilkovy-cukr-pytliky.*` paths there.
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
- Do not deploy to the Cloud Run service named `juzlova-web` by hand — that is
  production, and merging to `main` already deploys it. `deploy-cloudrun-preview.yml`
  exists for previews and uses a different service name.
- `PR #3` carries a whole parallel site — its own `assets/`, fonts, stylesheet,
  `404.html`. Do not merge it; it would collide across most of the tree.

## Ask before

DNS changes, deleting a bucket or Cloud Run service, force-pushing `main`, or
anything that changes what visitors see without a way back.
