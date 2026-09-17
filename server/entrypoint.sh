#!/bin/sh
# Start the ratings/contact API and wait until it listens, then nginx.
# Cloud Run marks the container ready when $PORT is bound — nginx must not
# bind first or the first /api request after a cold start returns 502.
set -eu
if [ -f /opt/juzlova-api/inject-analytics.py ]; then
  python3 /opt/juzlova-api/inject-analytics.py
fi
python3 /opt/juzlova-api/app.py &
i=0
while [ "$i" -lt 50 ]; do
  if python3 -c "import socket; s=socket.create_connection(('127.0.0.1', 8090), 1); s.close()" 2>/dev/null; then
    break
  fi
  i=$((i + 1))
  sleep 0.1
done
sed -i "s/listen 8080/listen ${PORT}/" /etc/nginx/conf.d/default.conf
if [ "${PREVIEW_READ_ONLY:-0}" = "1" ]; then
  sed -i '/server_name _;/a\    add_header X-Robots-Tag "noindex, nofollow" always;' /etc/nginx/conf.d/default.conf
fi
exec nginx -g "daemon off;"
