# Deploying juzlova.cz to Google Cloud

The site is a static build (no server code), so the cheapest solid setup on
Google Cloud is a **Cloud Storage bucket + Cloud CDN/load balancer**, in
**europe-central2 (Warsaw)** — the Google Cloud region nearest the Czech
Republic (Czechia has no region of its own; Warsaw and Frankfurt
`europe-west3` are the closest).

The repo already contains `.github/workflows/deploy-gcp.yml`, which deploys
automatically on every push to `main` once three repository secrets exist.
Until then the workflow skips itself and GitHub Pages keeps serving the site.

## One-time setup (≈10 minutes, done by the project owner)

1. In [Google Cloud Console](https://console.cloud.google.com/) create (or
   pick) a project, note its **project id**.
2. Create a service account: IAM & Admin → Service Accounts → Create.
   Grant it the **Storage Admin** role. Create a **JSON key** and download it.
3. In the GitHub repo: Settings → Secrets and variables → Actions → add:
   - `GCP_SA_KEY` — the full JSON key file contents
   - `GCP_PROJECT` — the project id
   - `GCS_BUCKET` — bucket name; use `www.juzlova.cz` if you'll serve the
     custom domain directly from the bucket (requires domain verification in
     Search Console), otherwise something like `juzlova-site`.
4. Re-run the "Deploy to Google Cloud Storage" workflow (Actions tab) or push
   any commit to `main`.

## Custom domain + HTTPS

A bare bucket serves HTTP only. For `https://juzlova.cz`:

1. Reserve a global static IP; create an **external Application Load
   Balancer** with a backend bucket pointing at the site bucket, enable
   **Cloud CDN** on it.
2. Attach a **Google-managed certificate** for `juzlova.cz` and
   `www.juzlova.cz`.
3. Point DNS `A` records for `juzlova.cz`/`www` at the load-balancer IP.
4. Set `SITE_BASE=https://juzlova.cz` when running
   `python scripts/build_site.py`, rebuild and push, so canonical URLs,
   sitemap.xml and llms.txt reference the production domain.

## Alternative

Firebase Hosting (also Google) gives HTTPS + CDN + custom domain with less
setup (`firebase init hosting && firebase deploy`), if you prefer that over
the load-balancer route.
