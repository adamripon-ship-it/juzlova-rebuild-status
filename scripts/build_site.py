#!/usr/bin/env python3
"""Build the multilingual juzlova.cz site into the repo root.

Languages: cs (root, default), en/, de/, sk/. Content comes from
scripts/content_{cs,en,de,sk}.py. Recipes are merged from
scripts/recipes_{lang}.py when present.

Outputs per page: redesigned HTML with full SEO metadata, hreflang
alternates, JSON-LD (Organization, Product, Recipe, FAQPage,
BreadcrumbList), plus sitemap.xml, robots.txt, llms.txt, llms-full.txt
and legacy-URL redirect stubs.
"""
import hashlib
import html as H
import importlib.util
import json
import os
import pathlib
import re
import shutil
import sys
import urllib.parse

_SCRIPTS = pathlib.Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))
from aeo_pages import (
    AEO_PAGE_KEYS, AEO_PAGES, B2B_SLUGS, GEO_SLUGS, TOPIC_KEYS,
    apply_aeo_ui, merge_product_faq, page_faq,
)
from cocoa_blocks import (
    cocoa_apps_html, cocoa_facts_html, cocoa_nutrition_html, cocoa_sensory_html,
)
from geo_faq import b2b_faq, home_faq, recipe_faq, site_faq
from reviews_data import load_reviews, stars_html
from seo_data import (
    CUISINE, PRODUCT_PRIORITY, RECIPE_CATEGORY, RECIPE_PRIORITY, RECIPE_TIMES,
    SITEMAP_PRIORITY, compose_meta, keywords_for, rating_payload,
)
from team_data import TEAM

ROOT = pathlib.Path(__file__).resolve().parent.parent


def _load_dotenv():
    path = ROOT / ".env"
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


_load_dotenv()
BASE = os.environ.get("SITE_BASE", "https://www.juzlova.cz").rstrip("/")
TODAY = "2026-09-03"
ASSET_VER = "20260906a"
REVIEWS = load_reviews()

LANGS = ["cs", "en", "de", "sk"]
PRODUCT_SLUGS = {
    "bramborove_knedliky": "bramborove_knedliky",
    "chlupate_knedliky": "chlupate-knedliky",
    "vanilkovy_pudink": "vanilkovy_pudink",
    "kakao_holandskeho_typu": "kakao-holandskeho-typu",
    "vanilkovy_cukr": "vanilkovy-cukr",
}
PAGE_SLUGS = {
    "kdo_jsme": "kdo_jsme",
    "kde_nas_najdete": "kde-nas-najdete",
    "velkoobchod": "velkoobchod",
    "do_eu": "do-eu",
    "kontakt": "kontakt",
    "ceny": "ceny",
}
RECIPE_SLUGS = [
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
]
CHOUX_SLUGS = frozenset({
    "rychle-venecky-ci-vetrnicky-recept",
    "venecky-s-vanilkovym-kremem-recept",
    "kremrole-recept",
    "minivetrnicky-recept",
    "karamelove-vetrniky-recept",
})
DUMPLING_SLUGS = frozenset({
    "sisky-s-makem-recept",
    "strapacky-se-zelim-a-slaninou-recept",
    "bramborovo-tvarohove-knedliky-s-jahodami",
})
SUGGESTED_RECIPES = 6
HOME_RECIPE_SLUGS = [
    "sisky-s-makem-recept",
    "hruskovy-kolac-s-vanilkovym-pudinkem-recept",
    "strapacky-se-zelim-a-slaninou-recept",
    "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem",
    "slehackova-rolada-recept",
    "domaci-pernik-recept-podle-jirina-juzlova",
]
# archive image file -> public img name (used when archive/images is populated)
IMAGE_MAP = {
    "wp-content_uploads_2017_06_juzlova-logo-black-2017.png": "logo.png",
    "wp-content_uploads_2012_07_Bramborov_-knedl_ky-300x225.png": "bramborove-knedliky.png",
    # Named for chlupaté knedlíky on the old site, but the picture is actually
    # two packets of vanilla sugar. Published under what it shows.
    "wp-content_uploads_2012_07_Chlupat_-knedl_ky-300x225.png": "vanilkovy-cukr-pytliky.png",
    "wp-content_uploads_2012_07_Vanilkov_-puding-juzlova-300x225.png": "vanilkovy-puding.png",
    "wp-content_uploads_2012_07_Kakaov_-puding-juzlova-224x300.png": "kakaovy-puding.png",
    "wp-content_uploads_2012_07_HERO_Hot-Cocoa_363x276-300x228.jpg": "kakao.jpg",
    "wp-content_uploads_2012_07_Vanilkov_-cukr-juzlova-300x103.png": "vanilkovy-cukr.png",
    "wp-content_uploads_2012_07_Koch_nov-300x225.png": "kochanov.png",
    "wp-content_uploads_2017_04_Domaci-pernik-300x206.png": "domaci-pernik.png",
    "wp-content_uploads_2017_04_Bebe-rezy-s-cokoladovym-pudingem-300x231-300x206.gif": "bebe-rezy.gif",
    "wp-content_uploads_2017_04_slehackova-rolada-juzlova-1-1-300x206.gif": "slehackova-rolada.gif",
    "wp-content_uploads_2017_04_Strapacky-se-zelim-a-slaninou-recept-juzlova.jpg": "strapacky.jpg",
    "wp-content_uploads_2017_04_Hruskovy-kolac-s-vanilkovym-pudinkem-2-300x300-300x206.png": "hruskovy-kolac.png",
    "wp-content_uploads_2017_04_Pe_en_-_i_ky-s-m_kem-recept-300x206.png": "sisky-s-makem.png",
    "wp-content_uploads_2012_07_IMG_20141026_100948-300x225.png": "vyroba.png",
    "wp-content_uploads_2017_04_Bramborovo-tvarohove-knedliky-s-jahodami-podle-lucie-kuzelove.jpg": "bramborovo-tvarohove-knedliky.jpg",
}
PRODUCT_IMG = {
    "bramborove_knedliky": "produkt-bramborove-knedliky.webp",
    "chlupate_knedliky": "produkt-chlupate-knedliky.webp",
    "vanilkovy_pudink": "produkt-vanilkovy-puding.webp",
    "kakao_holandskeho_typu": "produkt-kakao.webp",
    "vanilkovy_cukr": "vanilkovy-cukr.webp",
}
RECIPE_IMG = {
    "sisky-s-makem-recept": "sisky-s-makem.webp",
    "hruskovy-kolac-s-vanilkovym-pudinkem-recept": "hruskovy-kolac.webp",
    "strapacky-se-zelim-a-slaninou-recept": "strapacky.webp",
    "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": "bebe-rezy.webp",
    "slehackova-rolada-recept": "slehackova-rolada.webp",
    "domaci-pernik-recept-podle-jirina-juzlova": "domaci-pernik.webp",
    "bramborovo-tvarohove-knedliky-s-jahodami": "bramborovo-tvarohove-knedliky.webp",
    "rychle-venecky-ci-vetrnicky-recept": "rychle-venecky-vetrnicky.webp",
    "venecky-s-vanilkovym-kremem-recept": "venecky-s-vanilkovym-kremem.webp",
    "kremrole-recept": "kremrole.webp",
    "minivetrnicky-recept": "minivetrnicky.webp",
    "karamelove-vetrniky-recept": "karamelove-vetrniky.webp",
    "irsky-sticky-toffee-pudding-recept": "irsky-sticky-toffee-pudding.webp",
}
PRICE_ROWS = [  # (product key, package, price CZK)
    ("bramborove_knedliky", "5 kg", "250 Kč"),
    ("chlupate_knedliky", "5 kg", "260 Kč"),
    ("vanilkovy_pudink", "1 kg / 400 g", "60 Kč / 30 Kč"),
    ("kakao_holandskeho_typu", "500 g", "270 Kč"),
    ("vanilkovy_cukr", "1 kg", "60 Kč"),
]
# General averaged supermarket estimate for same quantity / higher quality.
SUPERMARKET_PRICE_FACTOR = 4


def price_amounts_czk(price_str):
    return [int(x) for x in re.findall(r"\d+", str(price_str))]


def format_czk_parts(amounts):
    return " / ".join(f"{n} Kč" for n in amounts)


def price_board_html(L, depth):
    """Visual pick-up prices + averaged supermarket comparison (~4×)."""
    ui = L["ui"]
    pages = page_rel(L["code"], depth)
    tiles = []
    compares = []
    for i, (key, pack, price) in enumerate(PRICE_ROWS):
        name = L["products"][key]["name"]
        href = f"{pages}{PRODUCT_SLUGS[key]}/"
        amounts = price_amounts_czk(price)
        shop_amounts = [n * SUPERMARKET_PRICE_FACTOR for n in amounts]
        save_amounts = [s - u for u, s in zip(amounts, shop_amounts)]
        shop_label = format_czk_parts(shop_amounts)
        save_label = format_czk_parts(save_amounts)
        tiles.append(
            f"""<article class="price-tile" style="--i:{i}">
<a class="price-tile-link" href="{href}" aria-label="{esc(name)} — {esc(price)}">
<span class="price-tile-badge">{esc(ui.get('price_pickup_badge', ui['price_label']))}</span>
<h3 class="price-tile-name">{esc(name)}</h3>
<p class="price-tile-pack">{esc(ui['package_label'])}: {esc(pack)}</p>
<p class="price-tile-amount"><span class="price-num">{esc(price)}</span></p>
</a>
</article>"""
        )
        # Bar widths: workshop = 25% (1/4), supermarket = 100%
        compares.append(
            f"""<div class="compare-row" style="--i:{i}">
<div class="compare-meta">
<a class="compare-name" href="{href}">{esc(name)}</a>
<span class="compare-pack">{esc(pack)}</span>
</div>
<div class="compare-bars" role="img" aria-label="{esc(ui.get('compare_us', 'Workshop'))}: {esc(price)}; {esc(ui.get('compare_shop', 'Supermarket'))}: {esc(shop_label)}">
<div class="compare-bar compare-bar--us" style="--w:25%">
<span class="compare-bar-label">{esc(ui.get('compare_us', 'Workshop'))}</span>
<span class="compare-bar-val">{esc(price)}</span>
</div>
<div class="compare-bar compare-bar--shop" style="--w:100%">
<span class="compare-bar-label">{esc(ui.get('compare_shop', 'Supermarket'))}</span>
<span class="compare-bar-val">≈ {esc(shop_label)}</span>
</div>
</div>
<p class="compare-save">{esc(ui.get('compare_factor', 'About 4×'))} · {esc(ui.get('compare_keep', 'you keep roughly'))} {esc(save_label)}</p>
</div>"""
        )
    board = (
        f'<div class="price-board" aria-label="{esc(ui.get("price_board_label", ui["price_label"]))}">'
        + "".join(tiles)
        + "</div>"
    )
    compare = (
        f'<section class="price-compare" aria-labelledby="price-compare-h">'
        f'<p class="kicker">{esc(ui.get("compare_kicker", ""))}</p>'
        f'<h2 id="price-compare-h">{esc(ui.get("compare_h2", "Comparing price with supermarket?"))}</h2>'
        f'<p class="lead">{esc(ui.get("compare_lead", ""))}</p>'
        f'<div class="compare-list">{"".join(compares)}</div>'
        f'<p class="compare-note">{esc(ui.get("compare_note", ""))}</p>'
        f"</section>"
    )
    return board + compare
LEGACY_REDIRECTS = {
    "kakao": "kakao-holandskeho-typu", "kakaovy_puding": "vanilkovy_pudink",
    "kakaovy_pudink": "vanilkovy_pudink",
    "vanilkovy_puding": "vanilkovy_pudink", "jiri-juzl": "kontakt",
    "jirina-juzlova": "kontakt", "jirina-juzlova-praha": "kontakt",
    "dotaz-na-produkty": "kontakt", "kdo-jsme": "kdo_jsme",
    "potravinarske-smesi-kontact-praha-ceske-republiky": "kontakt",
    "recepty-index": "recepty",
}


def load(lang):
    spec = importlib.util.spec_from_file_location(
        f"content_{lang}", ROOT / "scripts" / f"content_{lang}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    data = mod.LANG
    rp = ROOT / "scripts" / f"recipes_{lang}.py"
    if rp.exists():
        rspec = importlib.util.spec_from_file_location(f"recipes_{lang}", rp)
        rmod = importlib.util.module_from_spec(rspec)
        rspec.loader.exec_module(rmod)
        data["recipes"] = rmod.RECIPES
    return apply_aeo_ui(data)


def esc(s):
    return H.escape(str(s), quote=True)


GA_ID_RE = re.compile(r"^G-[A-Z0-9]{4,20}$")


def ga_measurement_id():
    raw = (
        os.environ.get("GOOGLE_ANALYTICS_MEASUREMENT_ID")
        or os.environ.get("GA_MEASUREMENT_ID")
        or ""
    ).strip()
    if not GA_ID_RE.match(raw):
        return ""
    return raw


def analytics_html():
    parts = []
    token = (os.environ.get("CLOUDFLARE_WEB_ANALYTICS_TOKEN") or "").strip()
    if token:
        parts.append(
            '<script defer src="https://static.cloudflareinsights.com/beacon.min.js" '
            f'data-cf-beacon=\'{{"token":"{esc(token)}"}}\'></script>'
        )
    ga_id = ga_measurement_id()
    if ga_id:
        parts.append(f"<script>window.__GA_MEASUREMENT_ID={json.dumps(ga_id)}</script>")
        parts.append(
            "<script>window.dataLayer=window.dataLayer||[];"
            "function gtag(){dataLayer.push(arguments)}"
            "gtag('consent','default',{"
            "analytics_storage:'denied',"
            "ad_storage:'denied',"
            "ad_user_data:'denied',"
            "ad_personalization:'denied',"
            "wait_for_update:500"
            "})</script>"
        )
    return "\n".join(parts)


def consent_bar_html(L):
    ui = L["ui"]
    return f"""<aside class="consent-bar" data-consent-bar hidden role="region" aria-label="{esc(ui['cookie_aria'])}">
  <div class="consent-bar-inner">
    <p>{esc(ui['cookie_text'])}</p>
    <div class="consent-bar-actions">
      <button type="button" class="consent-accept" data-consent-accept>{esc(ui['cookie_accept'])}</button>
      <button type="button" class="consent-essential" data-consent-essential>{esc(ui['cookie_essential'])}</button>
    </div>
  </div>
</aside>"""


def lang_prefix(lang):
    return "" if lang == "cs" else f"{lang}/"


def url_for(lang, path):
    """Absolute URL for a page path ('' = home, 'kontakt/' etc.)."""
    return f"{BASE}/{lang_prefix(lang)}{path}"


# Google listing name confirmed by owner + Maps embed of that name.
MAP_QUERY = "Juzlova - Potravinářské směsi, Kochánov 40, 582 53"
MAP_ADDR = "Kochánov 40, 582 53"
GEO_LAT = 49.53367
GEO_LNG = 15.54002
MAP_SEARCH = (
    "https://www.google.com/maps/search/?api=1&query="
    + urllib.parse.quote("Juzlova - Potravinarske smesi, Kochánov 40, 582 53")
)
MAP_DIR = (
    "https://www.google.com/maps/dir/?api=1&destination="
    + urllib.parse.quote("Juzlova - Potravinarske smesi, Kochánov 40, 582 53")
)
# Seznam Mapy search for "Juzlova" (pro.mapy.cz/suggest) returns this firm:
# Jůzlová, Výroba potravin, Kochánov 40, source=firm id=12906730
MAPY_LISTING = "https://mapy.cz/?source=firm&id=12906730"
MAPY_NAV = (
    "https://mapy.cz/zakladni?planovani-trasy"
    "&source=firm&id=12906730"
    f"&x={GEO_LNG}&y={GEO_LAT}&z=17"
)
MAPS_SAME_AS = [
    MAP_SEARCH,
    MAPY_LISTING,
    "https://www.firmy.cz/detail/12906730-juzlova-kochanov.html",
]


def place_map_src(lang):
    query = urllib.parse.quote(MAP_QUERY)
    return (
        f"https://maps.google.com/maps?q={query}"
        f"&hl={lang}&z=16&output=embed"
    )


def place_map_html(L):
    ui = L["ui"]
    title = ui.get("map_title") or MAP_QUERY
    src = place_map_src(L["code"])
    addr = ui.get("map_addr") or MAP_ADDR
    google_nav = ui.get("map_nav_google") or "Google Maps"
    seznam_nav = ui.get("map_nav_seznam") or "Seznam Mapy"
    return f"""<div class="place-map" data-place-map>
<iframe title="{esc(title)}" src="{esc(src)}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
<p class="place-map-addr"><a href="{esc(MAP_SEARCH)}" rel="noopener noreferrer" target="_blank">{esc(addr)}</a></p>
<div class="place-map-nav">
<a class="btn gold" href="{esc(MAP_DIR)}" rel="noopener noreferrer" target="_blank">{esc(google_nav)}</a>
<a class="btn map-seznam" href="{esc(MAPY_NAV)}" rel="noopener noreferrer" target="_blank">{esc(seznam_nav)}</a>
</div>
</div>"""


def reviews_html(L, depth=0):
    """Google + Seznam star cards linked to live profiles."""
    ui = L["ui"]
    g = REVIEWS["google"]
    s = REVIEWS["seznam"]

    def card(key, data, brand):
        rating = data["rating"]
        count = data["count"]
        url = data["url"]
        rating_lbl = ui.get("reviews_rating_of", "{rating} / 5").format(rating=rating)
        count_lbl = ui.get("reviews_count", "{n} reviews").format(n=count)
        score = str(rating).replace(".", ",")
        return f"""<a class="reviews-card reviews-card--{key}" href="{esc(url)}" rel="noopener noreferrer" target="_blank" aria-label="{esc(brand)}: {esc(rating_lbl)}, {esc(count_lbl)}">
<span class="reviews-brand">{esc(brand)}</span>
{stars_html(float(rating), brand)}
<span class="reviews-score">{esc(score)}</span>
<span class="reviews-count">{esc(count_lbl)}</span>
<span class="reviews-cta">{esc(ui.get('reviews_open', 'Open reviews'))} →</span>
</a>"""

    return f"""<section class="reviews-board" aria-labelledby="reviews-h">
<p class="kicker">{esc(ui.get('reviews_kicker', 'Reviews'))}</p>
<h2 id="reviews-h">{esc(ui.get('reviews_h2', 'Customer ratings'))}</h2>
<p class="lead">{esc(ui.get('reviews_lead', ''))}</p>
<div class="reviews-grid">
{card('google', g, ui.get('reviews_google', 'Google'))}
{card('seznam', s, ui.get('reviews_seznam', 'Seznam'))}
</div>
<p class="reviews-note">{esc(ui.get('reviews_note', ''))}</p>
</section>"""


def team_html(L, depth=0):
    """About-page family member cards with placeholder photos."""
    ui = L["ui"]
    lg = L["code"]
    img_base = ("../" * depth) + "img/"
    cards = []
    for i, member in enumerate(TEAM):
        name = member["name"][lg]
        role = member["role"][lg]
        wiifm = member["wiifm"][lg]
        photo = img_base + member["photo"]
        cards.append(
            f"""<article class="team-card" style="--i:{i}" id="{esc(member['id'])}">
<div class="team-photo-wrap">
<img class="team-photo" src="{esc(photo)}" alt="" width="640" height="800" loading="lazy" decoding="async">
</div>
<div class="team-pad">
<h3 class="team-name">{esc(name)}</h3>
<p class="team-role">{esc(role)}</p>
<p class="team-wiifm">{esc(wiifm)}</p>
</div>
</article>"""
        )
    return f"""<section class="team-board" aria-labelledby="team-h">
<p class="kicker">{esc(ui.get('team_kicker', ''))}</p>
<h2 id="team-h">{esc(ui.get('team_h2', 'The family'))}</h2>
<p class="lead">{esc(ui.get('team_lead', ''))}</p>
<div class="team-grid">{"".join(cards)}</div>
<p class="team-note">{esc(ui.get('team_photo_note', ''))}</p>
</section>"""


def b2b_showcase_html(L, depth=0):
    """Visual blocks for the wholesale page only."""
    ui = L["ui"]
    pages = page_rel(L["code"], depth)
    items = [
        ("b2b_vis_1_h", "b2b_vis_1_p"),
        ("b2b_vis_2_h", "b2b_vis_2_p"),
        ("b2b_vis_3_h", "b2b_vis_3_p"),
        ("b2b_vis_4_h", "b2b_vis_4_p"),
    ]
    cards = "".join(
        f'<article class="b2b-tile" style="--i:{i}"><h3>{esc(ui.get(hk, ""))}</h3>'
        f'<p>{esc(ui.get(pk, ""))}</p></article>'
        for i, (hk, pk) in enumerate(items)
    )
    links = "".join(
        f'<a class="b2b-chip" href="{pages}{slug}/">{esc(AEO_PAGES[L["code"]][key]["h1"])}</a>'
        for key, slug in B2B_SLUGS.items()
    )
    return f"""<div class="b2b-showcase">
<div class="b2b-tiles">{cards}</div>
<p class="b2b-brno-callout">{esc(ui.get('b2b_brno_free', ''))}</p>
<div class="b2b-chip-row" aria-label="{esc(ui.get('b2b_hub', 'Wholesale by place'))}">{links}</div>
</div>"""


FLAG_CZ = (
    '<svg class="flag" viewBox="0 0 6 4" aria-hidden="true">'
    '<rect width="6" height="2" fill="#fff"/>'
    '<rect y="2" width="6" height="2" fill="#D7141A"/>'
    '<polygon points="0,0 3,2 0,4" fill="#11457E"/></svg>'
)
FLAG_IE = (
    '<svg class="flag" viewBox="0 0 3 2" aria-hidden="true">'
    '<rect width="1" height="2" fill="#169B62"/>'
    '<rect x="1" width="1" height="2" fill="#fff"/>'
    '<rect x="2" width="1" height="2" fill="#FF883E"/></svg>'
)
FLAG_DE = (
    '<svg class="flag" viewBox="0 0 5 3" aria-hidden="true">'
    '<rect width="5" height="1" fill="#000"/>'
    '<rect y="1" width="5" height="1" fill="#D00"/>'
    '<rect y="2" width="5" height="1" fill="#FFCE00"/></svg>'
)
FLAG_SK = (
    '<svg class="flag" viewBox="0 0 6 4" aria-hidden="true">'
    '<rect width="6" height="1.34" fill="#fff"/>'
    '<rect y="1.33" width="6" height="1.34" fill="#0B4EA2"/>'
    '<rect y="2.66" width="6" height="1.34" fill="#EE1C25"/></svg>'
)
ICON_GLOBE = (
    '<svg class="flag globe" viewBox="0 0 24 24" aria-hidden="true">'
    '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/>'
    '<ellipse cx="12" cy="12" rx="4" ry="9" fill="none" stroke="currentColor" stroke-width="1.8"/>'
    '<path d="M3 12h18" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>'
)


def contact_form_html(L, kind="contact"):
    ui = L["ui"]
    lang = L["code"]
    boxes = []
    for key in PRODUCT_SLUGS:
        name = L["products"][key]["name"]
        boxes.append(
            f'<label class="chk"><input type="checkbox" name="product" value="{esc(name)}">'
            f"<span>{esc(name)}</span></label>"
        )
    checks = "\n  ".join(boxes)
    is_b2b = kind == "b2b"
    extra = ""
    if is_b2b:
        topics = ui.get("form_topics") or {}
        opts = [f'<option value="">{esc(ui.get("form_topic_prompt") or "")}</option>']
        for key in TOPIC_KEYS:
            label = topics.get(key, key)
            opts.append(f'<option value="{esc(key)}">{esc(label)}</option>')
        extra = (
            f'<label>{esc(ui.get("form_topic") or "Topic")}'
            f'<select name="topic" required aria-required="true">{"".join(opts)}</select></label>'
            f'<label>{esc(ui["form_qty"])}'
            f'<input type="text" name="quantity" autocomplete="off" maxlength="200"></label>'
            f'<input type="hidden" name="buyer" value="restaurant">'
        )
    else:
        extra = '<input type="hidden" name="buyer" value="household">'
    heading = ui.get("form_b2b_h") if is_b2b else ui["form_h"]
    hint = ui.get("form_b2b_hint") if is_b2b else ui["form_hint"]
    heading_id = "b2b-write" if is_b2b else "write-to-us"
    return f"""<form class="order-form" data-contact-form data-form-type="{esc(kind)}" data-lang="{esc(lang)}" data-i18n-success="{esc(ui['form_success'])}" data-i18n-error="{esc(ui['form_error'])}" data-i18n-captcha="{esc(ui['form_captcha'])}" data-i18n-sending="{esc(ui['form_sending'])}" data-i18n-need-contact="{esc(ui['form_need_contact'])}" action="/api/contact" method="post">
<h2 id="{heading_id}">{esc(heading)}</h2>
<p class="form-hint">{esc(hint)}</p>
<label class="hp" aria-hidden="true">{esc(ui['form_honeypot'])}<input type="text" name="bot-field" tabindex="-1" autocomplete="off"></label>
<label>{esc(ui['form_name'])}<input type="text" name="name" required aria-required="true" autocomplete="name" maxlength="200"></label>
<label>{esc(ui['form_phone'])}<input type="tel" name="phone" autocomplete="tel" inputmode="tel" maxlength="40"></label>
<label>{esc(ui['form_email'])}<input type="email" name="email" autocomplete="email" inputmode="email" maxlength="200"></label>
{extra}
<fieldset>
<legend>{esc(ui['form_products'])}</legend>
  {checks}
</fieldset>
<fieldset class="fulfill">
<legend>{esc(ui['form_fulfill'])}</legend>
<label class="chk"><input type="radio" name="fulfillment" value="factory"><span>{esc(ui['form_fulfill_factory'])}</span></label>
<label class="chk"><input type="radio" name="fulfillment" value="humpolec"><span>{esc(ui['form_fulfill_humpolec'])}</span></label>
<label class="chk"><input type="radio" name="fulfillment" value="delivery"><span>{esc(ui['form_fulfill_delivery'])}</span></label>
</fieldset>
<label>{esc(ui['form_message'])}<textarea name="message" maxlength="4000" rows="5"></textarea></label>
<div class="turnstile-slot" data-turnstile-slot></div>
<p class="form-status" data-form-status role="status" aria-live="polite" hidden></p>
<button type="submit" class="btn gold">{esc(ui['form_submit'])}</button>
</form>"""


def newsletter_form_html(L):
    ui = L["ui"]
    lang = L["code"]
    return f"""<form class="order-form newsletter-form" data-contact-form data-form-type="newsletter" data-lang="{esc(lang)}" data-i18n-success="{esc(ui['nl_success'])}" data-i18n-error="{esc(ui['form_error'])}" data-i18n-captcha="{esc(ui['form_captcha'])}" data-i18n-sending="{esc(ui['form_sending'])}" data-i18n-need-contact="{esc(ui['nl_need_email'])}" action="/api/contact" method="post">
<h2 id="newsletter">{esc(ui['nl_h'])}</h2>
<p class="form-hint">{esc(ui['nl_lead'])}</p>
<label class="hp" aria-hidden="true">{esc(ui['form_honeypot'])}<input type="text" name="bot-field" tabindex="-1" autocomplete="off"></label>
<label>{esc(ui['form_name'])}<input type="text" name="name" autocomplete="name" maxlength="200"></label>
<label>{esc(ui['form_email'])}<input type="email" name="email" required aria-required="true" autocomplete="email" inputmode="email" maxlength="200"></label>
<label class="chk consent"><input type="checkbox" name="consent" value="yes" required aria-required="true"><span>{esc(ui['nl_consent'])}</span></label>
<div class="turnstile-slot" data-turnstile-slot></div>
<p class="form-status" data-form-status role="status" aria-live="polite" hidden></p>
<button type="submit" class="btn gold">{esc(ui['nl_submit'])}</button>
</form>"""


def rel(depth):
    return "../" * depth


def asset_rel(depth):
    """Prefix from this page to the site root (img, css, js)."""
    return rel(depth)


def page_rel(lang, depth):
    """Prefix from this page to the language home (nav, products, footer)."""
    extra = 0 if lang == "cs" else 1
    return rel(max(depth - extra, 0))


def lang_href(other, path, depth):
    """Relative language-switcher URL (works on file:// and preview hosts)."""
    root = asset_rel(depth)
    if other == "cs":
        return (root if root else "./") + path
    return root + other + "/" + path


def hreflangs(path):
    out = []
    for lg in LANGS:
        out.append(f'<link rel="alternate" hreflang="{lg}" href="{url_for(lg, path)}">')
    out.append(f'<link rel="alternate" hreflang="x-default" href="{url_for("cs", path)}">')
    return "\n".join(out)


def lang_switcher_html(L, path, depth):
    ui = L["ui"]
    lg = L["code"]
    tip = ui.get("de_tooltip") or ""
    more_label = ui.get("lang_more") or "More"
    other_note = ui.get("lang_other") or ""
    names = {
        "cs": ui.get("lang_cs") or "Čeština",
        "en": ui.get("lang_en") or "English",
        "de": ui.get("lang_de") or "Deutsch",
        "sk": ui.get("lang_sk") or "Slovenčina",
    }
    flags = {"cs": FLAG_CZ, "en": FLAG_IE, "de": FLAG_DE, "sk": FLAG_SK}

    def chip(other, extra_class=""):
        on = " on" if other == lg else ""
        href = lang_href(other, path, depth)
        if other == "de":
            return (
                f'<a class="lang-opt lang-de is-dim{on}{extra_class}" lang="de" hreflang="de" '
                f'href="{href}" aria-label="{esc(names["de"])}. {esc(tip)}" '
                f'title="{esc(tip)}" data-de-tip>'
                f'{FLAG_DE}<span class="lang-code">DE</span>'
                f'<span class="lang-de-bubble" role="tooltip">{esc(tip)}</span></a>'
            )
        return (
            f'<a class="lang-opt{on}{extra_class}" lang="{other}" hreflang="{other}" '
            f'href="{href}" aria-label="{esc(names[other])}">'
            f'{flags[other]}<span class="lang-code">{other.upper()}</span></a>'
        )

    primary = chip("cs") + chip("en") + chip("de")
    extra = (
        f'{chip("sk")}'
        f'<p class="lang-other">{esc(other_note)}</p>'
    )
    return f"""<div class="langs" data-langs>
  <div class="lang-primary" role="group" aria-label="{esc(ui['lang_label'])}">{primary}</div>
  <div class="lang-more">
    <button type="button" class="lang-more-btn" aria-expanded="false" aria-controls="lang-more-panel" data-lang-more>
      {ICON_GLOBE}<span class="lang-code">+</span><span class="visually-hidden">{esc(more_label)}</span>
    </button>
    <div class="lang-more-panel" id="lang-more-panel" hidden data-lang-panel>
      <p class="lang-more-label">{esc(more_label)}</p>
      {extra}
    </div>
  </div>
</div>"""


def nav(L, depth, active, path):
    """Return (header_inner_html, backdrop_html).

    Header keeps logo + toggle + nav. Backdrop is a body sibling.
    Mobile drawer uses position:fixed against the viewport (header must not
    use backdrop-filter/filter/transform, or fixed children get trapped).
    """
    assets = asset_rel(depth)
    pages = page_rel(L["code"], depth)
    ui = L["ui"]
    home = pages if pages else "./"

    def a(slug, label, key):
        cls = ' class="active"' if active == key else ""
        href = home if slug == "" else f"{pages}{slug}"
        return f'<a href="{href}"{cls}>{esc(label)}</a>'
    prods = "".join(
        f'<a href="{pages}{PRODUCT_SLUGS[k]}/">{esc(L["products"][k]["name"])}</a>'
        for k in PRODUCT_SLUGS)
    langsel = lang_switcher_html(L, path, depth)
    header_inner = f"""<div class="bar">
  <a class="brand" href="{home}" aria-label="Jůzlová.cz">
    <img class="wordmark on-light" src="{assets}img/logo-wordmark-black.png" alt="Jůzlová" width="650" height="200">
    <img class="wordmark on-dark" src="{assets}img/logo-wordmark-white.png" alt="" aria-hidden="true" width="650" height="200">
  </a>
  <button type="button" class="menu-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="{esc(ui['menu_open'])}" data-open-label="{esc(ui['menu_open'])}" data-close-label="{esc(ui['menu_close'])}">
    <span class="menu-toggle-bars" aria-hidden="true"></span>
  </button>
</div>
<nav class="main" id="site-nav" aria-label="{esc(ui['nav_aria'])}">
  {a('', ui['nav_home'], 'home')}
  {a('kdo_jsme/', ui['nav_about'], 'kdo_jsme')}
  {a('kde-nas-najdete/', ui['nav_delivery'], 'kde_nas_najdete')}
  {a('velkoobchod/', ui['nav_b2b'], 'velkoobchod')}
  <span class="navgroup">
    <button type="button" class="nav-products" aria-expanded="false" aria-controls="nav-products-list">{esc(ui['nav_products'])} ▾</button>
    <span class="drop" id="nav-products-list">{prods}</span>
  </span>
  {a('ceny/', ui['nav_prices'], 'ceny')}
  {a('recepty/', ui['nav_recipes'], 'recepty')}
  {a('faq/', ui['nav_faq'], 'faq')}
  {a('kontakt/', ui['nav_contact'], 'kontakt')}
  {langsel}
</nav>"""
    backdrop = '<div class="nav-backdrop" hidden></div>'
    return header_inner, backdrop


def footer(L, depth):
    assets = asset_rel(depth)
    pages = page_rel(L["code"], depth)
    ui = L["ui"]
    prods = "".join(
        f'<a href="{pages}{PRODUCT_SLUGS[k]}/">{esc(L["products"][k]["name"])}</a>'
        for k in PRODUCT_SLUGS)
    recs = "".join(
        f'<a href="{pages}{slug}/">{esc(L["recipes"].get(slug, {}).get("name", slug))}</a>'
        for slug in RECIPE_SLUGS)
    return f"""<footer class="site">
  <img class="footmark" src="{assets}img/mark-white.png" alt="" aria-hidden="true" width="640" height="640">
  <div class="wrap">
    <div class="cols">
      <div>
        <img class="footlogo" src="{assets}img/logo-wordmark-white.png" alt="Jůzlová" width="650" height="200">
        <p style="font-size:.92rem;margin:.2rem 0 1rem">{esc(ui['footer_note'])}</p>
        <p style="font-size:.88rem">{esc(ui['footer_addr'])}<br>+420 728 466 141 · +420 607 629 931<br><a href="mailto:juzlj@seznam.cz" style="display:inline">juzlj@seznam.cz</a></p>
      </div>
      <div><h4>{esc(ui['footer_products'])}</h4>{prods}</div>
      <div><h4>{esc(ui['footer_recipes'])}</h4>{recs}</div>
      <div><h4>{esc(ui['footer_company'])}</h4>
        <a href="{pages}kdo_jsme/">{esc(ui['nav_about'])}</a>
        <a href="{pages}kde-nas-najdete/">{esc(ui['nav_delivery'])}</a>
        <a href="{pages}velkoobchod/">{esc(ui['nav_b2b'])}</a>
        <a href="{pages}do-eu/">{esc(ui['nav_d2c'])}</a>
        <a href="{pages}ceny/">{esc(ui['nav_prices'])}</a>
        <a href="{pages}faq/">{esc(ui['nav_faq'])}</a>
        <a href="{pages}kontakt/">{esc(ui['nav_contact'])}</a>
        <h4>{esc(ui.get('geo_hub') or '')}</h4>
        <a href="{pages}objednavka-cesko/">{esc(AEO_PAGES[L['code']]['objednavka_cesko']['h1'])}</a>
        <a href="{pages}vysocina/">{esc(AEO_PAGES[L['code']]['vysocina']['h1'])}</a>
        <a href="{pages}havlickuv-brod/">{esc(AEO_PAGES[L['code']]['havlickuv_brod']['h1'])}</a>
        <a href="{pages}humpolec/">{esc(AEO_PAGES[L['code']]['humpolec']['h1'])}</a>
        <a href="{pages}kochanov/">{esc(AEO_PAGES[L['code']]['kochanov']['h1'])}</a>
        <a href="{pages}navstevnikum/">{esc(AEO_PAGES[L['code']]['navstevnikum']['h1'])}</a>
        <h4>{esc(ui.get('b2b_hub') or '')}</h4>
        <a href="{pages}velkoobchod-vysocina/">{esc(AEO_PAGES[L['code']]['velkoobchod_vysocina']['h1'])}</a>
        <a href="{pages}velkoobchod-kochanov/">{esc(AEO_PAGES[L['code']]['velkoobchod_kochanov']['h1'])}</a>
        <a href="{pages}velkoobchod-praha/">{esc(AEO_PAGES[L['code']]['velkoobchod_praha']['h1'])}</a>
        <a href="{pages}velkoobchod-brno/">{esc(AEO_PAGES[L['code']]['velkoobchod_brno']['h1'])}</a>
        <a href="{pages}velkoobchod-zahranici/">{esc(AEO_PAGES[L['code']]['velkoobchod_zahranici']['h1'])}</a>
      </div>
    </div>
    <div class="fine"><span>© 2004–2026 Jůzlová s.r.o. · IČO 45900124 · <a href="{assets}llms.txt">llms.txt</a> · <a href="{assets}llms-full.txt">llms-full.txt</a></span><span>{esc(ui['open_hours'])}</span></div>
  </div>
</footer>"""


def org_jsonld():
    return {
        "@context": "https://schema.org",
        "@type": ["Organization", "LocalBusiness", "FoodManufacturer"],
        "@id": BASE + "/#org",
        "name": "Juzlova - Potravinářské směsi",
        "legalName": "Jůzlová s.r.o.",
        "alternateName": [
            "Jůzlová",
            "Juzlova",
            "Juzlova - Potravinarske smesi",
            "Jůzlová.cz",
            "Juzlova.cz",
        ],
        "url": BASE + "/",
        "logo": {
            "@type": "ImageObject",
            "url": BASE + "/img/logo-wordmark-black.png",
            "width": 650, "height": 200,
        },
        "image": BASE + "/img/dilna-panorama.webp",
        "foundingDate": "2004",
        "email": "juzlj@seznam.cz",
        "telephone": ["+420728466141", "+420607629931"],
        "vatID": "CZ45900124",
        "taxID": "45900124",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Kochánov 40",
            "addressLocality": "Kochánov",
            "postalCode": "582 53",
            "addressRegion": "Vysočina",
            "addressCountry": "CZ",
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": GEO_LAT,
            "longitude": GEO_LNG,
        },
        "hasMap": MAP_SEARCH,
        "sameAs": MAPS_SAME_AS,
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": REVIEWS["google"]["rating"],
            "reviewCount": REVIEWS["google"]["count"],
            "bestRating": 5,
            "worstRating": 1,
        },
        "areaServed": [
            {"@type": "Place", "name": "Kochánov"},
            {"@type": "City", "name": "Havlíčkův Brod"},
            {"@type": "AdministrativeArea", "name": "Vysočina"},
        ],
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": [
                "Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday",
            ],
            "opens": "08:00", "closes": "19:00",
        },
        "priceRange": "$$",
        "currenciesAccepted": "CZK",
        "paymentAccepted": "Cash, Bank transfer",
        "knowsLanguage": ["cs", "en", "de", "sk"],
        "identifier": {
            "@type": "PropertyValue",
            "name": "IČO",
            "value": "45900124",
        },
        "founder": [
            {"@type": "Person", "@id": BASE + "/#jirina", "name": "Jiřina Jůzlová"},
            {"@type": "Person", "@id": BASE + "/#jiri", "name": "Jiří Jůzl"},
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "contactType": "sales",
                "telephone": "+420728466141",
                "email": "juzlj@seznam.cz",
                "availableLanguage": ["cs", "en", "de", "sk"],
                "areaServed": "CZ",
                "hoursAvailable": {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": [
                        "Monday", "Tuesday", "Wednesday", "Thursday",
                        "Friday", "Saturday", "Sunday",
                    ],
                    "opens": "08:00", "closes": "19:00",
                },
            },
        ],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Jůzlová food mixes",
            "numberOfItems": 5,
            "itemListElement": [
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Product",
                        "@id": BASE + f"/#product-{key}",
                        "name": name,
                    },
                    "priceCurrency": "CZK",
                    "price": price.split()[0] if price.split() else price,
                    "url": url_for("cs", PRODUCT_SLUGS[key] + "/"),
                }
                for key, name, price in (
                    ("bramborove_knedliky", "Bramborové knedlíky v prášku", "250"),
                    ("chlupate_knedliky", "Chlupaté knedlíky (bosáky)", "260"),
                    ("vanilkovy_pudink", "Vanilkový puding bez lepku", "60"),
                    ("kakao_holandskeho_typu", "Kakao holandského typu", "270"),
                    ("vanilkovy_cukr", "Vanilínový cukr", "60"),
                )
            ],
        },
        "description": (
            "Rodinná dílna potravinářských směsí od roku 2004 v Kochánově na Vysočině: "
            "bramborové knedlíky v prášku, chlupaté knedlíky (bosáky), vanilkový puding "
            "bez lepku, vanilínový cukr a kakao holandského typu (20–22 % tuku). "
            "Objednávky telefonem, e-mailem nebo formulářem. Vyzvednutí v Kochánově a Humpolci."
        ),
    }


def website_jsonld():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": BASE + "/#website",
        "url": BASE + "/",
        "name": "Jůzlová.cz",
        "inLanguage": LANGS,
        "publisher": {"@id": BASE + "/#org"},
        "isFamilyFriendly": True,
        "copyrightYear": 2004,
        "copyrightHolder": {"@id": BASE + "/#org"},
    }


def webpage_jsonld(L, path, title, desc):
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "@id": url_for(L["code"], path) + "#webpage",
        "url": url_for(L["code"], path),
        "name": title,
        "description": desc,
        "inLanguage": L["code"],
        "dateModified": TODAY,
        "isPartOf": {"@id": BASE + "/#website"},
        "about": {"@id": BASE + "/#org"},
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": ["h1", "article.page .sub", ".faq"],
        },
    }


def aggregate_rating_ld(slug):
    r = rating_payload(slug)
    return {
        "@type": "AggregateRating",
        "ratingValue": r["ratingValue"],
        "ratingCount": r["ratingCount"],
        "bestRating": r["bestRating"],
        "worstRating": r["worstRating"],
    }


def rating_widget_html(L, slug):
    ui = L["ui"]
    r = rating_payload(slug)
    value = r["ratingValue"]
    count = r["ratingCount"]
    stars = []
    for n in range(1, 6):
        filled = " is-on" if n <= round(value) else ""
        label = ui["rate_star"].replace("{n}", str(n))
        stars.append(
            f'<button type="button" class="star{filled}" data-stars="{n}" '
            f'aria-label="{esc(label)}" style="min-width:48px;min-height:48px">'
            f'<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true">'
            f'<path d="M12 2.6l2.7 6.1 6.6.7-5 4.6 1.4 6.5L12 17.8 6.3 20.5 7.7 14 2.7 9.4l6.6-.7z"/>'
            f"</svg></button>"
        )
    count_txt = ui["rate_count"].replace("{n}", str(count)) if count else ""
    meta = (
        f'<p class="recipe-rating-meta"><strong data-rating-out>{value}</strong> / 5 · '
        f'<span data-count-out>{esc(count_txt)}</span></p>'
        if count else
        '<p class="recipe-rating-meta" hidden><strong data-rating-out></strong> / 5 · '
        '<span data-count-out></span></p>'
    )
    return f"""<div class="recipe-rating" data-rating-slug="{esc(slug)}" data-rating-value="{value}" data-rating-count="{count}" data-api="/api/ratings" data-count-tpl="{esc(ui['rate_count'])}" data-thanks="{esc(ui['rate_thanks'])}" data-already="{esc(ui['rate_already'])}" data-error="{esc(ui['rate_error'])}">
<p class="recipe-rating-label" id="rate-{esc(slug)}">{esc(ui['rate_label'])}</p>
<div class="recipe-rating-stars" role="radiogroup" aria-labelledby="rate-{esc(slug)}">{''.join(stars)}</div>
{meta}
<p class="recipe-rating-status" hidden></p>
</div>"""


def people_jsonld():
    return [
        {
            "@context": "https://schema.org",
            "@type": "Person",
            "@id": BASE + "/#jirina",
            "name": "Jiřina Jůzlová",
            "jobTitle": "Co-owner",
            "telephone": "+420728466141",
            "worksFor": {"@id": BASE + "/#org"},
        },
        {
            "@context": "https://schema.org",
            "@type": "Person",
            "@id": BASE + "/#jiri",
            "name": "Jiří Jůzl",
            "jobTitle": "Co-owner",
            "telephone": "+420607629931",
            "worksFor": {"@id": BASE + "/#org"},
        },
    ]


def shell(L, *, title, desc, path, depth, active, body, jsonld=None, og_img=None, body_class="", keywords="", meta_kind="home", meta_key="", extra_head=""):
    lg = L["code"]
    title, desc = compose_meta(lg, meta_kind, meta_key, title, desc)
    canonical = url_for(lg, path)
    blocks = [org_jsonld(), website_jsonld(), webpage_jsonld(L, path, title, desc)]
    blocks += (jsonld or [])
    ld = "\n".join(
        f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>'
        for b in blocks)
    ogimg = og_img or f"{BASE}/img/hero.webp"
    p = asset_rel(depth)
    body_cls = f' class="{body_class}"' if body_class else ""
    kw = f'<meta name="keywords" content="{esc(keywords)}">\n' if keywords else ""
    og_alts = "\n".join(
        f'<meta property="og:locale:alternate" content="{loc}">'
        for code, loc in (("cs", "cs_CZ"), ("en", "en_US"), ("de", "de_DE"), ("sk", "sk_SK"))
        if code != lg
    )
    header_inner, nav_backdrop = nav(L, depth, active, path)
    return f"""<!doctype html>
<html lang="{lg}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{kw}<link rel="canonical" href="{canonical}">
{hreflangs(path)}
<link rel="describedby" type="text/plain" title="llms.txt" href="{BASE}/llms.txt">
<link rel="alternate" type="text/plain" title="llms-full.txt" href="{BASE}/llms-full.txt">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Jůzlová.cz">
<meta property="og:locale" content="{L['locale']}">
{og_alts}
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ogimg}">
<meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
{extra_head}<link rel="stylesheet" href="{p}assets/site.css?v={ASSET_VER}">
<link rel="icon" href="{p}img/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{p}img/icon-32.png">
<link rel="icon" type="image/png" sizes="32x32" media="(prefers-color-scheme: dark)" href="{p}img/icon-white-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="{p}img/icon-192.png">
<link rel="apple-touch-icon" href="{p}img/apple-touch-icon.png">
<link rel="manifest" href="{p}site.webmanifest">
<meta name="theme-color" content="#021536">
{ld}
{analytics_html()}
</head>
<body{body_cls}>
<header class="site">
  <div class="wrap">{header_inner}</div>
</header>
{nav_backdrop}
{body}
{footer(L, depth)}
{consent_bar_html(L)}
<script src="{p}assets/site.js?v={ASSET_VER}" defer></script>
</body>
</html>
"""


def price_note_html(L):
    note = L["ui"].get("price_excludes_shipping") or ""
    if not note:
        return ""
    return f'<p class="price-note">{esc(note)}</p>'


def aeo_slug(key):
    if key in GEO_SLUGS:
        return GEO_SLUGS[key]
    return B2B_SLUGS[key]


def aeo_links_html(L, kind, depth):
    pages = page_rel(L["code"], depth)
    pack = AEO_PAGES.get(L["code"]) or AEO_PAGES["cs"]
    ui = L["ui"]
    if kind == "b2b":
        slugs = B2B_SLUGS
        heading = ui.get("b2b_hub") or ""
        extra = [("velkoobchod/", ui.get("nav_b2b") or "")]
    else:
        slugs = GEO_SLUGS
        heading = ui.get("geo_hub") or ""
        extra = [
            ("kde-nas-najdete/", ui.get("nav_delivery") or ""),
            ("do-eu/", ui.get("nav_d2c") or ""),
        ]
    items = []
    for key, slug in slugs.items():
        pg = pack.get(key) or {}
        label = pg.get("h1") or slug
        items.append(f'<li><a href="{pages}{slug}/">{esc(label)}</a></li>')
    for href, label in extra:
        if label:
            items.append(f'<li><a href="{pages}{href}">{esc(label)}</a></li>')
    return (
        f'<nav class="aeo-links" aria-label="{esc(heading)}">'
        f"<h2>{esc(heading)}</h2><ul>{''.join(items)}</ul></nav>"
    )


def render_body(L, body_spec, depth, product=None):
    pages = page_rel(L["code"], depth)
    show = (product or {}).get("showcase") or {}
    out = []
    for kind, val in body_spec:
        if kind == "p":
            out.append(f"<p>{esc(val)}</p>")
        elif kind in ("h2", "h3"):
            out.append(f"<{kind}>{esc(val)}</{kind}>")
        elif kind == "ul":
            out.append("<ul>" + "".join(f"<li>{esc(x)}</li>" for x in val) + "</ul>")
        elif kind == "ol":
            out.append("<ol>" + "".join(f"<li>{esc(x)}</li>" for x in val) + "</ol>")
        elif kind == "contacts":
            out.append("""<div class="factbox"><dl>
<dt>Jiřina Jůzlová</dt><dd>Kochánov 40, 582 53 · <a href="tel:+420728466141">+420 728 466 141</a> · <a href="mailto:juzlj@seznam.cz">juzlj@seznam.cz</a></dd>
<dt>Jiří Jůzl</dt><dd>Kochánov 40, 582 53 · <a href="tel:+420607629931">+420 607 629 931</a> · <a href="mailto:juzlj@seznam.cz">juzlj@seznam.cz</a></dd>
</dl></div>""")
        elif kind == "pricetable":
            out.append(price_board_html(L, depth))
            note = price_note_html(L)
            if note:
                out.append(note)
        elif kind == "links":
            out.append(aeo_links_html(L, val or "geo", depth))
        elif kind == "price_note":
            note = price_note_html(L)
            if note:
                out.append(note)
        elif kind == "form":
            out.append(contact_form_html(L))
        elif kind == "form_b2b":
            out.append(contact_form_html(L, "b2b"))
        elif kind == "newsletter":
            out.append(newsletter_form_html(L))
        elif kind == "map":
            out.append(place_map_html(L))
        elif kind == "cocoa_sensory":
            out.append(cocoa_sensory_html(show))
        elif kind == "cocoa_apps":
            out.append(cocoa_apps_html(show))
        elif kind == "cocoa_nutrition":
            out.append(cocoa_nutrition_html(show))
        elif kind == "cocoa_facts":
            out.append(cocoa_facts_html(show))
        elif kind == "reviews":
            out.append(reviews_html(L, depth))
        elif kind == "team":
            out.append(team_html(L, depth))
        elif kind == "b2b_showcase":
            out.append(b2b_showcase_html(L, depth))
        else:
            unknown: str = kind
            raise ValueError(f"unknown body block: {unknown}")
    return "\n".join(out)


def faq_html(faq, heading=""):
    if not faq:
        return ""
    items = "".join(
        f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faq)
    head = f"<h2>{esc(heading)}</h2>" if heading else ""
    return f'<section class="faq" aria-label="{esc(heading) if heading else "FAQ"}">{head}{items}</section>'


def faq_jsonld(faq):
    return {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}}
                       for q, a in faq],
    }


def breadcrumb_jsonld(L, crumbs):
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u}
            for i, (n, u) in enumerate(crumbs)],
    }


def write(path_parts, content):
    f = ROOT.joinpath(*path_parts)
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(content)


def img_or_none(depth, name):
    if name and (ROOT / "img" / name).exists():
        return asset_rel(depth) + "img/" + name
    return None


def product_img_src(depth, key):
    return img_or_none(depth, PRODUCT_IMG.get(key))


# Compact convert-first hero uses one still. Film frames stay on disk unused.
HERO_STILLS = ["kochanov-letecky.webp", "hero.webp"]


def build_home(L):
    lg = L["code"]
    depth = 0 if lg == "cs" else 1
    ui = L["ui"]
    pages = page_rel(lg, depth)
    prod_cards = ""
    for k in PRODUCT_SLUGS:
        pr = L["products"][k]
        im = product_img_src(depth, k)
        imtag = f'<img class="thumb" src="{im}" alt="{esc(pr["name"])}" loading="lazy">' if im else ""
        prod_cards += f"""<li class="card rv">{imtag}<div class="pad">
<h3><a href="{pages}{PRODUCT_SLUGS[k]}/">{esc(pr['name'])}</a></h3>
<p>{esc(pr['short'])}</p><p class="price">{esc(pr['price'])}</p></div></li>"""
    rec_slides = ""
    for slug in HOME_RECIPE_SLUGS:
        r = L["recipes"].get(slug)
        if not r:
            continue
        im = img_or_none(depth, RECIPE_IMG.get(slug))
        imtag = (
            f'<img class="thumb" src="{im}" alt="{esc(r["name"])}" width="1200" height="800" loading="lazy">'
            if im else ""
        )
        rec_slides += f"""<li class="recipes-carousel-slide" aria-label="{esc(r['name'])}">
<a class="card recipes-carousel-card" href="{pages}{slug}/">{imtag}<div class="pad">
<h3>{esc(r['name'])}</h3><p>{esc(r.get('teaser',''))}</p></div></a>
</li>"""
    rec_carousel = f"""<div class="recipes-carousel" data-recipes-carousel tabindex="0" role="region" aria-roledescription="carousel" aria-label="{esc(ui['carousel_label'])}" data-status="{esc(ui['carousel_status'])}" data-goto="{esc(ui['carousel_goto'])}">
  <div class="recipes-carousel-scroller" data-carousel-scroller>
    <ul class="recipes-carousel-track">{rec_slides}</ul>
  </div>
  <div class="recipes-carousel-bar">
    <button type="button" class="recipes-carousel-btn" data-carousel-prev aria-label="{esc(ui['carousel_prev'])}">‹</button>
    <div class="recipes-carousel-dots" data-carousel-dots></div>
    <button type="button" class="recipes-carousel-btn" data-carousel-next aria-label="{esc(ui['carousel_next'])}">›</button>
  </div>
  <p class="visually-hidden" data-carousel-live aria-live="polite"></p>
</div>"""
    ticker_items = "".join(
        f"<span>{esc(L['products'][k]['name'])} · <b>{esc(L['products'][k]['price'])}</b></span>"
        for k in PRODUCT_SLUGS)
    ticker_items += f"<span><b>{esc(ui['ticker_pickup'])}</b></span>"
    still_name = None
    still = None
    for name in HERO_STILLS:
        still = img_or_none(depth, name)
        if still:
            still_name = name
            break
    hero_preload = ""
    if still and still_name:
        phone = img_or_none(depth, "kochanov-letecky-960.webp")
        srcset = f'{phone} 960w, {still} 2200w' if phone else still
        sizes = "(max-width: 700px) 960px, 2200px"
        media = (
            f'<div class="media"><img src="{still}" srcset="{srcset}" sizes="{sizes}" '
            f'alt="{esc(ui["hero_img_alt"])}" width="2200" height="1244" '
            f'fetchpriority="high" decoding="async"></div>'
        )
        hero_preload = (
            f'<link rel="preload" as="image" href="{still}" '
            f'imagesrcset="{srcset}" imagesizes="{sizes}">\n'
        )
    else:
        media = '<div class="media"><div class="hero-fallback"></div></div>'
    hero_html = f"""<section class="hero convert">
  {media}
  <div class="inner">
    <div class="est">{esc(ui['est'])}</div>
    <h1>{esc(ui['hero_h1'])}</h1>
    <p class="lead">{esc(ui['hero_lead'])}</p>
    <p class="hero-actions">
      <a class="btn gold" href="#produkty">{esc(ui['hero_cta2'])}</a>
      <a class="btn ghost" href="{pages}kontakt/">{esc(ui['hero_cta'])}</a>
    </p>
  </div>
</section>
<div class="marquee" aria-hidden="true"><div class="track">{ticker_items}{ticker_items}</div></div>"""
    wshop = img_or_none(depth, "workshop.webp") or img_or_none(depth, "workshop.jpg")
    why_inner = f"""
  <p class="kicker" style="color:var(--gold)">{esc(ui['sec_why_kicker'])}</p>
  <h2 class="sec">{esc(ui['sec_why'])}</h2>
  <div class="grid c3">
    <div class="rv"><h3>{esc(ui['why_1_h'])}</h3><p>{esc(ui['why_1_p'])}</p></div>
    <div class="rv"><h3>{esc(ui['why_2_h'])}</h3><p>{esc(ui['why_2_p'])}</p></div>
    <div class="rv"><h3>{esc(ui['why_3_h'])}</h3><p>{esc(ui['why_3_p'])}</p></div>
  </div>"""
    if wshop:
        why_band = f"""<section class="plx" data-plx>
  <div class="plx-img"><img src="{wshop}" alt="" width="2752" height="1536" loading="lazy" decoding="async"></div>
  <div class="inner"><div class="wrap">{why_inner}</div></div>
</section>"""
    else:
        why_band = f'<section class="band cream"><div class="wrap">{why_inner}</div></section>'
    body = f"""<main id="main">
{hero_html}
<section class="band" id="produkty"><div class="wrap">
  <p class="kicker">{esc(ui['sec_products_kicker'])}</p>
  <h2 class="sec">{esc(ui['sec_products'])}</h2>
  <p class="lead">{esc(ui['sec_products_lead'])}</p>
  <ul class="grid products" style="list-style:none;padding:0">{prod_cards}</ul>
  <p><a href="{pages}ceny/">{esc(ui['full_price_list'])} →</a></p>
</div></section>
{why_band}
<section class="band"><div class="wrap">
  <p class="kicker">{esc(ui['sec_recipes_kicker'])}</p>
  <h2 class="sec">{esc(ui['sec_recipes'])}</h2>
  <p class="lead">{esc(ui['sec_recipes_lead'])}</p>
  {rec_carousel}
  <p><a href="{pages}recepty/">{esc(ui['all_recipes'])} →</a></p>
</div></section>
<section class="band cream" id="recenze"><div class="wrap">
  {reviews_html(L, depth)}
</div></section>
<section class="band" id="faq"><div class="wrap">
  <p class="kicker">{esc(ui['sec_faq_kicker'])}</p>
  <h2 class="sec">{esc(ui['sec_faq'])}</h2>
  <p class="lead">{esc(ui['sec_faq_lead'])}</p>
  {faq_html(home_faq(lg))}
  <p style="margin-top:1.4rem"><a href="{pages}faq/">{esc(ui['all_faq'])} →</a></p>
</div></section>
<section class="band cream" id="velkoobchod-teaser"><div class="wrap">
  <p class="kicker">{esc(ui['sec_b2b_kicker'])}</p>
  <h2 class="sec">{esc(ui['sec_b2b'])}</h2>
  <p class="lead">{esc(ui['sec_b2b_lead'])}</p>
  <p><a class="btn gold" href="{pages}velkoobchod/">{esc(ui['sec_b2b_btn'])}</a></p>
</div></section>
<section class="band" id="do-eu"><div class="wrap">
  <p class="kicker">{esc(ui['sec_d2c_kicker'])}</p>
  <h2 class="sec">{esc(ui['sec_d2c'])}</h2>
  <p class="lead">{esc(ui['sec_d2c_lead'])}</p>
  <p><a class="btn ghost" href="{pages}do-eu/">{esc(ui['sec_d2c_btn'])}</a></p>
</div></section>
<section class="band cream" id="novinky"><div class="wrap">
  <p class="kicker">{esc(ui['nl_kicker'])}</p>
  {newsletter_form_html(L)}
</div></section>
<section class="band cream center"><div class="wrap">
  <h2 class="sec" style="display:inline-block">{esc(ui['cta_sample_h'])}</h2>
  <p class="lead" style="max-width:560px;margin:.6rem auto 1.4rem">{esc(ui['cta_sample_p'])}</p>
  <a class="btn gold" href="{pages}kontakt/">{esc(ui['cta_sample_btn'])}</a>
</div></section>
</main>"""
    html_out = shell(L, title=L["meta"]["home_title"], desc=L["meta"]["home_desc"],
                     path="", depth=depth, active="home", body=body,
                     keywords=keywords_for(lg, "home"), meta_kind="home",
                     extra_head=hero_preload,
                     jsonld=[
                         {
                             "@context": "https://schema.org",
                             "@type": "ItemList",
                             "name": ui["sec_products"],
                             "itemListOrder": "https://schema.org/ItemListOrderAscending",
                             "numberOfItems": 5,
                             "itemListElement": [
                                 {
                                     "@type": "ListItem",
                                     "position": i + 1,
                                     "url": url_for(lg, PRODUCT_SLUGS[key] + "/"),
                                     "name": L["products"][key]["name"],
                                 }
                                 for i, key in enumerate(PRODUCT_SLUGS)
                             ],
                         },
                         faq_jsonld(home_faq(lg)),
                     ])
    write(([lg] if lg != "cs" else []) + ["index.html"], html_out)


def build_page(L, key):
    lg = L["code"]
    slug = PAGE_SLUGS[key]
    depth = (0 if lg == "cs" else 1) + 1
    pg = L["pages"][key]
    path = f"{slug}/"
    crumbs = [(L["ui"]["breadcrumb_home"], url_for(lg, "")), (pg["h1"], url_for(lg, path))]
    fig = ""
    if key == "kdo_jsme":
        # Their own production room — sacks, scale and bag sealer — recovered
        # from the archive, in preference to a generic workshop picture.
        w = (img_or_none(depth, "dilna-panorama.webp")
             or img_or_none(depth, "workshop.webp") or img_or_none(depth, "workshop.jpg"))
        if w:
            cap = esc(L["ui"].get("workshop_caption", ""))
            fig = (f'<figure><img src="{w}" alt="{esc(pg["h1"])} — Kochánov" loading="lazy">'
                   + (f"<figcaption>{cap}</figcaption>" if cap else "") + "</figure>")
    pages = page_rel(lg, depth)
    home = pages if pages else "./"
    faqs = page_faq(lg, key)
    if key == "velkoobchod":
        faqs = b2b_faq(lg)
    price_bit = ""
    if key in ("kde_nas_najdete", "do_eu"):
        price_bit = price_note_html(L)
    page_cls = "page page--prices" if key == "ceny" else "page"
    body = f"""<main id="main" class="wrap"><article class="{page_cls}">
<nav class="breadcrumb"><a href="{home}">{esc(L['ui']['breadcrumb_home'])}</a> › {esc(pg['h1'])}</nav>
<h1>{esc(pg['h1'])}</h1>
<p class="sub">{esc(pg['sub'])}</p>
{fig}
{render_body(L, pg['body'], depth)}
{price_bit}
{faq_html(faqs, L['ui'].get('sec_faq', 'FAQ'))}
</article></main>"""
    extra_ld = [breadcrumb_jsonld(L, crumbs)]
    if faqs:
        extra_ld.append(faq_jsonld(faqs))
    if key == "kontakt":
        extra_ld.extend(people_jsonld())
    html_out = shell(L, title=pg["title"], desc=pg["desc"], path=path, depth=depth,
                     active=key, body=body, jsonld=extra_ld,
                     keywords=keywords_for(lg, key), meta_kind=key)
    write(([lg] if lg != "cs" else []) + [slug, "index.html"], html_out)


def build_product(L, key):
    lg = L["code"]
    slug = PRODUCT_SLUGS[key]
    depth = (0 if lg == "cs" else 1) + 1
    pr = L["products"][key]
    path = f"{slug}/"
    pages = page_rel(lg, depth)
    home = pages if pages else "./"
    im = product_img_src(depth, key)
    figure = (f'<figure><img src="{im}" alt="{esc(pr["name"])} — Jůzlová"></figure>' if im else "")
    price_num = re.search(r"(\d+)\s*(?:Kč|CZK)", pr["price"])
    img_name = PRODUCT_IMG.get(key)
    product_ld = {
        "@context": "https://schema.org", "@type": "Product",
        "@id": BASE + f"/#product-{key}",
        "name": pr["name"], "description": pr["desc"],
        "brand": {"@type": "Brand", "name": "Jůzlová", "@id": BASE + "/#org"},
        "manufacturer": {"@id": BASE + "/#org"},
        "category": "Food mix",
        "inLanguage": lg,
        "url": url_for(lg, path),
        "sku": key,
        **({"image": {
            "@type": "ImageObject",
            "url": f"{BASE}/img/{img_name}",
            "contentUrl": f"{BASE}/img/{img_name}",
            "caption": pr["name"],
        }} if img_name else {}),
        "offers": {
            "@type": "Offer",
            "priceCurrency": "CZK",
            "price": price_num.group(1) if price_num else "0",
            "availability": "https://schema.org/InStock",
            "url": url_for(lg, path),
            "seller": {"@id": BASE + "/#org"},
            "itemCondition": "https://schema.org/NewCondition",
        },
        "keywords": keywords_for(lg, "product", key),
    }
    faqs = merge_product_faq(lg, key, list(pr.get("faq") or []))
    lds = [product_ld, breadcrumb_jsonld(L, [
        (L["ui"]["breadcrumb_home"], url_for(lg, "")),
        (pr["name"], url_for(lg, path))])]
    if faqs:
        lds.append(faq_jsonld(faqs))
    body = f"""<main id="main" class="wrap"><article class="page">
<nav class="breadcrumb"><a href="{home}">{esc(L['ui']['breadcrumb_home'])}</a> › {esc(pr['name'])}</nav>
<h1>{esc(pr['name'])}</h1>
<p class="sub">{esc(pr['short'])}</p>
<div class="factbox"><dl><dt>{esc(L['ui']['price_label'])}</dt><dd><strong>{esc(pr['price'])}</strong></dd>
<dt>{esc(L['ui']['order_info'])}</dt><dd><a href="{pages}kontakt/">{esc(L['ui']['nav_contact'])}</a> · +420 728 466 141 · juzlj@seznam.cz</dd></dl></div>
{price_note_html(L)}
{figure}
{render_body(L, pr['body'], depth, product=pr)}
{faq_html(faqs, L['ui'].get('sec_faq', 'FAQ'))}
<p style="margin-top:2rem"><a class="btn gold" href="{pages}kontakt/">{esc(L['ui']['cta_sample_btn'])}</a></p>
</article></main>"""
    html_out = shell(L, title=pr["title"], desc=pr["desc"], path=path, depth=depth,
                     active=None, body=body, jsonld=lds,
                     keywords=keywords_for(lg, "product", key),
                     meta_kind="product", meta_key=key,
                     og_img=f"{BASE}/img/{PRODUCT_IMG[key]}" if PRODUCT_IMG.get(key) else None)
    write(([lg] if lg != "cs" else []) + [slug, "index.html"], html_out)


def build_recipes_index(L):
    lg = L["code"]
    depth = (0 if lg == "cs" else 1) + 1
    pages = page_rel(lg, depth)
    home = pages if pages else "./"
    cards = ""
    for slug in RECIPE_SLUGS:
        r = L["recipes"].get(slug)
        if not r:
            continue
        im = img_or_none(depth, RECIPE_IMG.get(slug))
        imtag = f'<img class="thumb" src="{im}" alt="{esc(r["name"])}" loading="lazy">' if im else ""
        cards += f"""<li class="card rv">{imtag}<div class="pad"><h3><a href="{pages}{slug}/">{esc(r['name'])}</a></h3><p>{esc(r.get('teaser',''))}</p></div></li>"""
    ui = L["ui"]
    body = f"""<main id="main" class="wrap"><article class="page" style="max-width:none">
<nav class="breadcrumb"><a href="{home}">{esc(ui['breadcrumb_home'])}</a> › {esc(ui['nav_recipes'])}</nav>
<h1>{esc(ui['nav_recipes'])}</h1>
<p class="sub">{esc(L['recipes_intro'])}</p>
<ul class="grid c3" style="list-style:none;padding:0">{cards}</ul>
</article></main>"""
    title = {"cs": "Recepty z našich směsí — knedlíky, dezerty, pudingy",
             "en": "Recipes from our mixes — dumplings, desserts, puddings",
             "de": "Rezepte aus unseren Mischungen — Knödel, Desserts, Pudding",
             "sk": "Recepty z našich zmesí — knedle, dezerty, pudingy"}[lg]
    html_out = shell(L, title=title, desc=L["recipes_intro"], path="recepty/",
                     depth=depth, active="recepty", body=body,
                     keywords=keywords_for(lg, "recepty"), meta_kind="recepty",
                     jsonld=[breadcrumb_jsonld(L, [
                         (ui["breadcrumb_home"], url_for(lg, "")),
                         (ui["nav_recipes"], url_for(lg, "recepty/")),
                     ]), {
                         "@context": "https://schema.org",
                         "@type": "ItemList",
                         "name": title,
                         "itemListElement": [
                             {"@type": "ListItem", "position": i + 1,
                              "url": url_for(lg, f"{slug}/"),
                              "name": L["recipes"][slug]["name"]}
                             for i, slug in enumerate(RECIPE_SLUGS)
                             if slug in L["recipes"]
                         ],
                     }])
    write(([lg] if lg != "cs" else []) + ["recepty", "index.html"], html_out)


def recipe_family(slug):
    if slug in CHOUX_SLUGS:
        return "choux"
    if slug in DUMPLING_SLUGS:
        return "dumpling"
    return "dessert"


def suggested_recipe_slugs(L, current_slug):
    """Related first: same pastry family, then same mix, then the rest."""
    current = L["recipes"].get(current_slug) or {}
    current_product = current.get("product")
    current_family = recipe_family(current_slug)
    others = [s for s in RECIPE_SLUGS if s != current_slug and s in L["recipes"]]

    def rank(slug):
        rec = L["recipes"][slug]
        same_family = recipe_family(slug) == current_family
        same_product = bool(current_product) and rec.get("product") == current_product
        related = 0
        if same_family:
            related += 2
        if same_product:
            related += 3
        return (-related, RECIPE_SLUGS.index(slug))

    others.sort(key=rank)
    return others[:SUGGESTED_RECIPES]


def more_recipes_html(L, current_slug, depth):
    """Suggested recipes based on the one you are reading."""
    ui = L["ui"]
    pages = page_rel(L["code"], depth)
    cards = []
    for other in suggested_recipe_slugs(L, current_slug):
        rec = L["recipes"].get(other)
        if not rec:
            continue
        name = rec["name"]
        teaser = rec.get("teaser", "")
        href = f"{pages}{other}/"
        label = ui["more_recipe_open"].replace("{name}", name)
        im = img_or_none(depth, RECIPE_IMG.get(other))
        media = ""
        if im:
            media = (
                f'<span class="more-recipe-media">'
                f'<img src="{im}" alt="" width="480" height="320" loading="lazy">'
                f"</span>"
            )
        teaser_html = (
            f'<span class="more-recipe-teaser">{esc(teaser)}</span>' if teaser else ""
        )
        cards.append(
            f'<li>'
            f'<a class="more-recipe" href="{href}" aria-label="{esc(label)}">'
            f"{media}"
            f'<span class="more-recipe-body">'
            f'<span class="more-recipe-name">{esc(name)}</span>'
            f"{teaser_html}"
            f'<span class="more-recipe-go">{esc(ui["detail"])}</span>'
            f"</span></a></li>"
        )
    if not cards:
        return ""
    return f"""<nav class="more-recipes" aria-labelledby="more-recipes-h">
<div class="wrap">
<p class="kicker">{esc(ui["more_recipes_kicker"])}</p>
<h2 id="more-recipes-h" class="sec">{esc(ui["more_recipes"])}</h2>
<p class="more-recipes-lead">{esc(ui["more_recipes_lead"])}</p>
<ul class="more-recipes-grid">{"".join(cards)}</ul>
</div>
</nav>"""


def build_recipe(L, slug):
    lg = L["code"]
    r = L["recipes"].get(slug)
    if not r:
        return
    depth = (0 if lg == "cs" else 1) + 1
    pages = page_rel(lg, depth)
    home = pages if pages else "./"
    im = img_or_none(depth, RECIPE_IMG.get(slug))
    figure = f'<figure><img src="{im}" alt="{esc(r["name"])}"></figure>' if im else ""
    ing = "".join(f"<li>{esc(x)}</li>" for x in r.get("ingredients", []))
    steps = "".join(f"<li>{esc(x)}</li>" for x in r.get("steps", []))
    prod_key = r.get("product")
    prod_link = ""
    if prod_key and prod_key in L["products"]:
        prod_link = (f'<div class="factbox"><dl><dt>{esc(L["ui"]["uses_product"])}</dt>'
                     f'<dd><a href="{pages}{PRODUCT_SLUGS[prod_key]}/">'
                     f'{esc(L["products"][prod_key]["name"])}</a></dd></dl></div>')
    recipe_ld = {
        "@context": "https://schema.org", "@type": "Recipe",
        "name": r["name"],
        "description": r.get("teaser") or r.get("desc", ""),
        "recipeCuisine": CUISINE.get(lg, "Czech"),
        "recipeCategory": RECIPE_CATEGORY.get(lg, RECIPE_CATEGORY["cs"]).get(slug, ""),
        "keywords": keywords_for(lg, "recipe", slug),
        "inLanguage": lg,
        "author": {"@type": "Organization", "name": "Jůzlová", "@id": BASE + "/#org"},
        "publisher": {"@id": BASE + "/#org"},
        "url": url_for(lg, f"{slug}/"),
        "mainEntityOfPage": url_for(lg, f"{slug}/"),
        **({"image": [{
            "@type": "ImageObject",
            "url": f"{BASE}/img/{RECIPE_IMG[slug]}",
            "contentUrl": f"{BASE}/img/{RECIPE_IMG[slug]}",
            "caption": r["name"],
            "representativeOfPage": True,
        }]} if RECIPE_IMG.get(slug) else {}),
        **({"recipeIngredient": r["ingredients"]} if r.get("ingredients") else {}),
        **({"recipeInstructions": [
            {"@type": "HowToStep", "position": i + 1, "text": s, "name": s[:80]}
            for i, s in enumerate(r["steps"])
        ]} if r.get("steps") else {}),
    }
    times = RECIPE_TIMES.get(slug) or {}
    for field in ("prepTime", "cookTime", "totalTime", "recipeYield",
                  "datePublished", "suitableForDiet"):
        if times.get(field):
            recipe_ld[field] = times[field]
    recipe_ld["dateModified"] = TODAY
    rec_faqs = recipe_faq(lg, slug)
    ing_h = {"cs": "Suroviny", "en": "Ingredients", "de": "Zutaten", "sk": "Suroviny"}[lg]
    steps_h = {"cs": "Postup", "en": "Method", "de": "Zubereitung", "sk": "Postup"}[lg]
    ing_block = f"<h2>{ing_h}</h2><ul>{ing}</ul>" if ing else ""
    steps_block = f"<h2>{steps_h}</h2><ol>{steps}</ol>" if steps else ""
    extra = "".join(f"<p>{esc(x)}</p>" for x in r.get("notes", []))
    more = more_recipes_html(L, slug, depth)
    lds = [recipe_ld, breadcrumb_jsonld(L, [
        (L["ui"]["breadcrumb_home"], url_for(lg, "")),
        (L["ui"]["nav_recipes"], url_for(lg, "recepty/")),
        (r["name"], url_for(lg, f"{slug}/"))])]
    if rec_faqs:
        lds.append(faq_jsonld(rec_faqs))
    body = f"""<main id="main">
<div class="wrap"><article class="page">
<nav class="breadcrumb"><a href="{home}">{esc(L['ui']['breadcrumb_home'])}</a> › <a href="{pages}recepty/">{esc(L['ui']['nav_recipes'])}</a> › {esc(r['name'])}</nav>
<h1>{esc(r['name'])}</h1>
<p class="sub">{esc(r.get('teaser',''))}</p>
{rating_widget_html(L, slug)}
{prod_link}
{figure}
{ing_block}
{steps_block}
{extra}
{faq_html(rec_faqs, L['ui'].get('sec_faq', 'FAQ'))}
</article></div>
{more}
</main>"""
    html_out = shell(L, title=r.get("title", r["name"]), desc=r.get("desc", r.get("teaser", "")),
                     path=f"{slug}/", depth=depth, active="recepty", body=body,
                     jsonld=lds, meta_kind="recipe", meta_key=slug,
                     keywords=keywords_for(lg, "recipe", slug),
                     og_img=f"{BASE}/img/{RECIPE_IMG[slug]}" if RECIPE_IMG.get(slug) else None)
    write(([lg] if lg != "cs" else []) + [slug, "index.html"], html_out)


def build_faq_page(L):
    lg = L["code"]
    depth = (0 if lg == "cs" else 1) + 1
    pages = page_rel(lg, depth)
    home = pages if pages else "./"
    ui = L["ui"]
    pg = L["faq_page"]
    items = site_faq(lg)
    body = f"""<main id="main" class="wrap"><article class="page">
<nav class="breadcrumb"><a href="{home}">{esc(ui['breadcrumb_home'])}</a> › {esc(pg['h1'])}</nav>
<h1>{esc(pg['h1'])}</h1>
<p class="sub">{esc(pg['sub'])}</p>
{faq_html(items)}
<p style="margin-top:1.6rem">{esc(ui.get('faq_b2b_hint', 'Kitchens and shops: see Wholesale.'))} <a href="{pages}velkoobchod/">{esc(ui['nav_b2b'])} →</a></p>
<p style="margin-top:1.2rem"><a class="btn gold" href="{pages}kontakt/">{esc(ui['cta_sample_btn'])}</a></p>
</article></main>"""
    html_out = shell(
        L, title=pg["title"], desc=pg["desc"], path="faq/", depth=depth,
        active="faq", body=body, keywords=keywords_for(lg, "faq"),
        meta_kind="faq",
        jsonld=[
            breadcrumb_jsonld(L, [
                (ui["breadcrumb_home"], url_for(lg, "")),
                (pg["h1"], url_for(lg, "faq/")),
            ]),
            faq_jsonld(items),
        ],
    )
    write(([lg] if lg != "cs" else []) + ["faq", "index.html"], html_out)


def build_aeo_page(L, key):
    lg = L["code"]
    slug = aeo_slug(key)
    depth = (0 if lg == "cs" else 1) + 1
    pack = AEO_PAGES[lg][key]
    path = f"{slug}/"
    pages = page_rel(lg, depth)
    home = pages if pages else "./"
    crumbs = [
        (L["ui"]["breadcrumb_home"], url_for(lg, "")),
        (pack["h1"], url_for(lg, path)),
    ]
    is_b2b = key in B2B_SLUGS
    faqs = pack.get("faq") or []
    if not is_b2b:
        # Strip accidental B2B keywords from geo / D2C AEO FAQs.
        b2b_markers = ("restaurac", "velkoobchod", "provozovn", "wholesale", "großhandel", "25 kg")
        faqs = [
            (q, a) for q, a in faqs
            if not any(m in (q + a).lower() for m in b2b_markers)
        ]
    extra_ld = [breadcrumb_jsonld(L, crumbs)]
    if faqs:
        extra_ld.append(faq_jsonld(faqs))
    active = "velkoobchod" if is_b2b else "kde_nas_najdete"
    meta_kind = "velkoobchod" if is_b2b else "kde_nas_najdete"
    body = f"""<main id="main" class="wrap"><article class="page">
<nav class="breadcrumb"><a href="{home}">{esc(L['ui']['breadcrumb_home'])}</a> › {esc(pack['h1'])}</nav>
<h1>{esc(pack['h1'])}</h1>
<p class="sub">{esc(pack['sub'])}</p>
{render_body(L, pack['body'], depth)}
{faq_html(faqs, L['ui'].get('sec_faq', 'FAQ'))}
</article></main>"""
    html_out = shell(
        L, title=pack["title"], desc=pack["desc"], path=path, depth=depth,
        active=active, body=body, jsonld=extra_ld,
        keywords=pack.get("keywords") or "", meta_kind=meta_kind,
    )
    write(([lg] if lg != "cs" else []) + [slug, "index.html"], html_out)


def build_redirects():
    for old, new in LEGACY_REDIRECTS.items():
        for lg in LANGS:
            target = url_for(lg, f"{new}/")
            parts = [old, "index.html"] if lg == "cs" else [lg, old, "index.html"]
            write(parts, f"""<!doctype html>
<html lang="{lg}"><head><meta charset="utf-8"><title>Jůzlová.cz</title>
<link rel="canonical" href="{target}">
<meta http-equiv="refresh" content="0;url={target}">
</head><body><p><a href="{target}">→ {target}</a></p></body></html>
""")


def all_paths(langs_data):
    paths = [""]
    paths += [f"{slug}/" for slug in PAGE_SLUGS.values()]
    paths += [f"{slug}/" for slug in PRODUCT_SLUGS.values()]
    paths.append("recepty/")
    paths.append("faq/")
    paths += [f"{slug}/" for slug in GEO_SLUGS.values()]
    paths += [f"{slug}/" for slug in B2B_SLUGS.values()]
    cs = langs_data["cs"]
    paths += [f"{slug}/" for slug in RECIPE_SLUGS if slug in cs["recipes"]]
    return paths


def _path_priority(path):
    if path in SITEMAP_PRIORITY:
        return SITEMAP_PRIORITY[path]
    slug = path.rstrip("/")
    if slug in PRODUCT_SLUGS.values():
        return PRODUCT_PRIORITY
    if slug in RECIPE_SLUGS:
        return RECIPE_PRIORITY
    return 0.6


def _image_tag(langs_data, path, lg):
    slug = path.rstrip("/")
    inv_prod = {v: k for k, v in PRODUCT_SLUGS.items()}
    if slug in inv_prod:
        key = inv_prod[slug]
        img = PRODUCT_IMG.get(key)
        name = langs_data[lg]["products"][key]["name"]
        if img:
            return (f"<image:image><image:loc>{BASE}/img/{img}</image:loc>"
                    f"<image:title>{esc(name)}</image:title></image:image>")
    if slug in RECIPE_SLUGS:
        img = RECIPE_IMG.get(slug)
        rec = langs_data[lg]["recipes"].get(slug) or {}
        name = rec.get("name", slug)
        if img:
            cap = rec.get("teaser", name)
            return (f"<image:image><image:loc>{BASE}/img/{img}</image:loc>"
                    f"<image:title>{esc(name)}</image:title>"
                    f"<image:caption>{esc(cap)}</image:caption></image:image>")
    return ""


def _urlset_xml(entries):
    ns = (
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml" '
        'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">'
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        + ns + "\n" + "\n".join(entries) + "\n</urlset>\n"
    )


def _llms_sitemap_entries():
    entries = [
        "<!-- Language-model discovery: short index then full extract (https://llmstxt.org) -->",
        (
            f"<url><loc>{BASE}/llms.txt</loc>"
            f"<lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq>"
            f"<priority>0.95</priority></url>"
        ),
        (
            f"<url><loc>{BASE}/llms-full.txt</loc>"
            f"<lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq>"
            f"<priority>0.9</priority></url>"
        ),
    ]
    for lg in LANGS:
        loc = f"{BASE}/llms-{lg}.txt"
        entries.append(
            f"<url><loc>{loc}</loc><lastmod>{TODAY}</lastmod>"
            f"<changefreq>weekly</changefreq><priority>0.7</priority></url>"
        )
    return entries


def _page_sitemap_entry(langs_data, path, lg):
    pri = f"{_path_priority(path):.1f}"
    freq = "daily" if path == "" else "weekly"
    alts = "".join(
        f'<xhtml:link rel="alternate" hreflang="{o}" href="{url_for(o, path)}"/>'
        for o in LANGS)
    alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{url_for("cs", path)}"/>'
    img = _image_tag(langs_data, path, lg)
    return (
        f"<url><loc>{url_for(lg, path)}</loc>{alts}{img}"
        f"<lastmod>{TODAY}</lastmod><changefreq>{freq}</changefreq>"
        f"<priority>{pri}</priority></url>"
    )


def build_sitemap(langs_data):
    paths = all_paths(langs_data)
    for lg in LANGS:
        entries = _llms_sitemap_entries() if lg == "cs" else []
        entries += [_page_sitemap_entry(langs_data, path, lg) for path in paths]
        write([f"sitemap-{lg}.xml"], _urlset_xml(entries))
    index = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for lg in LANGS:
        index.append(
            f"<sitemap><loc>{BASE}/sitemap-{lg}.xml</loc>"
            f"<lastmod>{TODAY}</lastmod></sitemap>"
        )
    index.append("</sitemapindex>")
    write(["sitemap.xml"], "\n".join(index) + "\n")


def build_manifest():
    write(["site.webmanifest"], json.dumps({
        "name": "Jůzlová — potravinářské směsi",
        "short_name": "Jůzlová",
        "start_url": BASE + "/",
        "display": "standalone",
        "background_color": "#faf6ef",
        "theme_color": "#021536",
        "icons": [
            {"src": BASE + "/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": BASE + "/img/icon-512.png", "sizes": "512x512", "type": "image/png"},
        ],
    }, ensure_ascii=False, indent=1))


def build_forms_skeleton():
    """Hidden form so Netlify detects fields at build time."""
    fields = "".join(
        f'<input type="checkbox" name="product" value="{esc(k)}">\n'
        for k in PRODUCT_SLUGS
    )
    write(["__forms.html"], f"""<!DOCTYPE html>
<html lang="cs">
<head><meta charset="utf-8"><title>forms</title></head>
<body>
<form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" hidden>
  <input type="hidden" name="form-name" value="contact">
  <input type="hidden" name="lang" value="cs">
  <input type="hidden" name="subject" value="Jůzlová — poptávka z webu">
  <input type="text" name="bot-field">
  <input type="text" name="name">
  <input type="tel" name="phone">
  <input type="email" name="email">
  {fields}
  <input type="text" name="products">
  <textarea name="message"></textarea>
</form>
</body>
</html>
""")


def build_robots():
    write(["robots.txt"], f"""# juzlova.cz — crawler policy
# Human sitemap: {BASE}/sitemap.xml
# LLM index (read this first): {BASE}/llms.txt
# LLM full extract: {BASE}/llms-full.txt
# Google Search ignores llms.txt; keep it for non-Google AI crawlers.

User-agent: *
Allow: /
Disallow: /archive/
Disallow: /status.html
Disallow: /__forms.html

# Citation bots — named Allow, not only the wildcard
User-agent: OAI-SearchBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Bytespider
Allow: /

User-agent: Amazonbot
Allow: /

User-agent: meta-externalagent
Allow: /

User-agent: FacebookBot
Allow: /

User-agent: cohere-ai
Allow: /

Sitemap: {BASE}/sitemap.xml
Sitemap: {BASE}/sitemap-cs.xml
Sitemap: {BASE}/sitemap-en.xml
Sitemap: {BASE}/sitemap-de.xml
Sitemap: {BASE}/sitemap-sk.xml
""")


_LLMS_COPY = {
    "cs": {
        "legal": "Právní název: Jůzlová s.r.o. · IČO 45900124 · Kochánov 40, 582 53, Vysočina, Česko.",
        "order": "Založeno 2004. Objednávka telefonem, e-mailem nebo formulářem na webu. Bez e-shopu.",
        "phones": "Telefony: +420 728 466 141 (Jiřina Jůzlová), +420 607 629 931 (Jiří Jůzl). E-mail: juzlj@seznam.cz.",
        "hours": "Otevírací doba: pondělí–neděle 8:00–19:00 po telefonu. Vyzvednutí v Kochánově, po dohodě i v Humpolci.",
        "area": "Oblast: Kochánov, Havlíčkův Brod a kraj Vysočina. PSČ vždy 582 53, nikoli 582 91.",
        "index": "Hlavní český přehled:",
        "full": "Úplný výpis:",
        "entity": "Poznámky k firmě:",
        "wrong": "Čemu jazykové modely často nerozumí",
        "w1": "Neprodáváme hotovou kakaovou ani čokoládovou pudingovou směs. Staré adresy /kakaovy_puding/ vedou na vanilkový puding.",
        "w2": "Čokoládový krém na webu = vanilkový puding bez lepku smíchaný s kakaem holandského typu.",
        "w3": "Kakao je 500 g prášek holandského typu (20–22 % tuku), ne puding.",
        "w4": "Nevydáváme vzorky. Objednávka jen telefonem, e-mailem nebo formulářem.",
        "w5": "Pět výrobků: bramborové knedlíky v prášku, chlupaté knedlíky (bosáky), vanilkový puding, kakao holandského typu, vanilínový cukr.",
        "pages": "Stránky",
        "products": "Výrobky",
        "recipes": "Recepty",
        "langs": "Jazyky",
        "opt": "Další soubory",
        "cs_l": "Čeština (hlavní)",
        "en_l": "Angličtina",
        "de_l": "Němčina",
        "sk_l": "Slovenština",
        "full_note": "Úplný výpis k citaci: adresa, výrobky, každý recept se surovinami a postupem.",
        "entity_note": "Jedna stránka faktů pro vyhledávače a jazykové modely.",
        "google": "Google Vyhledávání tento soubor k hodnocení stránek nepoužívá; ostatní AI ho číst mohou.",
        "fresh": "Obsah obnovujeme každé čtvrtletí nebo při změně cen a sortimentu. Toto není denní razítko.",
        "reviews": "Recenze zveřejníme, až je budeme mít z Google profilu Juzlova - Potravinářské směsi. Hvězdičky si nevymýšlíme.",
        "places": "Objednávka podle místa",
        "wholesale": "Velkoobchod podle místa",
    },
    "en": {
        "legal": "Legal name: Jůzlová s.r.o. · Company ID 45900124 · Kochánov 40, 582 53, Vysočina, Czechia.",
        "order": "Founded 2004. Order by phone, e-mail or the website form. No web shop.",
        "phones": "Phones: +420 728 466 141 (Jiřina Jůzlová), +420 607 629 931 (Jiří Jůzl). E-mail: juzlj@seznam.cz.",
        "hours": "Hours: Monday–Sunday 8:00–19:00 by phone. Pick-up in Kochánov, and in Humpolec by arrangement.",
        "area": "Area: Kochánov, Havlíčkův Brod and the Vysočina Region. Postcode is always 582 53, never 582 91.",
        "index": "Main Czech index:",
        "full": "Full extract:",
        "entity": "Entity notes:",
        "wrong": "Facts language models get wrong",
        "w1": "We do not sell a ready-made cocoa or chocolate pudding mix. Legacy /kakaovy_puding/ URLs go to vanilla pudding.",
        "w2": "Chocolate cream on this site = gluten-free vanilla pudding mixed with Dutch-process cocoa by the cook.",
        "w3": "Cocoa is a 500 g Dutch-process powder (20–22% fat), not a pudding.",
        "w4": "We do not send samples. Order by phone, e-mail or the form only.",
        "w5": "Five products: potato dumpling mix, hairy dumplings (bosáky), vanilla pudding, Dutch-process cocoa, vanilla sugar.",
        "pages": "Pages",
        "products": "Products",
        "recipes": "Recipes",
        "langs": "Languages",
        "opt": "More files",
        "cs_l": "Czech (main)",
        "en_l": "English",
        "de_l": "German",
        "sk_l": "Slovak",
        "full_note": "Full extract for citation: address, products, every recipe with ingredients and method.",
        "entity_note": "One-page facts for retrieval.",
        "google": "Google Search ignores this file for ranking; other AI crawlers may read it.",
        "fresh": "We refresh this file quarterly or when prices or the product range change. This is not a daily stamp.",
        "reviews": "We will publish reviews only from the Google listing Juzlova - Potravinářské směsi. We do not invent stars.",
        "places": "Order by place",
        "wholesale": "Wholesale by place",
    },
    "de": {
        "legal": "Rechtsname: Jůzlová s.r.o. · IČO 45900124 · Kochánov 40, 582 53, Vysočina, Tschechien.",
        "order": "Gegründet 2004. Bestellung telefonisch, per E-Mail oder über das Formular. Kein Onlineshop.",
        "phones": "Telefone: +420 728 466 141 (Jiřina Jůzlová), +420 607 629 931 (Jiří Jůzl). E-Mail: juzlj@seznam.cz.",
        "hours": "Öffnungszeiten: Montag–Sonntag 8:00–19:00 Uhr telefonisch. Abholung in Kochánov, nach Absprache auch in Humpolec.",
        "area": "Gebiet: Kochánov, Havlíčkův Brod und Region Vysočina. PLZ immer 582 53, niemals 582 91.",
        "index": "Tschechischer Hauptindex:",
        "full": "Vollständiger Auszug:",
        "entity": "Firmennotizen:",
        "wrong": "Was Sprachmodelle oft falsch verstehen",
        "w1": "Wir verkaufen keine fertige Kakao- oder Schokoladenpuddingmischung. Alte /kakaovy_puding/-Adressen führen zum Vanillepudding.",
        "w2": "Schokoladencreme auf dieser Website = glutenfreier Vanillepudding, vom Koch mit Kakao holländischer Art gemischt.",
        "w3": "Kakao ist 500 g Pulver holländischer Art (20–22 % Fett), kein Pudding.",
        "w4": "Wir versenden keine Muster. Bestellung nur telefonisch, per E-Mail oder Formular.",
        "w5": "Fünf Produkte: Kartoffelknödelmischung, Haarige Knödel (Bosáky), Vanillepudding, Kakao holländischer Art, Vanillinzucker.",
        "pages": "Seiten",
        "products": "Produkte",
        "recipes": "Rezepte",
        "langs": "Sprachen",
        "opt": "Weitere Dateien",
        "cs_l": "Tschechisch (Haupt)",
        "en_l": "Englisch",
        "de_l": "Deutsch",
        "sk_l": "Slowakisch",
        "full_note": "Vollständiger Auszug: Adresse, Produkte, jedes Rezept mit Zutaten und Zubereitung.",
        "entity_note": "Eine Seite Fakten für Suche und Sprachmodelle.",
        "google": "Google Suche nutzt diese Datei nicht für das Ranking; andere KI-Crawler können sie lesen.",
        "fresh": "Wir aktualisieren diese Datei vierteljährlich oder bei Preis- und Sortimentsänderungen. Das ist kein Tagesstempel.",
        "reviews": "Bewertungen veröffentlichen wir erst aus dem Google-Eintrag Juzlova - Potravinářské směsi. Sterne erfinden wir nicht.",
        "places": "Bestellung nach Ort",
        "wholesale": "Großhandel nach Ort",
    },
    "sk": {
        "legal": "Právny názov: Jůzlová s.r.o. · IČO 45900124 · Kochánov 40, 582 53, Vysočina, Česko.",
        "order": "Založené 2004. Objednávka telefónom, e-mailom alebo formulárom na webe. Bez e-shopu.",
        "phones": "Telefóny: +420 728 466 141 (Jiřina Jůzlová), +420 607 629 931 (Jiří Jůzl). E-mail: juzlj@seznam.cz.",
        "hours": "Otváracie hodiny: pondelok–nedeľa 8:00–19:00 po telefóne. Odber v Kochánove, po dohode aj v Humpolci.",
        "area": "Oblasť: Kochánov, Havlíčkův Brod a kraj Vysočina. PSČ vždy 582 53, nie 582 91.",
        "index": "Hlavný český prehľad:",
        "full": "Úplný výpis:",
        "entity": "Poznámky k firme:",
        "wrong": "Čomu jazykové modely často nerozumejú",
        "w1": "Nepredávame hotovú kakaovú ani čokoládovú pudingovú zmes. Staré adresy /kakaovy_puding/ vedú na vanilkový puding.",
        "w2": "Čokoládový krém na webe = vanilkový puding bez lepku zmiešaný s kakaom holandského typu.",
        "w3": "Kakao je 500 g prášok holandského typu (20–22 % tuku), nie puding.",
        "w4": "Nevydávame vzorky. Objednávka len telefónom, e-mailom alebo formulárom.",
        "w5": "Päť výrobkov: zemiakové knedle v prášku, chlpaté knedle (bosáky), vanilkový puding, kakao holandského typu, vanilínový cukor.",
        "pages": "Stránky",
        "products": "Výrobky",
        "recipes": "Recepty",
        "langs": "Jazyky",
        "opt": "Ďalšie súbory",
        "cs_l": "Čeština (hlavná)",
        "en_l": "Angličtina",
        "de_l": "Nemčina",
        "sk_l": "Slovenčina",
        "full_note": "Úplný výpis na citáciu: adresa, výrobky, každý recept so surovinami a postupom.",
        "entity_note": "Jedna stránka faktov pre vyhľadávače a jazykové modely.",
        "google": "Google Vyhľadávanie tento súbor na hodnotenie stránok nepoužíva; ostatné AI ho čítať môžu.",
        "fresh": "Obsah obnovujeme každé štvrťrok alebo pri zmene cien a sortimentu. Toto nie je denná pečiatka.",
        "reviews": "Recenzie zverejníme, až ich budeme mať z Google profilu Juzlova - Potravinářské směsi. Hviezdičky si nevymýšľame.",
        "places": "Objednávka podľa miesta",
        "wholesale": "Veľkoobchod podľa miesta",
    },
}


def _llms_index(langs_data, lang):
    """Short llmstxt.org index. Czech is the main file. Keep under 200 lines."""
    L = langs_data[lang]
    ui = L["ui"]
    c = _LLMS_COPY.get(lang) or _LLMS_COPY["cs"]
    lines = [
        "# Jůzlová",
        "",
        f"> {L['meta']['home_desc']}",
        "",
        c["legal"],
        c["order"],
        c["phones"],
        c["hours"],
        c["area"],
        c["google"],
        c["fresh"],
        c["reviews"],
        "",
        f"{c['index']} {BASE}/llms.txt",
        f"{c['full']} {BASE}/llms-full.txt",
        f"{c['entity']} {BASE}/ai/about.md",
        "",
        f"## {c['wrong']}",
        f"- {c['w1']}",
        f"- {c['w2']}",
        f"- {c['w3']}",
        f"- {c['w4']}",
        f"- {c['w5']}",
        "",
        f"## {c['pages']}",
        f"- [{ui['nav_home']}]({url_for(lang, '')}): {L['meta']['home_desc']}",
        f"- [{ui['nav_about']}]({url_for(lang, 'kdo_jsme/')}): {L['pages']['kdo_jsme']['desc']}",
        f"- [{ui['nav_delivery']}]({url_for(lang, 'kde-nas-najdete/')}): {L['pages']['kde_nas_najdete']['desc']}",
        f"- [{ui['nav_b2b']}]({url_for(lang, 'velkoobchod/')}): {L['pages']['velkoobchod']['desc']}",
        f"- [{ui['nav_d2c']}]({url_for(lang, 'do-eu/')}): {L['pages']['do_eu']['desc']}",
        f"- [{ui['nav_prices']}]({url_for(lang, 'ceny/')}): {L['pages']['ceny']['desc']}",
        f"- [{ui['nav_faq']}]({url_for(lang, 'faq/')}): {L['faq_page']['desc']}",
        f"- [{ui['nav_contact']}]({url_for(lang, 'kontakt/')}): {L['pages']['kontakt']['desc']}",
        f"- [{ui['nav_recipes']}]({url_for(lang, 'recepty/')}): {L['recipes_intro']}",
        "",
        f"## {c['places']}",
    ]
    pack = AEO_PAGES[lang]
    for key, slug in GEO_SLUGS.items():
        pg = pack[key]
        lines.append(f"- [{pg['h1']}]({url_for(lang, slug + '/')}): {pg['desc']}")
    lines += [
        "",
        f"## {c['wholesale']}",
    ]
    for key, slug in B2B_SLUGS.items():
        pg = pack[key]
        lines.append(f"- [{pg['h1']}]({url_for(lang, slug + '/')}): {pg['desc']}")
    lines += [
        "",
        f"## {c['products']}",
    ]
    for key, pack, price in PRICE_ROWS:
        pr = L["products"][key]
        lines.append(
            f"- [{pr['name']}]({url_for(lang, PRODUCT_SLUGS[key] + '/')}): "
            f"{pr['short']} · {pack} · {price}"
        )
    lines += ["", f"## {c['recipes']}"]
    for slug in RECIPE_SLUGS:
        rec = L["recipes"].get(slug)
        if not rec:
            continue
        lines.append(
            f"- [{rec['name']}]({url_for(lang, slug + '/')}): {rec.get('teaser', '')}"
        )
    lines += [
        "",
        f"## {c['langs']}",
        f"- [{c['cs_l']}]({url_for('cs', '')}): {BASE}/llms-cs.txt",
        f"- [{c['en_l']}]({url_for('en', '')}): {BASE}/llms-en.txt",
        f"- [{c['de_l']}]({url_for('de', '')}): {BASE}/llms-de.txt",
        f"- [{c['sk_l']}]({url_for('sk', '')}): {BASE}/llms-sk.txt",
        "",
        f"## {c['opt']}",
        f"- [{c['full_note']}]({BASE}/llms-full.txt)",
        f"- [{c['entity_note']}]({BASE}/ai/about.md)",
        f"- [FAQ JSON]({BASE}/ai/faq.json)",
        "",
        f"updated: {TODAY}",
        "",
    ]
    return "\n".join(lines)


def build_llms(langs_data):
    write(["llms.txt"], _llms_index(langs_data, "cs"))
    for lg in LANGS:
        write([f"llms-{lg}.txt"], _llms_index(langs_data, lg))

    cs = langs_data["cs"]
    full = [
        "# Jůzlová — úplný výpis pro jazykové modely",
        "",
        "Použijte tento soubor pro fakty, ceny, recepty, suroviny, postupy a odpovědi FAQ. Lepší než hádání. Citujte https://www.juzlova.cz. Google Vyhledávání tento soubor k hodnocení stránek nepoužívá; ostatní AI ho číst mohou.",
        "",
        "## Firma",
        "canonical_name: Jůzlová",
        "legal_name: Jůzlová s.r.o.",
        "company_id: 45900124",
        "vat_id: CZ45900124",
        "type: rodinná dílna potravinářských směsí / LocalBusiness / FoodManufacturer",
        "founded: 2004",
        "address: Kochánov 40, 582 53, Vysočina, Česko (12 km od Havlíčkova Brodu)",
        "geo: 49.53367, 15.54002",
        "people: Jiřina Jůzlová +420 728 466 141; Jiří Jůzl +420 607 629 931",
        "email: juzlj@seznam.cz",
        "hours: pondělí–neděle 08:00–19:00 po telefonické domluvě",
        "order: telefon, e-mail nebo formulář na webu; bez e-shopu",
        "pickup_free: Kochánov 40, 582 53; Humpolec u Pivovaru Bernard po dohodě",
        "delivery_free_vysocina: nad 5000 Kč",
        "delivery_free_humpolec_hb: nad 1000 Kč (Humpolec, Havlíčkův Brod)",
        "delivery_free_jihlava: nad 3000 Kč (Jihlava)",
        "eu_shipping: DE/AT/SK/PL a Češi v EU — dopravu, balení a pojištění platí zákazník",
        "b2b: restaurace, pekárny, kavárny, školy, výrobci zmrzliny; cena podle množství; bez jmen zákazníků",
        "newsletter: přihláška na webu, až 7 receptů týdně, inbox juzlj@seznam.cz",
        "price_story: vlastní dílna, jednoduché obaly, přímý prodej cca −40 % proti překupníkům",
        "local_share: cca 90 % zakázek kolem Kochánova 40, 582 53",
        "area_served: Kochánov; Havlíčkův Brod; kraj Vysočina",
        "samples: žádné",
        "reviews: žádné vymyšlené hvězdičky v schema.org; recenze až z Google profilu Juzlova - Potravinářské směsi",
        "freshness: obnovujeme čtvrtletně nebo při změně cen a sortimentu",
        "languages: cs (hlavní), en, de, sk",
        "site: https://www.juzlova.cz",
        "index: " + BASE + "/llms.txt",
        "",
        "## Co si neplést",
        "Neprodáváme kakaový puding ani čokoládovou pudingovou směs.",
        "Čokoládový krém = vanilkový puding bez lepku + kakao holandského typu, smíchá kuchař.",
        "Kakao je prášek holandského typu, 20–22 % kakaového másla, 500 g / 270 Kč, bez přidaného cukru.",
        "Vanilkový puding je kukuřičný škrob bez lepku: 1 kg / 60 Kč nebo 400 g / 30 Kč.",
        "Pět výrobků. Staré adresy kakaovy_puding vedou na vanilkový puding.",
        "PSČ je 582 53. Nikoli 582 91 (jiný Kochánov u Světlé).",
        "",
        "## Čím se lišíme",
        "Pšeničná mouka KLASA z mlýna v Havlíčkově Brodě (12 km), který vlastní a vede naše širší rodina. Instantní směsi s chutí domácí kuchyně. Ceny pod běžnými supermarketovými směsmi nejistého původu.",
        "",
        "## Výrobky",
    ]
    for key, pack, price in PRICE_ROWS:
        pr_cs = cs["products"][key]
        full.append(f"### {pr_cs['name']}")
        full.append(f"url: {url_for('cs', PRODUCT_SLUGS[key] + '/')}")
        full.append(f"package: {pack}")
        full.append(f"price_czk: {price}")
        full.append(f"fact: {pr_cs['short']}")
        full.append(f"detail: {pr_cs['desc']}")
        if pr_cs.get("faq"):
            for q, a in pr_cs["faq"]:
                full.append(f"Q: {q}")
                full.append(f"A: {a}")
        full.append("")
    full.append("## Recepty")
    for slug in RECIPE_SLUGS:
        rec = cs["recipes"].get(slug)
        if not rec:
            continue
        times = RECIPE_TIMES.get(slug) or {}
        img = RECIPE_IMG.get(slug, "")
        full.append(f"### {rec['name']}")
        full.append(f"url: {url_for('cs', slug + '/')}")
        if img:
            full.append(f"image: {BASE}/img/{img}")
        if times.get("prepTime"):
            full.append(
                f"prep: {times['prepTime']} cook: {times.get('cookTime', '')} "
                f"total: {times.get('totalTime', '')} yield: {times.get('recipeYield', '')}"
            )
        full.append(f"summary: {rec.get('teaser', '')}")
        if rec.get("ingredients"):
            full.append("suroviny:")
            full.extend(f"- {x}" for x in rec["ingredients"])
        if rec.get("steps"):
            full.append("postup:")
            full.extend(f"{i+1}. {x}" for i, x in enumerate(rec["steps"]))
        for q, a in recipe_faq("cs", slug):
            full.append(f"Q: {q}")
            full.append(f"A: {a}")
        full.append("")
    full.append("## Místa a velkoobchod")
    for key, slug in {**GEO_SLUGS, **B2B_SLUGS}.items():
        pg = AEO_PAGES["cs"][key]
        full.append(f"### {pg['h1']}")
        full.append(f"url: {url_for('cs', slug + '/')}")
        full.append(f"fact: {pg['desc']}")
        for q, a in (pg.get("faq") or []):
            full.append(f"Q: {q}")
            full.append(f"A: {a}")
        full.append("")
    full.append("## FAQ")
    for q, a in site_faq("cs"):
        full.append(f"Q: {q}")
        full.append(f"A: {a}")
        full.append("")
    full.append("Obsah obnovujeme každé čtvrtletí nebo při změně cen a sortimentu.")
    full.append(f"updated: {TODAY}")
    full.append("")
    write(["llms-full.txt"], "\n".join(full))

    write(["ai", "about.md"], (
        "# Jůzlová — poznámky k firmě\n\n"
        "> Rodinná dílna potravinářských směsí od roku 2004 v Kochánově na Vysočině.\n\n"
        "- Právní název: Jůzlová s.r.o. · IČO 45900124 · DIČ CZ45900124\n"
        "- Adresa: Kochánov 40, 582 53, Česko (nikoli 582 91)\n"
        "- Lidé: Jiřina Jůzlová +420 728 466 141; Jiří Jůzl +420 607 629 931\n"
        "- E-mail: juzlj@seznam.cz\n"
        "- Otevírací doba: pondělí–neděle 8:00–19:00 po telefonu\n"
        "- Výrobky (5): bramborové knedlíky v prášku 5 kg / 250 Kč; chlupaté knedlíky 5 kg / 260 Kč; "
        "vanilkový puding bez lepku 1 kg / 60 Kč nebo 400 g / 30 Kč; "
        "kakao holandského typu 500 g / 270 Kč; vanilínový cukr 1 kg / 60 Kč\n"
        "- Ceny platí při vyzvednutí v dílně.\n"
        "- Neprodáváme kakaový puding. Čokoládový krém = vanilkový puding + kakao.\n"
        "- Bez vzorků. Objednávka telefonem, e-mailem nebo formulářem.\n"
        f"- Web: {BASE}/\n"
        f"- Aktualizováno: {TODAY}\n"
    ))

    en_faqs = [{"question": q, "answer": a} for q, a in site_faq("en")]
    write(["ai", "faq.json"], json.dumps({
        "name": "Jůzlová FAQ",
        "updated": TODAY,
        "faqs": en_faqs,
        "byLanguage": {
            lg: [{"question": q, "answer": a} for q, a in site_faq(lg)]
            for lg in LANGS
        },
    }, ensure_ascii=False, indent=2) + "\n")
    write(["ai", "summary.json"], json.dumps({
        "name": "Jůzlová",
        "description": (
            "Czech family food-mix workshop since 2004 in Kochánov, Vysočina: "
            "potato dumpling mix, hairy dumpling mix (bosáky), gluten-free vanilla "
            "pudding, Dutch-process cocoa and vanilla sugar. Orders by phone or email."
        ),
        "url": BASE + "/",
        "llms": BASE + "/llms.txt",
        "llmsFull": BASE + "/llms-full.txt",
        "foundingDate": "2004",
        "address": "Kochánov 40, 582 53, Czech Republic",
        "telephone": ["+420728466141", "+420607629931"],
        "email": "juzlj@seznam.cz",
        "products": [
            {"id": k, "name": langs_data["en"]["products"][k]["name"],
             "price": p, "url": url_for("en", PRODUCT_SLUGS[k] + "/")}
            for k, _, p in PRICE_ROWS
        ],
        "recipes": [
            {"slug": s, "name": langs_data["en"]["recipes"][s]["name"],
             "url": url_for("en", s + "/")}
            for s in RECIPE_SLUGS if s in langs_data["en"]["recipes"]
        ],
        "updated": TODAY,
    }, ensure_ascii=False, indent=2) + "\n")
    write(["ai", "service.json"], json.dumps({
        "name": "Jůzlová food mixes",
        "description": "Family workshop selling five food mixes from Kochánov, Czech Republic.",
        "url": BASE + "/",
        "capabilities": [
            "Sell potato dumpling mix (5 kg)",
            "Sell hairy dumpling mix / bosáky (5 kg)",
            "Sell gluten-free vanilla pudding (1 kg or 400 g)",
            "Sell Dutch-process cocoa (500 g)",
            "Sell vanilla sugar (1 kg)",
            "Free pick-up at Kochánov 40, 582 53 and in Humpolec near Pivovar Bernard by arrangement",
            "Free Vysočina delivery from 5000 CZK; free to Humpolec and Havlíčkův Brod from 1000 CZK; free to Jihlava from 3000 CZK",
            "Take orders by phone or email",
        ],
        "updated": TODAY,
    }, ensure_ascii=False, indent=2) + "\n")
    write([".well-known", "ai.txt"], f"""# AI crawler hint for Jůzlová
llms.txt: {BASE}/llms.txt
llms-full.txt: {BASE}/llms-full.txt
entity: {BASE}/ai/about.md
sitemap: {BASE}/sitemap.xml
contact: juzlj@seznam.cz
""")


def copy_images():
    src = ROOT / "archive" / "images"
    dst = ROOT / "img"
    dst.mkdir(exist_ok=True)
    if src.exists():
        skip_if_brand = {
            "vanilkovy-cukr-pytliky.png": "vanilkovy-cukr.webp",
            "vanilkovy-cukr.png": "vanilkovy-cukr.webp",
            "sisky-s-makem.png": "sisky-s-makem.webp",
        }
        for a_name, pub in IMAGE_MAP.items():
            keep = skip_if_brand.get(pub)
            if keep and (dst / keep).exists():
                continue
            f = src / a_name
            if f.exists():
                shutil.copyfile(f, dst / pub)
        # 2017 recipe plates were never captured. Use the 150x150 archive
        # thumb once, under the canonical name — never as a second -alt file.
        for pub, a_name in (
            ("sisky-s-makem.png",
             "wp-content_uploads_2015_02_bramborove-sisky-s-makem-recept3-150x150.png"),
            ("strapacky.jpg",
             "wp-content_uploads_2015_03_Strapacky-se-zellm-a-slaninou-2-150x150.png"),
        ):
            dest = dst / pub
            f = src / a_name
            if dest.exists() or not f.exists():
                continue
            if pub.startswith("strapacky") and (dst / "strapacky.webp").exists():
                continue
            if pub.startswith("sisky-s-makem") and (dst / "sisky-s-makem.webp").exists():
                continue
            shutil.copyfile(f, dest)
    drop_duplicate_images(dst)
    # img/logo.png is the recovered 2017 logo, kept as an archive asset; the
    # icons the site actually links come from scripts/make_brand_assets.py.


def drop_duplicate_images(dst):
    """Keep one file per checksum. Prefer names the site actually links."""
    if not dst.exists():
        return
    canonical = (
        set(PRODUCT_IMG.values()) | set(RECIPE_IMG.values()) | set(IMAGE_MAP.values())
    )
    by_hash = {}
    for p in dst.iterdir():
        if not p.is_file():
            continue
        digest = hashlib.md5(p.read_bytes()).hexdigest()
        by_hash.setdefault(digest, []).append(p)
    for paths in by_hash.values():
        if len(paths) < 2:
            continue
        keep = next(
            (p for p in paths if p.name in canonical),
            sorted(paths, key=lambda x: x.name)[0],
        )
        for p in paths:
            if p != keep:
                p.unlink()


def main():
    copy_images()
    langs_data = {lg: load(lg) for lg in LANGS}
    for lg in LANGS:
        L = langs_data[lg]
        build_home(L)
        for key in PAGE_SLUGS:
            build_page(L, key)
        for key in PRODUCT_SLUGS:
            build_product(L, key)
        build_recipes_index(L)
        build_faq_page(L)
        for slug in RECIPE_SLUGS:
            build_recipe(L, slug)
        for key in AEO_PAGE_KEYS:
            build_aeo_page(L, key)
    build_redirects()
    build_sitemap(langs_data)
    build_robots()
    build_forms_skeleton()
    build_manifest()
    build_llms(langs_data)
    print("built:", ", ".join(LANGS))


if __name__ == "__main__":
    main()
