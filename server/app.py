#!/usr/bin/env python3
"""Ratings + contact API for Cloud Run (nginx reverse-proxies /api/* here).

Durable store is GCS. The Cloud Run disk is ephemeral and is never the
source of truth. Local/dev falls back to a directory so the widget works
without credentials.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import smtplib
import ssl
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from email.message import EmailMessage
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

LISTEN_HOST = os.environ.get("API_HOST", "127.0.0.1")
LISTEN_PORT = int(os.environ.get("API_PORT", "8090"))
DATA_BUCKET = os.environ.get("DATA_BUCKET", "aiapply-ch-juzlova-data")
RATINGS_OBJECT = os.environ.get("RATINGS_OBJECT", "recipe-ratings.json")
CONTACT_TO = os.environ.get("CONTACT_TO", "juzlj@seznam.cz")
SEED_PATH = Path(os.environ.get(
    "RATINGS_SEED",
    str(Path(__file__).resolve().parent / "ratings-seed.json"),
))
LOCAL_DIR = Path(os.environ.get("DATA_DIR", "/tmp/juzlova-data"))
IS_CLOUD_RUN = bool(os.environ.get("K_SERVICE"))

SLUGS = (
    "sisky-s-makem-recept",
    "hruskovy-kolac-s-vanilkovym-pudinkem-recept",
    "strapacky-se-zelim-a-slaninou-recept",
    "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem",
    "slehackova-rolada-recept",
    "domaci-pernik-recept-podle-jirina-juzlova",
    "bramborovo-tvarohove-knedliky-s-jahodami",
    "rychle-venecky-ci-vetrnicky-recept",
    "venecky-s-vanilkovym-kremem-recept",
    "kremrole-recept",
    "minivetrnicky-recept",
    "karamelove-vetrniky-recept",
    "irsky-sticky-toffee-pudding-recept",
)
EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
LANGS = ("cs", "en", "de", "sk")
SUBJECT = {
    "cs": "Jůzlová — poptávka z webu",
    "en": "Jůzlová — website enquiry",
    "de": "Jůzlová — Anfrage über die Website",
    "sk": "Jůzlová — dopyt z webu",
}

_lock = threading.Lock()
_token = {"value": "", "exp": 0.0}


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_seed() -> dict:
    raw = json.loads(SEED_PATH.read_text(encoding="utf-8"))
    recipes = {}
    for slug in SLUGS:
        row = (raw.get("recipes") or {}).get(slug) or {}
        recipes[slug] = {
            "sum_tenths": int(row.get("sum_tenths") or 0),
            "count": int(row.get("count") or 0),
        }
    return {"version": 1, "recipes": recipes, "votes": {}}


def merge_doc(existing: dict | None) -> dict:
    seed = load_seed()
    if not existing or not isinstance(existing.get("recipes"), dict):
        return seed
    merged = {"version": 1, "recipes": dict(seed["recipes"]), "votes": {}}
    votes = existing.get("votes")
    if isinstance(votes, dict):
        merged["votes"] = {
            str(k)[:64]: str(v)[:16]
            for k, v in votes.items()
            if k
        }
    for slug in SLUGS:
        row = existing["recipes"].get(slug)
        if not isinstance(row, dict):
            continue
        count = row.get("count")
        tenths = row.get("sum_tenths")
        if not isinstance(count, (int, float)) or not isinstance(tenths, (int, float)):
            continue
        count = int(round(count))
        tenths = int(round(tenths))
        if count > 0:
            merged["recipes"][slug] = {"sum_tenths": tenths, "count": count}
    return merged


def public_row(row: dict) -> dict:
    count = max(int(row["count"]), 1)
    value = round(row["sum_tenths"] / 10 / count, 1)
    return {
        "ratingValue": value,
        "ratingCount": int(row["count"]),
        "bestRating": 5,
        "worstRating": 1,
    }


def public_all(doc: dict) -> dict:
    return {
        "version": 1,
        "recipes": {slug: public_row(doc["recipes"][slug]) for slug in SLUGS},
    }


def json_bytes(data: object) -> bytes:
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def clip(value: object, max_len: int) -> str:
    return str(value or "").replace("\r", "").strip()[:max_len]


def fingerprint(ip: str, ua: str, slug: str) -> str:
    raw = f"{ip}|{ua}|{slug}".encode("utf-8", "replace")
    return hashlib.sha256(raw).hexdigest()[:32]


def metadata_token() -> str:
    now = time.time()
    if _token["value"] and now < _token["exp"] - 60:
        return _token["value"]
    req = urllib.request.Request(
        "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token",
        headers={"Metadata-Flavor": "Google"},
    )
    with urllib.request.urlopen(req, timeout=4) as res:
        payload = json.loads(res.read().decode("utf-8"))
    _token["value"] = payload["access_token"]
    _token["exp"] = now + float(payload.get("expires_in") or 3500)
    return _token["value"]


def gcs_headers(token: str, extra: dict | None = None) -> dict:
    headers = {"Authorization": f"Bearer {token}"}
    if extra:
        headers.update(extra)
    return headers


def gcs_get(name: str) -> tuple[dict | None, str]:
    token = metadata_token()
    quoted = urllib.parse.quote(name, safe="")
    url = (
        f"https://storage.googleapis.com/storage/v1/b/{DATA_BUCKET}/o/{quoted}"
        f"?alt=media"
    )
    req = urllib.request.Request(url, headers=gcs_headers(token))
    try:
        with urllib.request.urlopen(req, timeout=8) as res:
            generation = res.headers.get("x-goog-generation") or "0"
            body = json.loads(res.read().decode("utf-8"))
            return body, str(generation)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None, "0"
        raise


def gcs_put(name: str, doc: dict, generation: str) -> bool:
    token = metadata_token()
    query = urllib.parse.urlencode({
        "uploadType": "media",
        "name": name,
        "ifGenerationMatch": generation,
    })
    url = f"https://storage.googleapis.com/upload/storage/v1/b/{DATA_BUCKET}/o?{query}"
    data = json.dumps(doc, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers=gcs_headers(token, {"Content-Type": "application/json; charset=utf-8"}),
    )
    try:
        with urllib.request.urlopen(req, timeout=8) as res:
            res.read()
        return True
    except urllib.error.HTTPError as exc:
        if exc.code in (412, 409):
            return False
        raise


def local_path(name: str) -> Path:
    LOCAL_DIR.mkdir(parents=True, exist_ok=True)
    return LOCAL_DIR / name.replace("/", "_")


def load_ratings() -> tuple[dict, str]:
    if IS_CLOUD_RUN:
        raw, generation = gcs_get(RATINGS_OBJECT)
        return merge_doc(raw), generation
    path = local_path(RATINGS_OBJECT)
    if path.is_file():
        raw = json.loads(path.read_text(encoding="utf-8"))
        return merge_doc(raw), "local"
    return merge_doc(None), "local"


def save_ratings(doc: dict, generation: str) -> bool:
    if IS_CLOUD_RUN:
        return gcs_put(RATINGS_OBJECT, doc, generation)
    local_path(RATINGS_OBJECT).write_text(
        json.dumps(doc, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return True


def save_contact(payload: dict) -> None:
    stamp = utc_now().replace(":", "")
    digest = hashlib.sha256(json_bytes(payload)).hexdigest()[:12]
    name = f"contacts/{stamp}-{digest}.json"
    record = dict(payload)
    record["receivedAt"] = utc_now()
    if IS_CLOUD_RUN:
        gcs_put(name, record, "0")
        return
    path = local_path(name)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")


def format_mail(payload: dict) -> str:
    lines = [
        SUBJECT[payload["lang"]],
        "",
        f"Jméno / Name: {payload['name']}",
    ]
    if payload["phone"]:
        lines.append(f"Telefon / Phone: {payload['phone']}")
    lines.append(f"E-mail: {payload['email']}")
    if payload["products"]:
        lines.append(f"Směsi / Mixes: {', '.join(payload['products'])}")
    if payload["message"]:
        lines.append(f"Zpráva / Message:\n{payload['message']}")
    return "\n".join(lines)


def is_zapier_hook(url: str) -> bool:
    try:
        parsed = urllib.parse.urlparse(url)
    except ValueError:
        return False
    host = (parsed.hostname or "").lower()
    return parsed.scheme == "https" and (
        host == "hooks.zapier.com" or host.endswith(".hooks.zapier.com")
    )


def http_json(url: str, payload: dict, timeout: int = 10) -> bool:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={"Content-Type": "application/json", "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            return 200 <= res.status < 300
    except (urllib.error.URLError, TimeoutError, OSError):
        return False


def send_zapier(payload: dict) -> bool:
    hook = (os.environ.get("ZAPIER_WEBHOOK_URL") or "").strip()
    if not is_zapier_hook(hook):
        return False
    return http_json(hook, {
        "to": CONTACT_TO,
        "subject": SUBJECT[payload["lang"]],
        "name": payload["name"],
        "phone": payload["phone"],
        "email": payload["email"],
        "message": payload["message"],
        "products": ", ".join(payload["products"]),
        "lang": payload["lang"],
        "body": format_mail(payload),
    })


def send_smtp(payload: dict) -> bool:
    host = (os.environ.get("SMTP_HOST") or "").strip()
    user = (os.environ.get("SMTP_USER") or "").strip()
    password = os.environ.get("SMTP_PASS") or ""
    if not host or not user or not password:
        return False
    port = int(os.environ.get("SMTP_PORT") or "465")
    mail_from = (os.environ.get("SMTP_FROM") or user).strip()
    msg = EmailMessage()
    msg["Subject"] = SUBJECT[payload["lang"]]
    msg["From"] = mail_from
    msg["To"] = CONTACT_TO
    msg["Reply-To"] = payload["email"]
    msg.set_content(format_mail(payload))
    context = ssl.create_default_context()
    try:
        if port == 465:
            with smtplib.SMTP_SSL(host, port, timeout=10, context=context) as smtp:
                smtp.login(user, password)
                smtp.send_message(msg)
        else:
            with smtplib.SMTP(host, port, timeout=10) as smtp:
                smtp.starttls(context=context)
                smtp.login(user, password)
                smtp.send_message(msg)
        return True
    except (OSError, smtplib.SMTPException):
        return False


def deliver_contact(payload: dict) -> str:
    save_contact(payload)
    if send_zapier(payload):
        return "zapier"
    if send_smtp(payload):
        return "smtp"
    if not IS_CLOUD_RUN:
        return "dev"
    return "stored"


def parse_contact(raw: object) -> dict | str:
    if not isinstance(raw, dict):
        return "invalid"
    name = clip(raw.get("name"), 200)
    phone = clip(raw.get("phone"), 40)
    email = clip(raw.get("email"), 200)
    message = clip(raw.get("message"), 4000)
    lang_raw = clip(raw.get("lang"), 8).lower()
    lang = lang_raw if lang_raw in LANGS else "cs"
    honeypot = clip(raw.get("honeypot"), 200)
    products_raw = raw.get("products")
    products = []
    if isinstance(products_raw, list):
        for item in products_raw[:12]:
            value = clip(item, 120)
            if value:
                products.append(value)
    if not name or not email or not message:
        return "invalid"
    if not EMAIL_RE.match(email):
        return "invalid"
    return {
        "name": name,
        "phone": phone,
        "email": email,
        "message": message,
        "products": products,
        "lang": lang,
        "honeypot": honeypot,
    }


def handle_ratings_get(slug: str | None) -> tuple[int, dict]:
    doc, _gen = load_ratings()
    if not slug:
        return 200, public_all(doc)
    if slug not in SLUGS:
        return 404, {"error": "unknown_recipe"}
    return 200, {"slug": slug, **public_row(doc["recipes"][slug])}


def handle_ratings_post(slug: str, stars: int, ip: str, ua: str) -> tuple[int, dict]:
    if slug not in SLUGS:
        return 404, {"error": "unknown_recipe"}
    if stars < 1 or stars > 5:
        return 400, {"error": "invalid_stars"}
    vote = fingerprint(ip, ua, slug)
    for _ in range(8):
        doc, generation = load_ratings()
        row = doc["recipes"][slug]
        if vote in doc["votes"]:
            return 200, {"slug": slug, "already": True, **public_row(row)}
        row["sum_tenths"] += stars * 10
        row["count"] += 1
        doc["votes"][vote] = str(stars)
        if save_ratings(doc, generation):
            return 200, {"slug": slug, "already": False, **public_row(row)}
    return 503, {"error": "busy"}


class Handler(BaseHTTPRequestHandler):
    server_version = "juzlova-api/1"

    def log_message(self, fmt: str, *args: object) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _send(self, status: int, payload: dict) -> None:
        body = json_bytes(payload)
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self) -> object:
        length = int(self.headers.get("Content-Length") or "0")
        if length <= 0 or length > 20000:
            raise ValueError("invalid")
        raw = self.rfile.read(length)
        return json.loads(raw.decode("utf-8"))

    def _client_ip(self) -> str:
        forwarded = self.headers.get("X-Forwarded-For") or ""
        if forwarded:
            return forwarded.split(",")[0].strip()[:80]
        return (self.headers.get("X-Real-IP") or self.client_address[0] or "unknown")[:80]

    def do_OPTIONS(self) -> None:
        self.send_response(204)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Accept")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()

    def do_GET(self) -> None:
        path = urllib.parse.urlparse(self.path).path.rstrip("/")
        if path == "/api/contact":
            key = (os.environ.get("TURNSTILE_SITE_KEY") or "").strip()
            self._send(200, {"siteKey": key or None})
            return
        if path == "/api/ratings":
            status, payload = handle_ratings_get(None)
            self._send(status, payload)
            return
        if path.startswith("/api/ratings/"):
            slug = path.split("/", 3)[-1]
            status, payload = handle_ratings_get(slug)
            self._send(status, payload)
            return
        self._send(404, {"error": "not_found"})

    def do_POST(self) -> None:
        path = urllib.parse.urlparse(self.path).path.rstrip("/")
        if path == "/api/contact":
            try:
                raw = self._read_json()
            except (ValueError, json.JSONDecodeError):
                self._send(400, {"ok": False, "error": "invalid"})
                return
            parsed = parse_contact(raw)
            if isinstance(parsed, str):
                self._send(400, {"ok": False, "error": parsed})
                return
            if parsed["honeypot"]:
                self._send(200, {"ok": True})
                return
            try:
                with _lock:
                    mode = deliver_contact(parsed)
            except Exception:
                self._send(502, {"ok": False, "error": "mail"})
                return
            self._send(200, {"ok": True, "mode": mode})
            return
        if path.startswith("/api/ratings/"):
            slug = path.split("/", 3)[-1]
            try:
                raw = self._read_json()
                stars = int(raw.get("stars")) if isinstance(raw, dict) else 0
            except (ValueError, json.JSONDecodeError, TypeError):
                self._send(400, {"error": "invalid"})
                return
            if stars < 1 or stars > 5:
                self._send(400, {"error": "invalid_stars"})
                return
            try:
                with _lock:
                    status, payload = handle_ratings_post(
                        slug,
                        stars,
                        self._client_ip(),
                        self.headers.get("User-Agent") or "",
                    )
            except Exception:
                self._send(503, {"error": "store"})
                return
            self._send(status, payload)
            return
        self._send(404, {"error": "not_found"})


def main() -> None:
    httpd = ThreadingHTTPServer((LISTEN_HOST, LISTEN_PORT), Handler)
    print(f"juzlova-api listening on {LISTEN_HOST}:{LISTEN_PORT}", flush=True)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
