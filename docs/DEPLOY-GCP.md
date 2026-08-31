# Deploying juzlova.cz to Google Cloud

The live domain already points at **Cloud Run**. `www.juzlova.cz` is CNAME
`ghs.googlehosted.com`. Do **not** point `www` at GitHub Pages
(`adamripon-ship-it.github.io`). The four-language `main` build goes live by
replacing the container on that Cloud Run service.

`.github/workflows/deploy-cloudrun.yml` rebuilds with `SITE_BASE=https://juzlova.cz`
and deploys to **`juzlova-web`** in **europe-west3** on every push to `main`
(and from **Actions → Deploy latest main to Cloud Run**).

`Dockerfile` + `nginx.conf` serve the static tree (clean URLs, cache headers).
`archive/`, `scripts/` and git metadata stay out of the image.

## One-time setup (Google Cloud Console)

Use the project that already has the Cloud Run service behind juzlova.cz.

1. Open [Cloud Run](https://console.cloud.google.com/run) and confirm the
   service mapped to `www.juzlova.cz` (expected name: `juzlova-web`,
   region `europe-west3`).
2. [IAM → Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
   → Create. Grant **Cloud Run Admin** and **Service Account User**.
3. Keys → Add key → JSON. Download the file.
4. In GitHub: Settings → Secrets and variables → Actions → add:
   - `GCP_SA_KEY` — the full JSON key contents
   - `GCP_PROJECT` — that project's id
5. Run **Deploy latest main to Cloud Run** (target `juzlova-web`).

Until those two secrets exist the workflow **fails** instead of skipping, so
a missing key is visible. DNS is left alone.

Optional GCS sync still lives in `.github/workflows/deploy-gcp.yml` and still
skips without `GCS_BUCKET`. That path is not what serves juzlova.cz.

## After deploy

Check all four languages on the real domain (no DNS change):

- `https://www.juzlova.cz/`
- `https://www.juzlova.cz/en/`
- `https://www.juzlova.cz/de/`
- `https://www.juzlova.cz/sk/`

Success is English / German / Slovak copy, not the Czech 404 "Tady nic nepeče".
