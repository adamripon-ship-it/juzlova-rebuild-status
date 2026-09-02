#!/usr/bin/env bash
# Local development server for the static site.
#
# Serves the built site from the repository root with the same clean-URL
# behaviour, cache headers and gzip as the production nginx image, so what you
# see locally matches what GitHub Pages / Cloud Run serve. Runs nginx in the
# foreground; stop with Ctrl-C.
#
#   PORT=8080 scripts/dev_server.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PORT="${PORT:-8080}"
API_PORT="${API_PORT:-8090}"
RUNTIME="${TMPDIR:-/tmp}/juzlova-dev-nginx"

mkdir -p "$RUNTIME/logs" "$RUNTIME/tmp"

cat > "$RUNTIME/nginx.conf" <<NGINX
worker_processes 1;
error_log /dev/stderr info;
pid $RUNTIME/nginx.pid;
events { worker_connections 128; }
http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;
    access_log /dev/stdout;
    client_body_temp_path $RUNTIME/tmp;
    proxy_temp_path $RUNTIME/tmp;
    fastcgi_temp_path $RUNTIME/tmp;
    uwsgi_temp_path $RUNTIME/tmp;
    scgi_temp_path $RUNTIME/tmp;

    server {
        listen 0.0.0.0:$PORT;
        server_name _;
        root $ROOT;
        index index.html;

        location /api/ {
            proxy_pass http://127.0.0.1:${API_PORT};
            proxy_http_version 1.1;
            proxy_set_header Host \$host;
            proxy_set_header X-Real-IP \$remote_addr;
            proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
            proxy_set_header User-Agent \$http_user_agent;
        }
        location / {
            try_files \$uri \$uri/ \$uri/index.html =404;
        }
        location /assets/ { add_header Cache-Control "public, max-age=604800"; }
        location /img/    { add_header Cache-Control "public, max-age=604800"; }
        location ~* \.html\$ { add_header Cache-Control "public, max-age=300"; }

        # Match the production image: keep source trees out of the served site.
        location /archive/ { return 404; }
        location /scripts/ { return 404; }
        location /server/  { return 404; }
        location /data/    { return 404; }
        location /.git/    { return 404; }
        location /.github/ { return 404; }

        gzip on;
        # text/html is always gzipped by nginx, so it is intentionally omitted
        # here to avoid a "duplicate MIME type" startup warning.
        gzip_types text/css application/javascript image/svg+xml application/json text/xml application/xml text/plain;
    }
}
NGINX

API_HOST=127.0.0.1 API_PORT="$API_PORT" DATA_DIR="$RUNTIME/data" \
  RATINGS_SEED="$ROOT/data/ratings-seed.json" \
  python3 "$ROOT/server/app.py" &
API_PID=$!
trap 'kill "$API_PID" 2>/dev/null || true' EXIT INT TERM

echo "Serving $ROOT at http://0.0.0.0:$PORT (Ctrl-C to stop)"
nginx -p "$RUNTIME" -c "$RUNTIME/nginx.conf" -g 'daemon off;'
kill "$API_PID" 2>/dev/null || true
