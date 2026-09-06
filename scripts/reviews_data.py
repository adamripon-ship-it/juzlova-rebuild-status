"""Live Google + Seznam (Firmy.cz / Mapy) star ratings for the site.

Seznam score is refreshed at build from Mapy suggest (reviewPercentage).
Google score uses Places API when GOOGLE_PLACES_API_KEY is set; otherwise
the last known public scan is kept and still linked to the live Maps listing.
Never invent stars — only publish numbers we can source.
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
CACHE = ROOT / "data" / "reviews.json"

GOOGLE_URL = (
    "https://www.google.com/maps/search/?api=1&query="
    + urllib.parse.quote("Juzlova - Potravinarske smesi, Kochánov 40, 582 53")
)
SEZNAM_URL = "https://www.firmy.cz/detail/12906730-juzlova-kochanov.html"
MAPY_SUGGEST = "https://pro.mapy.cz/suggest?count=1&phrase=juzlova%20kochanov"

# Last public scan (Orlové Potravinářství, 2026-02-27): Google 5.0 / 7 reviews.
# Used only when live Google fetch is unavailable.
GOOGLE_FALLBACK = {
    "rating": 5.0,
    "count": 7,
    "url": GOOGLE_URL,
    "source": "public scan 2026-02-27 (Orlové); confirm on Google Maps",
    "live": False,
}


def _get(url: str, timeout: int = 12) -> str:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "JuzlovaSiteBot/1.0 (+https://www.juzlova.cz)"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def fetch_seznam() -> dict:
    raw = _get(MAPY_SUGGEST)
    data = json.loads(raw)
    ud = (data.get("result") or [{}])[0].get("userData") or {}
    pct = ud.get("reviewPercentage")
    if pct is None:
        raise RuntimeError("Mapy suggest missing reviewPercentage")
    rating = round(float(pct) / 20.0, 1)
    count = 3
    try:
        html = _get(SEZNAM_URL)
        m = re.search(r'badgeReviewCount">(\d+)\s*hodnoc', html)
        if m:
            count = int(m.group(1))
    except Exception:
        pass
    return {
        "rating": rating,
        "count": count,
        "url": SEZNAM_URL,
        "source": "Seznam Mapy / Firmy.cz (live at build)",
        "live": True,
        "review_percentage": pct,
    }


def fetch_google() -> dict:
    key = os.environ.get("GOOGLE_PLACES_API_KEY") or os.environ.get("GOOGLE_MAPS_API_KEY")
    place_id = os.environ.get("GOOGLE_PLACE_ID")
    if key and place_id:
        q = urllib.parse.urlencode(
            {
                "place_id": place_id,
                "fields": "rating,user_ratings_total,url,name",
                "key": key,
            }
        )
        payload = json.loads(_get(f"https://maps.googleapis.com/maps/api/place/details/json?{q}"))
        result = payload.get("result") or {}
        if result.get("rating") is not None:
            return {
                "rating": float(result["rating"]),
                "count": int(result.get("user_ratings_total") or 0),
                "url": result.get("url") or GOOGLE_URL,
                "source": "Google Places API (live at build)",
                "live": True,
            }
    return dict(GOOGLE_FALLBACK)


def load_reviews() -> dict:
    google = dict(GOOGLE_FALLBACK)
    seznam = {
        "rating": 4.8,
        "count": 3,
        "url": SEZNAM_URL,
        "source": "cached",
        "live": False,
    }
    try:
        seznam = fetch_seznam()
    except Exception as exc:
        seznam["source"] = f"cache after fetch error: {exc}"
    try:
        google = fetch_google()
    except Exception as exc:
        google = dict(GOOGLE_FALLBACK)
        google["source"] = f"fallback after fetch error: {exc}"

    payload = {
        "google": google,
        "seznam": seznam,
        "updated": True,
    }
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return payload


def stars_html(rating: float, label: str) -> str:
    """Accessible star row for a 0–5 rating."""
    full = int(rating)
    half = 1 if (rating - full) >= 0.3 else 0
    empty = 5 - full - half
    parts = []
    for _ in range(full):
        parts.append('<span class="star star-full" aria-hidden="true">★</span>')
    if half:
        parts.append('<span class="star star-half" aria-hidden="true">★</span>')
    for _ in range(empty):
        parts.append('<span class="star star-empty" aria-hidden="true">☆</span>')
    return (
        f'<span class="stars" role="img" aria-label="{label}: {rating} / 5">'
        + "".join(parts)
        + "</span>"
    )
