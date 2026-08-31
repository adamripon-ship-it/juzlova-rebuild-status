FROM nginx:1.27-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY . /usr/share/nginx/html/

# Cloud Run sends traffic to $PORT (default 8080). Bind that, not 80.
ENV PORT=8080
EXPOSE 8080

CMD ["sh", "-c", "sed -i \"s/listen 8080/listen ${PORT}/\" /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]
