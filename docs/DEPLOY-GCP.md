# Deploying juzlova.cz to Google Cloud

The live domain already points at **Cloud Run**. `www.juzlova.cz` is CNAME
`ghs.googlehosted.com`. Do **not** point `www` at GitHub Pages.

The four-language `main` build goes live by replacing the container on that
service. Prefer the **Cloud Run MCP / API**, not a downloaded JSON key.

## Preferred: Cloud Run MCP (OAuth)

Google’s official Cloud Run Admin MCP is a remote HTTP API:

`https://run.googleapis.com/mcp`

It is configured in `.cursor/mcp.json`. Tools: `list_services`, `get_service`,
`deploy_service_from_image`, `deploy_service_from_archive`,
`deploy_service_from_file_contents`. Calls need a Google OAuth access token
(Cloud Run does not accept API keys). This is Google’s own endpoint, not
Runlayer.

In Cursor: **Settings → MCP → cloud-run → Connect**. Sign in with the Google
account that owns the project already serving juzlova.cz. Grant Cloud Run
access.

Then ask the agent to:

1. `list_services` in `europe-west3` (find `juzlova-web` and the project id)
2. Deploy latest `main` onto that service
3. Leave DNS on `ghs.googlehosted.com`

## Fallback: GitHub Actions (still API, still no dashboard DNS)

`.github/workflows/deploy-cloudrun.yml` deploys `main` to `juzlova-web` in
`europe-west3`. It needs two GitHub secrets only if you want CI:

- `GCP_SA_KEY` — service account JSON (Cloud Run Admin + Service Account User)
- `GCP_PROJECT` — project id

Until those exist the workflow fails on purpose. DNS is not changed.

## After deploy

- `https://www.juzlova.cz/`
- `https://www.juzlova.cz/en/`
- `https://www.juzlova.cz/de/`
- `https://www.juzlova.cz/sk/`

Success is English / German / Slovak copy, not the Czech 404 "Tady nic nepeče".
