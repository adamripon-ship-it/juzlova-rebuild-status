# 6. Software and services

[← Back to the handbook](README.md)

---

## Software in the repository

| Software | Version | Used for |
|---|---|---|
| **Python** | 3.12+ (standard library only) | The site generator and the contact/ratings API |
| **Pillow** | any recent | Only for the two image scripts (`optimize_images.py`, `make_brand_assets.py`) |
| **nginx** | 1.27 (Alpine Linux) | Web server inside the production container |
| **Docker** | — | Packs the site and server into one container (`Dockerfile`) |
| HTML / CSS / JavaScript | plain, no framework | The pages. `assets/site.css` and `assets/site.js` |
| **Fonts** | Fraunces, Geologica | Self-hosted in `assets/fonts/`, open-source licence (OFL) |

There is **no npm, no build framework, and no database**. Building the site
needs only Python.

## Outside services

| Service | Role | Account / where managed |
|---|---|---|
| **GitHub** | Code, history, automatic checks and deploys | `adamripon-ship-it/juzlova-rebuild-status` |
| **Google Cloud Run** | Serves the live website | Project `aiapply-ch`, service `juzlova-web` |
| **Google Cloud Build + Artifact Registry** | Builds and stores the container image | Same project |
| **Google Cloud Storage** | Stores ratings and contact messages | Bucket `aiapply-ch-juzlova-data` |
| **Google Search Console** | Search performance, sitemaps | Verified by DNS TXT record |
| **Google Maps** | Map on the "Where to find us" page; business listing | Owner's existing listing |
| **Cloudflare** | DNS for `juzlova.cz`; Web Analytics visitor counter | Cloudflare dashboard |
| **Cloudflare Turnstile** | Optional captcha for the contact form | Off |
| **Google Analytics 4** | Optional, after cookie consent | Off until an ID is set |
| **ACTIVE 24** | Domain registrar | Renew by 20 Oct 2027 |
| **Seznam Mapy / Firmy.cz** | Czech business listing and reviews | Owner's existing listing |
| **Zapier or SMTP (Seznam)** | Delivers contact-form messages to `juzlj@seznam.cz` | Set on Cloud Run |
| **Wayback Machine** | Source of the recovered original site | Public |

## Helper scripts (`scripts/`)

| Script | What it does |
|---|---|
| `build_site.py` | Builds every page, sitemap, redirect and AI file |
| `export_docs.py` | Writes this handbook's site map, page copy and image gallery |
| `verify_refs.py` | Fails if any page links to a file that doesn't exist |
| `optimize_images.py` | Shrinks large images to web WebP |
| `make_brand_assets.py` | Makes favicons and logos from `brand/` |
| `wayback_archive.py` | Re-downloads the old site; `--check` confirms the archive is complete |
| `dev_server.sh` | Local preview at <http://localhost:8080> that behaves like production |
| `cloudflare_dns.sh`, `gcp_domain_mapping.sh` | DNS and domain tools. Refuse to run unless `I_MEAN_IT=yes` |
