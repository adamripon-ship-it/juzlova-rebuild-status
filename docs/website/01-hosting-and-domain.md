# 1. Hosting, domain and accounts

[← Back to the handbook](README.md)

Checked against the live internet on **29 October 2026**.

---

## The short version

```
Visitor ──► Cloudflare DNS ──► Google Cloud Run (juzlova-web, europe-west4) ──► the page
```

- The **domain** is registered at **ACTIVE 24**.
- **Cloudflare** answers the DNS, meaning it tells browsers where the site
  lives. Cloudflare does not sit in front of the site as a proxy.
- **Google Cloud Run** serves every page.
- **GitHub** holds the code and deploys it to Google automatically.

---

## Domain name

| | |
|---|---|
| Domain | `juzlova.cz` |
| Registry | CZ.NIC (the `.cz` registry) |
| Registrar | **ACTIVE 24, s.r.o.** |
| First registered | 21 October 2014 |
| **Expires** | **20 October 2027.** Renew at ACTIVE 24 before this date |
| Status | Active |
| Nameservers | `elly.ns.cloudflare.com`, `sam.ns.cloudflare.com` |
| DNSSEC | Not enabled |

Registrant and admin contacts are held at the registrar (handles `ADAM` and
`JIRINA`). Personal details are deliberately not copied into this repository.

---

## DNS (Cloudflare)

The zone `juzlova.cz` is managed in the Cloudflare dashboard. Both web records
are **DNS only (grey cloud)**. They point straight at Google, which issues and
renews the HTTPS certificate itself.

| Name | Type | Value | Purpose |
|---|---|---|---|
| `juzlova.cz` | A / AAAA | Google addresses (e.g. `172.253.122.121`) | Bare domain, forwards to `www` |
| `www.juzlova.cz` | CNAME | `ghs.googlehosted.com` | The live site on Cloud Run |
| `juzlova.cz` | TXT | `google-site-verification=qG1hAG4g…` | Proves ownership to Google (Search Console and Cloud Run domain mapping) |
| `juzlova.cz` | MX | *(none)* | No email on this domain. The business uses `juzlj@seznam.cz` |

**Redirects that happen before a page loads**

| You type | You end up at |
|---|---|
| `http://www.juzlova.cz` | `https://www.juzlova.cz/` |
| `https://juzlova.cz` | `https://www.juzlova.cz/` (permanent, 301) |

> ⚠️ **Before changing any DNS record**, export the Cloudflare zone first. The
> old Shopify records no longer exist, so "putting the old records back" is
> not a rollback plan. The only supported automated DNS change is
> `.github/workflows/cutover-pages-dns.yml`.

---

## Google Cloud

| | |
|---|---|
| Project ID | `aiapply-ch` |
| **Production service** | Cloud Run **`juzlova-web`**, region **europe-west4** (Eemshaven, Netherlands) |
| Domain mappings | `juzlova.cz` and `www.juzlova.cz` → `juzlova-web` (europe-west4) |
| Preview service | Cloud Run `juzlova-main-preview`, europe-west3 (manual runs only) |
| Leftover copy | A second `juzlova-web` in europe-west3 receives no traffic. It can be deleted once the owner agrees |
| Data storage | Cloud Storage bucket `aiapply-ch-juzlova-data`: star ratings and contact-form inbox |
| Build | Cloud Build turns the repository's `Dockerfile` into an image, stored in Artifact Registry |
| Deploy identity | Service account `github-deploy@aiapply-ch.iam.gserviceaccount.com`, used by GitHub through Workload Identity Federation (no password or key file exists) |

### Settings stored on the Cloud Run service (not in GitHub)

These are environment variables on `juzlova-web`. They are changed in the
Google Cloud console, not in code. `.env.example` lists them all.

| Setting | What it does | Live status |
|---|---|---|
| `CLOUDFLARE_WEB_ANALYTICS_TOKEN` | Visitor counting | ✅ on |
| `GOOGLE_ANALYTICS_MEASUREMENT_ID` | Google Analytics 4, loads only after cookie consent | ⏸ not set |
| `TURNSTILE_SITE_KEY` | Captcha on the contact form | ⏸ not set |
| `ZAPIER_WEBHOOK_URL` / `SMTP_*` / `FORMSPREE_*` | Where contact-form messages are delivered | set by owner |
| `CONTACT_TO` | Inbox for contact-form messages | `juzlj@seznam.cz` |
| `DATA_BUCKET` | Storage bucket for ratings and inbox | `aiapply-ch-juzlova-data` |

---

## Google Search Console

- Ownership of `juzlova.cz` is verified through the DNS TXT record above.
- Submit **one** sitemap: `https://www.juzlova.cz/sitemap.xml`. It is an index
  that lists the four language sitemaps (`sitemap-cs.xml`, `-en`, `-de`, `-sk`).
- Old WordPress URLs either forward permanently (301) to the new page or answer
  **410 Gone**, so Google drops them. See the [site map](generated/site-map.md).
- Do **not** add those old paths to `robots.txt` as `Disallow`. Google would
  then stop seeing the 410 and list them as "Blocked by robots.txt" forever.
- Open task: resubmit the sitemaps after the September 2026 URL change.

## Maps listings

| Service | Listing |
|---|---|
| Google Maps | "Juzlova - Potravinářské směsi", Kochánov 40, 582 53 |
| Seznam Mapy / Firmy.cz | <https://mapy.cz/?source=firm&id=12906730> |

Both already exist and belong to the owner. Do not create new ones.

## Analytics

- **Cloudflare Web Analytics**: on. A cookie-free visitor counter, added to
  every page by the server when it starts.
- **Google Analytics 4**: ready in the code but switched off until a real
  `G-…` ID is added on Cloud Run (see [`docs/GA4-AEO.md`](../GA4-AEO.md)).

## GitHub

| | |
|---|---|
| Repository | `adamripon-ship-it/juzlova-rebuild-status` |
| Live branch | `main`. Every merge deploys to production |
| Work branch | `develop`, a copy of `main` for new work |
| Deploy settings | Repository *variables* `GCP_PROJECT`, `GCP_WIF_PROVIDER`, `GCP_DEPLOY_SA` |
