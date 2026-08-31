#!/bin/bash
# Double-click on a Mac to preview the Jůzlová site in your browser.
cd "$(dirname "$0")/.." || exit 1
PORT=8765
URL="http://127.0.0.1:${PORT}/"

if command -v lsof >/dev/null 2>&1 && lsof -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  open "$URL"
  exit 0
fi

open "$URL"
echo "Jůzlová local copy is open at ${URL}"
echo "Leave this window open. Close it to stop the local server."
echo
python3 -m http.server "$PORT" --bind 127.0.0.1
