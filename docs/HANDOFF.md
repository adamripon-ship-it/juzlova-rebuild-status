# Handoff: finishing the juzlova.cz rebuild

Written 2026-08-31 for whoever picks this up next. It covers what is deployed,
what is in this repo, where the two disagree, and what has to happen to close
the gap. Open issues reference this file rather than repeating it.

## The situation in one paragraph

Two different rebuilds of juzlova.cz exist. One is live on the real domain and
is Czech-only. The other is on `main` in this repo, has four languages, and is
served from GitHub Pages. Neither is a draft — both are finished work, built in
parallel by separate sessions that could not see each other. Before any deploy
work happens, somebody has to decide which one juzlova.cz should serve.

## What is live right now

`https://juzlova.cz` serves a working Czech site. Checked 2026-08-31 by
fetching the homepage and `/en/`.

It is not the build on `main`. Its assets live under `/assets/img/...`, its
404 page reads "Tady nic nepeče", its nav orders products
Chlupaté → Kakao → Vanilínový cukr → Vanilkový puding → Bramborové, and four
recipe cards carry the placeholder "Fotografie se z archivu nepodařilo
obnovit". All four details match the diff in PR #3 exactly, so production is
almost certainly running that branch. Confirm the host before touching DNS —
nobody has recorded where it is deployed.

Two gaps against the brief the owner gave:

- **`/en/` returns the Czech 404 page.** There is no English, German or Slovak
  version. The brief asked for all four, fully translated, with a language
  selector and per-language metadata.
- **Four recipes show a "photo could not be recovered" placeholder** — pear
  tart, whipped-cream roulade, gingerbread, and potato-quark dumplings with
  strawberries.

## What is on `main`

Built by `python scripts/build_site.py`, no dependencies outside the standard
library, output committed to the repo root. Served at
`https://adamripon-ship-it.github.io/juzlova-rebuild-status/`.

- 68 pages across Czech (root), `en/`, `de/`, `sk/`, with a language selector,
  hreflang plus `x-default`, and localised titles and descriptions.
- `sitemap.xml` (72 URLs, 360 hreflang alternates), `robots.txt`, `llms.txt`
  and `llms-full.txt`.
- JSON-LD: Organization, Product with Offer, Recipe, FAQPage, BreadcrumbList.
- The owner's wordmark and monogram, swapped by contrast, plus a full favicon
  set in navy and white and a web manifest.
- A scroll-driven film hero that opens on the recovered aerial of Kochánov.
- All seven recipes have photographs; all five products show the right product.
- `archive/` holds the full Wayback mirror: 40 pages, 56 images, 16 other
  files, no failures. `scripts/wayback_archive.py --check` verifies it.

### Building and checking it

```sh
python scripts/build_site.py                 # writes the site into the repo root
python scripts/wayback_archive.py --check    # archive completeness, exit 0 = fine
python scripts/optimize_images.py            # resizes oversized art to WebP
```

`build_site.py` reads `SITE_BASE` from the environment and falls back to the
GitHub Pages URL. Every canonical URL, hreflang alternate, sitemap entry,
JSON-LD `url` and `llms.txt` link is built from it, so the production domain
has to be passed in at cutover:

```sh
SITE_BASE=https://juzlova.cz python scripts/build_site.py
```

Copy lives in `scripts/content_{cs,en,de,sk}.py` and
`scripts/recipes_{cs,en,de,sk}.py`. Czech is the source of truth.

## Three deploy proposals, one of which shipped

| | Where | Serves | State |
|---|---|---|---|
| `.github/workflows/deploy-gcp.yml` on `main` | GCS bucket, europe-central2 (Warsaw) | the `main` build | merged, skips itself until secrets exist |
| PR #2 | Cloud Run, europe-west3 (Frankfurt) | whatever the repo holds | open, adds `Dockerfile` + `nginx.conf` only |
| PR #3 | Cloud Run, europe-west3, with automated Cloudflare DNS cutover | its own parallel site build | open, appears to be what production runs |

They differ on two axes that should be decided separately.

**Which site.** PR #3 carries a complete second site — its own `assets/`,
fonts, images, stylesheet and `404.html`. Merging it into `main` would collide
with the build there across most of the tree. This is the decision that
matters; the hosting question is minor next to it.

**Which host.** Warsaw is nearer Czechia than Frankfurt, but both are one hop
away and the difference will not be visible to a visitor. A bucket is cheaper
and simpler for a static site; Cloud Run gives clean URLs and cache headers
through nginx without a load balancer. PR #3 is the only one that also
automates the Cloudflare DNS change.

Recommendation, for whoever decides: keep the `main` build, because it meets
the four-language brief and production does not, and take PR #3's DNS
automation (`scripts/cloudflare_dns.sh`, `scripts/gcp_domain_mapping.sh`)
rather than its site. That reduces the merge to two small scripts instead of a
whole tree.

## DNS

From PR #3, verified by that session on 2026-08-31 and not re-checked here —
confirm before relying on it:

| Record | Value |
|---|---|
| Nameservers | `sam.ns.cloudflare.com`, `elly.ns.cloudflare.com` |
| `juzlova.cz` A | `23.227.38.65` (Shopify) |
| `www.juzlova.cz` | CNAME `shops.myshopify.com` |

Those Shopify records cannot still be authoritative, since the domain serves a
Google-hosted site today. Re-read the live zone first.

Google issues its managed certificate over an unproxied record, so a Cloudflare
record has to stay grey-cloud until the certificate is provisioned, then go
orange with SSL/TLS set to Full (strict).

## What only the owner can do

- Add the repository secrets. `deploy-gcp.yml` on `main` wants `GCP_SA_KEY`,
  `GCP_PROJECT` and `GCS_BUCKET`; PR #3's workflow wants `GCP_SA_KEY`,
  `GCP_PROJECT_ID` and `CLOUDFLARE_API_TOKEN`. The names differ — match them to
  whichever workflow survives.
- Decide which site juzlova.cz serves.

Until the secrets exist the deploy workflow skips itself and GitHub Pages keeps
serving `main`, so nothing breaks in the meantime.

## Known limits

- The scroll hero scrubs still keyframes rather than video frames. Slicing a
  real clip needs a paid Higgsfield plan; the code path is the same either way.
- `img/vanilkovy-cukr-pytliky.webp` is the workshop's own 2012 photograph of
  their labelled packets, warm-toned to sit in the page palette. The four other
  product photographs are generated, because the recovered files for those
  products turned out to show the wrong products.
