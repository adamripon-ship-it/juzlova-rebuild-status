# juzlova.cz — where things stand

Last verified 2026-08-31 by fetching the live site. For how to work on the
code, read [`AGENTS.md`](../AGENTS.md); this file is history and open questions.

## 2026-09-17 — production is `juzlova-web` in **europe-west4**, not west3

The Cloud Run domain mappings for `juzlova.cz` and `www.juzlova.cz` live in
**europe-west4** and route to the `juzlova-web` service **in europe-west4**.
A second service with the same name exists in europe-west3; it is an orphan
copy that nothing routes to (its own run.app URL works, the domain does not
reach it). `deploy-cloudrun.yml` now targets europe-west4. When deploying by
hand, always pass `--region europe-west4`. Cleanup candidate: delete the
europe-west3 service once the owner confirms nothing else uses it.

`deploy-cloudrun.yml` still needs the repository secrets `GCP_SA_KEY` and
`GCP_PROJECT`; without them it prints a warning and deploys nothing, while the
run still shows a green tick. Verify a deploy by checking the live H1.

## Follow-ups after the 2026-09-17 deploy (nginx, small)

Both belong in `nginx.conf`; the design session is editing that file for
security headers, so land them in the same change:

1. Move `include /etc/nginx/juzlova-redirects.conf;` **above** the apex
   `if ($http_host …) return 301` block. Today an old URL on the apex takes
   two hops (apex → www old → www new); with the include first it is one.
2. Add `absolute_redirect off;` (or `port_in_redirect off;`) in the server
   block if a slash-less URL such as `/cenik` is ever seen redirecting to
   `http://www.juzlova.cz:8080/cenik/` — nginx's directory redirect uses the
   container's listen port and scheme unless told otherwise.

Also still open: repository secrets `GCP_SA_KEY` / `GCP_PROJECT` for
`deploy-cloudrun.yml`; resubmit the four sitemaps in Google Search Console
after the URL change; delete the orphan `juzlova-web` service in europe-west3.

## 2026-09-16 — translated slugs and messaging rewrite

All copy was rewritten from `docs/messaging/` (persona research, rules, page by
page copy). URLs changed to per-language keyword slugs with region hreflang;
every old URL 301s via `redirects.conf` (nginx) and meta-refresh stubs. Local
pages are Czech-only. Open items for the owners are in
`docs/messaging/06-needs-verification.md` (KLASA certificate for the flour,
cocoa spec sheet, EU parcel payment method, wholesale lead time).

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

`scripts/cloudflare_dns.sh` still aims at `ghs.googlehosted.com`, which is where
production is today. It and `gcp_domain_mapping.sh` refuse to run unless
`I_MEAN_IT=yes` is set.

## Hosting options that exist but are not in use

| Workflow | Target | State |
|---|---|---|
| `deploy-cloudrun.yml` | **Cloud Run `juzlova-web`, europe-west4 — this is production** (a same-named orphan exists in europe-west3) | runs on push to `main`; needs `GCP_SA_KEY` + `GCP_PROJECT` |
| `deploy-gcp.yml` | GCS bucket, europe-central2 (Warsaw) | dispatch-only; not what serves the domain |
| `deploy-cloudrun-preview.yml` | Cloud Run `juzlova-main-preview`, europe-west3 | dispatch-only; deliberately not the live `juzlova-web` |
| `cutover-pages-dns.yml` | points `www` at GitHub Pages | needs `CLOUDFLARE_API_TOKEN` |

Warsaw is nearer Czechia than Frankfurt, but both are one hop away and no
visitor will notice.

`juzlova-web` is production. Until 2026-09-03 nothing in the repo deployed it —
it was updated by hand with `gcloud run deploy`, so merging a change did not
ship it, and `deploy-gcp.yml` reported a green "Deploy" on every push while
skipping every step. A corrected price list sat on `main` for an hour while the
site still quoted the 2017 prices. `deploy-cloudrun.yml` now owns that deploy.
It is the one production deploy path: change it rather than adding a second.

## Known limits

- The scroll hero scrubs still keyframes rather than video frames. Slicing a
  real clip needs a paid Higgsfield plan; the code path is the same either way.
- Four product photographs and four recipe photographs are generated, because
  the recovered originals for those products showed the wrong products and the
  Wayback Machine holds no working capture of those recipe thumbnails.
  `img/vanilkovy-cukr-pytliky.webp` is the workshop's own photograph.
- `assets/style.css` is unreferenced. Safe to delete once someone confirms it.
