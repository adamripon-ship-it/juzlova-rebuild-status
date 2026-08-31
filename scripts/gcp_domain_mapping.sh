#!/usr/bin/env bash
# Verify domain ownership and map juzlova.cz + www to the Cloud Run service.
# Runs in CI after `gcloud auth` with the deploy service account.
# Requires: CLOUDFLARE_API_TOKEN (to place the Google site-verification TXT record),
#           GCP_PROJECT_ID, and the service already deployed.
set -euo pipefail

DOMAIN="juzlova.cz"
SERVICE="juzlova-web"
REGION="europe-west3"
API="https://api.cloudflare.com/client/v4"
AUTH=(-H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" -H "Content-Type: application/json")

ACCESS_TOKEN=$(gcloud auth print-access-token)
ZONE_ID=$(curl -fsS "${AUTH[@]}" "${API}/zones?name=${DOMAIN}" | python3 -c 'import json,sys; print(json.load(sys.stdin)["result"][0]["id"])')

# 1. Get a site-verification TXT token for the domain.
TOKEN=$(curl -fsS -X POST \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" -H "Content-Type: application/json" \
  "https://www.googleapis.com/siteVerification/v1/token" \
  --data "{\"site\":{\"type\":\"INET_DOMAIN\",\"identifier\":\"${DOMAIN}\"},\"verificationMethod\":\"DNS_TXT\"}" \
  | python3 -c 'import json,sys; print(json.load(sys.stdin)["token"])')
echo "Verification token obtained."

# 2. Publish the TXT record in Cloudflare (idempotent).
EXISTING=$(curl -fsS "${AUTH[@]}" "${API}/zones/${ZONE_ID}/dns_records?type=TXT&name=${DOMAIN}" \
  | python3 -c 'import json,sys; rs=[r for r in json.load(sys.stdin)["result"] if "google-site-verification" in r["content"]]; print(rs[0]["id"] if rs else "")')
PAYLOAD=$(python3 - "$DOMAIN" "$TOKEN" <<'PY'
import json, sys
print(json.dumps({"name": sys.argv[1], "type": "TXT", "content": sys.argv[2], "ttl": 300}))
PY
)
if [ -n "$EXISTING" ]; then
  curl -fsS -X PUT "${AUTH[@]}" "${API}/zones/${ZONE_ID}/dns_records/${EXISTING}" --data "$PAYLOAD" >/dev/null
else
  curl -fsS -X POST "${AUTH[@]}" "${API}/zones/${ZONE_ID}/dns_records" --data "$PAYLOAD" >/dev/null
fi
echo "TXT record published; waiting for propagation..."
sleep 60

# 3. Ask Google to verify (the deploy SA becomes an owner).
for attempt in 1 2 3 4 5; do
  if curl -fsS -X POST \
    -H "Authorization: Bearer ${ACCESS_TOKEN}" -H "Content-Type: application/json" \
    "https://www.googleapis.com/siteVerification/v1/webResource?verificationMethod=DNS_TXT" \
    --data "{\"site\":{\"type\":\"INET_DOMAIN\",\"identifier\":\"${DOMAIN}\"}}"; then
    echo "Domain verified."
    break
  fi
  echo "Verification attempt ${attempt} failed; retrying in 60s..."
  sleep 60
done

# 4. Create the domain mappings (idempotent — ignore already-exists).
for host in "${DOMAIN}" "www.${DOMAIN}"; do
  gcloud beta run domain-mappings create \
    --service "${SERVICE}" --domain "${host}" --region "${REGION}" \
    --project "${GCP_PROJECT_ID}" || echo "Mapping for ${host} may already exist; continuing."
done

gcloud beta run domain-mappings list --region "${REGION}" --project "${GCP_PROJECT_ID}"
