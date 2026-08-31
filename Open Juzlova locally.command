#!/bin/bash
# Double-click on a Mac to preview the Jůzlová site in your browser.
set -e

HERE="$(cd "$(dirname "$0")" && pwd)"
if [ -f "$HERE/index.html" ]; then
  ROOT="$HERE"
elif [ -f "$HERE/../index.html" ]; then
  ROOT="$(cd "$HERE/.." && pwd)"
else
  echo "Could not find index.html next to this file."
  echo "Put this command inside the unzipped site folder and try again."
  read -r _
  exit 1
fi
cd "$ROOT"

PORT=""
for p in 8765 8766 8767 8768 8770 8771; do
  if ! lsof -iTCP:"$p" -sTCP:LISTEN >/dev/null 2>&1; then
    PORT="$p"
    break
  fi
done

if [ -z "$PORT" ]; then
  echo "Ports 8765–8771 are already in use."
  echo "Close the old Terminal window that is serving the site, then try again."
  read -r _
  exit 1
fi

URL="http://127.0.0.1:${PORT}/"
echo "Serving: $ROOT"
echo "Open:    $URL"
echo "Leave this window open. Close it to stop the local server."
echo
open "$URL"
python3 -m http.server "$PORT" --bind 127.0.0.1
