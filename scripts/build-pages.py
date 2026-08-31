#!/usr/bin/env python3
"""Generate public HTML pages for juzlova.cz with shared chrome."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PRODUCTS = [
    ("/chlupate-knedliky/", "Chlupaté knedlíky", "5 kg / 185 Kč", "/assets/img/Chlupate-knedliky-300x225.png", "Pytle směsi na chlupaté knedlíky"),
    ("/kakao-holandskeho-typu/", "Kakao holandského typu", "500 g / 100 Kč", "/assets/img/HERO_Hot-Cocoa-300x228.jpg", "Kakao holandského typu"),
    ("/vanilkovy-cukr/", "Vanilínový cukr", "1 kg / 38 Kč", "/assets/img/Vanilkovy-cukr-juzlova-300x103.png", "Vanilínový cukr Jůzlová"),
    ("/vanilkovy_pudink/", "Vanilkový puding bez lepku", "1 kg / 34 Kč, 400 g / 17 Kč", "/assets/img/Vanilkovy-puding-juzlova-300x225.png", "Vanilkový puding Jůzlová"),
    ("/bramborove_knedliky/", "Bramborové knedlíky", "5 kg / 165 Kč", "/assets/img/Bramborove-knedliky-300x225.png", "Pytle směsi na bramborové knedlíky"),
]

RECIPES = [
    ("/sisky-s-makem-recept/", "Šišky s mákem", "/assets/img/Pečené-šišky-s-mákem-recept-300x206.png", "Pečené šišky s mákem"),
    ("/hruskovy-kolac-s-vanilkovym-pudinkem-recept/", "Hruškový koláč s vanilkovým pudinkem", None, None),
    ("/strapacky-se-zelim-a-slaninou-recept/", "Strapačky se zelím a slaninou", "/assets/img/Strapacky-se-zelim-a-slaninou-recept-juzlova.jpg", "Strapačky se zelím a slaninou"),
    ("/podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem/", "Bebe řezy s čokoládovým pudingem", "/assets/img/Bebe-rezy-s-cokoladovym-pudingem-300x231-300x206.gif", "Bebe řezy s čokoládovým pudingem"),
    ("/slehackova-rolada-recept/", "Šlehačková roláda", None, None),
    ("/domaci-pernik-recept-podle-jirina-juzlova/", "Domácí perník", None, None),
    ("/bramborovo-tvarohove-knedliky-s-jahodami/", "Bramborovo-tvarohové knedlíky s jahodami", None, None),
]


def head(title, desc, og="/assets/img/Kochanov-provozovna-firmy.jpg"):
    return f"""<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:image" content="{og}">
<link rel="stylesheet" href="/assets/style.css">
<link rel="icon" href="/assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/img/favicon-192x192.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
</head>
<body>
"""


def nav(active):
    def item(href, label, key):
        cls = ' class="is-active"' if active == key else ""
        return f'<a href="{href}"{cls}>{label}</a>'

    prod_links = "".join(f'<a href="{h}">{n}</a>' for h, n, *_ in PRODUCTS)
    rec_links = "".join(f'<a href="{h}">{n}</a>' for h, n, *_ in RECIPES)
    return f"""<a class="skip" href="#obsah">Přeskočit na obsah</a>
<header class="site">
  <div class="wrap bar">
    <a class="brand" href="/">
      <picture>
        <source srcset="/assets/img/juzlova-logo-black-2017.png" media="(prefers-color-scheme: light)">
        <img class="brand-logo" src="/assets/img/juzlova-logo-untitled-2017.png" alt="" width="220" height="72">
      </picture>
      <span class="name">Jůzlová</span>
      <span class="place">Kochánov</span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="hlavni-menu">Menu</button>
    <nav id="hlavni-menu" class="main" aria-label="Hlavní menu">
      {item("/", "Úvod", "home")}
      {item("/kdo_jsme/", "Kdo jsme", "about")}
      <details>
        <summary>Produkty</summary>
        <div class="drop">{prod_links}</div>
      </details>
      <details>
        <summary>Recepty</summary>
        <div class="drop">{rec_links}</div>
      </details>
      {item("/ceny/", "Ceny", "prices")}
      {item("/kde-nas-najdete/", "Dodání zboží", "delivery")}
      {item("/kontakt/", "Kontakt", "contact")}
    </nav>
  </div>
</header>
"""


def foot():
    return """<footer class="site">
  <div class="wrap foot">
    <div>
      <p><strong>Jůzlová</strong><br>Kochánov 40, 582 53<br>Jůzlová s.r.o., IČO 45900124</p>
      <p><a href="tel:+420728466141">+420 728 466 141</a><br>
      <a href="mailto:juzlj@seznam.cz">juzlj@seznam.cz</a></p>
    </div>
    <nav aria-label="Patička">
      <a href="/kdo_jsme/">Kdo jsme</a>
      <a href="/recepty/">Recepty</a>
      <a href="/ceny/">Ceny</a>
      <a href="/kde-nas-najdete/">Dodání zboží</a>
    </nav>
    <p class="legal">© 2004-2026 Jůzlová. Otevřeno denně po telefonické domluvě, 8:00-19:00.</p>
  </div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""


DESC = "Jůzlová, potravinářské směsi z Vysočiny. Bramborové a chlupaté knedlíky, pudingy, vanilínový cukr, kakao."


def write(rel, html):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", rel)


def homepage():
    plist = "".join(
        f'<li><a href="{h}"><img src="{img}" alt="{alt}" width="300" height="225" loading="lazy"><strong>{n}</strong><span>{p}</span></a></li>'
        for h, n, p, img, alt in PRODUCTS
        if h != "/bramborove_knedliky/"
    )
    mosaic = []
    for href, name, img, alt in RECIPES:
        if img:
            media = f'<img src="{img}" alt="{alt}" width="300" height="206" loading="lazy">'
        else:
            media = '<div class="ph">Fotografie se z archivu nepodařilo obnovit</div>'
        mosaic.append(f'<a class="tile" href="{href}">{media}<h3>{name}</h3></a>')
    body = f"""{head("Jůzlová, potravinářské směsi z Vysočiny", DESC, "/assets/img/juzlova-background-image.jpg")}
{nav("home")}
<main id="obsah">
  <section class="hero wrap">
    <div class="hero-copy">
      <h1>Poctivé potravinářské směsi z&nbsp;Vysočiny</h1>
      <p>Od roku 2004 vyrábíme v rodinné dílně v Kochánově bramborová těsta, knedlíky v prášku, pudingy, vanilínový cukr a kakao.</p>
      <div class="actions"><a class="btn" href="/kontakt/">Ozvěte se</a></div>
    </div>
    <figure class="hero-photo">
      <img src="/assets/img/juzlova-background-image.jpg" alt="Kochánov z výšky, sídlo dílny Jůzlová" width="1600" height="900">
      <figcaption>Kochánov, Vysočina</figcaption>
    </figure>
  </section>

  <section class="section wrap">
    <h2>Bramborové knedlíky v prášku</h2>
    <article class="feature">
      <img src="/assets/img/Bramborove-knedliky-300x225.png" alt="Pytle směsi na bramborové knedlíky" width="600" height="450">
      <div class="copy">
        <h3>Náš nejvyhledávanější výrobek</h3>
        <p class="price">5 kg / 165 Kč</p>
        <p>Mouka KLASA z mlýna v Havlíčkově Brodě a sušené bramborové vločky. Na knedlíky k masu, šišky, krokety i gnocchi.</p>
        <a class="btn btn-ghost" href="/bramborove_knedliky/">Více o směsi</a>
      </div>
    </article>
    <ul class="plist">{plist}</ul>
  </section>

  <section class="placeband">
    <img src="/assets/img/Kochanov-provozovna-firmy.jpg" alt="Provozovna Jůzlová v Kochánově" width="800" height="533">
    <div class="copy">
      <h2>Rodinná dílna v Kochánově</h2>
      <p class="lede">Dodáváme do domácností, restaurací, jídelen a cukráren. Vyzvednutí u nás, v Humpolci, nebo závoz po Vysočině.</p>
      <a class="btn btn-ghost" href="/kdo_jsme/">Kdo jsme</a>
    </div>
  </section>

  <section class="section wrap">
    <h2>Recepty z našich směsí</h2>
    <div class="mosaic">{''.join(mosaic)}</div>
  </section>

  <figure class="banner-collage wrap">
    <img src="/assets/img/Juzlova-homepage.png" alt="Pokrmy připravené z výrobků Jůzlová" width="1349" height="450" loading="lazy">
  </figure>

  <section class="section wrap">
    <h2>Jak ke zboží</h2>
    <div class="deliver">
      <article>
        <h3>Kochánov a Humpolec</h3>
        <p>Vyzvednutí na provozovně zdarma, po předchozí domluvě.</p>
      </article>
      <article>
        <h3>Závoz po Vysočině</h3>
        <p>Havlíčkův Brod, Světlá nad Sázavou, Jihlava a okolí.</p>
      </article>
      <article>
        <h3>Dopravce dle vás</h3>
        <p>Poštovné podle ceníku zvoleného dopravce.</p>
      </article>
    </div>
  </section>

  <section class="cta-band">
    <div class="wrap">
      <h2>Máte zájem ochutnat?</h2>
      <p>Rádi vám nabídneme vzorek zdarma. Stačí zavolat nebo napsat.</p>
      <a class="btn" href="/kontakt/">Ozvěte se</a>
    </div>
  </section>
</main>
{foot()}"""
    write("index.html", body)


def page(rel, title, active, inner, og="/assets/img/Kochanov-40-dum.jpg"):
    html = f"""{head(title + " - Jůzlová.cz", DESC, og)}
{nav(active)}
<main id="obsah" class="wrap">
<article class="page">
<a class="crumb" href="/">Zpět na úvod</a>
{inner}
</article>
</main>
{foot()}"""
    write(rel, html)


def missing(text="Fotografie k tomuto receptu se z veřejného archivu nepodařilo obnovit."):
    return f'<div class="missing-photo" role="img" aria-label="Chybějící fotografie"><p>{text}</p></div>'


def main():
    homepage()

    page(
        "kdo_jsme/index.html",
        "Kdo jsme",
        "about",
        """<h1>Kdo jsme</h1>
<img class="portrait" src="/assets/img/Jirina-Juzlova-150x150.png" alt="Jiřina Jůzlová" width="150" height="150">
<p>Výrobu potravinářských směsí jsme v malé dílně v Kochánově zahájili v roce 2004. Během let jsme citlivě upravovali receptury a vybírali nejkvalitnější dodavatele surovin, až jsme dosáhli jedinečné kombinace chuti a kvality, kvůli které nás vyhledávají zákazníci v Čechách i na Moravě.</p>
<p>Dnes jako obchodní firma „Jůzlová“ dodáváme nejen do domácností, ale do řady restaurací, jídelen a cukráren. Naši zákazníci oceňují především tradiční domácí chuť a zároveň rychlost, se kterou je možné z našich instantních výrobků připravit výborné přílohy a dezerty.</p>
<ul class="place-photos">
<li><img src="/assets/img/Kochanov-40-dum.jpg" alt="Dům Kochánov 40" width="800" height="533" loading="lazy"></li>
<li><img src="/assets/img/Kochanov-provozovna-firmy.jpg" alt="Provozovna Jůzlová, Kochánov" width="800" height="533" loading="lazy"></li>
</ul>
<p>Naším nejvyhledávanějším výrobkem je bramborové těsto v prášku. Při jeho výrobě používáme kvalitní a značkou KLASA oceněnou pšeničnou mouku z blízkého mlýna v Havlíčkově Brodě. Typickou chuť a charakteristickou konzistenci zajišťují sušené bramborové vločky. Těsto se hodí pro přípravu bramborových knedlíků, ať už klasických, plněných masem nebo ovocem, šišek, kroket či gnocchi.</p>
<p>Instantní vanilkový a čokoládový puding je skvělý na přípravu sladkých dezertů. Základem je kvalitní kukuřičný škrob, který neobsahuje lepek, takže je vhodný i pro bezlepkovou dietu. Do kakaového pudingu mícháme vysoce kvalitní kakao holandského typu s 21 % tuku, které dodává výraznou čokoládovou chuť.</p>
<p>Naším cílem je vyrábět potravinářské směsi nejvyšší kvality za cenu pod úrovní supermarketových výrobků nejistého původu. Používáme suroviny nejvyšší jakosti, protože věříme, že naši zákazníci si zaslouží jen to nejlepší. Klademe důraz na přímý kontakt se zákazníky a vždy se snažíme přizpůsobit jejich potřebám.</p>
<p>Máte zájem ochutnat? <a href="/kontakt/">Ozvěte se</a>, rádi vám nabídneme vzorek zdarma.</p>""",
        "/assets/img/Jirina-Juzlova-150x150.png",
    )

    page(
        "kde-nas-najdete/index.html",
        "Kde nás najdete",
        "delivery",
        """<h1>Kde nás najdete</h1>
<figure class="page-hero">
  <img src="/assets/img/juzlova-background-image.jpg" alt="Kochánov z výšky" width="1600" height="900">
</figure>
<h2>Způsob dodání zboží</h2>
<p>Naše rodinná dílna se nachází v obci Kochánov, 12 km od Havlíčkova Brodu, a jsme vám k dispozici každý den v týdnu, od 8:00 do 19:00, včetně víkendů.</p>
<ul class="place-photos">
<li><img src="/assets/img/Kochanov-provozovna-firmy.jpg" alt="Provozovna Jůzlová s nápisem Kochánov" width="800" height="533" loading="lazy"></li>
<li><img src="/assets/img/Kochanov-40-dum.jpg" alt="Kochánov 40" width="800" height="533" loading="lazy"></li>
</ul>
<p>Uvědomujeme si, že pro naše zákazníky je vedle vysoké kvality výrobků důležitá i jejich cena. Protože současné ceny smluvních dopravců mohou naše výrobky prodražit, nabízíme možnost vyzvednutí zboží přímo u nás v provozovně v Kochánově. Stačí, když se nám předem ozvete a my vám kdykoli zboží připravíme k odběru.</p>
<p>Kromě vyzvednutí zboží na provozovně v Kochánově si jej po předchozí domluvě můžete také vyzvednout v Humpolci. V případě zájmu a po individuální domluvě vám můžeme zboží přivést i přímo k vám domů. V současné době rozvážíme zboží v Havlíčkově Brodě, Humpolci, Světlé nad Sázavou, Jihlavě a okolí.</p>
<div class="deliver">
  <article><h3>Vyzvednutí zdarma</h3><p>Provozovna v Kochánově nebo Humpolec po domluvě.</p></article>
  <article><h3>Bezplatný závoz</h3><p>Havlíčkův Brod, Světlá nad Sázavou a Jihlava.</p></article>
  <article><h3>Smluvní dopravce</h3><p>Cena poštovného dle ceníku dopravce.</p></article>
</div>
<h2>Kdy se můžete zastavit</h2>
<p>Otevřeno denně po telefonické domluvě.</p>
<div class="hours">
  <div><span>Pondělí</span><span>8:00-19:00</span></div>
  <div><span>Úterý</span><span>8:00-19:00</span></div>
  <div><span>Středa</span><span>8:00-19:00</span></div>
  <div><span>Čtvrtek</span><span>8:00-19:00</span></div>
  <div><span>Pátek</span><span>8:00-19:00</span></div>
  <div><span>Sobota</span><span>8:00-19:00</span></div>
</div>
<p>Dotazy: Jiřina Jůzlová, <a href="tel:+420728466141">+420 728 466 141</a>, nebo Jiří Jůzl, <a href="tel:+420607629931">+420 607 629 931</a>.</p>""",
        "/assets/img/juzlova-background-image.jpg",
    )

    page(
        "ceny/index.html",
        "Ceny",
        "prices",
        """<h1>Ceny</h1>
<div class="pricelist">
  <article class="pricecard">
    <img src="/assets/img/Bramborove-knedliky-300x225.png" alt="Bramborové knedlíky" width="300" height="225" loading="lazy">
    <h2>Bramborové knedlíky v prášku</h2>
    <p>Klasické knedlíky k pečenému masu, knedlíky plněné masem i ovocem, šišky s mákem, fritované krokety i domácí gnocchi.</p>
    <p class="amt">5 kg / 165 Kč</p>
  </article>
  <article class="pricecard">
    <img src="/assets/img/Chlupate-knedliky-300x225.png" alt="Chlupaté knedlíky" width="300" height="225" loading="lazy">
    <h2>Chlupaté knedlíky v prášku</h2>
    <p>Bosáky podle tradiční receptury. Hotové za 15 minut, chuť jako z domácí kuchyně.</p>
    <p class="amt">5 kg / 185 Kč</p>
  </article>
  <article class="pricecard">
    <img src="/assets/img/HERO_Hot-Cocoa-300x228.jpg" alt="Kakao holandského typu" width="300" height="228" loading="lazy">
    <h2>Kakao holandského typu</h2>
    <p>Tmavé cukrářské kakao s 21 % tuku do moučníků, koktejlů i krémů.</p>
    <p class="amt">500 g / 100 Kč</p>
  </article>
  <article class="pricecard">
    <img src="/assets/img/Vanilkovy-cukr-juzlova-300x103.png" alt="Vanilínový cukr" width="300" height="103" loading="lazy">
    <h2>Vanilínový cukr</h2>
    <p>Jemně mletý cukr s vanilínovým aromatem do těsta i na posyp cukroví.</p>
    <p class="amt">1 kg / 38 Kč</p>
  </article>
  <article class="pricecard">
    <img src="/assets/img/Vanilkovy-puding-juzlova-300x225.png" alt="Vanilkový puding" width="300" height="225" loading="lazy">
    <h2>Vanilkový puding</h2>
    <p>Na lehké dezerty i pečení. Chuť bez chemických odstínů.</p>
    <p class="amt">1 kg / 34 Kč, 400 g / 17 Kč</p>
  </article>
  <article class="pricecard">
    <img src="/assets/img/Kakaovy-puding-juzlova-224x300.png" alt="Kakaový puding" width="224" height="300" loading="lazy">
    <h2>Kakaový puding</h2>
    <p>S kakaem holandského typu, 21 % tuku.</p>
    <p class="amt">1 kg / 44 Kč, 400 g / 22 Kč</p>
  </article>
</div>""",
        "/assets/img/Bramborove-knedliky-300x225.png",
    )

    page(
        "kontakt/index.html",
        "Kontakt",
        "contact",
        """<h1>Kontakt</h1>
<div class="people">
  <div class="person">
    <h2>Jiřina Jůzlová</h2>
    <p>Kochánov 40, 582 53<br>
    <a href="tel:+420728466141">+420 728 466 141</a><br>
    <a href="mailto:juzlj@seznam.cz">juzlj@seznam.cz</a></p>
  </div>
  <div class="person">
    <h2>Jiří Jůzl</h2>
    <p>Kochánov 40, 582 53<br>
    <a href="tel:+420607629931">+420 607 629 931</a><br>
    <a href="mailto:juzlj@seznam.cz">juzlj@seznam.cz</a></p>
  </div>
</div>
<h2>Humpolec, Vysočina</h2>
<p>Po předchozí domluvě je možné vyzvednutí zboží také v Humpolci.</p>
<h2>Otevírací doba</h2>
<p>Otevřeno denně po telefonické domluvě, 8:00-19:00 (včetně víkendů).</p>
<p>Jůzlová s.r.o., IČO 45900124</p>
<h2>Napište nám</h2>
<form class="mail" action="mailto:juzlj@seznam.cz" method="post" enctype="text/plain">
  <label>Jméno
    <input name="jmeno" type="text" autocomplete="name" required>
  </label>
  <label>E-mail
    <input name="email" type="email" autocomplete="email" required>
  </label>
  <label>Zpráva
    <textarea name="zprava" required></textarea>
  </label>
  <button class="btn" type="submit">Odeslat e-mailem</button>
</form>""",
        "/assets/img/Jirina-Juzlova-150x150.png",
    )

    rec_tiles = []
    for href, name, img, alt in RECIPES:
        if img:
            media = f'<img src="{img}" alt="{alt}" width="300" height="206" loading="lazy">'
        else:
            media = '<div class="ph">Fotografie se z archivu nepodařilo obnovit</div>'
        rec_tiles.append(f'<a class="tile" href="{href}">{media}<h3>{name}</h3></a>')
    page(
        "recepty/index.html",
        "Recepty",
        None,
        f"""<h1>Recepty</h1>
<p class="lede">Recepty z našich směsí. Některé starší texty se z archivu obnovily jen částečně.</p>
<div class="mosaic">{''.join(rec_tiles)}</div>
<div class="notice"><p>Archivní kontaktní údaje z roku 2019: Jiřina Jůzlová a Jiří Jůzl, Kochánov 40, IČO 45900124. Aktuální spojení je na stránce <a href="/kontakt/">Kontakt</a>.</p></div>""",
        "/assets/img/Strapacky-se-zelim-a-slaninou-recept-juzlova.jpg",
    )

    page(
        "chlupate-knedliky/index.html",
        "Chlupaté knedlíky",
        None,
        """<h1>Chlupaté knedlíky</h1>
<figure class="page-hero"><img src="/assets/img/Chlupate-knedliky-300x225.png" alt="Chlupaté knedlíky Jůzlová" width="600" height="450"></figure>
<p>Chlupaté knedlíky, známé také jako bosáky, patří mezi naše nejoblíbenější výrobky. Vyrábíme je podle tradiční receptury. Pro rychlou a snadnou přípravu jsou oblíbené v jídelnách a restauracích, ale svou chutí a konzistencí obstojí i v domácnostech.</p>
<p>Hotové jsou za 15 minut a jejich chuť nerozeznáte od knedlíků připravovaných tradičním způsobem.</p>
<p class="price">5 kg / 185 Kč</p>
<p>Máte zájem ochutnat? <a href="/kontakt/">Ozvěte se</a>, rádi vám nabídneme vzorek zdarma.</p>""",
        "/assets/img/Chlupate-knedliky-300x225.png",
    )

    page(
        "bramborove_knedliky/index.html",
        "Bramborové knedlíky",
        None,
        """<h1>Bramborové knedlíky</h1>
<figure class="page-hero"><img src="/assets/img/Bramborove-knedliky-300x225.png" alt="Bramborové knedlíky Jůzlová" width="600" height="450"></figure>
<p>Bramborové těsto v prášku je náš nejvyhledávanější výrobek. Při jeho výrobě používáme kvalitní a značkou KLASA oceněnou pšeničnou mouku z blízkého mlýna v Havlíčkově Brodě. Typickou chuť a charakteristickou konzistenci zajišťují sušené bramborové vločky.</p>
<p>Na našich bramborových knedlících oceníte nejen přirozenou chuť, ale i všestranné využití. Z našeho těsta snadno připravíte:</p>
<ul>
<li>klasické bramborové knedlíky k pečenému masu</li>
<li>knedlíky plněné masem i ovocem</li>
<li>šišky s mákem</li>
<li>fritované krokety</li>
<li>a jestli chcete experimentovat, i domácí gnocchi</li>
</ul>
<p class="price">5 kg / 165 Kč</p>
<p>Máte zájem ochutnat? <a href="/kontakt/">Ozvěte se</a>, rádi vám nabídneme vzorek zdarma.</p>""",
        "/assets/img/Bramborove-knedliky-300x225.png",
    )

    page(
        "kakao-holandskeho-typu/index.html",
        "Kakao holandského typu",
        None,
        """<h1>Kakao holandského typu</h1>
<figure class="page-hero"><img src="/assets/img/HERO_Hot-Cocoa-300x228.jpg" alt="Kakao holandského typu" width="600" height="456"></figure>
<p>Nabízíme vám výborné tmavé cukrářské kakao holandského typu s 21 % tuku. Kakao oceníte nejen při přípravě vašich moučníků, kterým dodá výraznou kakaovou chuť a bohatou tmavou barvu, ale vychutnáte si ho i v mléčných koktejlech, dortech a krémech.</p>
<h2>Jak vybrat kakao</h2>
<p>Tmavý prášek, který nese název kakao, je předmětem vyhlášky č. 76/2003 Sb. V ní se říká, že kakaový prášek musí obsahovat nejméně 20 % kakaového másla. Většina kakaa na našem trhu však obsahuje tuku méně a spadá tak do kategorie „kakao se sníženým obsahem tuku“.</p>
<p>Podle platné české legislativy lze v regálech narazit na kakaový prášek s alespoň 20 % kakaového másla v sušině, nebo na kakao se sníženým obsahem tuku. Podíl tuku svědčí do značné míry o kvalitě. Čím více kakaového másla, tím dražší a kvalitnější surovinu získáváte.</p>
<p>Přírodní kakao je přirozeně kyselé a světlejší. Kakao holandské prošlo alkalizací, která ho ztmaví, zjemní chuť a zlepší rozpustnost.</p>
<dl class="facts">
  <div><dt>Sacharidy</dt><dd>43 g / 100 g</dd></div>
  <div><dt>Bílkoviny</dt><dd>19,5 g / 100 g</dd></div>
  <div><dt>Tuky</dt><dd>21 g / 100 g</dd></div>
  <div><dt>Energie</dt><dd>1559 kJ / 100 g</dd></div>
  <div><dt>Lepek</dt><dd>neobsahuje</dd></div>
</dl>
<p class="price">500 g / 100 Kč</p>
<p><a href="/kontakt/">Ozvěte se</a>, pokud chcete kakao objednat.</p>""",
        "/assets/img/HERO_Hot-Cocoa-300x228.jpg",
    )

    page(
        "vanilkovy-cukr/index.html",
        "Vanilínový cukr",
        None,
        """<h1>Vanilínový cukr</h1>
<figure class="page-hero"><img src="/assets/img/Vanilkovy-cukr-juzlova-300x103.png" alt="Vanilínový cukr Jůzlová" width="600" height="206"></figure>
<p>Vanilínový cukr obsahuje kromě jemně mletého cukru také vanilínové aroma, které dodává cukru příjemnou, jedinečnou vůni vanilky.</p>
<p>Vanilínový cukr oceníte při pečení koláčů, zákusků i ostatních dezertů. Skvěle se hodí při přípravě vánočního cukroví, a to nejen jako přísada do těsta, ale i pro posypy hotového cukroví.</p>
<p class="price">1 kg / 38 Kč</p>
<p>Máte zájem ochutnat? <a href="/kontakt/">Ozvěte se</a>, rádi vám nabídneme vzorek zdarma.</p>""",
        "/assets/img/Vanilkovy-cukr-juzlova-300x103.png",
    )

    page(
        "vanilkovy_pudink/index.html",
        "Vanilkový puding bez lepku",
        None,
        """<h1>Pudink bez lepku, příchuť vanilka</h1>
<figure class="page-hero"><img src="/assets/img/Vanilkovy-puding-juzlova-300x225.png" alt="Vanilkový puding Jůzlová" width="600" height="450"></figure>
<p>Vanilkový pudink bez lepku patří mezi naše tradiční produkty. Skvěle se uplatní při přípravě lehkých dezertů i při pečení. Vyzkoušejte jeho přirozenou chuť bez chemických odstínů.</p>
<h2>Jak na to</h2>
<p>Z půllitru mléka oddělte třetinu, rozmíchejte v ní 40 g cukru a 40 g pudingu. Zbylé mléko přiveďte k varu. Přidejte rozmíchanou směs a za stálého míchání ještě 2 minuty vařte.</p>
<h2>Buchtičky s rumovým šodó</h2>
<p>Z půllitru mléka oddělte třetinu, rozmíchejte v ní 30 g cukru a 30 g pudingu. Zbylé mléko přiveďte k varu, přidejte rozmíchanou směs a za stálého míchání ještě 2 minuty vařte. Před odstavením pudingu ze sporáku přidejte dvě polévkové lžíce tuzemského rumu.</p>
<dl class="facts">
  <div><dt>Sacharidy</dt><dd>87,0 g / 100 g</dd></div>
  <div><dt>Bílkoviny</dt><dd>0,0 g / 100 g</dd></div>
  <div><dt>Tuky</dt><dd>stopové množství</dd></div>
  <div><dt>Energie</dt><dd>1479 kJ / 100 g</dd></div>
  <div><dt>Lepek</dt><dd>neobsahuje</dd></div>
</dl>
<p class="price">1 kg / 34 Kč, 400 g / 17 Kč</p>""",
        "/assets/img/Vanilkovy-puding-juzlova-300x225.png",
    )

    page(
        "sisky-s-makem-recept/index.html",
        "Šišky s mákem",
        None,
        """<h1>Šišky s mákem</h1>
<figure class="page-hero"><img src="/assets/img/Pečené-šišky-s-mákem-recept-300x206.png" alt="Pečené šišky s mákem" width="600" height="412"></figure>
<p>Pečené šišky s mákem z našeho bramborového těsta v prášku. Tradiční sladká večeře, kterou zvládnete rychle a jednoduše.</p>
<div class="notice"><p>Plné znění tohoto receptu se z archivu zatím nepodařilo obnovit. Základ: z bramborového těsta Jůzlová vytvarujte šišky, uvařte, obalte v mletém máku s cukrem a přelijte rozpuštěným máslem.</p></div>""",
        "/assets/img/Pečené-šišky-s-mákem-recept-300x206.png",
    )

    page(
        "strapacky-se-zelim-a-slaninou-recept/index.html",
        "Strapačky se zelím a slaninou",
        None,
        """<h1>Strapačky se zelím a slaninou</h1>
<figure class="page-hero"><img src="/assets/img/Strapacky-se-zelim-a-slaninou-recept-juzlova.jpg" alt="Strapačky se zelím a slaninou" width="800" height="533"></figure>
<p>Slovenská klasika z našeho bramborového těsta: strapačky se zelím a opečenou slaninou.</p>
<div class="notice"><p>Plné znění tohoto receptu se z archivu zatím nepodařilo obnovit. Doplníme jej, jakmile bude archiv dostupný.</p></div>""",
        "/assets/img/Strapacky-se-zelim-a-slaninou-recept-juzlova.jpg",
    )

    page(
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem/index.html",
        "Bebe řezy s čokoládovým pudingem",
        None,
        """<h1>Bebe řezy s čokoládovým pudingem</h1>
<figure class="page-hero"><img src="/assets/img/Bebe-rezy-s-cokoladovym-pudingem-300x231-300x206.gif" alt="Bebe řezy s čokoládovým pudingem" width="600" height="412"></figure>
<p>Rádi byste pohostili návštěvu, ale nejste zrovna Jamie Oliver, ani Zdeněk Pohlreich? Nevadí. Nepečené bebe řezy s naším čokoládovým (kakaovým) pudingem zvládne opravdu každý.</p>
<div class="notice"><p>Plné znění tohoto receptu (podle Lucie Kůželové) se z archivu zatím nepodařilo obnovit.</p></div>""",
        "/assets/img/Bebe-rezy-s-cokoladovym-pudingem-300x231-300x206.gif",
    )

    page(
        "slehackova-rolada-recept/index.html",
        "Šlehačková roláda",
        None,
        f"""<h1>Šlehačková roláda</h1>
<p>Podle Jiřiny Jůzlové. S trochou gryfu vám tento lehký moučník sebere slabou půlhodinku. Kontrast lehce nahořklého kakaa a jemně sladké šlehačky je neopakovatelný. Dezert neobsahuje mouku, tedy ani lepek.</p>
{missing("K tomuto receptu se fotografie z archivu nepodařilo obnovit.")}
<div class="meta"><span>Ingredience</span></div>
<ul>
<li>5 vajec</li>
<li>100 g moučkového cukru</li>
<li>1 lžíce kakaa holandského typu</li>
<li>1 smetana ke šlehání (případně ztužovač smetany)</li>
</ul>
<h2>Postup</h2>
<p>Z vaječných bílků ušleháme tuhý sníh, až pak k němu přidáme žloutky a moučkový cukr. Opatrným mísením vznikne hladké těsto. Jako poslední přidáme kakao holandského typu.</p>
<p>Aby šlo roládu po upečení dobře sbalit, připravte pečící papír a lehce ho vymastěte. Roládu pečeme v troubě předehřáté na 180 °C asi 8 min, troubu po celou dobu neotevírejte. Nechte vychladnout, pak opatrně sejměte z papíru.</p>
<p>Ušlehejte tuhou šlehačku, potřete roládu a zabalte ji. Zbylá šlehačka může ozdobit hřbet, na efekt přidejte čokoládové hoblinky.</p>
<p>Tip: roládu můžete doplnit jahodami, malinami nebo banánem. Související recept: <a href="/podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem/">Bebe řezy s čokoládovým pudingem</a>.</p>""",
    )

    page(
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept/index.html",
        "Hruškový koláč s vanilkovým pudinkem",
        None,
        f"""<h1>Hruškový koláč s vanilkovým pudinkem</h1>
<p>Podle Lucie Kůželové. Přípravu tohoto dezertu si s vámi užijí i vaše děti.</p>
{missing("K tomuto receptu se fotografie z archivu nepodařilo obnovit.")}
<div class="meta">
  <div>Příprava <span>20 minut</span></div>
  <div>Pečení <span>45 minut</span></div>
  <div>Porce <span>8</span></div>
</div>
<h2>Ingredience</h2>
<ul>
<li>2 vejce</li>
<li>80 g rozehřátého másla</li>
<li>150 g krystalového cukru</li>
<li>200 g hladké mouky (můžete kombinovat s celozrnou nebo špaldovou)</li>
<li>1 kypřící prášek</li>
<li>2 zakysané smetany</li>
<li>1 smetana (30 %)</li>
<li>40 g vanilkového pudinku (prášek)</li>
<li>5 hrušek (lze nahradit jiným ovocem)</li>
</ul>
<h2>Postup</h2>
<p>Smícháme jedno vejce, máslo, 50 g cukru, mouku a kypřící prášek. Těsto rukama vypracujeme a vložíme do formy vyložené pečícím papírem. Pokud se těsto drolí, vymačkejte ho do formy. Okrájené hrušky nakrájíme na plátky a rozprostřeme na koláč. Do misky vložíme zakysanou smetanu, šlehačku, vanilkový puding, 100 g cukru a jedno vejce. Vše promícháme a nalijeme na koláč. Pečeme uprostřed ve vyhřáté troubě na 180 °C asi 45 min.</p>""",
    )

    page(
        "domaci-pernik-recept-podle-jirina-juzlova/index.html",
        "Domácí perník",
        None,
        f"""<h1>Domácí perník</h1>
<p>Podle Jiřiny Jůzlové. Hrníčkový perník si zamilujete pro snadnou přípravu i chuť. Váhu nepotřebujete, vystačíte si s hrnečkem (200 ml).</p>
{missing("K tomuto receptu se fotografie z archivu nepodařilo obnovit.")}
<div class="meta">
  <div>Příprava <span>10 minut</span></div>
  <div>Pečení <span>20-25 minut</span></div>
  <div>Porce <span>25-30</span></div>
</div>
<h2>Ingredience</h2>
<ul>
<li>3 hrnečky hladké mouky</li>
<li>2 hrnečky cukru krystal</li>
<li>1 hrneček oleje</li>
<li>2 středně velká vejce</li>
<li>2 vrchovaté polévkové lžíce vanilkového pudinku v prášku</li>
<li>1 prášek do perníku</li>
<li>½ prášku do pečiva</li>
<li>250 ml mléka (1 ¼ hrnečku)</li>
<li>kakao holandského typu dle chuti</li>
</ul>
<h2>Postup</h2>
<p>Všechny ingredience nasypte do jedné nádoby a důkladně je promíchejte mixérem, aby se netvořily hrudky. Těsto nalijte na vymaštěný plech vysypaný hrubou moukou. Pečte v troubě předehřáté na 180 °C, 20 až 25 minut. Hotovost ověříte dřevěným párátkem.</p>
<p>Tip: do těsta můžete přidat rum, skořici, nasekané vlašské ořechy nebo čokoládu.</p>""",
    )

    page(
        "bramborovo-tvarohove-knedliky-s-jahodami/index.html",
        "Bramborovo-tvarohové knedlíky s jahodami",
        None,
        f"""<h1>Bramborovo-tvarohové knedlíky s jahodami</h1>
<p>Léto je tady a s ním i dozrávání jahod. S tímhle jednoduchým a rychlým receptem za 20 minut potěšíte i ty největší mlsouny.</p>
{missing("Galerie tohoto receptu (jahody a těsto z roku 2017) ve veřejném archivu chybí. Místo falešné fotky necháváme prázdné pole.")}
<div class="notice"><p>Plné znění tohoto receptu (podle Lucie Kůželové) se z archivu zatím nepodařilo obnovit.</p></div>""",
    )

    page(
        "potravinarske-smesi-kontact-praha-ceske-republiky/index.html",
        "Kontakt, Vyšehrad, Praha 2",
        "contact",
        """<h1>Kontakt, Vyšehrad, Praha 2</h1>
<p>Tato adresa pochází ze staršího webu. Aktuální provozovna je v Kochánově. Pro objednávky používejte <a href="/kontakt/">současný kontakt</a>.</p>
<p>Archivní telefon: <a href="tel:+420723957826">+420 723 957 826</a></p>
<form class="mail" action="mailto:juzlj@seznam.cz" method="post" enctype="text/plain">
  <label>Jméno
    <input name="jmeno" type="text" autocomplete="name" required>
  </label>
  <label>E-mail
    <input name="email" type="email" autocomplete="email" required>
  </label>
  <label>Zpráva
    <textarea name="zprava" required></textarea>
  </label>
  <button class="btn" type="submit">Odeslat e-mailem</button>
</form>""",
    )

    write(
        "404.html",
        f"""{head("Stránka se nenašla - Jůzlová.cz", DESC)}
{nav(None)}
<main id="obsah" class="wrap">
  <div class="notfound">
    <h1>Tady nic nepeče</h1>
    <p class="lede">Tuto adresu na webu nemáme. Zkuste úvod, recepty, nebo nám napište.</p>
    <div class="actions">
      <a class="btn" href="/">Úvod</a>
      <a class="btn btn-ghost" href="/recepty/">Recepty</a>
    </div>
  </div>
</main>
{foot()}""",
    )


if __name__ == "__main__":
    main()
