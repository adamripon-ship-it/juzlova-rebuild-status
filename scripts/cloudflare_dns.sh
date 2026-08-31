#!/usr/bin/env bash
# Point juzlova.cz + www at the Cloud Run domain mapping via the Cloudflare API.
# Requires: CLOUDFLARE_API_TOKEN (Zone:Read + DNS:Edit for juzlova.cz).
set -euo pipefail

DOMAIN="juzlova.cz"
API="https://api.cloudflare.com/client/v4"
AUTH=(-H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" -H "Content-Type: application/json")

ZONE_ID=$(curl -fsS "${AUTH[@]}" "${API}/zones?name=${DOMAIN}" | python3 -c 'import json,sys; print(json.load(sys.stdin)["result"][0]["id"])')
echo "Zone: ${ZONE_ID}"

# name, type, content, proxied
# Cloud Run domain mappings need DNS-only (grey cloud) until the Google-managed
# cert is issued; run with PROXIED=true afterwards to turn the orange cloud on.
PROXIED="${PROXIED:-false}"

upsert() {
  local name="$1" type="$2" content="$3"
  local existing
  existing=$(curl -fsS "${AUTH[@]}" "${API}/zones/${ZONE_ID}/dns_records?name=${name}" \
    | python3 -c 'import json,sys; rs=json.load(sys.stdin)["result"]; print(rs[0]["id"] if rs else "")')
  local payload
  payload=$(python3 - "$name" "$type" "$content" "$PROXIED" <<'PY'
import json, sys
name, rtype, content, proxied = sys.argv[1:5]
print(json.dumps({"name": name, "type": rtype, "content": content,
                  "proxied": proxied == "true", "ttl": 1}))
PY
)
  if [ -n "$existing" ]; then
    curl -fsS -X PUT "${AUTH[@]}" "${API}/zones/${ZONE_ID}/dns_records/${existing}" --data "$payload" >/dev/null
    echo "Updated ${type} ${name} -> ${content} (proxied=${PROXIED})"
  else
    curl -fsS -X POST "${AUTH[@]}" "${API}/zones/${ZONE_ID}/dns_records" --data "$payload" >/dev/null
    echo "Created ${type} ${name} -> ${content} (proxied=${PROXIED})"
  fi
}

# Cloud Run domain mapping targets.
upsert "${DOMAIN}" "CNAME" "ghs.googlehosted.com"
upsert "www.${DOMAIN}" "CNAME" "ghs.googlehosted.com"

echo "Done. Verify with: https://dns.google/resolve?name=${DOMAIN}&type=CNAME"
