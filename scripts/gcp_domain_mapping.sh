#!/usr/bin/env bash
# Verify domain ownership and map juzlova.cz + www to a Cloud Run service.
#
# Taken from PR #3's automation, without that PR's parallel site. This script
# publishes a TXT record and creates domain mappings. Do not run it until
# issues #7 and #9 are decided.
#
# Requires: CLOUDFLARE_API_TOKEN, gcloud auth, and the service already deployed.
# Uses GCP_PROJECT (main's secret name), falling back to GCP_PROJECT_ID.
# Safety:   refuses to run unless I_MEAN_IT=yes.
set -euo pipefail

if [ "${I_MEAN_IT:-}" != "yes" ]; then
  echo "Refusing to map juzlova.cz. This is issue #9." >&2
  echo "Set I_MEAN_IT=yes only after #7 is decided and the current" >&2
  echo "Cloudflare zone has been recorded for rollback." >&2
  exit 1
fi

if [ -z "${CLOUDFLARE_API_TOKEN:-}" ]; then
  echo "CLOUDFLARE_API_TOKEN is not set." >&2
  exit 1
fi

DOMAIN="juzlova.cz"
SERVICE="${CLOUD_RUN_SERVICE:-juzlova-web}"
REGION="${CLOUD_RUN_REGION:-europe-west3}"
PROJECT="${GCP_PROJECT:-${GCP_PROJECT_ID:-}}"
API="https://api.cloudflare.com/client/v4"
AUTH=(-H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" -H "Content-Type: application/json")

if [ -z "${PROJECT}" ]; then
  echo "Set GCP_PROJECT (or GCP_PROJECT_ID)." >&2
  exit 1
fi

ACCESS_TOKEN=$(gcloud auth print-access-token)
ZONE_ID=$(curl -fsS "${AUTH[@]}" "${API}/zones?name=${DOMAIN}" | python3 -c 'import json,sys; print(json.load(sys.stdin)["result"][0]["id"])')

TOKEN=$(curl -fsS -X POST \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" -H "Content-Type: application/json" \
  "https://www.googleapis.com/siteVerification/v1/token" \
  --data "{\"site\":{\"type\":\"INET_DOMAIN\",\"identifier\":\"${DOMAIN}\"},\"verificationMethod\":\"DNS_TXT\"}" \
  | python3 -c 'import json,sys; print(json.load(sys.stdin)["token"])')
echo "Verification token obtained."

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

for host in "${DOMAIN}" "www.${DOMAIN}"; do
  gcloud beta run domain-mappings create \
    --service "${SERVICE}" --domain "${host}" --region "${REGION}" \
    --project "${PROJECT}" || echo "Mapping for ${host} may already exist; continuing."
done

gcloud beta run domain-mappings list --region "${REGION}" --project "${PROJECT}"
