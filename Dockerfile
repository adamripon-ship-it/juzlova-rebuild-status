FROM nginx:1.27-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY . /usr/share/nginx/html

# Cloud Run provides $PORT (default 8080); nginx.conf listens on 8080.
EXPOSE 8080
