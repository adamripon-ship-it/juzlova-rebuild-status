"""Where customers rate Jůzlová, and what those ratings say.

NOTHING IN THIS FILE MAY BE INVENTED. A rating or a review is a claim about
what real people said; making one up is both a lie to customers and, in the
EU, an unfair commercial practice. Every number here must be copied from the
profile it names, on the date recorded next to it, or fetched from an API.
If a figure is not known, leave it out — the site renders the section without
it rather than guessing.

PROFILES are the public pages themselves. They are safe to link and to put in
`sameAs` regardless of whether we know the score, and linking all three is
what tells a search engine or an assistant that these listings are one
business rather than three.

RATINGS carries the aggregate for each profile. Filling one in makes the
score visible on the site and, for the primary profile, emits
`aggregateRating` in the Organization schema. Google requires that a marked-up
aggregate be genuine and visible on the page, so the two move together by
design: the number cannot appear in the markup without also appearing to a
human reader.

Why no live fetch, per source:

  Google    The Places API returns up to five reviews and the aggregate, but
            it needs an API key and it is billed per call. A key in the page
            would be scraped and spent by someone else, so the fetch belongs
            in CI: set GOOGLE_PLACES_API_KEY and GOOGLE_PLACE_ID as repository
            secrets and scripts/fetch_reviews.py writes the result here.
  Facebook  Meta has restricted the Page `ratings` edge; for an ordinary page
            there is no supported way to read review text any more, and the
            Page Plugin embeds a timeline, not reviews. Link only.
  Firmy.cz  Seznam publishes no API. The score has to be read off the page and
            typed in, which is what `checked` is for.
"""
import json
import pathlib

# ── the public profiles ─────────────────────────────────────────────────────
# `url` must be the profile itself, not a search that happens to find it —
# these go into schema.org `sameAs`, which asserts identity.

PROFILES = [
    {
        "key": "facebook",
        "name": "Facebook",
        "url": "https://www.facebook.com/juzlova/",
        "reviews_url": "https://www.facebook.com/juzlova/reviews",
    },
    {
        # Supplied by the owner. Firmy.cz also serves a Czech-language path for
        # the same listing, but only this URL has been confirmed to resolve, and
        # a sameAs pointing at a guess is worse than one pointing at English.
        "key": "firmy",
        "name": "Firmy.cz",
        "url": "https://en.firmy.cz/company/12906730-juzlova-kochanov.html",
        "reviews_url": "https://en.firmy.cz/company/12906730-juzlova-kochanov.html",
    },
    # Google Business Profile: add it here once the owner supplies the profile
    # URL (or the Place ID). It is deliberately absent rather than guessed —
    # a Maps search URL is not the business's own page and does not belong in
    # sameAs.
]

# ── aggregate scores ────────────────────────────────────────────────────────
# key -> {"value": "4.9", "count": 27, "best": 5, "checked": "YYYY-MM-DD"}
# Copy from the profile; record the date you read it.

RATINGS = {}

# Which profile's aggregate represents the business in structured data.
# Only used when RATINGS holds an entry for it.
PRIMARY = "google"

# ── individual reviews ──────────────────────────────────────────────────────
# Each entry: {"source": <profile key>, "author": str, "rating": int,
#              "date": "YYYY-MM-DD", "text": {"cs": str, "en": str, ...}}
# Quote reviews verbatim in their original language. A translation is a
# convenience for other locales, never a rewrite of what the customer said.

REVIEWS = []


# ── optional overlay written by CI ──────────────────────────────────────────
# scripts/fetch_reviews.py writes data/reviews.json when the Google credentials
# are present. Loading it here rather than rewriting this file keeps the
# hand-entered figures above readable and reviewable in a diff.

def _load_overlay():
    path = pathlib.Path(__file__).resolve().parent.parent / "data" / "reviews.json"
    if not path.exists():
        return
    data = json.loads(path.read_text())
    for key, rating in (data.get("ratings") or {}).items():
        RATINGS[key] = rating
    for review in (data.get("reviews") or []):
        REVIEWS.append(review)


_load_overlay()


def profile(key):
    for p in PROFILES:
        if p["key"] == key:
            return p
    return None


def same_as():
    """Profile URLs for schema.org sameAs."""
    return [p["url"] for p in PROFILES]


def aggregate():
    """The rating to publish, or None when no real figure is on file."""
    r = RATINGS.get(PRIMARY)
    if not r:
        # Fall back to any profile we do have a figure for, so one known score
        # is better than none.
        for p in PROFILES:
            if p["key"] in RATINGS:
                r = RATINGS[p["key"]]
                key = p["key"]
                break
        else:
            return None
    else:
        key = PRIMARY
    if not r.get("value") or not r.get("count"):
        return None
    return {**r, "key": key, "profile": profile(key)}


def known_ratings():
    """Every profile that has a real score on file, in PROFILES order."""
    out = []
    for p in PROFILES:
        r = RATINGS.get(p["key"])
        if r and r.get("value") and r.get("count"):
            out.append({**r, "key": p["key"], "profile": p})
    return out
