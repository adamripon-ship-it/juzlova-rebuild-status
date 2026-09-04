#!/usr/bin/env python3
"""Pull the Google rating and reviews into data/reviews.json.

Meant for CI, not for the page. The Places API is billed per call and a key
shipped to the browser gets scraped and spent by somebody else, so the fetch
happens once at build time behind a repository secret and the result is
committed as plain JSON.

    GOOGLE_PLACES_API_KEY   an API key with Places API (New) enabled
    GOOGLE_PLACE_ID         the Place ID for Kochánov 40

Exits 0 and writes nothing when either is missing, so the workflow can call it
unconditionally. Standard library only, like everything else that runs in the
build.

The API returns at most five reviews. That is a Google limit, not a bug here.
"""
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "reviews.json"

FIELDS = "rating,userRatingCount,reviews,googleMapsUri"


def fetch(place_id, key):
    req = urllib.request.Request(
        f"https://places.googleapis.com/v1/places/{place_id}",
        headers={"X-Goog-Api-Key": key, "X-Goog-FieldMask": FIELDS},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main():
    key = os.environ.get("GOOGLE_PLACES_API_KEY", "").strip()
    place_id = os.environ.get("GOOGLE_PLACE_ID", "").strip()
    if not key or not place_id:
        print("GOOGLE_PLACES_API_KEY / GOOGLE_PLACE_ID not set — "
              "leaving data/reviews.json alone.")
        return 0

    try:
        data = fetch(place_id, key)
    except urllib.error.HTTPError as e:
        # A failed fetch must not overwrite good data with nothing, and must
        # not fail the build: the site renders fine without a rating.
        print(f"::warning title=Reviews not refreshed::Places API returned "
              f"{e.code}. data/reviews.json is unchanged.")
        return 0
    except OSError as e:
        print(f"::warning title=Reviews not refreshed::{e}. "
              f"data/reviews.json is unchanged.")
        return 0

    rating, count = data.get("rating"), data.get("userRatingCount")
    if not rating or not count:
        print("::warning title=No rating::The place has no rating yet.")
        return 0

    reviews = []
    for r in data.get("reviews", []):
        text = (r.get("originalText") or r.get("text") or {})
        body = (text.get("text") or "").strip()
        if not body:
            continue
        reviews.append({
            "source": "google",
            "author": (r.get("authorAttribution") or {}).get("displayName", ""),
            "rating": r.get("rating"),
            # publishTime is RFC 3339; the date alone is all the page shows.
            "date": (r.get("publishTime") or "")[:10],
            "lang": text.get("languageCode", ""),
            "text": {text.get("languageCode", "cs"): body},
            "url": r.get("googleMapsUri", ""),
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "ratings": {"google": {
            "value": f"{rating:.1f}",
            "count": count,
            "best": 5,
            "checked": __import__("datetime").date.today().isoformat(),
        }},
        "reviews": reviews,
    }, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {OUT.relative_to(ROOT)}: {rating} from {count} ratings, "
          f"{len(reviews)} reviews.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
