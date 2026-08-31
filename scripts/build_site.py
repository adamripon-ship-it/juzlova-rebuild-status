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
import html as H
import importlib.util
import json
import os
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = os.environ.get("SITE_BASE", "https://adamripon-ship-it.github.io/juzlova-rebuild-status")
TODAY = "2026-08-31"

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
]
# archive image file -> public img name (used when archive/images is populated)
IMAGE_MAP = {
    "wp-content_uploads_2017_06_juzlova-logo-black-2017.png": "logo.png",
    "wp-content_uploads_2012_07_Bramborov_-knedl_ky-300x225.png": "bramborove-knedliky.png",
    "wp-content_uploads_2012_07_Chlupat_-knedl_ky-300x225.png": "chlupate-knedliky.png",
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
    "wp-content_uploads_2015_02_bramborove-sisky-s-makem-recept3-150x150.png": "sisky-s-makem-alt.png",
    "wp-content_uploads_2015_03_Strapacky-se-zellm-a-slaninou-2-150x150.png": "strapacky-alt.png",
    "wp-content_uploads_2012_07_IMG_20141026_100948-300x225.png": "vyroba.png",
    "wp-content_uploads_2017_04_Bramborovo-tvarohove-knedliky-s-jahodami-podle-lucie-kuzelove.jpg": "bramborovo-tvarohove-knedliky.jpg",
}
PRODUCT_IMG = {
    "bramborove_knedliky": "bramborove-knedliky.png",
    "chlupate_knedliky": "chlupate-knedliky.png",
    "vanilkovy_pudink": "vanilkovy-puding.png",
    "kakao_holandskeho_typu": "kakao.jpg",
    "vanilkovy_cukr": "vanilkovy-cukr.png",
}
RECIPE_IMG = {
    "sisky-s-makem-recept": "sisky-s-makem.png",
    "hruskovy-kolac-s-vanilkovym-pudinkem-recept": "hruskovy-kolac.png",
    "strapacky-se-zelim-a-slaninou-recept": "strapacky.jpg",
    "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": "bebe-rezy.gif",
    "slehackova-rolada-recept": "slehackova-rolada.gif",
    "domaci-pernik-recept-podle-jirina-juzlova": "domaci-pernik.png",
    "bramborovo-tvarohove-knedliky-s-jahodami": "bramborovo-tvarohove-knedliky.jpg",
}
PRICE_ROWS = [  # (product key, package, price CZK)
    ("bramborove_knedliky", "5 kg", "165 Kč"),
    ("chlupate_knedliky", "5 kg", "185 Kč"),
    ("vanilkovy_pudink", "1 kg / 400 g", "34 Kč / 17 Kč"),
    (None, "1 kg / 400 g", "44 Kč / 22 Kč"),  # kakaovy puding row, name via lang
    ("kakao_holandskeho_typu", "500 g", "100 Kč"),
    ("vanilkovy_cukr", "1 kg", "38 Kč"),
]
KAKAOVY_PUDING_NAME = {
    "cs": "Kakaový puding", "en": "Cocoa pudding", "de": "Kakaopudding", "sk": "Kakaový puding",
}
LEGACY_REDIRECTS = {
    "kakao": "kakao-holandskeho-typu", "kakaovy_puding": "vanilkovy_pudink",
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
    return data


def esc(s):
    return H.escape(str(s), quote=True)


def lang_prefix(lang):
    return "" if lang == "cs" else f"{lang}/"


def url_for(lang, path):
    """Absolute URL for a page path ('' = home, 'kontakt/' etc.)."""
    return f"{BASE}/{lang_prefix(lang)}{path}"


def rel(depth):
    return "../" * depth


def hreflangs(path):
    out = []
    for lg in LANGS:
        out.append(f'<link rel="alternate" hreflang="{lg}" href="{url_for(lg, path)}">')
    out.append(f'<link rel="alternate" hreflang="x-default" href="{url_for("cs", path)}">')
    return "\n".join(out)


def nav(L, depth, active, path):
    p = rel(depth)
    ui = L["ui"]
    lg = L["code"]
    home = p + ("" if lg == "cs" else "")  # within language tree, p already points at language root
    def a(slug, label, key):
        cls = ' class="active"' if active == key else ""
        return f'<a href="{p}{slug}"{cls}>{esc(label)}</a>'
    prods = "".join(
        f'<a href="{p}{PRODUCT_SLUGS[k]}/">{esc(L["products"][k]["name"])}</a>'
        for k in PRODUCT_SLUGS)
    langsel = ""
    for other in LANGS:
        cls = ' class="on"' if other == lg else ""
        langsel += f'<a{cls} lang="{other}" hreflang="{other}" href="{url_for(other, path)}">{other.upper()}</a>'
    return f"""<div class="bar">
  <a class="brand" href="{p if p else './'}"><span class="name">Jůzlová.cz</span><span class="tag">{esc(ui["brand_tag"])}</span></a>
  <nav class="main" aria-label="hlavní navigace">
    {a('', ui['nav_home'], 'home')}
    {a('kdo_jsme/', ui['nav_about'], 'kdo_jsme')}
    {a('kde-nas-najdete/', ui['nav_delivery'], 'kde_nas_najdete')}
    <span class="navgroup"><button type="button">{esc(ui['nav_products'])} ▾</button><span class="drop">{prods}</span></span>
    {a('ceny/', ui['nav_prices'], 'ceny')}
    {a('recepty/', ui['nav_recipes'], 'recepty')}
    {a('kontakt/', ui['nav_contact'], 'kontakt')}
    <span class="langs" aria-label="{esc(ui['lang_label'])}">{langsel}</span>
  </nav>
</div>"""


def footer(L, depth):
    p = rel(depth)
    ui = L["ui"]
    prods = "".join(
        f'<a href="{p}{PRODUCT_SLUGS[k]}/">{esc(L["products"][k]["name"])}</a>'
        for k in PRODUCT_SLUGS)
    recs = "".join(
        f'<a href="{p}{slug}/">{esc(L["recipes"].get(slug, {}).get("name", slug))}</a>'
        for slug in RECIPE_SLUGS[:5])
    return f"""<footer class="site">
  <div class="wrap">
    <div class="cols">
      <div><h4>Jůzlová</h4>
        <p style="font-size:.92rem;margin:.2rem 0 1rem">{esc(ui['footer_note'])}</p>
        <p style="font-size:.88rem">{esc(ui['footer_addr'])}<br>+420 728 466 141 · +420 607 629 931<br><a href="mailto:juzlj@seznam.cz" style="display:inline">juzlj@seznam.cz</a></p>
      </div>
      <div><h4>{esc(ui['footer_products'])}</h4>{prods}</div>
      <div><h4>{esc(ui['footer_recipes'])}</h4>{recs}</div>
      <div><h4>{esc(ui['footer_company'])}</h4>
        <a href="{p}kdo_jsme/">{esc(ui['nav_about'])}</a>
        <a href="{p}kde-nas-najdete/">{esc(ui['nav_delivery'])}</a>
        <a href="{p}ceny/">{esc(ui['nav_prices'])}</a>
        <a href="{p}kontakt/">{esc(ui['nav_contact'])}</a>
      </div>
    </div>
    <div class="fine"><span>© 2004–2026 Jůzlová s.r.o. · IČO 45900124</span><span>{esc(ui['open_hours'])}</span></div>
  </div>
</footer>"""


def org_jsonld():
    return {
        "@context": "https://schema.org", "@type": ["Organization", "LocalBusiness"],
        "@id": BASE + "/#org", "name": "Jůzlová",
        "url": BASE + "/", "logo": BASE + "/img/logo.png",
        "foundingDate": "2004", "email": "juzlj@seznam.cz",
        "telephone": "+420728466141",
        "address": {"@type": "PostalAddress", "streetAddress": "Kochánov 40",
                    "postalCode": "582 53", "addressRegion": "Vysočina",
                    "addressCountry": "CZ"},
        "areaServed": ["Havlíčkův Brod", "Humpolec", "Světlá nad Sázavou", "Jihlava",
                       "Czech Republic"],
        "openingHours": "Mo-Sa 08:00-19:00",
        "description": "Rodinná výroba potravinářských směsí od roku 2004: knedlíky v prášku, pudingy bez lepku, vanilínový cukr, kakao holandského typu.",
    }


def shell(L, *, title, desc, path, depth, active, body, jsonld=None, og_img=None):
    lg = L["code"]
    canonical = url_for(lg, path)
    blocks = [org_jsonld()] + (jsonld or [])
    ld = "\n".join(
        f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>'
        for b in blocks)
    ogimg = og_img or f"{BASE}/img/hero.jpg"
    p = rel(depth)
    return f"""<!doctype html>
<html lang="{lg}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
{hreflangs(path)}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Jůzlová.cz">
<meta property="og:locale" content="{L['locale']}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ogimg}">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="{p}assets/site.css">
<link rel="icon" href="{p}img/favicon.png" type="image/png">
{ld}
</head>
<body>
<header class="site">
  <div class="wrap">{nav(L, depth, active, path)}</div>
</header>
{body}
{footer(L, depth)}
<script src="{p}assets/site.js" defer></script>
</body>
</html>
"""


def render_body(L, body_spec, depth):
    p = rel(depth)
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
            out.append(f"""<div class="factbox"><dl>
<dt>Jiřina Jůzlová</dt><dd>Kochánov 40, 582 53 · <a href="tel:+420728466141">+420 728 466 141</a> · <a href="mailto:juzlj@seznam.cz">juzlj@seznam.cz</a></dd>
<dt>Jiří Jůzl</dt><dd>Kochánov 40, 582 53 · <a href="tel:+420607629931">+420 607 629 931</a> · <a href="mailto:juzlj@seznam.cz">juzlj@seznam.cz</a></dd>
</dl></div>""")
        elif kind == "pricetable":
            ui = L["ui"]
            rows = ""
            for key, pack, price in PRICE_ROWS:
                if key is None:
                    name = KAKAOVY_PUDING_NAME[L["code"]]
                    link = esc(name)
                else:
                    name = L["products"][key]["name"]
                    link = f'<a href="{p}{PRODUCT_SLUGS[key]}/">{esc(name)}</a>'
                rows += f"<tr><td>{link}</td><td>{esc(pack)}</td><td><strong>{esc(price)}</strong></td></tr>"
            out.append(f"""<table class="tbl"><thead><tr><th>{esc(ui['nav_products'])}</th><th>{esc(ui['package_label'])}</th><th>{esc(ui['price_label'])}</th></tr></thead><tbody>{rows}</tbody></table>""")
    return "\n".join(out)


def faq_html(faq):
    if not faq:
        return ""
    items = "".join(
        f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faq)
    return f'<div class="faq">{items}</div>'


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
        return rel(depth) + "img/" + name
    return None


def build_home(L):
    lg = L["code"]
    depth = 0 if lg == "cs" else 1
    ui = L["ui"]
    p = rel(depth)
    hero_img = img_or_none(depth, "hero.jpg")
    hero_media = (f'<img src="{hero_img}" alt="" fetchpriority="high">' if hero_img
                  else '<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 30% 20%, #3a2c1c, #1d1712)"></div>')
    prod_cards = ""
    for k in PRODUCT_SLUGS:
        pr = L["products"][k]
        im = img_or_none(depth, PRODUCT_IMG.get(k))
        imtag = f'<img class="thumb" src="{im}" alt="{esc(pr["name"])}" loading="lazy">' if im else ""
        prod_cards += f"""<li class="card rv">{imtag}<div class="pad">
<h3><a href="{p}{PRODUCT_SLUGS[k]}/">{esc(pr['name'])}</a></h3>
<p>{esc(pr['short'])}</p><p class="price">{esc(pr['price'])}</p></div></li>"""
    rec_cards = ""
    for slug in RECIPE_SLUGS:
        r = L["recipes"].get(slug)
        if not r:
            continue
        im = img_or_none(depth, RECIPE_IMG.get(slug))
        imtag = f'<img class="thumb" src="{im}" alt="{esc(r["name"])}" loading="lazy">' if im else ""
        rec_cards += f"""<li class="card rv">{imtag}<div class="pad">
<h3><a href="{p}{slug}/">{esc(r['name'])}</a></h3><p>{esc(r.get('teaser',''))}</p></div></li>"""
    body = f"""<div class="hero"><div class="media">{hero_media}</div>
  <div class="inner">
    <div class="est">{esc(ui['est'])}</div>
    <h1>{esc(ui['hero_h1'])}</h1>
    <p class="lead">{esc(ui['hero_lead'])}</p>
    <a class="btn gold" href="{p}kontakt/">{esc(ui['hero_cta'])}</a><a class="btn ghost" href="#produkty">{esc(ui['hero_cta2'])}</a>
  </div></div>
<section class="band" id="produkty"><div class="wrap">
  <p class="kicker">{esc(ui['sec_products_kicker'])}</p>
  <h2 class="sec">{esc(ui['sec_products'])}</h2>
  <p class="lead">{esc(ui['sec_products_lead'])}</p>
  <ul class="grid c3" style="list-style:none;padding:0">{prod_cards}</ul>
  <p><a href="{p}ceny/">{esc(ui['full_price_list'])} →</a></p>
</div></section>
<section class="band cream"><div class="wrap">
  <p class="kicker">{esc(ui['sec_why_kicker'])}</p>
  <h2 class="sec">{esc(ui['sec_why'])}</h2>
  <div class="grid c3">
    <div class="rv"><h3>{esc(ui['why_1_h'])}</h3><p>{esc(ui['why_1_p'])}</p></div>
    <div class="rv"><h3>{esc(ui['why_2_h'])}</h3><p>{esc(ui['why_2_p'])}</p></div>
    <div class="rv"><h3>{esc(ui['why_3_h'])}</h3><p>{esc(ui['why_3_p'])}</p></div>
  </div>
</div></section>
<section class="band"><div class="wrap">
  <p class="kicker">{esc(ui['sec_recipes_kicker'])}</p>
  <h2 class="sec">{esc(ui['sec_recipes'])}</h2>
  <p class="lead">{esc(ui['sec_recipes_lead'])}</p>
  <ul class="grid c3" style="list-style:none;padding:0">{rec_cards}</ul>
  <p><a href="{p}recepty/">{esc(ui['all_recipes'])} →</a></p>
</div></section>
<section class="band cream center"><div class="wrap">
  <h2 class="sec" style="display:inline-block">{esc(ui['cta_sample_h'])}</h2>
  <p class="lead" style="max-width:560px;margin:.6rem auto 1.4rem">{esc(ui['cta_sample_p'])}</p>
  <a class="btn gold" href="{p}kontakt/">{esc(ui['cta_sample_btn'])}</a>
</div></section>"""
    html_out = shell(L, title=L["meta"]["home_title"], desc=L["meta"]["home_desc"],
                     path="", depth=depth, active="home", body=body)
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
        w = img_or_none(depth, "workshop.jpg")
        if w:
            fig = f'<figure><img src="{w}" alt="Jůzlová — dílna" loading="lazy"></figure>'
    body = f"""<main class="wrap"><article class="page">
<nav class="breadcrumb"><a href="{rel(depth)}">{esc(L['ui']['breadcrumb_home'])}</a> › {esc(pg['h1'])}</nav>
<h1>{esc(pg['h1'])}</h1>
<p class="sub">{esc(pg['sub'])}</p>
{fig}
{render_body(L, pg['body'], depth)}
</article></main>"""
    html_out = shell(L, title=pg["title"], desc=pg["desc"], path=path, depth=depth,
                     active=key, body=body, jsonld=[breadcrumb_jsonld(L, crumbs)])
    write(([lg] if lg != "cs" else []) + [slug, "index.html"], html_out)


def build_product(L, key):
    lg = L["code"]
    slug = PRODUCT_SLUGS[key]
    depth = (0 if lg == "cs" else 1) + 1
    pr = L["products"][key]
    path = f"{slug}/"
    im = img_or_none(depth, PRODUCT_IMG.get(key))
    figure = (f'<figure><img src="{im}" alt="{esc(pr["name"])}"></figure>' if im else "")
    price_num = re.search(r"(\d+)\s*(?:Kč|CZK)", pr["price"])
    product_ld = {
        "@context": "https://schema.org", "@type": "Product",
        "name": pr["name"], "description": pr["desc"],
        "brand": {"@type": "Brand", "name": "Jůzlová"},
        "url": url_for(lg, path),
        **({"image": f"{BASE}/img/{PRODUCT_IMG[key]}"} if PRODUCT_IMG.get(key) else {}),
        "offers": {"@type": "Offer", "priceCurrency": "CZK",
                   "price": price_num.group(1) if price_num else "0",
                   "availability": "https://schema.org/InStock",
                   "url": url_for(lg, path)},
    }
    lds = [product_ld, breadcrumb_jsonld(L, [
        (L["ui"]["breadcrumb_home"], url_for(lg, "")),
        (pr["name"], url_for(lg, path))])]
    if pr.get("faq"):
        lds.append(faq_jsonld(pr["faq"]))
    body = f"""<main class="wrap"><article class="page">
<nav class="breadcrumb"><a href="{rel(depth)}">{esc(L['ui']['breadcrumb_home'])}</a> › {esc(pr['name'])}</nav>
<h1>{esc(pr['name'])}</h1>
<p class="sub">{esc(pr['short'])}</p>
<div class="factbox"><dl><dt>{esc(L['ui']['price_label'])}</dt><dd><strong>{esc(pr['price'])}</strong></dd>
<dt>{esc(L['ui']['order_info'])}</dt><dd><a href="{rel(depth)}kontakt/">{esc(L['ui']['nav_contact'])}</a> · +420 728 466 141 · juzlj@seznam.cz</dd></dl></div>
{figure}
{render_body(L, pr['body'], depth)}
{faq_html(pr.get('faq'))}
<p style="margin-top:2rem"><a class="btn gold" href="{rel(depth)}kontakt/">{esc(L['ui']['cta_sample_btn'])}</a></p>
</article></main>"""
    html_out = shell(L, title=pr["title"], desc=pr["desc"], path=path, depth=depth,
                     active=None, body=body, jsonld=lds,
                     og_img=f"{BASE}/img/{PRODUCT_IMG[key]}" if PRODUCT_IMG.get(key) else None)
    write(([lg] if lg != "cs" else []) + [slug, "index.html"], html_out)


def build_recipes_index(L):
    lg = L["code"]
    depth = (0 if lg == "cs" else 1) + 1
    p = rel(depth)
    cards = ""
    for slug in RECIPE_SLUGS:
        r = L["recipes"].get(slug)
        if not r:
            continue
        im = img_or_none(depth, RECIPE_IMG.get(slug))
        imtag = f'<img class="thumb" src="{im}" alt="{esc(r["name"])}" loading="lazy">' if im else ""
        cards += f"""<li class="card rv">{imtag}<div class="pad"><h3><a href="{p}{slug}/">{esc(r['name'])}</a></h3><p>{esc(r.get('teaser',''))}</p></div></li>"""
    ui = L["ui"]
    body = f"""<main class="wrap"><article class="page" style="max-width:none">
<nav class="breadcrumb"><a href="{p}">{esc(ui['breadcrumb_home'])}</a> › {esc(ui['nav_recipes'])}</nav>
<h1>{esc(ui['nav_recipes'])}</h1>
<p class="sub">{esc(L['recipes_intro'])}</p>
<ul class="grid c3" style="list-style:none;padding:0">{cards}</ul>
</article></main>"""
    title = {"cs": "Recepty z našich směsí — knedlíky, dezerty, pudingy",
             "en": "Recipes from our mixes — dumplings, desserts, puddings",
             "de": "Rezepte aus unseren Mischungen — Knödel, Desserts, Pudding",
             "sk": "Recepty z našich zmesí — knedle, dezerty, pudingy"}[lg]
    html_out = shell(L, title=title, desc=L["recipes_intro"], path="recepty/",
                     depth=depth, active="recepty", body=body)
    write(([lg] if lg != "cs" else []) + ["recepty", "index.html"], html_out)


def build_recipe(L, slug):
    lg = L["code"]
    r = L["recipes"].get(slug)
    if not r:
        return
    depth = (0 if lg == "cs" else 1) + 1
    p = rel(depth)
    im = img_or_none(depth, RECIPE_IMG.get(slug))
    figure = f'<figure><img src="{im}" alt="{esc(r["name"])}"></figure>' if im else ""
    ing = "".join(f"<li>{esc(x)}</li>" for x in r.get("ingredients", []))
    steps = "".join(f"<li>{esc(x)}</li>" for x in r.get("steps", []))
    prod_key = r.get("product")
    prod_link = ""
    if prod_key and prod_key in L["products"]:
        prod_link = (f'<div class="factbox"><dl><dt>{esc(L["ui"]["uses_product"])}</dt>'
                     f'<dd><a href="{p}{PRODUCT_SLUGS[prod_key]}/">'
                     f'{esc(L["products"][prod_key]["name"])}</a></dd></dl></div>')
    recipe_ld = {
        "@context": "https://schema.org", "@type": "Recipe",
        "name": r["name"], "description": r.get("teaser", ""),
        "recipeCuisine": "Czech",
        "author": {"@type": "Organization", "name": "Jůzlová"},
        "url": url_for(lg, f"{slug}/"),
        **({"image": f"{BASE}/img/{RECIPE_IMG[slug]}"} if RECIPE_IMG.get(slug) else {}),
        **({"recipeIngredient": r["ingredients"]} if r.get("ingredients") else {}),
        **({"recipeInstructions": [{"@type": "HowToStep", "text": s} for s in r["steps"]]}
           if r.get("steps") else {}),
    }
    ing_h = {"cs": "Suroviny", "en": "Ingredients", "de": "Zutaten", "sk": "Suroviny"}[lg]
    steps_h = {"cs": "Postup", "en": "Method", "de": "Zubereitung", "sk": "Postup"}[lg]
    ing_block = f"<h2>{ing_h}</h2><ul>{ing}</ul>" if ing else ""
    steps_block = f"<h2>{steps_h}</h2><ol>{steps}</ol>" if steps else ""
    extra = "".join(f"<p>{esc(x)}</p>" for x in r.get("notes", []))
    body = f"""<main class="wrap"><article class="page">
<nav class="breadcrumb"><a href="{p}">{esc(L['ui']['breadcrumb_home'])}</a> › <a href="{p}recepty/">{esc(L['ui']['nav_recipes'])}</a> › {esc(r['name'])}</nav>
<h1>{esc(r['name'])}</h1>
<p class="sub">{esc(r.get('teaser',''))}</p>
{prod_link}
{figure}
{ing_block}
{steps_block}
{extra}
</article></main>"""
    html_out = shell(L, title=r.get("title", r["name"]), desc=r.get("desc", r.get("teaser", "")),
                     path=f"{slug}/", depth=depth, active="recepty", body=body,
                     jsonld=[recipe_ld, breadcrumb_jsonld(L, [
                         (L["ui"]["breadcrumb_home"], url_for(lg, "")),
                         (L["ui"]["nav_recipes"], url_for(lg, "recepty/")),
                         (r["name"], url_for(lg, f"{slug}/"))])],
                     og_img=f"{BASE}/img/{RECIPE_IMG[slug]}" if RECIPE_IMG.get(slug) else None)
    write(([lg] if lg != "cs" else []) + [slug, "index.html"], html_out)


def build_redirects():
    for old, new in LEGACY_REDIRECTS.items():
        target = f"{BASE}/{new}/"
        write([old, "index.html"], f"""<!doctype html>
<html lang="cs"><head><meta charset="utf-8"><title>Jůzlová.cz</title>
<link rel="canonical" href="{target}">
<meta http-equiv="refresh" content="0;url={target}">
</head><body><p><a href="{target}">→ {target}</a></p></body></html>
""")


def all_paths(langs_data):
    paths = [""]
    paths += [f"{slug}/" for slug in PAGE_SLUGS.values()]
    paths += [f"{slug}/" for slug in PRODUCT_SLUGS.values()]
    paths.append("recepty/")
    cs = langs_data["cs"]
    paths += [f"{slug}/" for slug in RECIPE_SLUGS if slug in cs["recipes"]]
    return paths


def build_sitemap(langs_data):
    ns = ('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
          'xmlns:xhtml="http://www.w3.org/1999/xhtml">')
    entries = []
    for path in all_paths(langs_data):
        for lg in LANGS:
            alts = "".join(
                f'<xhtml:link rel="alternate" hreflang="{o}" href="{url_for(o, path)}"/>'
                for o in LANGS)
            alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{url_for("cs", path)}"/>'
            entries.append(
                f"<url><loc>{url_for(lg, path)}</loc>{alts}"
                f"<lastmod>{TODAY}</lastmod></url>")
    write(["sitemap.xml"],
          '<?xml version="1.0" encoding="UTF-8"?>\n' + ns + "\n" + "\n".join(entries) + "\n</urlset>\n")


def build_robots():
    write(["robots.txt"], f"""User-agent: *
Allow: /
Disallow: /archive/
Disallow: /status.html

Sitemap: {BASE}/sitemap.xml
""")


def build_llms(langs_data):
    cs = langs_data["cs"]
    prods = "\n".join(
        f"- [{cs['products'][k]['name']}]({url_for('cs', PRODUCT_SLUGS[k] + '/')}): "
        f"{cs['products'][k]['short']} Cena: {cs['products'][k]['price']}."
        for k in PRODUCT_SLUGS)
    recs = "\n".join(
        f"- [{cs['recipes'][s]['name']}]({url_for('cs', s + '/')}): {cs['recipes'][s].get('teaser','')}"
        for s in RECIPE_SLUGS if s in cs["recipes"])
    write(["llms.txt"], f"""# Jůzlová.cz

> Jůzlová je rodinná česká výroba potravinářských směsí (od roku 2004, Kochánov 40, Vysočina): bramborové a chlupaté knedlíky v prášku, vanilkový a kakaový puding bez lepku, vanilínový cukr a kakao holandského typu. Prodej přímo z dílny, vzorky zdarma, rozvoz na Vysočině.

Fakta v tomto souboru odpovídají obsahu webu. Podrobnější strojově čitelný souhrn: [llms-full.txt]({BASE}/llms-full.txt)

## Hlavní stránky
- [Úvod]({url_for('cs','')}): co vyrábíme a pro koho
- [Kdo jsme]({url_for('cs','kdo_jsme/')}): rodinná dílna od roku 2004
- [Dodání zboží]({url_for('cs','kde-nas-najdete/')}): odběr Kochánov/Humpolec, rozvoz, dopravce
- [Ceník]({url_for('cs','ceny/')}): aktuální ceny všech směsí
- [Kontakt]({url_for('cs','kontakt/')}): telefony, e-mail, adresa

## Produkty
{prods}

## Recepty
{recs}

## Jazykové verze
- Čeština (výchozí): {url_for('cs','')}
- English: {url_for('en','')}
- Deutsch: {url_for('de','')}
- Slovenčina: {url_for('sk','')}

## Aktualizace
- Naposledy aktualizováno: {TODAY}
""")
    # llms-full.txt: inline the key content of every CS page + EN summary
    full = [f"# Jůzlová.cz — full reference for AI assistants\n"]
    full.append("Jůzlová s.r.o., IČO 45900124, Kochánov 40, 582 53, Vysočina, Czech Republic. "
                "Family production of food mixes since 2004. Phones: +420 728 466 141 (Jiřina Jůzlová), "
                "+420 607 629 931 (Jiří Jůzl). E-mail: juzlj@seznam.cz. "
                "Open daily 8:00–19:00 by phone arrangement. Free samples on request. "
                "Pick-up: Kochánov or Humpolec (free). Free local delivery: Havlíčkův Brod, "
                "Světlá nad Sázavou, Jihlava and surroundings.\n")
    full.append("## Products (name | package | price | key facts)\n")
    for key, pack, price in PRICE_ROWS:
        if key is None:
            full.append(f"- Kakaový puding | {pack} | {price} | cocoa pudding with Dutch-process cocoa, gluten-free corn starch base")
        else:
            pr = cs["products"][key]
            en = langs_data["en"]["products"][key]
            full.append(f"- {pr['name']} (EN: {en['name']}) | {pack} | {price} | {en['short']}")
    full.append("\n## Pages (Czech canonical text)\n")
    for key in PAGE_SLUGS:
        pg = cs["pages"][key]
        full.append(f"### {pg['h1']} — {url_for('cs', PAGE_SLUGS[key] + '/')}")
        for kind, val in pg["body"]:
            if kind == "p":
                full.append(val)
            elif kind in ("h2", "h3"):
                full.append(f"**{val}**")
            elif kind in ("ul", "ol"):
                full.extend(f"- {x}" for x in val)
        full.append("")
    full.append("## Recipes\n")
    for s in RECIPE_SLUGS:
        r = cs["recipes"].get(s)
        if not r:
            continue
        full.append(f"### {r['name']} — {url_for('cs', s + '/')}")
        if r.get("teaser"):
            full.append(r["teaser"])
        if r.get("ingredients"):
            full.append("Suroviny: " + "; ".join(r["ingredients"]))
        if r.get("steps"):
            full.extend(f"{i+1}. {x}" for i, x in enumerate(r["steps"]))
        full.append("")
    full.append(f"Last updated: {TODAY}\n")
    write(["llms-full.txt"], "\n".join(full))


def copy_images():
    src = ROOT / "archive" / "images"
    dst = ROOT / "img"
    dst.mkdir(exist_ok=True)
    if src.exists():
        for a_name, pub in IMAGE_MAP.items():
            f = src / a_name
            if f.exists():
                shutil.copyfile(f, dst / pub)
    # fallbacks for recipe thumbnails whose originals were never captured
    for want, alt in [("sisky-s-makem.png", "sisky-s-makem-alt.png"),
                      ("strapacky.jpg", "strapacky-alt.png")]:
        if not (dst / want).exists() and (dst / alt).exists():
            shutil.copyfile(dst / alt, dst / want)
    logo = dst / "logo.png"
    fav = dst / "favicon.png"
    if logo.exists() and not fav.exists():
        shutil.copyfile(logo, fav)


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
        for slug in RECIPE_SLUGS:
            build_recipe(L, slug)
    build_redirects()
    build_sitemap(langs_data)
    build_robots()
    build_llms(langs_data)
    print("built:", ", ".join(LANGS))


if __name__ == "__main__":
    main()
