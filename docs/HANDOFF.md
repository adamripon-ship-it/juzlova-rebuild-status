# Handoff: finishing the juzlova.cz rebuild

Written 2026-08-31 for whoever picks this up next. It covers what is deployed,
what is in this repo, where the two disagree, and what has to happen to close
the gap. Open issues reference this file rather than repeating it.

## Decision (2026-08-31)

The owner picked **Option 1: serve the `main` build** on juzlova.cz — four
languages, recovered photos, the workshop's own marks. Do **not** merge PR #3.
Its site stays as the previous production copy until DNS moves off Cloud Run.

`scripts/build_site.py` now defaults `SITE_BASE` to `https://juzlova.cz`. The
committed HTML, sitemap, llms.txt and redirect stubs use that domain.

To finish the cutover, point `www.juzlova.cz` at GitHub Pages (one Cloudflare
record). Apex already 301s to `www`, so that single change is enough:

| Record | Change to | Proxy |
|---|---|---|
| `www.juzlova.cz` CNAME | `adamripon-ship-it.github.io` | DNS only (grey cloud) until GitHub's certificate is issued |

Do not run `scripts/cloudflare_dns.sh` for this — that script still aims at
`ghs.googlehosted.com`, which is where production is today.

## The situation in one paragraph

Two different rebuilds of juzlova.cz exist. One is live on the real domain and
is Czech-only. The other is on `main` in this repo, has four languages, and is
served from GitHub Pages. The owner chose `main`. The remaining step is the
DNS flip above; until then juzlova.cz still serves the Czech-only Cloud Run
copy.

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
`2026-08-31 05:01:02 GMT`. Do not deploy a preview to a service named
`juzlova-web` — that is almost certainly what production is. Use a different
service name (`juzlova-main-preview`) until issue #7 is decided.

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

## Three deploy proposals, one of which shipped

| | Where | Serves | State |
|---|---|---|---|
| `.github/workflows/deploy-gcp.yml` on `main` | GCS bucket, europe-central2 (Warsaw) | the `main` build | merged, skips itself until secrets exist |
| `.github/workflows/deploy-cloudrun-preview.yml` | Cloud Run `juzlova-main-preview`, europe-west3 | the `main` build | dispatch-only; will not overwrite live `juzlova-web` |
| PR #2 | Cloud Run, europe-west3 (Frankfurt) | whatever the repo holds | open; its `Dockerfile` + `nginx.conf` are now on this tree |
| PR #3 | Cloud Run, europe-west3, with automated Cloudflare DNS cutover | its own parallel site build | open, appears to be what production runs — do not merge |

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

- **Connect the DNS-capable Cloudflare MCP.** Bindings (`bindings.mcp.cloudflare.com`)
  cannot edit DNS records. The project MCP config in `.cursor/mcp.json` points at
  Cloudflare's API MCP (`https://mcp.cloudflare.com/mcp`), which can. In Cursor:
  Settings → MCP → **cloudflare-api** → Connect / Sign in. Grant Zone DNS Edit
  for `juzlova.cz`. This is Cloudflare's official remote MCP, not Runlayer.
- **Add `CLOUDFLARE_API_TOKEN`** so `.github/workflows/cutover-pages-dns.yml`
  can flip `www` without the dashboard. Create a zone-scoped token
  (Zone:Read + DNS:Edit on `juzlova.cz`) at
  [API Tokens](https://dash.cloudflare.com/profile/api-tokens), then store it as
  a [repo Actions secret](https://github.com/adamripon-ship-it/juzlova-rebuild-status/settings/secrets/actions)
  named `CLOUDFLARE_API_TOKEN`. Re-run **Cut over www to GitHub Pages**.
- **DNS cutover (this is what makes juzlova.cz serve `main`).** Edit only
  `www.juzlova.cz` from CNAME `ghs.googlehosted.com` to CNAME
  `adamripon-ship-it.github.io`, grey cloud. Leave the apex as-is — it already
  301s to `www`. Prefer the MCP or the token+workflow above.
- Add the repository secrets if you still want the GCS / Cloud Run path:
  `GCP_SA_KEY`, `GCP_PROJECT`, `GCS_BUCKET`.

Until the secrets exist the deploy workflow skips itself and GitHub Pages keeps
serving `main`, so nothing breaks in the meantime.

A dispatch-only workflow, `.github/workflows/deploy-cloudrun-preview.yml`,
deploys `main` to a Cloud Run service named `juzlova-main-preview`. That is
the safe way to get a Google host URL for issue #8 without touching the
live `juzlova-web` mapping.

## Known limits

- The scroll hero scrubs still keyframes rather than video frames. Slicing a
  real clip needs a paid Higgsfield plan; the code path is the same either way.
- `img/vanilkovy-cukr-pytliky.webp` is the workshop's own 2012 photograph of
  their labelled packets, warm-toned to sit in the page palette. The four other
  product photographs are generated, because the recovered files for those
  products turned out to show the wrong products.
