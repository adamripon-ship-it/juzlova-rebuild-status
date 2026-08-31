# Handoff: finishing the juzlova.cz rebuild

Written 2026-08-31 for whoever picks this up next. It covers what is deployed,
what is in this repo, where the two disagree, and what has to happen to close
the gap. Open issues reference this file rather than repeating it.

## Decision (2026-08-31)

The owner picked **Option 1: serve the `main` build** on juzlova.cz — four
languages, recovered photos, the workshop's own marks. Do **not** merge PR #3.
Host that build on **Google Cloud Run**, which already serves the domain.
Do **not** CNAME `www` to `adamripon-ship-it.github.io`.

`scripts/build_site.py` now defaults `SITE_BASE` to `https://juzlova.cz`. The
committed HTML, sitemap, llms.txt and redirect stubs use that domain.

Cutover is a Cloud Run deploy of `main` onto the existing service
(`juzlova-web`, europe-west3). DNS stays CNAME `ghs.googlehosted.com`.
See [`docs/DEPLOY-GCP.md`](DEPLOY-GCP.md).

## The situation in one paragraph

Two different rebuilds of juzlova.cz exist. One is live on the real domain and
is Czech-only. The other is on `main` in this repo, has four languages, and is
served from GitHub Pages. The owner chose `main` on Google Cloud. Until `GCP_SA_KEY` and
`GCP_PROJECT` exist, juzlova.cz still serves the Czech-only Cloud Run copy.

## What is live right now

`https://juzlova.cz` serves a working Czech site. Re-checked 2026-08-31
(second session) by fetching the homepage, `/en/`, `/de/`, `/sk/` and
`/chlupate-knedliky/`, plus DNS.

It is not the build on `main`. Its assets live under `/assets/img/...`, its
404 page reads "Tady nic nepeče", its nav orders products
Chlupaté → Kakao → Vanilínový cukr → Vanilkový puding → Bramborové, and four
recipe cards carry the placeholder "Fotografie se z archivu nepodařilo
obnovit". `/de/` and `/sk/` also return that Czech 404. All of that matches
the diff in PR #3 exactly, so production is almost certainly running that
branch.

**Where it is hosted.** The apex `301`s to `https://www.juzlova.cz/`. The
`www` host is CNAME `ghs.googlehosted.com` and both answers come from
`Google Frontend`. That is a Cloud Run custom-domain mapping, last-modified
`2026-08-31 05:01:02 GMT`. That service is almost certainly `juzlova-web`.
Issue #7 is decided (`main` wins), so the four-language image should be
deployed **onto** `juzlova-web`. Use `juzlova-main-preview` only as a
scratch service.

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
python3 scripts/build_site.py                 # writes the site into the repo root
python3 scripts/wayback_archive.py --check    # archive completeness, exit 0 = fine
python3 scripts/verify_refs.py                # local src/href/url() must resolve
python3 scripts/optimize_images.py            # resizes oversized art to WebP
```

`build_site.py` reads `SITE_BASE` from the environment and defaults to
`https://juzlova.cz`. Every canonical URL, hreflang alternate, sitemap entry,
JSON-LD `url` and `llms.txt` link is built from it.

Copy lives in `scripts/content_{cs,en,de,sk}.py` and
`scripts/recipes_{cs,en,de,sk}.py`. Czech is the source of truth.

## Deploy paths

| | Where | Serves | State |
|---|---|---|---|
| `.github/workflows/deploy-cloudrun.yml` | Cloud Run `juzlova-web`, europe-west3 | the `main` build | **production path**; needs `GCP_SA_KEY` + `GCP_PROJECT` |
| `.github/workflows/deploy-gcp.yml` on `main` | GCS bucket, europe-central2 (Warsaw) | the `main` build | optional; skips until `GCS_BUCKET` exists |
| PR #3 | Cloud Run, europe-west3 | its own parallel site | closed; still what production runs until `juzlova-web` is redeployed |

DNS for `www` stays on Google (`ghs.googlehosted.com`). The Pages DNS cutover
workflow was removed so a Cloudflare token cannot point the domain at
github.io by accident.

## DNS

Re-read from the public resolvers on 2026-08-31. The Shopify records recorded
in PR #3 are **no longer authoritative**.

| Record | Value now | Stale value from PR #3 |
|---|---|---|
| Nameservers | `sam.ns.cloudflare.com`, `elly.ns.cloudflare.com` | same |
| `juzlova.cz` A | `172.217.222.121` (Google; apex 301s to `www`) | `23.227.38.65` (Shopify) |
| `www.juzlova.cz` | CNAME `ghs.googlehosted.com` | CNAME `shops.myshopify.com` |

Rollback is therefore **not** "put Shopify back". Capture the current
Cloudflare zone before any edit. The two scripts from PR #3
(`scripts/cloudflare_dns.sh`, `scripts/gcp_domain_mapping.sh`) are in this
repo for issue #9; they refuse to run unless `I_MEAN_IT=yes` is set.

Google issues its managed certificate over an unproxied record, so a Cloudflare
record has to stay grey-cloud until the certificate is provisioned, then go
orange with SSL/TLS set to Full (strict).

## What only the owner can do

- **Put `main` on the live Cloud Run service.** In
  [Google Cloud Console → Cloud Run](https://console.cloud.google.com/run)
  open the project that already serves `www.juzlova.cz`. Create a service
  account with **Cloud Run Admin** + **Service Account User**, download a
  JSON key, and add GitHub secrets `GCP_SA_KEY` and `GCP_PROJECT`. Then run
  **Deploy latest main to Cloud Run**. Leave Cloudflare DNS on
  `ghs.googlehosted.com`.
- Optional GCS path still wants `GCS_BUCKET` as well.

## Known limits

- The scroll hero scrubs still keyframes rather than video frames. Slicing a
  real clip needs a paid Higgsfield plan; the code path is the same either way.
- `img/vanilkovy-cukr-pytliky.webp` is the workshop's own 2012 photograph of
  their labelled packets, warm-toned to sit in the page palette. The four other
  product photographs are generated, because the recovered files for those
  products turned out to show the wrong products.
