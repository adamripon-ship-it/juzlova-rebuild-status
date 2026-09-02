FROM nginx:1.27-alpine

RUN apk add --no-cache python3

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY . /usr/share/nginx/html/
COPY server/ /opt/juzlova-api/
COPY data/ratings-seed.json /opt/juzlova-api/ratings-seed.json

# API code and data files must not be served as static assets.
RUN rm -rf /usr/share/nginx/html/server /usr/share/nginx/html/data \
    && chmod 755 /opt/juzlova-api/entrypoint.sh

# Cloud Run sends traffic to $PORT (default 8080). Bind that, not 80.
ENV PORT=8080
ENV API_HOST=127.0.0.1
ENV API_PORT=8090
ENV DATA_BUCKET=aiapply-ch-juzlova-data
ENV CONTACT_TO=juzlj@seznam.cz
EXPOSE 8080

CMD ["/opt/juzlova-api/entrypoint.sh"]
