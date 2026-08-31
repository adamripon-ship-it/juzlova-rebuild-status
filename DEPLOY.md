# Deploying juzlova.cz to Google Cloud (Cloud Run, Frankfurt)

The site is fully static; the container is just nginx serving this repo.
Google Cloud has no Czech region — `europe-west3` (Frankfurt) is the closest.

## 1. One-time setup

```sh
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud services enable run.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com
```

## 2. Build and deploy

From the repo root:

```sh
gcloud run deploy juzlova-web \
  --source . \
  --region europe-west3 \
  --allow-unauthenticated
```

This builds the `Dockerfile` with Cloud Build and deploys it. The command
prints a service URL like `https://juzlova-web-xxxxxxxx-ey.a.run.app` —
verify the site there before touching DNS.

Re-deploying after content changes is the same command.

## 3. Map the custom domain

```sh
gcloud beta run domain-mappings create --service juzlova-web --domain juzlova.cz --region europe-west3
gcloud beta run domain-mappings create --service juzlova-web --domain www.juzlova.cz --region europe-west3
```

(Domain ownership is verified via the Cloudflare zone; the command tells you
if a TXT record is needed first.)

## 4. Cloudflare DNS changes (in the existing juzlova.cz zone)

Replace the two Shopify records:

| Record | Old value | New value |
|---|---|---|
| `juzlova.cz` A `23.227.38.65` | Shopify | **delete**, add CNAME `juzlova.cz` → `ghs.googlehosted.com` |
| `www` CNAME `shops.myshopify.com` | Shopify | CNAME `www` → `ghs.googlehosted.com` |

Important: set both records to **DNS only (grey cloud)** until the domain
mapping shows its certificate as provisioned (`gcloud beta run
domain-mappings describe --domain juzlova.cz --region europe-west3`), then
switch them to Proxied (orange cloud). Google can't issue the cert while
Cloudflare is proxying. In Cloudflare SSL/TLS settings use **Full (strict)**
once proxied.

## Local preview

```sh
docker build -t juzlova-web . && docker run -p 8080:8080 juzlova-web
```
