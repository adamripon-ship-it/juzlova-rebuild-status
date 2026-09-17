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
import uuid
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
FORMSPREE_ID_RE = re.compile(r"^[A-Za-z0-9]{6,20}$")
PHONE_DIGITS_RE = re.compile(r"\d")
LANGS = ("cs", "en", "de", "sk")
OWNER_SUBJECT = "Jůzlová — nová poptávka z webu"
OWNER_SUBJECT_NL = "Jůzlová — nový odběr novinek"
LANG_NAME_CS = {
    "cs": "čeština",
    "en": "angličtina",
    "de": "němčina",
    "sk": "slovenština",
}
BUYER_NAME_CS = {
    "household": "domácnost",
    "restaurant": "restaurace, jídelna nebo cukrárna",
}
FULFILL_NAME_CS = {
    "factory": "vyzvednutí v dílně Kochánov 40, 582 53",
    "humpolec": "vyzvednutí v Humpolci u Pivovaru Bernard",
    "delivery": "rozvoz",
}
KIND_NAME_CS = {
    "contact": "poptávka",
    "b2b": "velkoobchod",
    "newsletter": "odběr novinek",
}
TOPIC_OWNER_CS = {
    "general": "obecná velkoobchodní poptávka",
    "praha": "Praha (min. 25 kg mix)",
    "brno": "Brno",
    "vysocina": "Vysočina",
    "international": "zahraniční velkoobchod",
    "restaurant": "restaurace / jídelna",
    "bakery": "pekárna / cukrárna",
    "school": "škola",
    "icecream": "výroba zmrzliny",
    "other": "jiné",
}

_lock = threading.Lock()
_token = {"value": "", "exp": 0.0}
_rate: dict[str, list[float]] = {}
RATE_WINDOW_SEC = 600
RATE_MAX = 8


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


def save_contact(payload: dict) -> bool:
    """Create once across instances/retries; False means this inquiry is stored."""
    name = f"contacts/{payload['submission_id']}.json"
    record = dict(payload, receivedAt=utc_now())
    if IS_CLOUD_RUN:
        return gcs_put(name, record, "0")
    path = local_path(name)
    try:
        with path.open("x", encoding="utf-8") as handle:
            json.dump(record, handle, ensure_ascii=False, indent=2)
    except FileExistsError:
        return False
    return True


def parse_attribution(raw: object) -> dict | None:
    if not isinstance(raw, dict) or raw.get("consent") is not True:
        return None
    sources = {"chatgpt", "perplexity", "claude", "gemini", "copilot",
               "organic_search", "other_referral", "direct", "unknown"}
    result = {"consent": True}
    for key in ("first_source", "last_source"):
        value = raw.get(key)
        result[key] = value if isinstance(value, str) and value in sources else "unknown"
    path = raw.get("landing_path")
    # Canonical paths only: never a raw referrer, query, fragment or full URL.
    if isinstance(path, str) and re.fullmatch(r"/[a-zA-Z0-9/_-]{0,240}", path) and "//" not in path:
        result["landing_path"] = path
    language = raw.get("language")
    result["language"] = language if isinstance(language, str) and language in LANGS else "cs"
    return result


def identify_submission(payload: dict, request_id: object) -> None:
    """Server-issued opaque ID; same request and fields share one durable record."""
    try:
        nonce = uuid.UUID(str(request_id)).hex
    except (ValueError, TypeError, AttributeError):
        nonce = uuid.uuid4().hex
    identity = json.dumps({k: v for k, v in payload.items() if k != "attribution"}, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    digest = hashlib.sha256((nonce + identity).encode()).hexdigest()[:32]
    prefix = "newsletter_" if payload["kind"] == "newsletter" else "lead_"
    payload["submission_id"] = prefix + digest


def save_llms_hit(ua: str, uri: str) -> None:
    """Store crawler user-agent and date only. No IP or extra personal data."""
    record = {
        "at": utc_now(),
        "ua": clip(ua, 400),
        "path": clip(uri, 80),
    }
    sys.stderr.write("llms-hit %s %s\n" % (record["at"], record["ua"][:160]))
    stamp = utc_now().replace(":", "")
    digest = hashlib.sha256(
        f"{record['at']}|{record['ua']}|{record['path']}".encode("utf-8", "replace")
    ).hexdigest()[:10]
    name = f"llms-hits/{stamp}-{digest}.json"
    try:
        if IS_CLOUD_RUN:
            gcs_put(name, record, "0")
            return
        path = local_path(name)
        path.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")
    except Exception as exc:
        sys.stderr.write("llms-hit store failed: %s\n" % exc)


def owner_subject(payload: dict) -> str:
    if payload.get("kind") == "newsletter":
        return OWNER_SUBJECT_NL
    return OWNER_SUBJECT


def format_mail(payload: dict) -> str:
    """Owner inbox is Czech-only. Visitor answers stay as typed."""
    lang = payload.get("lang") or "cs"
    lang_cs = LANG_NAME_CS.get(lang, lang)
    buyer_raw = payload.get("buyer") or ""
    buyer_cs = BUYER_NAME_CS.get(buyer_raw, buyer_raw)
    kind = payload.get("kind") or "contact"
    kind_cs = KIND_NAME_CS.get(kind, kind)
    fulfill_raw = payload.get("fulfillment") or ""
    fulfill_cs = FULFILL_NAME_CS.get(fulfill_raw, fulfill_raw)
    if kind == "newsletter":
        return "\n".join([
            "Nový odběr novinek z webu Jůzlová",
            "",
            f"Jazyk webu: {lang_cs}",
            f"Jméno: {payload['name']}",
            f"E-mail: {payload.get('email') or ''}",
            "Souhlas s novinkami: ano",
        ])
    lines = [
        "Nová poptávka z webu Jůzlová",
        "",
        f"ID poptávky: {payload.get('submission_id', '')}",
        f"Typ zprávy: {kind_cs}",
        f"Jazyk webu: {lang_cs}",
        f"Jméno: {payload['name']}",
    ]
    attribution = payload.get("attribution")
    if attribution:
        lines.append(f"Zdroj návštěvy (se souhlasem): {attribution['first_source']} / {attribution['last_source']}")
        if attribution.get("landing_path"):
            lines.append(f"Vstupní stránka: {attribution['landing_path']}")
    if payload["phone"]:
        lines.append(f"Telefon: {payload['phone']}")
    if payload["email"]:
        lines.append(f"E-mail: {payload['email']}")
    if buyer_cs:
        lines.append(f"Odebírá pro: {buyer_cs}")
    topic_raw = payload.get("topic") or ""
    topic_cs = TOPIC_OWNER_CS.get(topic_raw, "")
    if topic_cs:
        lines.append(f"Téma: {topic_cs}")
    if payload["products"]:
        lines.append(f"Zájem o směsi: {', '.join(payload['products'])}")
    if payload.get("quantity"):
        lines.append(f"Množství: {payload['quantity']}")
    if fulfill_cs:
        lines.append(f"Způsob odběru: {fulfill_cs}")
    if payload["message"]:
        lines.append(f"Zpráva návštěvníka:\n{payload['message']}")
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


def http_json(
    url: str,
    payload: dict,
    timeout: int = 10,
    extra_headers: dict | None = None,
) -> tuple[bool, object]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    if extra_headers:
        headers.update(extra_headers)
    req = urllib.request.Request(url, data=data, method="POST", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            raw = res.read().decode("utf-8", "replace")
            try:
                body: object = json.loads(raw) if raw.strip() else {}
            except json.JSONDecodeError:
                body = {"raw": raw[:400]}
            return 200 <= res.status < 300, body
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", "replace") if exc.fp else ""
        try:
            body = json.loads(raw) if raw.strip() else {"error": exc.code}
        except json.JSONDecodeError:
            body = {"raw": raw[:400], "error": exc.code}
        return False, body
    except (urllib.error.URLError, TimeoutError, OSError, ValueError):
        return False, {}


def mail_fields(payload: dict) -> dict:
    return {
        "to": CONTACT_TO,
        "subject": owner_subject(payload),
        "name": payload["name"],
        "phone": payload["phone"],
        "email": payload["email"],
        "message": payload["message"],
        "buyer": payload.get("buyer") or "",
        "products": ", ".join(payload["products"]),
        "lang": payload["lang"],
        "body": format_mail(payload),
    }


def send_zapier(payload: dict) -> bool:
    hook = (os.environ.get("ZAPIER_WEBHOOK_URL") or "").strip()
    if not is_zapier_hook(hook):
        return False
    ok, _body = http_json(hook, mail_fields(payload))
    return ok


def send_smtp(payload: dict) -> bool:
    host = (os.environ.get("SMTP_HOST") or "").strip()
    user = (os.environ.get("SMTP_USER") or "").strip()
    password = os.environ.get("SMTP_PASS") or ""
    if not host or not user or not password:
        return False
    port = int(os.environ.get("SMTP_PORT") or "465")
    mail_from = (os.environ.get("SMTP_FROM") or user).strip()
    msg = EmailMessage()
    msg["Subject"] = owner_subject(payload)
    msg["From"] = mail_from
    msg["To"] = CONTACT_TO
    if payload["email"]:
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


def formspree_url() -> str:
    raw_url = (os.environ.get("FORMSPREE_ENDPOINT") or "").strip()
    if raw_url:
        try:
            parsed = urllib.parse.urlparse(raw_url)
        except ValueError:
            return ""
        host = (parsed.hostname or "").lower()
        if parsed.scheme == "https" and host in ("formspree.io", "www.formspree.io"):
            if parsed.path.startswith("/f/") and len(parsed.path) > 3:
                return raw_url.split("?", 1)[0]
        return ""
    form_id = (os.environ.get("FORMSPREE_FORM_ID") or "").strip()
    if not FORMSPREE_ID_RE.match(form_id):
        return ""
    return f"https://formspree.io/f/{form_id}"


def send_formspree(payload: dict) -> bool:
    url = formspree_url()
    if not url:
        return False
    body = {
        "name": payload["name"],
        "phone": payload["phone"],
        "email": payload["email"] or "noreply@juzlova.cz",
        "message": format_mail(payload),
        "buyer": payload.get("buyer") or "",
        "products": ", ".join(payload["products"]),
        "lang": payload["lang"],
        "_subject": owner_subject(payload),
    }
    ok, data = http_json(url, body, extra_headers={"Origin": "https://www.juzlova.cz"})
    if not ok:
        return False
    if isinstance(data, dict) and data.get("error"):
        return False
    return True


def send_formsubmit(payload: dict) -> str:
    """Post to FormSubmit so juzlj@seznam.cz gets the enquiry.

    First use asks the inbox to click Activate Form once. After that,
    later posts are delivered without Cursor.
    """
    to = CONTACT_TO
    if not EMAIL_RE.match(to):
        return ""
    url = f"https://formsubmit.co/ajax/{urllib.parse.quote(to)}"
    body = {
        "name": payload["name"],
        "phone": payload["phone"],
        "email": payload["email"] or "noreply@juzlova.cz",
        "buyer": payload.get("buyer") or "",
        "products": ", ".join(payload["products"]),
        "lang": payload["lang"],
        "message": format_mail(payload),
        "_subject": owner_subject(payload),
        "_template": "box",
        "_captcha": "false",
        "_honey": payload.get("honeypot") or "",
    }
    ok, data = http_json(
        url,
        body,
        timeout=12,
        extra_headers={
            "Origin": "https://www.juzlova.cz",
            "Referer": "https://www.juzlova.cz/kontakt/",
            "User-Agent": (
                "Mozilla/5.0 (compatible; JuzlovaContact/1.0; "
                "+https://www.juzlova.cz/kontakt/)"
            ),
        },
    )
    if not isinstance(data, dict):
        return "formsubmit" if ok else ""
    success = str(data.get("success") or "").lower()
    text = str(data.get("message") or "")
    if "activation" in text.lower() or "activate form" in text.lower():
        return "formsubmit_activate"
    if ok and success in ("true", "1", "yes"):
        return "formsubmit"
    return ""


def deliver_contact(payload: dict) -> str:
    if not save_contact(payload):
        return "stored_existing"
    if send_zapier(payload):
        return "zapier"
    if send_smtp(payload):
        return "smtp"
    if send_formspree(payload):
        return "formspree"
    formsubmit = send_formsubmit(payload)
    if formsubmit:
        return formsubmit
    if not IS_CLOUD_RUN:
        return "dev"
    return "stored"


def rate_ok(ip: str) -> bool:
    now = time.time()
    hits = [t for t in _rate.get(ip, []) if now - t < RATE_WINDOW_SEC]
    if len(hits) >= RATE_MAX:
        _rate[ip] = hits
        return False
    hits.append(now)
    _rate[ip] = hits
    return True


def public_config() -> dict:
    key = (os.environ.get("TURNSTILE_SITE_KEY") or "").strip()
    token = (os.environ.get("CLOUDFLARE_WEB_ANALYTICS_TOKEN") or "").strip()
    maps = (
        (os.environ.get("GOOGLE_MAPS_API_KEY") or "").strip()
        or (os.environ.get("MAPS_API_KEY") or "").strip()
    )
    return {
        "revision": os.environ.get("SITE_REVISION", ""),
        "siteKey": key or None,
        "analyticsToken": token or None,
        "mapsKey": bool(maps) or None,
    }


def parse_contact(raw: object) -> dict | str:
    if not isinstance(raw, dict):
        return "invalid"
    kind_raw = clip(raw.get("type"), 20).lower()
    kind = kind_raw if kind_raw in KIND_NAME_CS else "contact"
    name = clip(raw.get("name"), 200)
    phone = clip(raw.get("phone"), 40)
    email = clip(raw.get("email"), 200)
    message = clip(raw.get("message"), 4000)
    quantity = clip(raw.get("quantity"), 200)
    lang_raw = clip(raw.get("lang"), 8).lower()
    lang = lang_raw if lang_raw in LANGS else "cs"
    honeypot = clip(raw.get("honeypot"), 200)
    buyer_raw = clip(raw.get("buyer"), 32).lower()
    buyer = buyer_raw if buyer_raw in ("household", "restaurant") else ""
    fulfill_raw = clip(raw.get("fulfillment"), 32).lower()
    fulfillment = fulfill_raw if fulfill_raw in FULFILL_NAME_CS else ""
    consent_raw = clip(raw.get("consent"), 8).lower()
    has_consent = consent_raw in ("yes", "true", "1", "on")
    products_raw = raw.get("products")
    products = []
    if isinstance(products_raw, list):
        for item in products_raw[:12]:
            value = clip(item, 120)
            if value:
                products.append(value)
    topic_raw = clip(raw.get("topic"), 40).lower()
    topic = topic_raw if topic_raw in TOPIC_OWNER_CS else ""
    if kind == "newsletter":
        if not email or not EMAIL_RE.match(email):
            return "need_contact"
        if not has_consent:
            return "consent"
        return {
            "kind": kind,
            "name": name or "Odběratel novinek",
            "phone": "",
            "email": email,
            "message": "",
            "buyer": "",
            "products": [],
            "quantity": "",
            "topic": "",
            "fulfillment": "",
            "lang": lang,
            "honeypot": honeypot,
        }
    if not name:
        return "invalid"
    if not phone and not email:
        return "need_contact"
    if email and not EMAIL_RE.match(email):
        return "invalid"
    if phone and len(PHONE_DIGITS_RE.findall(phone)) < 6:
        return "invalid"
    if kind == "b2b" and not topic:
        return "invalid"
    return {
        "kind": kind,
        "attribution": parse_attribution(raw.get("attribution")),
        "name": name,
        "phone": phone,
        "email": email,
        "message": message,
        "buyer": buyer,
        "products": products,
        "quantity": quantity,
        "topic": topic,
        "fulfillment": fulfillment,
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

    def _llms_log(self) -> None:
        ua = self.headers.get("User-Agent") or ""
        uri = self.headers.get("X-Original-URI") or "/llms.txt"
        if os.environ.get("PREVIEW_READ_ONLY") != "1":
            save_llms_hit(ua, uri)
        self.send_response(204)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self) -> None:
        path = urllib.parse.urlparse(self.path).path.rstrip("/")
        if path == "/api/llms-log":
            self._llms_log()
            return
        if path in ("/api/contact", "/api/config"):
            self._send(200, public_config())
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
        if os.environ.get("PREVIEW_READ_ONLY") == "1":
            self._send(403, {"ok": False, "error": "preview_read_only"})
            return
        path = urllib.parse.urlparse(self.path).path.rstrip("/")
        if path == "/api/llms-log":
            self._llms_log()
            return
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
            if not rate_ok(self._client_ip()):
                self._send(429, {"ok": False, "error": "rate"})
                return
            identify_submission(parsed, raw.get("requestId"))
            try:
                with _lock:
                    mode = deliver_contact(parsed)
            except Exception as exc:
                sys.stderr.write("contact deliver failed: %s\n" % exc)
                self._send(502, {"ok": False, "error": "mail"})
                return
            sys.stderr.write("contact delivered mode=%s\n" % mode)
            response = {"ok": True, "mode": mode}
            if parsed["kind"] != "newsletter":
                response["lead_id"] = parsed["submission_id"]
            self._send(200, response)
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
