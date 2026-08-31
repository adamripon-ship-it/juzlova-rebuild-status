#!/usr/bin/env bash
# Cloud Agent install step: refresh the built site so a preview is ready.
#
# The build script uses only the Python standard library. nginx is used by
# scripts/dev_server.sh to preview the site with production-like clean URLs;
# ensure it is present (a snapshot usually already has it, so this is a no-op).
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

if ! command -v nginx >/dev/null 2>&1; then
    echo "nginx not found — installing for the local preview server"
    sudo apt-get update -qq
    sudo apt-get install -y -qq nginx
fi

echo "Building the static site (all four languages) into the repo root"
python3 scripts/build_site.py

echo "Validating that generated pages reference no missing local files"
python3 scripts/verify_refs.py
