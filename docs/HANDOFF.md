# Handoff: finishing the juzlova.cz rebuild

Written 2026-08-31 for whoever picks this up next. It covers what is deployed,
what is in this repo, where the two disagree, and what has to happen to close
the gap. Open issues reference this file rather than repeating it.

## Status update — 2026-08-31 (verified live)

The gap this doc was written to close is **already closed**: `https://juzlova.cz`
now serves the four-language `main` build. Verified by fetching the live site —
the homepage is byte-for-byte identical to the committed `index.html`, and
`/en/`, `/de/`, `/sk/` return the real translated pages (no "Tady nic nepeče"
404, no `/assets/img/...`). The `server` header is `Google Frontend`, so the new
build is served by the **Google host (Cloud Run / GCS), not GitHub Pages**; the
`www.juzlova.cz` CNAME still points at `ghs.googlehosted.com`.

Consequence: the DNS cutover to GitHub Pages described below is now a
**host-preference choice, not a content fix** — both hosts serve the same build.
Older sections (e.g. "What is live right now" describing a Czech-only site) are
historical and superseded by this note.

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

**Not done yet.** #12-#14 added `.github/workflows/cutover-pages-dns.yml`, which
performs this change, but it has never run: it needs the `CLOUDFLARE_API_TOKEN`
secret and skips itself without it. The verified note at the top of this file
confirms `www` still resolves to `ghs.googlehosted.com`.

### Canonical cutover — do not add competing workflows (2026-08-31)

There is exactly one supported cutover mechanism:
`.github/workflows/cutover-pages-dns.yml`. It sets `www.juzlova.cz` CNAME →
`adamripon-ship-it.github.io` (proxied false) using the repo secret
`CLOUDFLARE_API_TOKEN`, and skips cleanly when that secret is absent. The only
outstanding step is owner-only:

1. Create a Cloudflare API token (Zone:Read + DNS:Edit, scoped to `juzlova.cz`).
2. Add it as the repo secret `CLOUDFLARE_API_TOKEN`.
3. Run the **Cut over www to GitHub Pages** workflow (Actions → Run workflow),
   or make the single `www` CNAME edit by hand in Cloudflare.

Do **not** open new branches/PRs that add parallel cutover or Cloud-Run-hosting
workflows. Two such attempts were closed as duplicative/off-decision: the
Cloudflare-MCP variant and the "deploy `main` to Cloud Run" variant. If the
hosting decision itself changes (Pages → Cloud Run), reverse this section first,
then change the workflow — don't add a second competing one.

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

## Deploying

**The live host is Google, not GitHub Pages.** Per the verified note at the top
of this file, `www.juzlova.cz` is still CNAME `ghs.googlehosted.com` and the live
responses carry `Google Frontend`. Both hosts serve the same `main` build, so
this is a host-preference question, not a content one — but it means the Pages
path below is not yet what the public hits.

GitHub Pages is configured and ready: `CNAME` holds `www.juzlova.cz`, `.nojekyll`
stops Jekyll touching the tree, and the build output is committed, so a push to
`main` is a Pages deploy. It becomes the live host only once the `www` record
moves (see *Canonical cutover* above).

Nothing in this repo deploys to the Google host. `deploy-gcp.yml` targeted a GCS
bucket and skipped itself for want of secrets; `deploy-cloudrun-preview.yml` was
dispatch-only and aimed at `juzlova-main-preview`, never at production
`juzlova-web`. Whatever put the current build on the Google host was done outside
this repo.

**Removed on this branch, pending the cutover.** `deploy-gcp.yml`,
`deploy-cloudrun-preview.yml`, `Dockerfile`, `nginx.conf`, `.dockerignore`,
`.gcloudignore`, `docs/DEPLOY-GCP.md`, `scripts/cloudflare_dns.sh` and
`scripts/gcp_domain_mapping.sh`. Note the caveat: while the domain still points
at the Google host, `Dockerfile` + `nginx.conf` are the only in-repo recipe for
the container that host runs, and `cloudflare_dns.sh` is the one-command way back
to today's DNS if a Pages cutover has to be rolled back. Git history keeps all of
them, but the safer sequence is to land the cutover first and remove this tooling
after. `scripts/dev_server.sh` is unaffected — it writes its own nginx config
inline and never read the root `nginx.conf`.

PR #3 remains open and carries a complete second, Czech-only site — its own
`assets/`, fonts, images, stylesheet and `404.html`. Merging it into `main` would
collide across most of the tree. Do not merge it.

## DNS

Re-read from the public resolvers on 2026-08-31. The Shopify records recorded
in PR #3 are **no longer authoritative**.

| Record | Value now | Stale value from PR #3 |
|---|---|---|
| Nameservers | `sam.ns.cloudflare.com`, `elly.ns.cloudflare.com` | same |
| `juzlova.cz` A | `172.217.222.121` (Google; apex 301s to `www`) | `23.227.38.65` (Shopify) |
| `www.juzlova.cz` | CNAME `ghs.googlehosted.com` | CNAME `shops.myshopify.com` |

Rollback is therefore **not** "put Shopify back". Capture the current
Cloudflare zone before any edit.

GitHub issues its certificate over an unproxied record, so the Cloudflare `www`
record has to stay grey-cloud until the certificate is provisioned, then go
orange with SSL/TLS set to Full (strict).

## What only the owner can do

- **DNS cutover (this is what makes juzlova.cz serve `main`).** In Cloudflare,
  edit `www.juzlova.cz` from CNAME `ghs.googlehosted.com` to CNAME
  `adamripon-ship-it.github.io`, grey cloud. Leave the apex as-is — it already
  301s to `www`.
- Add `CLOUDFLARE_API_TOKEN` (Zone:Read + DNS:Edit on juzlova.cz) if you want
  `.github/workflows/cutover-pages-dns.yml` to make that change instead. It
  skips itself when the secret is absent.

With the workflows above removed, `GCP_SA_KEY`, `GCP_PROJECT` and `GCS_BUCKET`
are read by nothing in this repo. Confirm the Google host is genuinely retired
before deleting them from repository settings — the domain still points there.

## Known limits

- The scroll hero scrubs still keyframes rather than video frames. Slicing a
  real clip needs a paid Higgsfield plan; the code path is the same either way.
- `img/vanilkovy-cukr-pytliky.webp` is the workshop's own 2012 photograph of
  their labelled packets, warm-toned to sit in the page palette. The four other
  product photographs are generated, because the recovered files for those
  products turned out to show the wrong products.
