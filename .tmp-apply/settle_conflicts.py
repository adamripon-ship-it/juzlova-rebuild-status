#!/usr/bin/env python3
"""Settle conflicts left by the owner's PDF. Every replacement asserts it found its target.
Nothing is written to disk until every edit has succeeded."""
import pathlib
import re

BUF = {}


def rd(f):
    return BUF.get(f) if f in BUF else pathlib.Path(f).read_text()


def wr(f, s):
    BUF[f] = s


def sub1(s, a, b, n=1):
    c = s.count(a)
    assert c == n, (c, a[:90])
    return s.replace(a, b)


def line(s, prefix, new=None):
    """Replace (or delete, when new is None) the single line starting with prefix after indentation."""
    pat = re.compile(r"^([ \t]*)" + re.escape(prefix) + r".*\n", re.M)
    assert len(pat.findall(s)) == 1, (len(pat.findall(s)), prefix[:90])
    return pat.sub((lambda m: m.group(1) + new + "\n") if new is not None else "", s)


def qa(s, q_prefix, new=None):
    """Two-line (q,\\n a) tuple: delete it, or replace it with new=(q, a)."""
    pat = re.compile(r"^([ \t]*)\(" + re.escape(q_prefix) + r'[^\n]*\n[^\n]*\),\n', re.M)
    assert len(pat.findall(s)) == 1, (len(pat.findall(s)), q_prefix[:90])
    if new is None:
        return pat.sub("", s)
    return pat.sub(lambda m: f'{m.group(1)}("{new[0]}",\n{m.group(1)} "{new[1]}"),\n', s)


def faq_t(s, q_prefix):
    """Multi-line (t("q"...),\\n t(...)), tuple in aeo files: delete it."""
    lines = s.split("\n")
    idx = [i for i, l in enumerate(lines) if l.strip().startswith('(t("' + q_prefix)]
    assert len(idx) == 1, (len(idx), q_prefix)
    j = idx[0] + 1
    while not lines[j].rstrip().endswith(")),"):
        j += 1
    del lines[idx[0]: j + 1]
    return "\n".join(lines)


T = {
    "cs": dict(
        deliv="Do Humpolce a Havlíčkova Brodu zboží dovezeme.",
        mill="Mouka do knedlíkových směsí je z mlýna v Havlíčkově Brodě, 12 km od dílny.",
        short="Mouka z mlýna v Havlíčkově Brodě. Celé složení najdete níže.",
        vis2="Složení a etikety pošleme e-mailem.",
        vis3="Vyzvednutí v Kochánově, rozvoz do Humpolce a Havlíčkova Brodu nebo váš dopravce.",
    ),
    "en": dict(
        deliv="We deliver to Humpolec and Havlíčkův Brod.",
        note="Collect at the workshop. We deliver to Humpolec and Havlíčkův Brod.",
        mill="The flour in our dumpling mixes comes from a mill in Havlíčkův Brod, 12 km from the workshop.",
        short="Flour from a mill in Havlíčkův Brod. The full ingredient list is below.",
        ingr="Flour, dried potato flakes, dried egg, salt, baking powder, potato starch",
        why="You know who picks up the phone.",
        two="Delivery to Havlíčkův Brod or Humpolec (free, day and time by arrangement)",
        hint="Kitchens and shops: more on the page",
        stat="from the workshop to the mill",
        c01="The same price for everyone who collects at the workshop or has it delivered to Havlíčkův Brod or Humpolec.",
        pick="Pick-up in Kochánov or Humpolec: free",
        cities="Humpolec and Havlíčkův Brod",
        faq_egg=("Do I have to add an egg?", "No. Mix with water as directed on the bag. Add an egg if you want a richer taste."),
        tip="Want it your way? Add an egg or a boiled, grated potato. Many of our customers do.",
        desc="Czech potato dumpling mix: just add water. Holds together, ready in 20 minutes. 5 kg / 250 Kč. Collect in Kochánov.",
        kdo_desc="The Jůzl family has made dumpling mix, pudding and cocoa in Kochánov since 2004. No web shop, no middlemen.",
        kdo_sub="The workshop is at Kochánov 40, twelve kilometres from Havlíčkův Brod. Jiřina takes the orders.",
        vis2="We e-mail ingredient lists and labels for your paperwork.",
        vis3="Pick-up in Kochánov, delivery to Humpolec and Havlíčkův Brod, or your own carrier.",
    ),
    "de": dict(
        deliv="Nach Humpolec und Havlíčkův Brod liefern wir.",
        note="Abholung in der Werkstatt. Nach Humpolec und Havlíčkův Brod liefern wir.",
        mill="Das Mehl in unseren Knödelmischungen stammt aus einer Mühle in Havlíčkův Brod, 12 km von der Werkstatt.",
        short="Mehl aus einer Mühle in Havlíčkův Brod. Die vollständige Zutatenliste finden Sie unten.",
        ingr="Mehl, getrocknete Kartoffelflocken, Trockenei, Salz, Backpulver, Kartoffelstärke",
        why="Sie wissen, wer ans Telefon geht.",
        two="Lieferung nach Havlíčkův Brod oder Humpolec (kostenlos, Tag und Uhrzeit nach Absprache)",
        hint="Küchen und Betriebe: mehr auf der Seite",
        stat="von der Werkstatt zur Mühle",
        c01="Derselbe Preis für alle, die in der Werkstatt abholen oder sich nach Havlíčkův Brod oder Humpolec liefern lassen.",
        pick="Abholung in Kochánov oder Humpolec: kostenlos",
        cities="Humpolec und Havlíčkův Brod",
        faq_egg=("Muss ich ein Ei zugeben?", "Nein. Mit Wasser nach Anleitung auf dem Beutel anrühren. Ein Ei können Sie für mehr Geschmack nach Belieben zugeben."),
        tip="Lieber nach eigener Art? Ein Ei oder eine gekochte, geriebene Kartoffel zugeben. Viele unserer Kunden machen das so.",
        desc="Knödelteig zum Anrühren, nur Wasser dazu. Zerfällt nicht, in 20 Minuten fertig. 5 kg / 250 Kč.",
        kdo_desc="Familie Jůzl stellt seit 2004 in Kochánov Knödelmischung, Pudding und Kakao her. Kein Onlineshop.",
        kdo_sub="Die Werkstatt liegt in Kochánov 40, zwölf Kilometer von Havlíčkův Brod. Bestellungen nimmt Jiřina entgegen.",
        vis2="Zutatenlisten und Etiketten schicken wir per E-Mail für Ihre Unterlagen.",
        vis3="Abholung in Kochánov, Lieferung nach Humpolec und Havlíčkův Brod oder Ihr Spediteur.",
    ),
    "sk": dict(
        deliv="Do Humpolca a Havlíčkovho Brodu tovar dovezieme.",
        note="Vyzdvihnete v prevádzke. Do Humpolca a Havlíčkovho Brodu tovar dovezieme.",
        mill="Múka do knedľových zmesí je z mlyna v Havlíčkovom Brode, 12 km od dielne.",
        short="Múka z mlyna v Havlíčkovom Brode. Celé zloženie nájdete nižšie.",
        ingr="Múka, sušené zemiakové vločky, sušené vajcia, soľ, prášok do pečiva, zemiakový škrob",
        why="Viete, komu voláte.",
        two="Rozvoz do Havlíčkovho Brodu alebo Humpolca (zadarmo, deň a hodinu dohodneme)",
        hint="Kuchyne a prevádzky: viac na stránke",
        stat="od dielne k mlynu",
        c01="Rovnaká cena pre všetkých, ktorí si tovar vyzdvihnú v dielni alebo ktorým ho doručíme do Havlíčkovho Brodu či Humpolca.",
        pick="Vyzdvihnutie v Kochánove alebo v Humpolci: zadarmo",
        cities="Humpolec a Havlíčkův Brod",
        faq_egg=("Musím pridať vajce?", "Nie. Zamiešate s vodou podľa návodu na vrecku. Vajce pridajte, ak chcete bohatšiu chuť."),
        tip="Chcete to „po svojom“? Pridajte vajce alebo jeden uvarený postrúhaný zemiak. Veľa našich zákazníkov to tak robí.",
        desc="Zemiakové cesto v prášku, stačí voda. Nerozvarí sa, hotové za 20 minút. 5 kg / 250 Kč. Vyzdvihnutie v dielni po dohode.",
        kdo_desc="Rodina Jůzlových mieša knedle v prášku, puding a kakao v Kochánove na Vysočine od roku 2004. Bez e-shopu.",
        kdo_sub="Dielňa je v Kochánove 40, dvanásť kilometrov od Havlíčkovho Brodu. Objednávky prijíma Jiřina.",
        vis2="Zloženie a etikety pošleme e-mailom.",
        vis3="Vyzdvihnutie v Kochánove, rozvoz do Humpolca a Havlíčkovho Brodu alebo váš dopravca.",
    ),
}

PAGES = {
    "en": dict(
        v_t="Dumpling mix, pudding & cocoa for kitchens | Jůzlová",
        v_d="Mixes for canteens, restaurants, bakeries and gelato makers. Pick-up in Kochánov, delivery to Humpolec and Havlíčkův Brod, or your carrier.",
        v_n="For kitchens",
        v_h="Dumpling mix, pudding and cocoa for canteens and restaurants: pick-up in Kochánov",
        v_s="We supply canteens, restaurants, bakeries, cafés, schools and ice-cream makers. We don't publish customer names.",
        v_h2a="Why kitchens use the mix",
        v_pa="Potato dough for 500 portions, without thirty kilos of potatoes to peel. The same consistency every day.",
        v_h2b="What we supply to whom",
        v_ul=["canteens and restaurants — dumpling mix and pudding for service",
              "bakeries and pastry shops — pudding, vanilla sugar, cocoa",
              "cafés — cocoa and pudding",
              "schools — mixes for children's meals",
              "ice-cream makers — Dutch-process cocoa that keeps its colour in the freezer"],
        v_h2c="How you get it",
        v_ol=["Pick-up at the workshop in Kochánov", "Delivery to Humpolec and Havlíčkův Brod", "Your own carrier"],
        e_t="Living abroad? Collect at the workshop | Jůzlová",
        e_d="We are a local family workshop and our customers collect at the workshop. We deliver to Humpolec and Havlíčkův Brod.",
        e_n="Living abroad",
        e_h="Living abroad? We are a local workshop and you collect from us",
        e_s="Collect at the workshop in Kochánov, by arrangement. We deliver to Humpolec and Havlíčkův Brod.",
        e_h2="Family in Czechia",
        e_p="Buying for family in Czechia? They can collect in Kochánov or Humpolec.",
    ),
    "de": dict(
        v_t="Knödelmischung, Pudding & Kakao für Küchen | Jůzlová",
        v_d="Mischungen für Kantinen, Gaststätten, Bäckereien und Eishersteller. Abholung in Kochánov, Lieferung nach Humpolec und Havlíčkův Brod oder Ihr Spediteur.",
        v_n="Für Küchen",
        v_h="Knödelmischung, Pudding und Kakao für Kantinen und Gaststätten: Abholung in Kochánov",
        v_s="Wir beliefern Kantinen, Gaststätten, Bäckereien, Cafés, Schulen und Eishersteller. Kundennamen veröffentlichen wir nicht.",
        v_h2a="Warum Küchen die Mischung nehmen",
        v_pa="Kartoffelteig für 500 Portionen, ohne dreißig Kilo Kartoffeln schälen zu müssen. Jeden Tag dieselbe Konsistenz.",
        v_h2b="Was wir wem liefern",
        v_ul=["Kantinen und Gaststätten — Knödelmischung und Pudding für die Ausgabe",
              "Bäckereien und Konditoreien — Pudding, Vanillinzucker, Kakao",
              "Cafés — Kakao und Pudding",
              "Schulen — Mischungen für Kinderessen",
              "Eishersteller — Kakao nach holländischer Art, der im Frost seine Farbe behält"],
        v_h2c="So bekommen Sie die Ware",
        v_ol=["Abholung in der Werkstatt in Kochánov", "Lieferung nach Humpolec und Havlíčkův Brod", "Ihr eigener Spediteur"],
        e_t="Wohnen Sie im Ausland? Abholung in der Werkstatt | Jůzlová",
        e_d="Wir sind eine kleine Familienwerkstatt, unsere Kunden holen in der Werkstatt ab. Nach Humpolec und Havlíčkův Brod liefern wir.",
        e_n="Wohnen im Ausland",
        e_h="Wohnen Sie im Ausland? Wir sind eine kleine Familienwerkstatt, abgeholt wird bei uns",
        e_s="Abholung in der Werkstatt in Kochánov nach Absprache. Nach Humpolec und Havlíčkův Brod liefern wir.",
        e_h2="Für die Familie in Tschechien",
        e_p="Kaufen Sie für die Familie in Tschechien? Sie kann in Kochánov oder Humpolec abholen.",
    ),
    "sk": dict(
        v_t="Knedle v prášku, puding a kakao pre kuchyne | Jůzlová",
        v_d="Zmesi pre jedálne, reštaurácie, pekárne a zmrzlinárov. Vyzdvihnutie v Kochánove, rozvoz do Humpolca a Havlíčkovho Brodu alebo váš dopravca.",
        v_n="Pre kuchyne",
        v_h="Knedle, puding a kakao pre jedálne a reštaurácie: odber v Kochánove",
        v_s="Zásobujeme jedálne, reštaurácie, pekárne, kaviarne, školy a zmrzlinárov. Mená zákazníkov nezverejňujeme.",
        v_h2a="Prečo kuchyne berú zmes",
        v_pa="Zemiakové cesto na 500 porcií bez tridsiatich kíl zemiakov na šúpanie. Rovnaká konzistencia každý deň.",
        v_h2b="Čo dodávame komu",
        v_ul=["jedálňam a reštauráciám — knedle a puding na výdaj",
              "pekárňam a cukrárňam — puding, vanilínový cukor, kakao",
              "kaviarňam — kakao a puding",
              "školám — zmesi na detské jedlá",
              "zmrzlinárom — kakao holandského typu, ktoré v mraze drží farbu"],
        v_h2c="Ako to dostanete",
        v_ol=["Vyzdvihnutie v dielni v Kochánove", "Rozvoz do Humpolca a Havlíčkovho Brodu", "Váš vlastný dopravca"],
        e_t="Bývate v zahraničí? Vyzdvihnutie v dielni | Jůzlová",
        e_d="Sme miestna rodinná dielňa a zákazníci si tovar vyzdvihnú v dielni. Do Humpolca a Havlíčkovho Brodu tovar dovezieme.",
        e_n="Bývate v zahraničí",
        e_h="Bývate v zahraničí? Sme miestna rodinná dielňa a tovar si vyzdvihnete u nás",
        e_s="Vyzdvihnutie v dielni v Kochánove po dohode. Do Humpolca a Havlíčkovho Brodu tovar dovezieme.",
        e_h2="Pre rodinu v Česku",
        e_p="Chcete zmesi pre rodičov v Česku? Môžu si ich vyzdvihnúť v Kochánove alebo v Humpolci.",
    ),
    "cs": dict(
        v_t="Velkoobchod: knedlíky v prášku, puding, kakao | Jůzlová",
        v_d="Směsi pro jídelny, restaurace, pekárny a zmrzlináře od výrobce z Vysočiny. Odběr v Kochánově, rozvoz do Humpolce a Havlíčkova Brodu nebo váš dopravce.",
        v_n="Pro kuchyně",
        v_h="Knedlíky, puding a kakao pro jídelny a restaurace: odběr v Kochánově",
        v_s="Zásobujeme jídelny, restaurace, pekárny, kavárny, školy a zmrzlináře. Jména zákazníků na web nedáváme.",
        v_h2a="Proč kuchyně berou směs",
        v_pa="Bramborové těsto na 500 porcí bez třiceti kil brambor k loupání. Stejná konzistence každý den.",
        v_h2b="Co dodáváme komu",
        v_ul=["jídelnám a restauracím — knedlíky a puding na výdej",
              "pekárnám a cukrárnám — puding, vanilínový cukr, kakao",
              "kavárnám — kakao a puding",
              "školám — směsi na dětská jídla",
              "zmrzlinářům — kakao holandského typu, které v mrazu drží barvu"],
        v_h2c="Jak to dostanete",
        v_ol=["Vyzvednutí v dílně v Kochánově", "Rozvoz do Humpolce a Havlíčkova Brodu", "Váš vlastní dopravce"],
        e_t="Bydlíte v zahraničí? Vyzvednutí v dílně | Jůzlová",
        e_d="Jsme malá dílna v Kochánově a zákazníci si směsi vyzvednou v dílně. Do Humpolce a Havlíčkova Brodu zboží dovezeme.",
        e_n="Bydlíte v zahraničí",
        e_h="Bydlíte v zahraničí? Jsme malá místní dílna a zboží si vyzvednete u nás",
        e_s="Vyzvednutí v dílně v Kochánově po domluvě. Do Humpolce a Havlíčkova Brodu zboží dovezeme.",
        e_h2="Pro rodinu v Česku",
        e_p="Chcete směsi pro rodiče v Česku? Nejjednodušší je, když si je vyzvednou v Kochánově nebo v Humpolci.",
    ),
}


def pages_block(p):
    q = lambda x: '"' + x + '"'
    ul = ",\n".join(" " * 20 + q(x) for x in p["v_ul"])
    ol = ",\n".join(" " * 20 + q(x) for x in p["v_ol"])
    return f'''        "velkoobchod": {{
            "title": {q(p['v_t'])},
            "desc": {q(p['v_d'])},
            "nav": {q(p['v_n'])},
            "h1": {q(p['v_h'])},
            "sub": {q(p['v_s'])},
            "cta": ("cta_call", None, None),
            "body": [
                ("h2", {q(p['v_h2a'])}),
                ("p", {q(p['v_pa'])}),
                ("b2b_showcase", None),
                ("h2", {q(p['v_h2b'])}),
                ("ul", [
{ul},
                ]),
                ("h2", {q(p['v_h2c'])}),
                ("ol", [
{ol},
                ]),
                ("form_b2b", None),
            ],
        }},
        "do_eu": {{
            "title": {q(p['e_t'])},
            "desc": {q(p['e_d'])},
            "nav": {q(p['e_n'])},
            "h1": {q(p['e_h'])},
            "sub": {q(p['e_s'])},
            "cta": ("cta_call", "kontakt", "cta_write"),
            "body": [
                ("h2", {q(p['e_h2'])}),
                ("p", {q(p['e_p'])}),
                ("form", None),
            ],
        }},
    }},
'''


def common(s, lg):
    """Edits with the same shape in every language file."""
    t = T[lg]
    m = re.search(r'^        "velkoobchod": \{.*?^    \},\n(?=    "products": \{)', s, re.M | re.S)
    assert m, lg
    s = s[:m.start()] + pages_block(PAGES[lg]) + s[m.end():]
    # the stats paragraph reuses why_1_p; the "why" column itself is gone
    s = line(s, '"why_1_h":')
    s = line(s, '"why_1_p":', f'"why_1_p": "{t["mill"]}",')
    s = line(s, '"deliver_2":', f'"deliver_2": "{t["deliv"]}",')
    s, n = re.subn(r'("unit_note": "[^"]*?\.) [^"]*"', r'\1"', s)
    assert n <= 1, lg
    s = line(s, '"b2b_vis_2_p":', f'"b2b_vis_2_p": "{t["vis2"]}",')
    s = line(s, '"b2b_vis_3_p":', f'"b2b_vis_3_p": "{t["vis3"]}",')
    s, n = re.subn(r'("bramborove_knedliky": \{.*?"short": ")[^"]*(")',
                   lambda m: m.group(1) + t["short"] + m.group(2), s, count=1, flags=re.S)
    assert n == 1, lg
    return s


# ---------- foreign language content ----------
for lg in ("en", "de", "sk"):
    f = f"scripts/content_{lg}.py"
    s = common(rd(f), lg)
    t = T[lg]
    s = line(s, '"deliver_3":')
    s, n = re.subn(r'"sec_why": "[^"]*",', f'"sec_why": "{t["why"]}", "why_cols": (2, 3),', s)
    assert n == 1, lg
    s = line(s, '"form_fulfill_humpolec":', f'"form_fulfill_two_cities": "{t["two"]}",')
    s = line(s, '"form_fulfill_delivery":')
    s, n = re.subn(r'"faq_b2b_hint": "[^"]*",', f'"faq_b2b_hint": "{t["hint"]}",', s)
    assert n == 1, lg
    s, n = re.subn(r"'stat_4': '[^']*'", f"'stat_4': '{t['stat']}'", s)
    assert n == 1, lg
    m = re.search(r'"kdo_jsme": \{.*?"body": \[', s, re.S)
    b = re.sub(r'"desc": "[^"]*"', f'"desc": "{t["kdo_desc"]}"', m.group(0), count=1)
    b = re.sub(r'"sub": "[^"]*"', f'"sub": "{t["kdo_sub"]}"', b, count=1)
    s = s[:m.start()] + b + s[m.end():]
    s, n = re.subn(r'\("p", "[^"]*12 km[^"]*KLASA[^"]*"\)', f'("p", "{t["mill"]}")', s)
    assert n == 1, (lg, n)
    m = re.search(r'"ceny": \{.*?"body": \[.*?\("pricetable", None\),\n(.*?)(\s+\("h2", "[^"]*"\),\n\s+\("p", "[^"]*2017[^"]*"\))', s, re.S)
    assert m, lg
    head = m.group(0)[: m.start(1) - m.start()]
    head, n = re.subn(r'"sub": "[^"]*"', f'"sub": "{t["c01"]}"', head, count=1)
    assert n == 1, lg
    h2 = re.search(r'\("h2", "[^"]*"\),', m.group(1)).group(0)
    mid = (f'                {h2}\n                ("ul", [\n                    "{t["pick"]}",\n'
           f'                    "{t["cities"]}",\n                ]),')
    s = s[:m.start()] + head + mid + m.group(2) + s[m.end():]
    pk = s.index('"bramborove_knedliky": {', s.index('"products": {'))
    pe = s.index('"chlupate_knedliky": {', pk)
    b = s[pk:pe]
    b, n = re.subn(r'\("p", "[^"]*KLASA[^"]*"\)', f'("p", "{t["ingr"]}")', b)
    assert n == 1, lg
    b, n = re.subn(r'\("tip", "[^"]*"\)', f'("tip", "{t["tip"]}")', b)
    assert n == 1, lg
    b, n = re.subn(r'"desc": "[^"]*"', f'"desc": "{t["desc"]}"', b, count=1)
    assert n == 1, lg
    b = b.replace('"short":', f'"price_note": "{t["note"]}",\n            "short":', 1)
    faq_q, faq_a = t["faq_egg"]
    b, n = re.subn(r'\("' + re.escape(faq_q) + r'", "[^"]*"\)', f'("{faq_q}", "{faq_a}")', b)
    assert n == 1, lg
    s = s[:pk] + b + s[pe:]
    p0 = s.index('"products": {')
    head, tail = s[:p0], s[p0:]
    tail, n = re.subn(r'\s+\("h2", "(?:For |Für |Pre |Pro )[^"]*"\),\n\s+\("p", "[^"]*"\),(?=\n\s+\],)', "", tail)
    assert n == 2, (lg, n)
    wr(f, head + tail)

s = rd("scripts/content_de.py")
s = sub1(s, "in der Vysočina — Mehl aus der Familienmühle, nur Wasser dazu", "in der Vysočina — nur Wasser dazu")
s = line(s, '"Humpolec und Havlíčkův Brod: kostenlose Lieferung ab 1000 Kč",', f'"{T["de"]["deliv"]}",')
s = line(s, '"Jihlava: kostenlos ab 3000 Kč",')
s = line(s, '"Übrige Vysočina: kostenlos ab 5000 Kč",')
s = line(s, '"Auf Anfrage schicken wir auch ein Paket (Tschechien')
wr("scripts/content_de.py", s)
s = rd("scripts/content_sk.py")
s = sub1(s, "na Vysočine — múka z rodinného mlyna, stačí voda", "na Vysočine — stačí voda")
s = line(s, '"Humpolec a Havlíčkův Brod: rozvoz zadarmo od 1000 Kč",', f'"{T["sk"]["deliv"]}",')
s = line(s, '"Jihlava: zadarmo od 3000 Kč",')
s = line(s, '"Zvyšok Vysočiny: zadarmo od 5000 Kč",')
s = line(s, '"Inde v Česku, na Slovensku')
wr("scripts/content_sk.py", s)
s = rd("scripts/content_en.py")
s = line(s, '"Humpolec and Havlíčkův Brod: free delivery from 1000 Kč",', f'"{T["en"]["deliv"]}",')
s = line(s, '"Jihlava: free from 3000 Kč",')
s = line(s, '"Rest of Vysočina: free from 5000 Kč",')
s = line(s, '"Elsewhere in Czechia or abroad:')
wr("scripts/content_en.py", s)

# ---------- Czech content ----------
f = "scripts/content_cs.py"
s = common(rd(f), "cs")
s = sub1(s, '"nav_d2c": "Balík do zahraničí"', '"nav_d2c": "Bydlíte v zahraničí"')
s, n = re.subn(r'"faq_b2b_hint": "[^"]*",', '"faq_b2b_hint": "Kuchyně a provozovny: více na stránce",', s)
assert n == 1
s = sub1(s, "'stat_4': 'od dílny k rodinnému mlýnu'", "'stat_4': 'od dílny k mlýnu'")
s = sub1(s, " Mouka z rodinného mlýna v Havlíčkově Brodě. Bez e-shopu", " Bez e-shopu")
s = sub1(s, " Mouku bereme z mlýna, který vede naše širší rodina. Objednávky", " Objednávky")
s, n = re.subn(r'\("p", "Pšeničná mouka do knedlíkových směsí[^"]*"\)', f'("p", "{T["cs"]["mill"]}")', s)
assert n == 1
s = sub1(s, " Po Vysočině i rozvážíme.", " " + T["cs"]["deliv"])
s = line(s, '("h2", "Rozvoz po Vysočině"),', '("h2", "Rozvoz"),')
s = line(s, '"Humpolec a Havlíčkův Brod: rozvoz zdarma od 1000 Kč",', f'"{T["cs"]["deliv"]}",')
s = line(s, '"Jihlava: zdarma od 3000 Kč",')
s = line(s, '"Zbytek Vysočiny: zdarma od 5000 Kč",')
s = line(s, '"Jinam, po Česku i do zahraničí:')
s = sub1(s, '"Bramborové těsto v prášku z mouky z mlýna v Havlíčkově Brodě a bramborových vloček. Zaděláte vodou', '"Bramborové těsto v prášku. Zaděláte vodou')
s = sub1(s, '"Ne. Těsto funguje jen s vodou. Vejce nebo mléko přidejte, chcete-li bohatší chuť."', '"Ne. Směs zaděláte vodou podle návodu. Vejce přidejte, chcete-li bohatší chuť."')
wr(f, s)

# ---------- FAQs ----------
f = "scripts/geo_faq.py"
s = rd(f)
s = qa(s, '"Platím předem, nebo při převzetí?"', ("Platím předem, nebo při převzetí?", "Při vyzvednutí a rozvozu platíte při převzetí."))
s = qa(s, '"Kdy je rozvoz zdarma?"', ("Kam zboží dovezete?", "Do Humpolce a Havlíčkova Brodu."))
s = qa(s, '"Posíláte i balíkem?"')
s = qa(s, '"Z čeho jsou knedlíky v prášku?"', ("Z čeho jsou knedlíky v prášku?", "Mouka, sušené bramborové vločky, sušená vejce, sůl, prášek do pečiva, bramborový škrob. Zaděláváte vodou podle návodu."))
s = qa(s, '"Jaká je minimální objednávka v Praze?"')
s = qa(s, '"What is the Prague minimum?"')
lines = s.split("\n")


def faq_by_answer(lines, ans_prefix, new):
    """Find a tuple by the start of its answer line; replace or delete question and answer."""
    idx = [i for i, l in enumerate(lines) if l.strip().startswith('"' + ans_prefix)]
    assert len(idx) == 1, (len(idx), ans_prefix)
    i = idx[0]
    ind = re.match(r"\s*", lines[i - 1]).group(0)
    if new is None:
        del lines[i - 1: i + 1]
    else:
        lines[i - 1: i + 1] = [f'{ind}("{new[0]}",', f'{ind} "{new[1]}"),']


for pref, new in [
    ("For pick-up and delivery you pay on hand-over.", ("Do I pay in advance or on collection?", "For pick-up and delivery you pay on hand-over.")),
    ("To Humpolec and Havlíčkův Brod from 1000 Kč", ("Where do you deliver?", "To Humpolec and Havlíčkův Brod.")),
    ("Wheat flour from the mill in Havlíčkův Brod", ("What is in the dumpling mix?", T["en"]["ingr"] + ". Mix with water as directed.")),
    ("Abholung und Lieferung: bei Übergabe.", ("Zahle ich im Voraus oder bei Übergabe?", "Abholung und Lieferung: bei Übergabe.")),
    ("Nach Humpolec und Havlíčkův Brod ab 1000 Kč", ("Wohin liefern Sie?", "Nach Humpolec und Havlíčkův Brod.")),
    ("Aus Weizenmehl der Mühle in Havlíčkův Brod", ("Woraus besteht die Knödelmischung?", T["de"]["ingr"] + ". Mit Wasser nach Anleitung anrühren.")),
    ("Pri vyzdvihnutí a rozvoze platíte pri prevzatí.", ("Platím vopred, alebo pri prevzatí?", "Pri vyzdvihnutí a rozvoze platíte pri prevzatí.")),
    ("Do Humpolca a Havlíčkovho Brodu od 1000 Kč", ("Kam tovar dovezete?", "Do Humpolca a Havlíčkovho Brodu.")),
    ("Z pšeničnej múky z mlyna v Havlíčkovom Brode", ("Z čoho sú knedle v prášku?", T["sk"]["ingr"] + ". Zamiešate s vodou podľa návodu.")),
    ("Do Prahy berieme zmiešanú objednávku od 25 kg.", None),
    ("Eine gemischte Bestellung ab 25 kg.", None),
]:
    faq_by_answer(lines, pref, new)
s = "\n".join(lines)
for q in ('"Can you post a parcel?"', '"Verschicken Sie auch Pakete?"', '"Posielate aj balíkom, napríklad na Slovensko?"'):
    s = qa(s, q)
s = sub1(s, "Ano. Často to vyjde levněji než náš rozvoz mimo bezplatné zóny.", "Ano. Zboží si vyzvedne v dílně v Kochánově.")
s = sub1(s, "Yes. That is often cheaper than our delivery outside the free zones.", "Yes. They collect at the workshop in Kochánov.")
s = sub1(s, "Áno. Často to vyjde lacnejšie než náš rozvoz mimo bezplatných zón.", "Áno. Tovar si vyzdvihne v dielni v Kochánove.")
wr(f, s)

f = "scripts/cocoa_faq.py"
s = rd(f)
s = sub1(s, " Cenu podle množství domluvíme.", "")
s = sub1(s, " Mengenpreise vereinbaren wir.", "")
s = sub1(s, " Cenu podľa množstva dohodneme.", "")
wr(f, s)

# ---------- aeo_pages ----------
f = "scripts/aeo_pages.py"
s = rd(f)
s = sub1(s, '"praha": "Praha (min. 25 kg mix)"', '"praha": "Praha"')
s = s.replace('"Praha — od 25 kg mix"', '"Praha"').replace('"Prague — from 25 kg mixed"', '"Prague"').replace('"Prag — ab 25 kg gemischt"', '"Prag"')
assert "25 kg mix" not in s.split("AEO_UI")[1].split("PAGE_FAQ")[0]
s = sub1(s, '            "Delivery by arrangement; posting costs extra."\n', f'            "{T["en"]["deliv"]}"\n')
s = sub1(s, '            "Lieferung nach Absprache; der Postversand kostet extra."\n', f'            "{T["de"]["deliv"]}"\n')
s = sub1(s, '            "Rozvoz po dohode, poslanie balíkom sa platí zvlášť."\n', f'            "{T["sk"]["deliv"]}"\n')
s = sub1(s, '        "Rozvoz po domluvě, poslání balíkem se platí zvlášť.",\n', f'        "{T["cs"]["deliv"]}",\n')
s, n = re.subn(r'"ceny": \[\n(?:\s+\(.*\),\n)*\s+\],', '"ceny": [],', s)
assert n >= 3, n
s, n = re.subn(r'"do_eu": \[\n(?:\s+\(.*\),\n)*\s+\],', '"do_eu": [],', s)
assert n >= 3, n
s, n = re.subn(r'^\s+\("[^"]*", "[^"]*(?:free zones|bezplatné zóny|bezplatných zón|kostenlosen Zonen|kostenlose Zonen)[^"]*"\),\n', "", s, flags=re.M)
assert n >= 3, n
for a, b in [
    ("Domluvíme vyzvednutí v dílně nebo v Humpolci, případně rozvoz.", "Domluvíme vyzvednutí v dílně nebo v Humpolci, nebo rozvoz do Humpolce a Havlíčkova Brodu."),
    ("Ceník 250 / 260 / 60 / 30 / 270 Kč platí v dílně. Dopravu mimo bezplatné zóny naceníme zvlášť.", "Ceník 250 / 260 / 60 / 30 / 270 Kč platí v dílně."),
    ("Ano, ale většina zákazníků si pro zboží přijede. Mimo Vysočinu pošleme na požádání balík; poštovné platíte celé vy a celkovou částku domluvíme předem.", "Ano, ale zboží si vyzvednete v dílně nebo vám ho dovezeme do Humpolce či Havlíčkova Brodu."),
    ("Rodinná dílna v Kochánově 40, 582 53. Směsi si vyzvednete zdarma v dílně nebo v Humpolci; po Vysočině je po domluvě rozvezeme.", "Rodinná dílna v Kochánově 40, 582 53. Směsi si vyzvednete zdarma v dílně nebo v Humpolci. Do Humpolce a Havlíčkova Brodu zboží dovezeme."),
    ("Většina sousedů si pro směsi přijede do dílny. Rozvoz po kraji domluvíme.", "Většina sousedů si pro směsi přijede do dílny. Do Humpolce a Havlíčkova Brodu zboží dovezeme."),
    ("Kdo nemůže přijet, tomu po kraji rozvezeme po domluvě.", "Do Humpolce a Havlíčkova Brodu zboží dovezeme."),
    ("Dílna Jůzlová je 12 km od Havlíčkova Brodu, v Kochánově 40. Mouku KLASA bereme z brodského mlýna naší širší rodiny. Nejdřív", "Dílna Jůzlová je 12 km od Havlíčkova Brodu, v Kochánově 40. Nejdřív"),
    ("Město je 12 km od dílny. Mouka se značkou KLASA je z místního mlýna, který vlastní a vede naše širší rodina.", "Město je 12 km od dílny. Mouka je z místního mlýna."),
    ("Havlíčkův Brod je nejbližší větší město. Pšeničnou mouku se značkou KLASA bereme ze zdejšího mlýna, který vlastní a vede naše širší rodina, 12 km od Kochánova.", "Havlíčkův Brod je nejbližší větší město, 12 km od Kochánova. Mouku bereme ze zdejšího mlýna."),
    ("Když nemůžete přijet, domluvíme rozvoz.", "Do Havlíčkova Brodu zboží dovezeme."),
    ("Z mlýna v Havlíčkově Brodě, se značkou KLASA — mlýn vlastní a vede naše širší rodina.", "Z mlýna v Havlíčkově Brodě."),
    ("Havlíčkův Brod Jůzlová, knedlíky v prášku, mouka KLASA, vyzvednutí Kochánov", "Havlíčkův Brod Jůzlová, knedlíky v prášku, vyzvednutí Kochánov"),
]:
    s = sub1(s, a, b)
s = faq_t(s, "Kdy je rozvoz zdarma?")
s = faq_t(s, "Od kolika je rozvoz po Vysočině zdarma?")
s = faq_t(s, "Od kolika je rozvoz do Havlíčkova Brodu zdarma?")
wr(f, s)

# ---------- aeo_more: Czech-only local wholesale pages ----------
f = "scripts/aeo_more.py"
s = rd(f)
s = faq_t(s, "Od kolika je rozvoz po Humpolci zdarma?")
s = faq_t(s, "Platí ceník i pro větší odběr?")
for a, b in [
    ("Provozovnám na Vysočině dodáváme knedlíky, puding a kakao. Cenu podle množství domluvíme, sazebník na webu není. Vyzvednutí v dílně zdarma.", "Provozovnám dodáváme knedlíky, puding a kakao. Vyzvednutí v dílně zdarma. Do Humpolce a Havlíčkova Brodu zboží dovezeme."),
    ('t("Velkoobchod na Vysočině — Jůzlová"', 't("Velkoobchod — Jůzlová"'),
    ("Restaurace, jídelny a cukrárny v kraji. Vyzvednete v dílně, nebo domluvíme rozvoz. Značky", "Restaurace, jídelny a cukrárny v kraji. Vyzvednete v dílně. Do Humpolce a Havlíčkova Brodu zboží dovezeme. Značky"),
    ("většina si pro zboží přijede, rozvoz po kraji domluvíme.", "většina si pro zboží přijede."),
    (" Cenu podle množství domluvíme telefonem nebo velkoobchodním formulářem.", ""),
    (" tu platí jako výchozí bod; větší množství oceníme zvlášť.", " tu platí."),
]:
    s = sub1(s, a, b)
i = s.index('"velkoobchod_praha": page(')
j = s.index('"velkoobchod_zahranici": page(')
k = s.index("\n        ),\n", j) + len("\n        ),\n")
DELIV = T["cs"]["deliv"]


def plain(key, title, h1, keywords):
    desc = f"Provozovny si zboží vyzvednou v dílně v Kochánově 40, 582 53; den a hodinu domluvíme po telefonu. {DELIV}"
    sub = f"Vyzvednete v dílně v Kochánově po domluvě. {DELIV}"
    return f'''"{key}": page(
            "{title}",
            "{desc}",
            "{h1}",
            "{sub}",
            [
                ("links", "b2b"),
                ("form_b2b", None),
            ],
            [],
            "{keywords}",
        ),
'''


new = ("# Czech-only pages, so these need no translations.\n        "
       + plain("velkoobchod_praha", "Velkoobchod pro Prahu — odběr v dílně | Jůzlová", "Velkoobchod pro Prahu", "velkoobchod Praha Jůzlová, knedlíky v prášku")
       + "        " + plain("velkoobchod_brno", "Velkoobchod pro Brno — odběr v dílně | Jůzlová", "Velkoobchod pro Brno", "velkoobchod Brno Jůzlová, knedlíky v prášku")
       + "        " + plain("velkoobchod_zahranici", "Velkoobchod mimo Česko — odběr v dílně | Jůzlová", "Velkoobchod mimo Česko", "velkoobchod Jůzlová, odběr v dílně"))
s = s[:i] + new + s[k:]
wr(f, s)

# ---------- seo keywords, structured data, llms ----------
f = "scripts/seo_data.py"
s = rd(f)
s, n = re.subn(r", KLASA(?: flour| Mehl| mouka| múka)?", "", s)
assert n >= 8, n
s = s.replace(", cena podle množství", "")
wr(f, s)

f = "scripts/build_site.py"
s = rd(f)
s = line(s, '"delivery_free_vysocina: nad 5000 Kč",')
s = line(s, '"delivery_free_humpolec_hb: nad 1000 Kč', '"delivery: Humpolec, Havlíčkův Brod",')
s = line(s, '"delivery_free_jihlava: nad 3000 Kč')
s = line(s, '"eu_shipping: DE/AT/SK/PL')
s = sub1(s, "školy, výrobci zmrzliny; cena podle množství; bez jmen zákazníků", "školy, výrobci zmrzliny; bez jmen zákazníků")
s = line(s, '"Pšeničná mouka z mlýna v Havlíčkově Brodě (12 km)',
         '"Mouka z mlýna v Havlíčkově Brodě (12 km). Těsto se zadělává vodou podle návodu. Prodáváme přímo z dílny, po kilech.",')
s = line(s, '"Free Vysočina delivery from 5000 CZK;', '"Delivery to Humpolec and Havlíčkův Brod",')
a = s.index('    if ui.get("form_fulfill_two_cities"):')
b = s.index('    fulfill = "\\n".join(', a)
s = s[:a] + ('    fulfill_opts = [("factory", ui["form_fulfill_factory"]),\n'
             '                    ("delivery_hb_humpolec", ui["form_fulfill_two_cities"])]\n') + s[b:]
wr(f, s)

f = "server/app.py"
s = rd(f)
s, n = re.subn(r'"praha": "[^"]*25 kg[^"]*"', '"praha": "Praha"', s)
assert n == 1, n
wr(f, s)

for f, s in BUF.items():
    pathlib.Path(f).write_text(s)
print("settled:", ", ".join(sorted(BUF)))
