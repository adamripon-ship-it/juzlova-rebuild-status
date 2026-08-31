# Deploying juzlova.cz to Google Cloud

The site is a static build (no server code). Two paths sit in this repo.
Neither one should touch DNS until issues #7 and #9 are decided.

**What is live today** is already on Google Cloud Run: `www.juzlova.cz` is
CNAME `ghs.googlehosted.com` and the apex 301s there. That service is
almost certainly named `juzlova-web` and is serving the Czech-only PR #3
build. Do not deploy a preview onto that name.

**GCS (merged workflow).** `.github/workflows/deploy-gcp.yml` syncs the
`main` build to a bucket in **europe-central2 (Warsaw)** on every push to
`main` once three repository secrets exist. Until then it skips itself and
GitHub Pages keeps serving the site.

**Cloud Run preview of `main`.** `.github/workflows/deploy-cloudrun-preview.yml`
is dispatch-only. It deploys to a service named `juzlova-main-preview` so
it cannot overwrite production. Use this for issue #8 if you want a
`*.run.app` URL to check the four-language build.

`Dockerfile` + `nginx.conf` serve `main`'s static tree (clean URLs, cache
headers). `archive/`, `scripts/` and git metadata stay out of the image.

## One-time setup (≈10 minutes, done by the project owner)

1. In [Google Cloud Console](https://console.cloud.google.com/) create (or
   pick) a project, note its **project id**.
2. Create a service account: IAM & Admin → Service Accounts → Create.
   Grant it **Storage Admin** (GCS path) and **Cloud Run Admin** plus
   **Service Account User** (preview path). Create a **JSON key** and
   download it.
3. In the GitHub repo: Settings → Secrets and variables → Actions → add:
   - `GCP_SA_KEY` — the full JSON key file contents
   - `GCP_PROJECT` — the project id
   - `GCS_BUCKET` — bucket name; use something like `juzlova-site` for a
     preview bucket. Do not reuse a name that already serves production.
4. For issue #8, run **Cloud Run preview of main** from the Actions tab
   (dispatch-only, service `juzlova-main-preview`). The GCS workflow still
   runs on push to `main` once the three secrets exist; it skips until then.

## Custom domain + HTTPS

A bare bucket serves HTTP only. For `https://juzlova.cz`:

1. Reserve a global static IP; create an **external Application Load
   Balancer** with a backend bucket pointing at the site bucket, enable
   **Cloud CDN** on it.
2. Attach a **Google-managed certificate** for `juzlova.cz` and
   `www.juzlova.cz`.
3. Point DNS `A` records for `juzlova.cz`/`www` at the load-balancer IP.
4. At cutover (issue #9) set the repository variable `SITE_BASE` to
   `https://juzlova.cz`. The GCS workflow then rebuilds before it syncs.
   Do not set this while GitHub Pages is still the public copy — every
   canonical, hreflang, sitemap and redirect stub is generated from it.

The Cloudflare / Cloud Run mapping scripts in `scripts/` refuse to run
unless `I_MEAN_IT=yes`. Rollback is **not** "put Shopify back"; capture
the live zone first. See `docs/HANDOFF.md`.

## Alternative

Firebase Hosting (also Google) gives HTTPS + CDN + custom domain with less
setup (`firebase init hosting && firebase deploy`), if you prefer that over
the load-balancer route.
