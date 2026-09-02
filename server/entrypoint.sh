#!/bin/sh
# Start the ratings/contact API, then nginx on Cloud Run's $PORT.
set -eu
python3 /opt/juzlova-api/app.py &
sed -i "s/listen 8080/listen ${PORT}/" /etc/nginx/conf.d/default.conf
exec nginx -g "daemon off;"
