#!/usr/bin/env python3
"""First pass: the PDF change IDs on the Czech sources."""
import pathlib


def sub(f, pairs):
    p = pathlib.Path(f)
    s = p.read_text()
    for a, b in pairs:
        assert s.count(a) == 1, (f, s.count(a), a[:70])
        s = s.replace(a, b)
    p.write_text(s)


DELIV = "Do Humpolce a Havlíčkova Brodu zboží dovezeme."
sub("scripts/content_cs.py", [
    ('"sec_why": "Víte, odkud je mouka. A komu voláte."', '"sec_why": "Víte, komu voláte."'),
    ('"sec_why_kicker": "Proč od nás",\n', '"sec_why_kicker": "Proč od nás",\n        "why_cols": (2, 3),\n'),
    ('"deliver_2": "Po Vysočině přivezeme zdarma: Humpolec a Havlíčkův Brod od 1000 Kč, Jihlava od 3000 Kč, zbytek Vysočiny od 5000 Kč.",\n        "deliver_3": "Poslat balíkem můžeme po domluvě; dopravu, balení a pojištění platíte navíc.",\n',
     f'"deliver_2": "{DELIV}",\n'),
    ('"form_fulfill_humpolec": "Vyzvednutí v Humpolci u Pivovaru Bernard (zdarma, den a hodinu domluvíme)",\n        "form_fulfill_delivery": "Rozvoz po Vysočině, nebo balík po domluvě",\n',
     '"form_fulfill_two_cities": "Rozvoz do Havlíčkova Brodu nebo Humpolce (zdarma, den a hodinu domluvíme)",\n'),
    ('vždy po předchozí domluvě. Odpovídáme česky.",', 'vždy po předchozí domluvě.",'),
    ('"sub": "Stejná cena pro každého, kdo si zboží vyzvedne v dílně nebo v Humpolci. Rozvoz po Vysočině najdete pod tabulkou.",',
     '"sub": "Stejná cena pro všechny, kteří si zboží vyzvednou v dílně nebo jimž ho doručíme do Havlíčkova Brodu či Humpolce.",'),
    ('''"Humpolec a Havlíčkův Brod: rozvoz zdarma od 1000 Kč",
                    "Jihlava: zdarma od 3000 Kč · zbytek Vysočiny: zdarma od 5000 Kč",
                    "Kuchyně: Brno zdarma od 5000 Kč, Praha smíšená objednávka od 25 kg",
                    "Balík po Česku i do zahraničí: po domluvě; dopravu, balení a pojištění platíte navíc",
''', '''"Humpolec a Havlíčkův Brod",
'''),
    ('''                ("h2", "Kuchyně a provozovny"),
                ("p", "Množstevní ceny řekneme po telefonu nebo přes formulář na stránce Pro kuchyně."),
''', ''),
    ('sušené bramborové vločky. Nic dalšího. Vejce nebo strouhanou bramboru přidáte, jak jste zvyklí.",\n            "price": "5 kg / 250 Kč",',
     'sušené bramborové vločky.",\n            "price_note": "Vyzvednete na provozovně. ' + DELIV + '",\n            "price": "5 kg / 250 Kč",'),
    ('("p", "Pšeničná mouka se značkou KLASA z mlýna v Havlíčkově Brodě, který vlastní a vede naše širší rodina, a sušené bramborové vločky. Vločky dávají těstu chuť brambor a drží ho při vaření pohromadě."),',
     '("p", "Mouka, sušené bramborové vločky, sušená vejce, sůl, prášek do pečiva, bramborový škrob"),'),
    ('Chcete to „svoje“? Část vody nahraďte mlékem, přidejte vejce', 'Chcete to „svoje“? Přidejte vejce'),
    ('''                ("h2", "Pro jídelny"),
                ("p", "Bosáky dodáváme i jídelnám a restauracím: stejná směs, množstevní cena, odběr v Kochánově, náš rozvoz nebo váš dopravce."),
''', ''),
    ('''                ("h2", "Pro cukrárny a zmrzlináře"),
                ("p", "Množstevní cena, certifikát k šarži, odběr nebo doprava. Poptejte na stránce Pro kuchyně."),
''', ''),
])
sub("scripts/aeo_pages.py", [
    ('''"price_excludes_shipping": (
            "Rozvoz po domluvě, poslání balíkem se platí zvlášť."
        ),''', f'''"price_excludes_shipping": (
            "{DELIV}"
        ),'''),
    ('''            ("Platí ceny i pro zásilku?", "Ceny zboží ano. Balík posíláme jen na požádání; poštovné, krabici a pojištění platíte celé vy a celkovou částku domluvíme předem."),
            ("Máte slevy pro velké odběry?", "Ano, pro provozovny podle množství. Cenu řekneme po telefonu."),
        ],
        "velkoobchod": [],
        "do_eu": [
            ("Platí se clo?"''', '''        ],
        "velkoobchod": [],
        "do_eu": [
            ("Platí se clo?"'''),
])
p = pathlib.Path("scripts/aeo_more.py")
s = p.read_text()
i = s.index('"velkoobchod_vysocina": page(')
j = s.index('\n        "velkoobchod_', i + 10)
b = s[i:j]
for a, c in [
    ('t("Velkoobchod po Vysočině",\n              "Wholesale across Vysočina",', 't("Velkoobchod",\n              "Wholesale across Vysočina",'),
    ('rozvoz po kraji domluvíme. Cenu směsí podle množství řekneme po telefonu — na webu velkoobchodní sazby nejsou.",', 'rozvoz po kraji domluvíme.",'),
    ('                ("p", price),\n                ("links", "b2b"),\n                ("form_b2b", None),\n', ''),
]:
    assert b.count(a) == 1, a[:60]
    b = b.replace(a, c)
k = b.index('            [\n                (t("Dodáváte jídelnám na Vysočině?"')
m = b.index('\n            ],\n', k) + len('\n            ],\n')
b = b[:k] + '            [],\n' + b[m:]
p.write_text(s[:i] + b + s[j:])

sub("scripts/build_site.py", [
    ('ASSET_VER = "20261018a"', 'ASSET_VER = "20261030a"'),
    ('''<label class="chk"><input type="radio" name="fulfillment" value="factory"><span>{esc(ui['form_fulfill_factory'])}</span></label>
<label class="chk"><input type="radio" name="fulfillment" value="humpolec"><span>{esc(ui['form_fulfill_humpolec'])}</span></label>
<label class="chk"><input type="radio" name="fulfillment" value="delivery"><span>{esc(ui['form_fulfill_delivery'])}</span></label>
''', '''{fulfill}
'''),
    ('''    heading_id = "b2b-write" if is_b2b else "write-to-us"
''', '''    heading_id = "b2b-write" if is_b2b else "write-to-us"
    if ui.get("form_fulfill_two_cities"):
        fulfill_opts = [("factory", ui["form_fulfill_factory"]),
                        ("delivery_hb_humpolec", ui["form_fulfill_two_cities"])]
    else:
        fulfill_opts = [("factory", ui["form_fulfill_factory"]),
                        ("humpolec", ui["form_fulfill_humpolec"]),
                        ("delivery", ui["form_fulfill_delivery"])]
    fulfill = "\\n".join(
        f'<label class="chk"><input type="radio" name="fulfillment" value="{v}"><span>{esc(label)}</span></label>'
        for v, label in fulfill_opts)
'''),
    ("""  {a('velkoobchod', ui['nav_b2b'])}\n  {a('kontakt', ui['nav_contact'])}""", """  {a('kontakt', ui['nav_contact'])}"""),
    ('''    "objednavka_cesko": "Objednávka po celém Česku",
    "navstevnikum": "Vyzvednutí po cestě",
}''', '''    "objednavka_cesko": "Jak objednat",
    "navstevnikum": "Vyzvednutí po cestě",
    "velkoobchod_vysocina": "Velkoobchod",
}

# Only these local pages are linked from the Czech footer; the others keep their routes.
FOOTER_GEO = ("objednavka_cesko", "navstevnikum")
FOOTER_B2B = ("velkoobchod_vysocina",)'''),
    ('''            for k in GEO_SLUGS)
        b2b = "".join(''', '''            for k in FOOTER_GEO)
        b2b = "".join('''),
    ('''            for k in B2B_SLUGS)
        groups +=''', '''            for k in FOOTER_B2B)
        groups +='''),
    ('''def price_note_html(L):
    note = L["ui"].get("price_excludes_shipping") or ""
''', '''def price_note_html(L, note=None):
    note = note or L["ui"].get("price_excludes_shipping") or ""
'''),
    ('''{price_note_html(L)}</div>
{cta_html(L, depth, ("cta_order", "kde_nas_najdete", "cta_pickup"))}''', '''{price_note_html(L, pr.get("price_note"))}</div>
{cta_html(L, depth, ("cta_order", "kde_nas_najdete", "cta_pickup"))}'''),
    ('''    why = f"""<section class="band gold why">''', '''    why_cols = ui.get("why_cols") or (1, 2, 3)
    why_html = "\\n      ".join(
        f"""<div class="rv"><h3>{esc(ui[f'why_{n}_h'])}</h3><p class="body bullet">{esc(ui[f'why_{n}_p'])}</p></div>"""
        for n in why_cols)
    why = f"""<section class="band gold why">'''),
    ('''    <div class="cols3">
      <div class="rv"><h3>{esc(ui['why_1_h'])}</h3><p class="body bullet">{esc(ui['why_1_p'])}</p></div>
      <div class="rv"><h3>{esc(ui['why_2_h'])}</h3><p class="body bullet">{esc(ui['why_2_p'])}</p></div>
      <div class="rv"><h3>{esc(ui['why_3_h'])}</h3><p class="body bullet">{esc(ui['why_3_p'])}</p></div>
    </div>''', '''    <div class="cols3{' cols-2' if len(why_cols) == 2 else ''}">
      {why_html}
    </div>'''),
    ('''for k in ("deliver_1", "deliver_2", "deliver_3"))''', '''for k in ("deliver_1", "deliver_2", "deliver_3") if ui.get(k))'''),
])
sub("assets/site.css", [
    ('''.cols3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 3rem; margin-top: 3.5rem; }
@media (max-width: 900px) { .cols3 { grid-template-columns: 1fr; } }''',
     '''.cols3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 3rem; margin-top: 3.5rem; }
.cols3.cols-2 { grid-template-columns: repeat(2, 1fr); }
@media (max-width: 900px) { .cols3, .cols3.cols-2 { grid-template-columns: 1fr; } }'''),
])
sub("server/app.py", [
    ('''    "delivery": "rozvoz",
}''', '''    "delivery": "rozvoz",
    "delivery_hb_humpolec": "rozvoz do Havlíčkova Brodu nebo Humpolce",
}'''),
])
sub("TODO.md", [
    ('''## 💡 Ideas, not scheduled''', '''- [ ] **Owner review of the PDF content corrections** (2026-10-30, Adam).
      Branch `content-corrections-owner-pdf`. Conflicting claims are settled in all
      four languages. Owner to confirm: Humpolec pick-up, and the en/de/sk wording.

## 💡 Ideas, not scheduled'''),
])
print("pre ok")
