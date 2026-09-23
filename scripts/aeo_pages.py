"""Multi-market AEO pages, extra FAQs, and UI strings.

Czech is the source of truth. DE / SK / EN are native, not relabeled Czech.
Do not invent reviews, wholesale rates, samples, or supplier brand names.

NEVER mention cocoa (or other ingredient) suppliers — not the brand name, and
not a FAQ that says we refuse to name them. Describe the product only
(Dutch-process / holandský typ, fat %, sugar, allergens, use).
"""

from aeo_more import more_pages

GEO_SLUGS = {
    "objednavka_cesko": "objednavka",
    "vysocina": "vysocina",
    "havlickuv_brod": "havlickuv-brod",
    "humpolec": "humpolec",
    "kochanov": "kochanov",
    "navstevnikum": "pro-navstevniky",
}

B2B_SLUGS = {
    "velkoobchod_vysocina": "velkoobchod-vysocina",
    "velkoobchod_kochanov": "velkoobchod-kochanov",
    "velkoobchod_praha": "velkoobchod-praha",
    "velkoobchod_brno": "velkoobchod-brno",
    "velkoobchod_zahranici": "velkoobchod-zahranici",
}

AEO_PAGE_KEYS = list(GEO_SLUGS) + list(B2B_SLUGS)

TOPIC_KEYS = [
    "general",
    "praha",
    "brno",
    "vysocina",
    "international",
    "restaurant",
    "bakery",
    "school",
    "icecream",
    "other",
]

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

AEO_UI = {
    "cs": {
        "price_excludes_shipping": (
            "Rozvoz po domluvě, poslání balíkem se platí zvlášť."
        ),
        "form_topic": "Téma poptávky",
        "form_topic_prompt": "Vyberte téma",
        "form_topics": {
            "general": "Obecná velkoobchodní poptávka",
            "praha": "Praha — od 25 kg mix",
            "brno": "Brno",
            "vysocina": "Vysočina",
            "international": "Zahraniční velkoobchod",
            "restaurant": "Restaurace nebo jídelna",
            "bakery": "Pekárna nebo cukrárna",
            "school": "Školní kuchyně",
            "icecream": "Výroba zmrzliny",
            "other": "Jiné",
        },
        "form_b2b_h": "Velkoobchodní poptávka",
        "form_b2b_hint": (
            "Tento formulář je jen pro provozovny. Domácnosti prosíme na stránku Kontakt."
        ),
        "lang_cs": "Čeština",
        "lang_en": "English",
        "lang_de": "Deutsch",
        "lang_sk": "Slovenčina",
        "lang_more": "Další jazyky",
        "reviews_later": (
            "Zákaznické recenze zveřejníme, až je budeme mít z Google profilu. "
            "Hvězdičky ani počet recenzí si nevymýšlíme."
        ),
        "geo_hub": "Objednávka podle místa",
        "b2b_hub": "Velkoobchod podle místa",
    },
    "en": {
        "price_excludes_shipping": (
            "Delivery by arrangement; posting costs extra."
        ),
        "form_topic": "Enquiry topic",
        "form_topic_prompt": "Choose a topic",
        "form_topics": {
            "general": "General wholesale enquiry",
            "praha": "Prague — from 25 kg mixed",
            "brno": "Brno",
            "vysocina": "Vysočina",
            "international": "International wholesale",
            "restaurant": "Restaurant or canteen",
            "bakery": "Bakery or pastry shop",
            "school": "School kitchen",
            "icecream": "Ice-cream production",
            "other": "Other",
        },
        "form_b2b_h": "Wholesale enquiry",
        "form_b2b_hint": (
            "This form is for kitchens and shops only. Households, please use the Contact page."
        ),
        "lang_cs": "Čeština",
        "lang_en": "English",
        "lang_de": "Deutsch",
        "lang_sk": "Slovenčina",
        "lang_more": "More languages",
        "reviews_later": (
            "We will publish customer reviews only when we have real ones from our Google listing. "
            "We do not invent star ratings or review counts."
        ),
        "geo_hub": "Order by place",
        "b2b_hub": "Wholesale by place",
    },
    "de": {
        "price_excludes_shipping": (
            "Lieferung nach Absprache; der Postversand kostet extra."
        ),
        "form_topic": "Thema der Anfrage",
        "form_topic_prompt": "Thema wählen",
        "form_topics": {
            "general": "Allgemeine Großhandelsanfrage",
            "praha": "Prag — ab 25 kg gemischt",
            "brno": "Brünn",
            "vysocina": "Vysočina",
            "international": "Ausländischer Großhandel",
            "restaurant": "Restaurant oder Kantine",
            "bakery": "Bäckerei oder Konditorei",
            "school": "Schulküche",
            "icecream": "Speiseeisproduktion",
            "other": "Sonstiges",
        },
        "form_b2b_h": "Großhandelsanfrage",
        "form_b2b_hint": (
            "Dieses Formular ist nur für Betriebe. Haushalte nutzen bitte die Kontaktseite."
        ),
        "lang_cs": "Čeština",
        "lang_en": "English",
        "lang_de": "Deutsch",
        "lang_sk": "Slovenčina",
        "lang_more": "Weitere Sprachen",
        "reviews_later": (
            "Kundenbewertungen veröffentlichen wir erst, wenn sie aus unserem Google-Eintrag vorliegen. "
            "Sterne und Bewertungszahlen erfinden wir nicht."
        ),
        "geo_hub": "Bestellung nach Ort",
        "b2b_hub": "Großhandel nach Ort",
    },
    "sk": {
        "price_excludes_shipping": (
            "Rozvoz po dohode, poslanie balíkom sa platí zvlášť."
        ),
        "form_topic": "Téma dopytu",
        "form_topic_prompt": "Vyberte tému",
        "form_topics": {
            "general": "Všeobecný veľkoobchodný dopyt",
            "praha": "Praha — od 25 kg mix",
            "brno": "Brno",
            "vysocina": "Vysočina",
            "international": "Zahraničný veľkoobchod",
            "restaurant": "Reštaurácia alebo jedáleň",
            "bakery": "Pekáreň alebo cukráreň",
            "school": "Školská kuchyňa",
            "icecream": "Výroba zmrzliny",
            "other": "Iné",
        },
        "form_b2b_h": "Veľkoobchodný dopyt",
        "form_b2b_hint": (
            "Tento formulár je len pre prevádzky. Domácnosti prosíme na stránku Kontakt."
        ),
        "lang_cs": "Čeština",
        "lang_en": "English",
        "lang_de": "Deutsch",
        "lang_sk": "Slovenčina",
        "lang_more": "Ďalšie jazyky",
        "reviews_later": (
            "Zákaznícke recenzie zverejníme, až ich budeme mať z Google profilu. "
            "Hviezdičky ani počet recenzií si nevymýšľame."
        ),
        "geo_hub": "Objednávka podľa miesta",
        "b2b_hub": "Veľkoobchod podľa miesta",
    },
}

PAGE_FAQ = {
    "cs": {
        "kdo_jsme": [
            ("Kde přesně jste?", "Kochánov 40, 582 53, Kraj Vysočina, 12 km od Havlíčkova Brodu. Nikoli 582 91 — to je jiný Kochánov."),
            ("Jste s.r.o.?", "Ano. Jůzlová s.r.o., IČO 45900124. Na mapách jsme jako Juzlova - Potravinářské směsi."),
        ],
        "kde_nas_najdete": [
            ("Musím volat předem?", "Ano. Dílna není obchod s otevírací dobou na dveřích. Denně 8:00–19:00 po telefonu, i o víkendu."),
            ("Kde v Humpolci zboží vyzvednu?", "V okolí Pivovaru Bernard, zdarma. Přesné místo a hodinu řekneme po telefonu."),
            ("Můžu poslat vlastního dopravce?", "Ano. Mimo bezplatné zóny to často vyjde levněji než náš rozvoz."),
        ],
        "kontakt": [
            ("Máte otevírací dobu?", "Ne. Dílna není obchod — nejdřív zavolejte. Bereme telefony denně 8:00–19:00 včetně soboty a neděle."),
            ("Dáváte ochutnat?", "Ne. Vzorky ani ochutnávky nenabízíme; objednáváte hotová balení."),
        ],
        "ceny": [
            ("Platí ceny i pro zásilku?", "Ceny zboží ano. Balík posíláme jen na požádání; poštovné, krabici a pojištění platíte celé vy a celkovou částku domluvíme předem."),
            ("Máte slevy pro velké odběry?", "Ano, pro provozovny podle množství. Cenu řekneme po telefonu."),
        ],
        "velkoobchod": [],
        "do_eu": [
            ("Platí se clo?", "Uvnitř EU ne. Balík posíláme na požádání; poštovné, krabici a pojištění platíte celé vy a částku domluvíme předem."),
            ("Odpovíte mi německy?", "Odpovídáme česky; s němčinou si pomáháme překladačem."),
        ],
    },
    "en": {
        "kdo_jsme": [
            ("Where exactly are you?", "Kochánov 40, 582 53, Vysočina Region, Czechia, 12 km from Havlíčkův Brod. Not 582 91 — that is a different Kochánov."),
            ("Are you a registered company?", "Yes. Jůzlová s.r.o., company ID 45900124. On maps we appear as Juzlova - Potravinářské směsi."),
        ],
        "kde_nas_najdete": [
            ("Do I have to phone first?", "Yes. The workshop is not a shop with opening hours on the door. We take calls daily 8:00–19:00, weekends included."),
            ("Where do I collect in Humpolec?", "Near the Bernard brewery, free of charge. We give the exact spot and time by phone."),
            ("Can I send my own courier?", "Yes. Outside the free zones it is often cheaper than our delivery."),
        ],
        "kontakt": [
            ("Do you have opening hours?", "No. The workshop is not a shop — phone first. We take calls daily 8:00–19:00 including Saturday and Sunday."),
            ("Can I taste before buying?", "No. We do not offer samples or tasting; you order finished packs."),
        ],
        "ceny": [
            ("Do the prices apply to parcels?", "The goods prices do. We post a parcel only on request; you pay the full postage, box and insurance, and we agree the total first."),
            ("Are there quantity discounts?", "Yes, for kitchens and shops by quantity. We quote by phone."),
        ],
        "velkoobchod": [],
        "do_eu": [
            ("Is there customs duty?", "Not inside the EU. We post on request; you pay the full postage, box and insurance, and we agree the total first."),
            ("Do you reply in English?", "We reply in Czech; for English and German we sometimes use a translation tool."),
        ],
    },
    "de": {
        "kdo_jsme": [
            ("Wo genau sind Sie?", "Kochánov 40, 582 53, Region Vysočina, Tschechien, 12 km von Havlíčkův Brod. Nicht 582 91 — das ist ein anderes Kochánov."),
            ("Sind Sie ein eingetragenes Unternehmen?", "Ja. Jůzlová s.r.o., IČO 45900124. Auf Karten stehen wir als Juzlova - Potravinářské směsi."),
        ],
        "kde_nas_najdete": [
            ("Muss ich vorher anrufen?", "Ja. Die Werkstatt ist kein Laden mit Öffnungszeiten an der Tür. Täglich 8:00–19:00 Uhr telefonisch, auch am Wochenende."),
            ("Wo hole ich in Humpolec ab?", "In der Nähe der Brauerei Bernard, kostenlos. Ort und Uhrzeit nennen wir telefonisch."),
            ("Kann ich einen eigenen Spediteur schicken?", "Ja. Außerhalb der Gratiszonen ist das oft günstiger als unsere Lieferung."),
        ],
        "kontakt": [
            ("Haben Sie Öffnungszeiten?", "Nein. Die Werkstatt ist kein Laden — bitte zuerst anrufen. Telefonisch täglich 8:00–19:00 Uhr, auch samstags und sonntags."),
            ("Kann ich vorher probieren?", "Nein. Muster oder Verkostung bieten wir nicht; Sie bestellen fertige Packungen."),
        ],
        "ceny": [
            ("Gelten die Preise auch für Pakete?", "Die Warenpreise ja. Ein Paket schicken wir nur auf Wunsch; Porto, Karton und Versicherung zahlen Sie vollständig, die Gesamtsumme vereinbaren wir vorab."),
            ("Gibt es Mengenrabatt?", "Ja, für Betriebe nach Menge. Den Preis nennen wir telefonisch."),
        ],
        "velkoobchod": [],
        "do_eu": [
            ("Fällt Zoll an?", "Innerhalb der EU nicht. Wir versenden auf Wunsch; Porto, Karton und Versicherung zahlen Sie vollständig, die Summe vereinbaren wir vorab."),
            ("Antworten Sie auf Deutsch?", "Wir antworten auf Tschechisch; für Deutsch nutzen wir manchmal ein Übersetzungsprogramm."),
        ],
    },
    "sk": {
        "kdo_jsme": [
            ("Kde presne ste?", "Kochánov 40, 582 53, kraj Vysočina, Česko, 12 km od Havlíčkovho Brodu. Nie 582 91 — to je iný Kochánov."),
            ("Ste s.r.o.?", "Áno. Jůzlová s.r.o., IČO 45900124. Na mapách sme ako Juzlova - Potravinářské směsi."),
        ],
        "kde_nas_najdete": [
            ("Musím volať vopred?", "Áno. Dielňa nie je obchod s otváracími hodinami na dverách. Denne 8:00–19:00 po telefóne, aj cez víkend."),
            ("Kde v Humpolci tovar vyzdvihnem?", "V okolí Pivovaru Bernard, zadarmo. Presné miesto a hodinu povieme po telefóne."),
            ("Môžem poslať vlastného dopravcu?", "Áno. Mimo bezplatných zón to často vyjde lacnejšie než náš rozvoz."),
        ],
        "kontakt": [
            ("Máte otváracie hodiny?", "Nie. Dielňa nie je obchod — najprv zavolajte. Telefóny berieme denne 8:00–19:00 vrátane soboty a nedele."),
            ("Dáte ochutnať?", "Nie. Vzorky ani ochutnávky neponúkame; objednávate hotové balenia."),
        ],
        "ceny": [
            ("Platia ceny aj pre zásielku?", "Ceny tovaru áno. Balík posielame len na požiadanie; poštovné, krabicu a poistenie platíte celé vy a celkovú sumu dohodneme vopred."),
            ("Máte zľavy pre veľké odbery?", "Áno, pre prevádzky podľa množstva. Cenu povieme po telefóne."),
        ],
        "velkoobchod": [],
        "do_eu": [
            ("Platí sa clo?", "V rámci EÚ nie. Balík posielame na požiadanie; poštovné, krabicu a poistenie platíte celé vy a sumu dohodneme vopred."),
            ("Odpoviete mi po slovensky?", "Odpovedáme po česky — rozumieme si bez problémov."),
        ],
    },
}

PRODUCT_FAQ_EXTRA = {
    "cs": {
        "bramborove_knedliky": [
            ("Je v ceně 250 Kč i doprava?",
             "Ne. 250 Kč za 5 kg je cena při vyzvednutí v dílně."),
            ("Kde směs vyzvednu?",
             "V Kochánově 40, 582 53, nebo po dohodě v Humpolci u Pivovaru Bernard."),
            ("Vyrábíte kakaový puding?",
             "Ne. Máme jen vanilkový puding bez lepku. Čokoládovou chuť získáte přimícháním kakaa holandského typu."),
        ],
        "chlupate_knedliky": [
            ("Jak rychle jsou chlupaté knedlíky hotové?",
             "Za 15 minut: směs s vodou, vytvarovat, povařit."),
            ("Je 260 Kč s dopravou?",
             "Ne. Cena 5 kg / 260 Kč je jen za zboží při vyzvednutí v dílně."),
            ("Jsou to bosáky?",
             "Ano. Říkáme jim chlupaté knedlíky i bosáky. Hodí se na strapačky a halušky."),
        ],
        "vanilkovy_puding": [
            ("Jaká jsou balení?",
             "1 kg / 60 Kč a 400 g / 30 Kč při vyzvednutí v Kochánově 40, 582 53."),
            ("Je v ceně doprava?",
             "Ne. Uvedená cena platí při vyzvednutí v dílně."),
            ("Můžu z něj udělat čokoládový krém?",
             "Ano. Smíchejte ho s naším kakaem holandského typu. Hotovou kakaovou pudingovou směs nevedeme."),
            ("Hodí se do pečení?",
             "Ano. Je v hruškovém koláči, perníku i věnečcích na tomto webu."),
        ],
        "kakao_holandskeho_typu": [
            ("Je kakao totéž co puding?",
             "Ne. Kakao je kakaový prášek holandského typu, 500 g za 270 Kč. Puding je samostatná vanilková směs."),
            ("Je v 270 Kč doprava?",
             "Ne. 270 Kč je cena při vyzvednutí v dílně."),
        ],
        "vanilkovy_cukr": [
            ("Kolik stojí kilogram?",
             "60 Kč při vyzvednutí v dílně Kochánov 40, 582 53."),
            ("Je doprava v ceně?",
             "Ne. Uvedená cena je jen za zboží."),
            ("Používáte ho v receptech na webu?",
             "Ano. Hodí se do těsta i na posyp cukroví a koláčů."),
            ("Je to vanilkový lusk?",
             "Ne. Je to vanilínový cukr — jemně mletý cukr s vanilínovým aromatem."),
        ],
    },
    "en": {
        "bramborove_knedliky": [
            ("Does 250 Kč include delivery?",
             "No. 250 Kč for 5 kg is the price when you collect at the workshop."),
            ("Where do I collect the mix?",
             "At Kochánov 40, 582 53, or in Humpolec near the Bernard brewery by arrangement."),
            ("Do you make cocoa pudding?",
             "No. We only sell gluten-free vanilla pudding. For a chocolate flavour, stir in Dutch-process cocoa."),
        ],
        "chlupate_knedliky": [
            ("How fast are hairy dumplings ready?",
             "In 15 minutes: mix with water, shape, boil."),
            ("Is 260 Kč with delivery?",
             "No. 5 kg / 260 Kč is for the goods only at workshop pick-up."),
            ("Are these bosáky?",
             "Yes. We call them hairy dumplings or bosáky. They are made for strapačky and halušky."),
        ],
        "vanilkovy_puding": [
            ("What pack sizes are there?",
             "1 kg / 60 Kč and 400 g / 30 Kč at pick-up in Kochánov 40, 582 53."),
            ("Is shipping included?",
             "No. The listed price is the price when you collect at the workshop."),
            ("Can I make a chocolate cream from it?",
             "Yes. Stir in our Dutch-process cocoa. We do not sell a ready-made cocoa pudding mix."),
            ("Does it work in baking?",
             "Yes. It is in the pear cake, gingerbread and cream-puff recipes on this site."),
        ],
        "kakao_holandskeho_typu": [
            ("Is the cocoa the same as pudding?",
             "No. The cocoa is a 500 g pack of Dutch-process powder for 270 Kč. The pudding is a separate vanilla mix."),
            ("Does 270 Kč include delivery?",
             "No. 270 Kč is the price when you collect at the workshop."),
        ],
        "vanilkovy_cukr": [
            ("What does a kilogram cost?",
             "60 Kč at pick-up in Kochánov 40, 582 53."),
            ("Is delivery included?",
             "No. The listed price is for the goods only."),
            ("Do your website recipes use it?",
             "Yes. It goes into doughs and is dusted over biscuits and cakes."),
            ("Is this a vanilla pod?",
             "No. It is vanilla sugar — finely milled sugar with vanillin aroma."),
        ],
    },
    "de": {
        "bramborove_knedliky": [
            ("Sind 250 Kč inklusive Lieferung?",
             "Nein. 250 Kč für 5 kg ist der Preis bei Abholung in der Werkstatt."),
            ("Wo hole ich die Mischung ab?",
             "In Kochánov 40, 582 53 oder nach Absprache in Humpolec bei Pivovar Bernard."),
            ("Machen Sie Kakaopudding?",
             "Nein. Wir führen nur glutenfreien Vanillepudding. Für Schokoladengeschmack rühren Sie Kakao holländischer Art ein."),
        ],
        "chlupate_knedliky": [
            ("Wie schnell sind haarige Knödel fertig?",
             "In 15 Minuten: Mischung mit Wasser, formen, kochen."),
            ("Sind 260 Kč mit Lieferung?",
             "Nein. 5 kg / 260 Kč gelten nur für die Ware bei Abholung."),
            ("Sind das Bosáky?",
             "Ja. Wir nennen sie haarige Knödel oder Bosáky. Sie eignen sich für Strapačky und Halušky."),
        ],
        "vanilkovy_puding": [
            ("Welche Packungen gibt es?",
             "1 kg / 60 Kč und 400 g / 30 Kč bei Abholung in Kochánov 40, 582 53."),
            ("Ist die Lieferung im Preis?",
             "Nein. Der angegebene Preis gilt nur für die Ware."),
            ("Kann ich daraus Schokocreme machen?",
             "Ja. Rühren Sie unseren Kakao holländischer Art ein. Eine fertige Kakaopuddingmischung führen wir nicht."),
            ("Geht er auch zum Backen?",
             "Ja. Er steckt im Birnenkuchen, Lebkuchen und in den Brandteig-Rezepten auf dieser Website."),
        ],
        "kakao_holandskeho_typu": [
            ("Ist Kakao dasselbe wie Pudding?",
             "Nein. Der Kakao ist eine 500-g-Packung Pulver holländischer Art für 270 Kč. Der Pudding ist eine eigene Vanillemischung."),
            ("Sind 270 Kč inklusive Lieferung?",
             "Nein. 270 Kč ist der Preis bei Abholung in der Werkstatt."),
        ],
        "vanilkovy_cukr": [
            ("Was kostet ein Kilogramm?",
             "60 Kč bei Abholung in Kochánov 40, 582 53."),
            ("Ist die Lieferung im Preis?",
             "Nein. Der angegebene Preis gilt nur für die Ware."),
            ("Steckt er in den Rezepten auf der Website?",
             "Ja. Er kommt in den Teig und als Bestreuung auf Gebäck und Kuchen."),
            ("Ist das eine Vanilleschote?",
             "Nein. Es ist Vanillinzucker — fein gemahlener Zucker mit Vanillinaroma."),
        ],
    },
    "sk": {
        "bramborove_knedliky": [
            ("Je v cene 250 Kč aj doprava?",
             "Nie. 250 Kč za 5 kg je cena pri vyzdvihnutí v dielni."),
            ("Kde zmes vyzdvihnem?",
             "V Kochánove 40, 582 53, alebo po dohode v Humpolci pri Pivovare Bernard."),
            ("Vyrábate kakaový puding?",
             "Nie. Máme len vanilkový puding bez lepku. Čokoládovú chuť získate primiešaním kakaa holandského typu."),
        ],
        "chlupate_knedliky": [
            ("Ako rýchlo sú chlpaté knedle hotové?",
             "Za 15 minút: zmes s vodou, vytvarovať, povariť."),
            ("Je 260 Kč s dopravou?",
             "Nie. Cena 5 kg / 260 Kč je len za tovar pri vyzdvihnutí v dielni."),
            ("Sú to bosáky?",
             "Áno. Hovoríme im chlpaté knedle aj bosáky. Hodia sa na strapačky a halušky."),
            ("Dodávate jedálňam?",
             "Áno. Značky prevádzok nemenujeme. Objednávka telefónom alebo veľkoobchodným formulárom."),
        ],
        "vanilkovy_puding": [
            ("Aké sú balenia?",
             "1 kg / 60 Kč a 400 g / 30 Kč pri vyzdvihnutí v Kochánove 40, 582 53."),
            ("Je v cene doprava?",
             "Nie. Uvedená cena je len za tovar."),
            ("Môžem z neho urobiť čokoládový krém?",
             "Áno. Zmiešajte ho s naším kakaom holandského typu. Hotovú kakaovú pudingovú zmes nevedieme."),
            ("Hodí sa do pečenia?",
             "Áno. Je v hruškovom koláči, perníku aj venčekoch na tomto webe."),
        ],
        "kakao_holandskeho_typu": [
            ("Je kakao to isté čo puding?",
             "Nie. Kakao je kakaový prášok holandského typu, 500 g za 270 Kč. Puding je samostatná vanilková zmes."),
            ("Je v 270 Kč doprava?",
             "Nie. 270 Kč je cena pri vyzdvihnutí v dielni."),
        ],
        "vanilkovy_cukr": [
            ("Koľko stojí kilogram?",
             "60 Kč pri vyzdvihnutí v dielni Kochánov 40, 582 53."),
            ("Je doprava v cene?",
             "Nie. Uvedená cena je len za tovar."),
            ("Používate ho v receptoch na webe?",
             "Áno. Hodí sa do cesta aj na posyp cukrovia a koláčov."),
            ("Je to vanilkový struk?",
             "Nie. Je to vanilínový cukor — jemne mletý cukor s vanilínovou arómou."),
        ],
    },
}


def _p(cs, en, de, sk, lang):
    return {"cs": cs, "en": en, "de": de, "sk": sk}[lang]


def aeo_page(lang, key):
    pack = AEO_PAGES[lang][key]
    return pack


def merge_product_faq(lang, key, existing):
    extra = (PRODUCT_FAQ_EXTRA.get(lang) or PRODUCT_FAQ_EXTRA["cs"]).get(key) or []
    seen = {q for q, _a in existing}
    out = list(existing)
    for item in extra:
        if item[0] not in seen:
            out.append(item)
            seen.add(item[0])
    return out[:24]


def page_faq(lang, key):
    pack = PAGE_FAQ.get(lang) or PAGE_FAQ["cs"]
    return list(pack.get(key) or [])


def apply_aeo_ui(L):
    extra = AEO_UI.get(L["code"]) or AEO_UI["cs"]
    ui = L["ui"]
    for key, value in extra.items():
        if key not in ui:
            ui[key] = value
    return L


def _page(title, desc, h1, sub, body, faq, keywords=""):
    return {
        "title": title,
        "desc": desc,
        "h1": h1,
        "sub": sub,
        "body": body,
        "faq": faq,
        "keywords": keywords,
    }


def _build_pages(lang):
    t = lambda cs, en, de, sk: _p(cs, en, de, sk, lang)
    price = t(
        "Rozvoz po domluvě, poslání balíkem se platí zvlášť.",
        "Delivery by arrangement; posting costs extra.",
        "Lieferung nach Absprache; der Postversand kostet extra.",
        "Rozvoz po dohode, poslanie balíkom sa platí zvlášť.",
    )
    first = {
        "objednavka_cesko": _page(
            t("Jak objednat knedlíky v prášku — vyzvednutí v Kochánově",
              "How to order — collect in Kochánov | Jůzlová",
              "So bestellen Sie — Abholung in Kochánov | Jůzlová",
              "Ako objednať — vyzdvihnutie v Kochánove | Jůzlová"),
            t("Objednáte telefonem nebo formulářem, e-shop nemáme. Zboží si zdarma vyzvednete v dílně v Kochánově 40 nebo v Humpolci. Telefon denně 8:00–19:00.",
              "Order by phone or the form; there is no web shop. Collect free of charge at the workshop, Kochánov 40, or in Humpolec. We take calls daily 8:00–19:00.",
              "Bestellung telefonisch oder per Formular, ohne Onlineshop. Kostenlose Abholung in der Werkstatt Kochánov 40 oder in Humpolec, nach Anruf.",
              "Objednáte telefónom alebo formulárom, e-shop nemáme. Tovar si zadarmo vyzdvihnete v dielni v Kochánove 40 alebo v Humpolci. Telefón denne 8:00–19:00."),
            t("Jak objednat: zavoláte nebo napíšete a zboží si vyzvednete v dílně",
              "How to order: phone or write, then collect at the workshop",
              "So bestellen Sie: anrufen oder schreiben, dann in der Werkstatt abholen",
              "Ako objednať: zavoláte alebo napíšete a tovar si vyzdvihnete v dielni"),
            t("E-shop nemáme a nechybí nám. Řeknete, co a kolik chcete a kde jste. Zbytek zařídíme.",
              "Five mixes from Kochánov 40, 582 53. Order by phone or the form. There is no web shop.",
              "Fünf Mischungen aus Kochánov 40, 582 53. Bestellung telefonisch oder über das Formular. Es gibt keinen Onlineshop.",
              "Päť zmesí z Kochánova 40, 582 53. Objednáte telefónom alebo formulárom. E-shop nemáme."),
            [
                ("p", t(
                    "Jůzlová je malá rodinná dílna v Kochánově na Vysočině. Většina zákazníků si pro zboží přijede osobně. Objednáte telefonem +420 728 466 141 nebo +420 607 629 931, nebo formulářem.",
                    "Jůzlová is a small family workshop in Kochánov in the Vysočina Region. Most customers come and collect in person. Order by phone on +420 728 466 141 or +420 607 629 931, or through the form.",
                    "Jůzlová ist eine kleine Familienwerkstatt in Kochánov in der Vysočina. Die meisten Kunden holen persönlich ab. Bestellung unter +420 728 466 141 oder +420 607 629 931 – oder über das Formular.",
                    "Jůzlová je malá rodinná dielňa v Kochánove na Vysočine. Väčšina zákazníkov si pre tovar príde osobne. Objednáte telefónom +420 728 466 141 alebo +420 607 629 931, alebo formulárom.",
                )),
                ("h2", t("Jak to probíhá", "How it works", "So läuft es", "Ako to prebieha")),
                ("ol", [
                    t("Zavoláte nebo napíšete, které směsi a kolik balení chcete.",
                      "Call or write which mixes and how many packs you want.",
                      "Sie rufen an oder schreiben, welche Mischungen und wie viele Packungen Sie möchten.",
                      "Zavoláte alebo napíšete, ktoré zmesi a koľko balení chcete."),
                    t("Domluvíme vyzvednutí v dílně nebo v Humpolci, případně rozvoz.",
                      "We agree pick-up at the workshop or in Humpolec, or a delivery.",
                      "Wir vereinbaren die Abholung in der Werkstatt oder in Humpolec, oder eine Lieferung.",
                      "Dohodneme vyzdvihnutie v dielni alebo v Humpolci, prípadne rozvoz."),
                    t("Ceník 250 / 260 / 60 / 30 / 270 Kč platí v dílně. Dopravu mimo bezplatné zóny naceníme zvlášť.",
                      "The 250 / 260 / 60 / 30 / 270 Kč price list applies at the workshop. Delivery outside the free zones is quoted separately.",
                      "Die Preise 250 / 260 / 60 / 30 / 270 Kč gelten in der Werkstatt. Die Lieferung außerhalb der Gratiszonen nennen wir separat.",
                      "Cenník 250 / 260 / 60 / 30 / 270 Kč platí v dielni. Dopravu mimo bezplatných zón naceníme zvlášť."),
                ]),
                ("p", price),
                ("links", "geo"),
                ("form", None),
            ],
            [
                (t("Objednáváte po celém Česku?", "Do you take orders from all of Czechia?", "Nehmen Sie Bestellungen aus ganz Tschechien an?", "Objednávate z celého Česka?"),
                 t("Ano, ale většina zákazníků si pro zboží přijede. Mimo Vysočinu pošleme na požádání balík; poštovné platíte celé vy a celkovou částku domluvíme předem.",
                   "Yes, though most customers come and collect. Outside Vysočina we post a parcel on request; you pay the full postage and we agree the total first.",
                   "Ja, auch wenn die meisten Kunden abholen. Außerhalb der Vysočina schicken wir auf Wunsch ein Paket; das Porto zahlen Sie vollständig, die Summe vereinbaren wir vorab.",
                   "Áno, ale väčšina zákazníkov si pre tovar príde. Mimo Vysočiny pošleme na požiadanie balík; poštovné platíte celé vy a celkovú sumu dohodneme vopred.")),
                (t("Máte e-shop?", "Is there a web shop?", "Gibt es einen Onlineshop?", "Máte e-shop?"),
                 t("Ne. Objednávka telefonem nebo formulářem.",
                   "No. Order by phone or the form.",
                   "Nein. Bestellung telefonisch oder über das Formular.",
                   "Nie. Objednávka telefónom alebo formulárom.")),
                (t("Kdy je rozvoz zdarma?", "When is delivery free?", "Wann ist die Lieferung kostenlos?", "Kedy je rozvoz zadarmo?"),
                 t("Po Vysočině od 5000 Kč. Do Humpolce a Havlíčkova Brodu od 1000 Kč. Do Jihlavy od 3000 Kč.",
                   "Across Vysočina from 5000 Kč. To Humpolec and Havlíčkův Brod from 1000 Kč. To Jihlava from 3000 Kč.",
                   "In der Vysočina ab 5000 Kč. Nach Humpolec und Havlíčkův Brod ab 1000 Kč. Nach Jihlava ab 3000 Kč.",
                   "Po Vysočine od 5000 Kč. Do Humpolca a Havlíčkovho Brodu od 1000 Kč. Do Jihlavy od 3000 Kč.")),
                (t("Posíláte vzorky?", "Do you send samples?", "Schicken Sie Muster?", "Posielate vzorky?"),
                 t("Ne. Objednáváte hotová balení.", "No. You order finished packs.", "Nein. Sie bestellen fertige Packungen.", "Nie. Objednávate hotové balenia.")),
                (t("Jaké je PSČ?", "What is the postcode?", "Welche PLZ?", "Aké je PSČ?"),
                 t("582 53. Nikoli 582 91.", "582 53, not 582 91.", "582 53, nicht 582 91.", "582 53. Nie 582 91.")),
            ],
            t("objednávka Jůzlová, knedlíky v prášku, vyzvednutí Kochánov Humpolec",
              "order Jůzlová, dumpling mix, collect in Kochánov, no web shop",
              "Bestellung Jůzlová, Knödelmischung, Abholung Kochánov",
              "objednávka Jůzlová, knedle v prášku, vyzdvihnutie Kochánov"),
        ),
        "vysocina": _page(
            t("Knedlíky v prášku z Vysočiny — dílna Kochánov",
              "Dumpling mix from Vysočina — Kochánov workshop",
              "Knödelmischung aus der Vysočina — Werkstatt Kochánov",
              "Knedle v prášku z Vysočiny — dielňa Kochánov"),
            t("Rodinná dílna v Kochánově 40, 582 53. Směsi si vyzvednete zdarma v dílně nebo v Humpolci; po Vysočině je po domluvě rozvezeme.",
              "A family workshop at Kochánov 40, 582 53. Collect the mixes free at the workshop or in Humpolec; around Vysočina we can deliver by arrangement.",
              "Eine Familienwerkstatt in Kochánov 40, 582 53. Abholung kostenlos in der Werkstatt oder in Humpolec; in der Vysočina liefern wir nach Absprache.",
              "Rodinná dielňa v Kochánove 40, 582 53. Zmesi si vyzdvihnete zadarmo v dielni alebo v Humpolci; po Vysočine ich po dohode rozvezieme."),
            t("Směsi z dílny na Vysočině, k vyzvednutí v Kochánově",
              "Mixes from a Vysočina workshop, collected in Kochánov",
              "Mischungen aus einer Werkstatt in der Vysočina, abgeholt in Kochánov",
              "Zmesi z dielne na Vysočine, na vyzdvihnutie v Kochánove"),
            t("Většina sousedů si pro směsi přijede do dílny. Rozvoz po kraji domluvíme.",
              "Most of our neighbours come to the workshop for their mixes. Delivery around the region is by arrangement.",
              "Die meisten Nachbarn holen ihre Mischungen in der Werkstatt ab. Lieferung in der Region nach Absprache.",
              "Väčšina susedov si pre zmesi príde do dielne. Rozvoz po kraji dohodneme."),
            [
                ("p", t(
                    "Kraj Vysočina je náš domov. Asi 90 % zakázek je místních kolem Kochánova a většina zákazníků si zboží vyzvedne v dílně nebo v Humpolci. Kdo nemůže přijet, tomu po kraji rozvezeme po domluvě.",
                    "The Vysočina Region is our home. About 90% of orders stay close to Kochánov, and most customers collect at the workshop or in Humpolec. If you cannot come, we deliver around the region by arrangement.",
                    "Die Region Vysočina ist unser Zuhause. Etwa 90 % der Aufträge bleiben um Kochánov, und die meisten Kunden holen in der Werkstatt oder in Humpolec ab. Wer nicht kommen kann, dem liefern wir in der Region nach Absprache.",
                    "Kraj Vysočina je náš domov. Asi 90 % zákaziek je miestnych okolo Kochánova a väčšina zákazníkov si tovar vyzdvihne v dielni alebo v Humpolci. Kto nemôže prísť, tomu po kraji rozvezieme po dohode.",
                )),
                ("h2", t("Co u nás koupíte", "What we make", "Was wir herstellen", "Čo u nás kúpite")),
                ("ul", [
                    t("bramborové knedlíky v prášku 5 kg / 250 Kč",
                      "potato dumpling mix 5 kg / 250 Kč",
                      "Kartoffelknödelmischung 5 kg / 250 Kč",
                      "zemiakové knedle v prášku 5 kg / 250 Kč"),
                    t("chlupaté knedlíky 5 kg / 260 Kč",
                      "hairy dumplings 5 kg / 260 Kč",
                      "haarige Knödel 5 kg / 260 Kč",
                      "chlpaté knedle 5 kg / 260 Kč"),
                    t("vanilkový puding 60 Kč / 30 Kč, vanilínový cukr 60 Kč, kakao 270 Kč",
                      "vanilla pudding 60 / 30 Kč, vanilla sugar 60 Kč, cocoa 270 Kč",
                      "Vanillepudding 60 / 30 Kč, Vanillinzucker 60 Kč, Kakao 270 Kč",
                      "vanilkový puding 60 Kč / 30 Kč, vanilínový cukor 60 Kč, kakao 270 Kč"),
                ]),
                ("p", price),
                ("links", "geo"),
                ("form", None),
            ],
            [
                (t("Od kolika je rozvoz po Vysočině zdarma?", "From what amount is Vysočina delivery free?", "Ab welchem Betrag ist die Vysočina-Lieferung kostenlos?", "Od koľkého je rozvoz po Vysočine zadarmo?"),
                 t("Po Vysočině od 5000 Kč, do Humpolce a Havlíčkova Brodu od 1000 Kč, do Jihlavy od 3000 Kč. Pod touto částkou dopravu naceníme.",
                   "Across Vysočina from 5000 Kč, to Humpolec and Havlíčkův Brod from 1000 Kč, to Jihlava from 3000 Kč. Below that we quote the delivery charge.",
                   "In der Vysočina ab 5000 Kč, nach Humpolec und Havlíčkův Brod ab 1000 Kč, nach Jihlava ab 3000 Kč. Darunter nennen wir die Lieferkosten.",
                   "Po Vysočine od 5000 Kč, do Humpolca a Havlíčkovho Brodu od 1000 Kč, do Jihlavy od 3000 Kč. Pod touto sumou dopravu naceníme.")),
                (t("Platí to i o víkendu?", "Does this apply at weekends?", "Gilt das am Wochenende?", "Platí to aj cez víkend?"),
                 t("Telefon bereme denně 8:00–19:00. Termín vyzvednutí nebo rozvozu domluvíme.",
                   "We take calls daily 8:00–19:00 and agree a collection or delivery time with you.",
                   "Telefon täglich 8:00–19:00 Uhr. Abhol- oder Liefertermin vereinbaren wir.",
                   "Telefón denne 8:00–19:00. Termín vyzdvihnutia alebo rozvozu dohodneme.")),
                (t("Je cena s dopravou?", "Is the price with delivery?", "Ist der Preis mit Lieferung?", "Je cena s dopravou?"),
                 t("Ne. Ceník je jen za zboží.", "No. The price list covers the goods only.", "Nein. Die Liste gilt nur für die Ware.", "Nie. Cenník je len za tovar.")),
                (t("Kde sídlíte na Vysočině?", "Where are you based in Vysočina?", "Wo sitzen Sie in der Vysočina?", "Kde sídlite na Vysočine?"),
                 t("Kochánov 40, 582 53, 12 km od Havlíčkova Brodu.",
                   "Kochánov 40, 582 53, 12 km from Havlíčkův Brod.",
                   "Kochánov 40, 582 53, 12 km von Havlíčkův Brod.",
                   "Kochánov 40, 582 53, 12 km od Havlíčkovho Brodu.")),
                (t("Máte kakaový puding?", "Do you make cocoa pudding?", "Haben Sie Kakaopudding?", "Máte kakaový puding?"),
                 t("Ne. Máme vanilkový puding a kakao zvlášť.",
                   "No. We sell vanilla pudding and cocoa separately.",
                   "Nein. Vanillepudding und Kakao führen wir getrennt.",
                   "Nie. Máme vanilkový puding a kakao zvlášť.")),
            ],
            t("knedlíky v prášku Vysočina, Jůzlová Kochánov, vyzvednutí v dílně",
              "dumpling mix Vysočina, Jůzlová Kochánov, workshop collection",
              "Knödelmischung Vysočina, Jůzlová Kochánov, Abholung",
              "knedle v prášku Vysočina, Jůzlová Kochánov, vyzdvihnutie v dielni"),
        ),
        "havlickuv_brod": _page(
            t("Havlíčkův Brod — dílna Jůzlová 12 km od města",
              "Havlíčkův Brod — Jůzlová workshop 12 km away",
              "Havlíčkův Brod — Werkstatt Jůzlová, 12 km entfernt",
              "Havlíčkův Brod — dielňa Jůzlová 12 km od mesta"),
            t("Dílna Jůzlová je 12 km od Havlíčkova Brodu, v Kochánově 40. Mouku KLASA bereme z brodského mlýna naší širší rodiny. Nejdřív zavolejte, denně 8:00–19:00.",
              "The Jůzlová workshop is 12 km from Havlíčkův Brod, at Kochánov 40. Our KLASA flour comes from the town mill run by our extended family. Phone first.",
              "Die Werkstatt Jůzlová liegt 12 km von Havlíčkův Brod in Kochánov 40. Das KLASA-Mehl kommt aus der Mühle unserer Familie in der Stadt. Bitte vorher anrufen.",
              "Dielňa Jůzlová je 12 km od Havlíčkovho Brodu, v Kochánove 40. Múku KLASA berieme z brodského mlyna našej širšej rodiny. Najprv zavolajte."),
            t("Havlíčkův Brod", "Havlíčkův Brod", "Havlíčkův Brod", "Havlíčkův Brod"),
            t("Město je 12 km od dílny. Mouka se značkou KLASA je z místního mlýna, který vlastní a vede naše širší rodina.",
              "The town is 12 km from the workshop. Our KLASA-certified flour comes from the local mill, owned and run by our extended family.",
              "Die Stadt liegt 12 km von der Werkstatt entfernt. Das Mehl mit dem KLASA-Siegel kommt aus der örtlichen Mühle, die unserer erweiterten Familie gehört und von ihr geführt wird.",
              "Mesto je 12 km od dielne. Múka so značkou KLASA je z miestneho mlyna, ktorý vlastní a vedie naša širšia rodina."),
            [
                ("p", t(
                    "Havlíčkův Brod je nejbližší větší město. Pšeničnou mouku se značkou KLASA bereme ze zdejšího mlýna, který vlastní a vede naše širší rodina, 12 km od Kochánova.",
                    "Havlíčkův Brod is the nearest larger town. We buy KLASA-certified wheat flour from the mill here, owned and run by our extended family, 12 km from Kochánov.",
                    "Havlíčkův Brod ist die nächste größere Stadt. Das Weizenmehl mit dem KLASA-Siegel holen wir aus der hiesigen Mühle, die unsere erweiterte Familie besitzt und führt, 12 km von Kochánov.",
                    "Havlíčkův Brod je najbližšie väčšie mesto. Pšeničnú múku so značkou KLASA berieme z tunajšieho mlyna, ktorý vlastní a vedie naša širšia rodina, 12 km od Kochánova.",
                )),
                ("h2", t("Jak objednat z Brodu", "How to order from Brod", "Bestellung aus Brod", "Ako objednať z Brodu")),
                ("p", t(
                    "Zavolejte +420 728 466 141 nebo +420 607 629 931 a přijeďte si pro zboží do Kochánova 40, 582 53. Když nemůžete přijet, domluvíme rozvoz.",
                    "Call +420 728 466 141 or +420 607 629 931 and come to Kochánov 40, 582 53, to collect. If you cannot come, we arrange a delivery.",
                    "Rufen Sie +420 728 466 141 oder +420 607 629 931 an und holen Sie die Ware in Kochánov 40, 582 53 ab. Wenn Sie nicht kommen können, vereinbaren wir eine Lieferung.",
                    "Zavolajte +420 728 466 141 alebo +420 607 629 931 a príďte si pre tovar do Kochánova 40, 582 53. Keď nemôžete prísť, dohodneme rozvoz.",
                )),
                ("p", price),
                ("links", "geo"),
                ("form", None),
            ],
            [
                (t("Můžu jet do dílny?", "Can I drive to the workshop?", "Kann ich zur Werkstatt fahren?", "Môžem ísť do dielne?"),
                 t("Ano. Vyzvednutí v Kochánově je zdarma po telefonu.",
                   "Yes. Pick-up at the workshop is free; please phone first.",
                   "Ja. Die Abholung in Kochánov ist kostenlos; bitte vorher anrufen.",
                   "Áno. Vyzdvihnutie v Kochánove je zadarmo po telefóne.")),
                (t("Od kolika je rozvoz do Havlíčkova Brodu zdarma?", "From what amount is Havlíčkův Brod delivery free?", "Ab wann ist die Lieferung nach Havlíčkův Brod kostenlos?", "Od koľkého je rozvoz do Havlíčkovho Brodu zadarmo?"),
                 t("Od 1000 Kč.", "From 1000 Kč.", "Ab 1000 Kč.", "Od 1000 Kč.")),
                (t("Jak daleko je dílna?", "How far is the workshop?", "Wie weit ist die Werkstatt?", "Ako ďaleko je dielňa?"),
                 t("12 km, Kochánov 40, 582 53.", "12 km, Kochánov 40, 582 53.", "12 km, Kochánov 40, 582 53.", "12 km, Kochánov 40, 582 53.")),
                (t("Odkud je mouka?", "Where is the flour from?", "Woher kommt das Mehl?", "Odkiaľ je múka?"),
                 t("Z mlýna v Havlíčkově Brodě, se značkou KLASA — mlýn vlastní a vede naše širší rodina.",
                   "From the mill in Havlíčkův Brod, with the KLASA quality mark — the mill is owned and run by our extended family.",
                   "Aus der Mühle in Havlíčkův Brod, mit dem KLASA-Siegel — die Mühle gehört unserer erweiterten Familie und wird von ihr geführt.",
                   "Z mlyna v Havlíčkovom Brode, značka KLASA — mlyn vlastní a vedie naša širšia rodina.")),
                (t("Je v ceně doprava?", "Is delivery included?", "Ist die Lieferung im Preis?", "Je v cene doprava?"),
                 t("Ne. Cena na webu je jen za zboží.", "No. The website price is for the goods only.", "Nein. Der Website-Preis gilt nur für die Ware.", "Nie. Cena na webe je len za tovar.")),
            ],
            t("Havlíčkův Brod Jůzlová, knedlíky v prášku, mouka KLASA, vyzvednutí Kochánov",
              "Havlíčkův Brod Jůzlová, dumpling mix, KLASA flour, collect in Kochánov",
              "Havlíčkův Brod Jůzlová, Knödelmischung, KLASA Mehl",
              "Havlíčkův Brod Jůzlová, knedle v prášku, múka KLASA"),
        ),
    }
    first.update(more_pages(lang, t, price, _page))
    return first


AEO_PAGES = {lg: _build_pages(lg) for lg in ("cs", "en", "de", "sk")}
