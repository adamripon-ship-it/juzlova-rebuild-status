# juzlova.cz → Google Cloud migration

Goal: serve the rebuilt static site from Google Cloud in **europe-west3 (Frankfurt)** —
the closest Google Cloud region to the Czech Republic (there is no CZ region;
europe-central2/Warsaw is the alternative) — with DNS staying on Cloudflare.

## Current state (verified 2026-08-31)

| Item | Value |
|---|---|
| Nameservers | `sam.ns.cloudflare.com`, `elly.ns.cloudflare.com` ✅ already on Cloudflare |
| `juzlova.cz` A | `23.227.38.65` (Shopify) — to be replaced |
| `www.juzlova.cz` | CNAME → `shops.myshopify.com` — to be replaced |

The nameservers are already correct; only the in-zone records change.

## How the pipeline works

`.github/workflows/deploy-gcp.yml` runs on every push to `main` and:

1. Deploys the site (nginx container, `Dockerfile` + `nginx.conf`) to Cloud Run
   service `juzlova-web` in `europe-west3`.
2. Verifies domain ownership with Google (publishes the site-verification TXT
   record via the Cloudflare API — `scripts/gcp_domain_mapping.sh`) and creates
   Cloud Run domain mappings for `juzlova.cz` and `www.juzlova.cz`.
3. Updates Cloudflare DNS: both hostnames become CNAME `ghs.googlehosted.com`
   (`scripts/cloudflare_dns.sh`). Records start DNS-only (grey cloud) so
   Google can issue its managed TLS certificate; once the site serves over
   HTTPS, re-run the script with `PROXIED=true` to turn Cloudflare's proxy on.

## One-time setup (the only human steps)

Add three **repository secrets** (GitHub → Settings → Secrets and variables → Actions):

1. `GCP_PROJECT_ID` — your Google Cloud project id.
2. `GCP_SA_KEY` — JSON key of a service account with roles:
   `roles/run.admin`, `roles/iam.serviceAccountUser`, `roles/cloudbuild.builds.editor`,
   `roles/storage.admin` (for the build source bucket). Also enable APIs:
   Cloud Run, Cloud Build, Site Verification (`siteverification.googleapis.com`).
3. `CLOUDFLARE_API_TOKEN` — Cloudflare token scoped to the `juzlova.cz` zone
   with **Zone:Read + DNS:Edit** permissions.

Then merge this PR (or run the workflow manually via *Actions → Deploy to
Google Cloud → Run workflow*). Everything else is automated.

## Rollback

Re-point the records at Shopify in Cloudflare:
`juzlova.cz` A `23.227.38.65`, `www` CNAME `shops.myshopify.com`.
