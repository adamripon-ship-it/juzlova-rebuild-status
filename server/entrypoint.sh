#!/bin/sh
# Start the ratings/contact API and wait until it listens, then nginx.
# Cloud Run marks the container ready when $PORT is bound — nginx must not
# bind first or the first /api request after a cold start returns 502.
set -eu
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
exec nginx -g "daemon off;"
