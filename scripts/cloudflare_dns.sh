#!/usr/bin/env bash
# Point juzlova.cz + www at a Cloud Run domain mapping via the Cloudflare API.
#
# Taken from PR #3's automation, without that PR's parallel site. This script
# changes live DNS. Do not run it until issues #7 and #9 are decided.
#
# Requires: CLOUDFLARE_API_TOKEN (Zone:Read + DNS:Edit for juzlova.cz).
# Safety:   refuses to run unless I_MEAN_IT=yes.
set -euo pipefail

if [ "${I_MEAN_IT:-}" != "yes" ]; then
  echo "Refusing to change live DNS for juzlova.cz." >&2
  echo "This is issue #9. Set I_MEAN_IT=yes only after #7 is decided and" >&2
  echo "the current Cloudflare zone has been recorded for rollback." >&2
  exit 1
fi

if [ -z "${CLOUDFLARE_API_TOKEN:-}" ]; then
  echo "CLOUDFLARE_API_TOKEN is not set." >&2
  exit 1
fi

DOMAIN="juzlova.cz"
API="https://api.cloudflare.com/client/v4"
AUTH=(-H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" -H "Content-Type: application/json")

ZONE_ID=$(curl -fsS "${AUTH[@]}" "${API}/zones?name=${DOMAIN}" | python3 -c 'import json,sys; print(json.load(sys.stdin)["result"][0]["id"])')
echo "Zone: ${ZONE_ID}"

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

upsert "${DOMAIN}" "CNAME" "ghs.googlehosted.com"
upsert "www.${DOMAIN}" "CNAME" "ghs.googlehosted.com"

echo "Done. Verify with: https://dns.google/resolve?name=${DOMAIN}&type=CNAME"
