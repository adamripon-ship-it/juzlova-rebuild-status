# juzlova.cz — where things stand

Last verified 2026-08-31 by fetching the live site. For how to work on the
code, read [`AGENTS.md`](../AGENTS.md); this file is history and open questions.

## The site is live, in four languages

`https://www.juzlova.cz` serves the `main` build. Verified by fetching `/en/`:
it returns the real English page — English navigation, the CS/EN/DE/SK selector,
the brand wordmark at `img/logo-wordmark-black.png`, the corrected product
photographs at `img/produkt-*.webp`, and all seven recipe thumbnails. `/de/` and
`/sk/` likewise.

The apex `juzlova.cz` 301s to `www`. Responses come from `Google Frontend`, so
`www` is a Google host (Cloud Run domain mapping), not GitHub Pages.

Earlier revisions of this file described juzlova.cz as serving a Czech-only site
with missing recipe photos, and said the four-language build was still waiting
on a DNS flip. That was true when written and is not true now. Those sections
have been removed rather than left to contradict this one.

## How it got here

Two rebuilds existed, built in parallel by sessions that could not see each
other: a Czech-only one (PR #3) and the four-language one on `main`.

The owner chose `main` — four languages, recovered photographs, the workshop's
own marks — and it was cut over in #11. **PR #3 must not be merged.** It carries
a complete second site, its own `assets/`, fonts, stylesheet and `404.html`, and
would collide across most of the tree.

`scripts/build_site.py` now defaults `SITE_BASE` to `https://juzlova.cz`, and
the committed HTML, sitemap, `llms.txt` and redirect stubs all use it.

## Open: canonical URLs point at a redirect

Every canonical link, hreflang alternate and sitemap entry points at the apex:

```html
<link rel="canonical" href="https://juzlova.cz/en/">
```

But production serves on `www.juzlova.cz`, and the apex 301s there. So every
canonical URL we publish redirects before it resolves. Search engines follow it,
but a canonical should name the final URL, not a hop to it.

Two ways to fix it, and they are not equivalent:

1. **Make `www` canonical.** Set `SITE_BASE=https://www.juzlova.cz`, rebuild,
   commit. Changes every URL in every page, the sitemap, `llms.txt` and the
   redirect stubs. Matches where the site is actually served.
2. **Make the apex canonical.** Leave `SITE_BASE` alone and flip the redirect so
   `www` 301s to the apex instead. One DNS/host change, no content churn, but
   the apex has to serve directly.

This is a preference about which hostname the brand uses, so it needs the
owner's answer before either is implemented. Tracked as an issue.

## DNS

Read from public resolvers on 2026-08-31. The Shopify records that older notes
mention are long gone — rollback is **not** "put Shopify back". Capture the
Cloudflare zone before any edit.

| Record | Value |
|---|---|
| Nameservers | `sam.ns.cloudflare.com`, `elly.ns.cloudflare.com` |
| `juzlova.cz` A | `172.217.222.121` (Google; 301s to `www`) |
| `www.juzlova.cz` | CNAME `ghs.googlehosted.com` |

Google issues its managed certificate over an unproxied record, so a Cloudflare
record stays grey-cloud until the certificate is provisioned, then goes orange
with SSL/TLS at Full (strict).

### One cutover mechanism only

`.github/workflows/cutover-pages-dns.yml` is the single supported way to move
`www` to GitHub Pages. It skips cleanly without the `CLOUDFLARE_API_TOKEN`
secret. Two competing attempts — a Cloudflare-MCP variant and a "deploy `main`
to Cloud Run" variant — were closed as duplicative. If the hosting choice
itself changes, revise this section first, then change that workflow. Do not
add a second one.

`scripts/cloudflare_dns.sh` and `scripts/gcp_domain_mapping.sh` have been
removed (see *Hosting tooling removed* below). Both aimed at
`ghs.googlehosted.com`, which is where production is today; git history has them
if that path is wanted again.

## Hosting tooling removed

`cutover-pages-dns.yml` remains — it points `www` at GitHub Pages and needs
`CLOUDFLARE_API_TOKEN`. Everything else on the Google Cloud side has been
removed from the tree:

| Removed | Was |
|---|---|
| `deploy-gcp.yml` | GCS bucket, europe-central2 (Warsaw); skipped itself for want of `GCP_SA_KEY` / `GCP_PROJECT` / `GCS_BUCKET` |
| `deploy-cloudrun-preview.yml` | dispatch-only Cloud Run `juzlova-main-preview`, europe-west3 |
| `cloudflare_dns.sh`, `gcp_domain_mapping.sh` | pointed `www` at Cloud Run; mapped the domain to it |
| `Dockerfile`, `nginx.conf`, `.dockerignore`, `.gcloudignore` | the Cloud Run container recipe |
| `docs/DEPLOY-GCP.md` | setup guide for all of it |

None of them deployed production: the two workflows targeted a bucket and a
preview service, never `juzlova-web`. Whatever puts the build on the Google host
is done outside this repo.

**Caveat worth knowing.** `www` still points at that Google host, so while it
serves the site, `Dockerfile` + `nginx.conf` were the only in-repo recipe for the
container it runs, and `cloudflare_dns.sh` was the one-command way back to
today's DNS if a Pages cutover had to be rolled back. Git history keeps all of
them. If the Google host is to stay, consider restoring the Dockerfile pair.

Do not deploy to the Cloud Run service named `juzlova-web` — that is production.
`scripts/dev_server.sh` is unaffected by the removal: it writes its own nginx
config inline and never read the root `nginx.conf`.

## Known limits

- The scroll hero scrubs still keyframes rather than video frames. Slicing a
  real clip needs a paid Higgsfield plan; the code path is the same either way.
- Four product photographs and four recipe photographs are generated, because
  the recovered originals for those products showed the wrong products and the
  Wayback Machine holds no working capture of those recipe thumbnails.
  `img/vanilkovy-cukr-pytliky.webp` is the workshop's own photograph.
- `assets/style.css` is unreferenced. Safe to delete once someone confirms it.
