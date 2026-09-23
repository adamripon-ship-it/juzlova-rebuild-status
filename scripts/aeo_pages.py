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
            "Uvedená cena je jen za zboží. Sledovaná doprava, balení a pojištění se účtují zvlášť."
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
            "The listed price is for the goods only. Tracked delivery, packaging and insurance are extra."
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
            "Der angegebene Preis gilt nur für die Ware. Nachverfolgbare Lieferung, Verpackung und Versicherung kommen hinzu."
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
            "Uvedená cena je len za tovar. Sledovaná doprava, balenie a poistenie sa účtujú zvlášť."
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
            ("Platí ceny i pro zásilku?", "Ceny zboží ano. K zásilce se přičte sledovaná doprava, balení a pojištění; částku řekneme předem."),
            ("Máte slevy pro velké odběry?", "Ano, pro provozovny podle množství. Cenu řekneme po telefonu."),
        ],
        "velkoobchod": [],
        "do_eu": [
            ("Platí se clo?", "Uvnitř EU ne. Platíte zboží, dopravu, krabici, pojištění a bublinkovou fólii."),
            ("Kam posíláte nejčastěji?", "Do Německa, Rakouska, na Slovensko a do Polska. Jinam v EU dopravu naceníme."),
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
            ("Do the prices apply to parcels?", "The goods prices do. A parcel adds tracked shipping, packaging and insurance; we quote the total in advance."),
            ("Are there quantity discounts?", "Yes, for kitchens and shops by quantity. We quote by phone."),
        ],
        "velkoobchod": [],
        "do_eu": [
            ("Is there customs duty?", "Not inside the EU. You pay the goods, shipping, box, insurance and bubble wrap."),
            ("Where do you ship most?", "Germany, Austria, Slovakia and Poland. Elsewhere in the EU we quote shipping."),
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
            ("Gelten die Preise auch für Pakete?", "Die Warenpreise ja. Beim Paket kommen versicherter Versand mit Sendungsverfolgung und Karton hinzu; die Summe nennen wir vorab."),
            ("Gibt es Mengenrabatt?", "Ja, für Betriebe nach Menge. Den Preis nennen wir telefonisch."),
        ],
        "velkoobchod": [],
        "do_eu": [
            ("Fällt Zoll an?", "Innerhalb der EU nicht. Sie zahlen Ware, Versand, Karton, Versicherung und Luftpolsterfolie."),
            ("Wohin versenden Sie am häufigsten?", "Nach Deutschland, Österreich, in die Slowakei und nach Polen. Anderswo in der EU nennen wir die Versandkosten."),
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
            ("Platia ceny aj pre zásielku?", "Ceny tovaru áno. K zásielke sa pripočíta sledovaná doprava, balenie a poistenie; sumu povieme vopred."),
            ("Máte zľavy pre veľké odbery?", "Áno, pre prevádzky podľa množstva. Cenu povieme po telefóne."),
        ],
        "velkoobchod": [],
        "do_eu": [
            ("Platí sa clo?", "V rámci EÚ nie. Platíte tovar, dopravu, krabicu, poistenie a bublinkovú fóliu."),
            ("Kam posielate najčastejšie?", "Na Slovensko, do Nemecka, Rakúska a Poľska. Inam v EÚ dopravu naceníme."),
            ("Odpoviete mi po slovensky?", "Odpovedáme po česky — rozumieme si bez problémov."),
        ],
    },
}

PRODUCT_FAQ_EXTRA = {
    "cs": {
        "bramborove_knedliky": [
            ("Je v ceně 250 Kč i doprava?",
             "Ne. 250 Kč za 5 kg platí při vyzvednutí v dílně. Sledovaná doprava, balení a pojištění se účtují zvlášť."),
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
             "Ne. Uvedená cena je jen za zboží. Sledovaná doprava, balení a pojištění zvlášť."),
            ("Můžu z něj udělat čokoládový krém?",
             "Ano. Smíchejte ho s naším kakaem holandského typu. Hotovou kakaovou pudingovou směs nevedeme."),
            ("Hodí se do pečení?",
             "Ano. Je v hruškovém koláči, perníku i věnečcích na tomto webu."),
        ],
        "kakao_holandskeho_typu": [
            ("Je kakao totéž co puding?",
             "Ne. Kakao je kakaový prášek holandského typu, 500 g za 270 Kč. Puding je samostatná vanilková směs."),
            ("Je v 270 Kč doprava?",
             "Ne. Cena platí při vyzvednutí. Sledovaná doprava, balení a pojištění se účtují zvlášť."),
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
             "No. 250 Kč for 5 kg applies at workshop pick-up. Tracked delivery, packaging and insurance are extra."),
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
             "No. The listed price is for the goods only. Tracked delivery, packaging and insurance are extra."),
            ("Can I make a chocolate cream from it?",
             "Yes. Stir in our Dutch-process cocoa. We do not sell a ready-made cocoa pudding mix."),
            ("Does it work in baking?",
             "Yes. It is in the pear cake, gingerbread and cream-puff recipes on this site."),
        ],
        "kakao_holandskeho_typu": [
            ("Is the cocoa the same as pudding?",
             "No. The cocoa is a 500 g pack of Dutch-process powder for 270 Kč. The pudding is a separate vanilla mix."),
            ("Does 270 Kč include delivery?",
             "No. The price applies at pick-up. Tracked delivery, packaging and insurance are extra."),
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
             "Nein. 250 Kč für 5 kg gelten bei Abholung in der Werkstatt. Nachverfolgbare Lieferung, Verpackung und Versicherung kommen hinzu."),
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
             "Nein. Der Preis gilt bei Abholung. Lieferung, Verpackung und Versicherung kommen hinzu."),
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
             "Nie. 250 Kč za 5 kg platí pri vyzdvihnutí v dielni. Sledovaná doprava, balenie a poistenie sa účtujú zvlášť."),
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
             "Nie. Cena platí pri vyzdvihnutí. Sledovaná doprava, balenie a poistenie zvlášť."),
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
        "Uvedená cena je jen za zboží. Sledovaná doprava, balení a pojištění se účtují zvlášť.",
        "The listed price is for the goods only. Tracked delivery, packaging and insurance are extra.",
        "Der angegebene Preis gilt nur für die Ware. Nachverfolgbare Lieferung, Verpackung und Versicherung kommen hinzu.",
        "Uvedená cena je len za tovar. Sledovaná doprava, balenie a poistenie sa účtujú zvlášť.",
    )
    first = {
        "objednavka_cesko": _page(
            t("Knedlíky v prášku po celé ČR — bez e-shopu | Jůzlová",
              "Order across Czechia — Jůzlová Kochánov",
              "Bestellung in Tschechien — Jůzlová Kochánov",
              "Objednávka po Česku — Jůzlová Kochánov"),
            t("Objednáte telefonem nebo formulářem. Vyzvednutí v Kochánově a Humpolci zdarma, rozvoz po Vysočině, balík kamkoli po Česku. Doprava zvlášť.",
              "Jůzlová supplies mixes across Czechia. Order by phone or the form; free pick-up in Kochánov and Humpolec. Workshop prices apply; shipping is extra.",
              "Jůzlová liefert Mischungen in ganz Tschechien. Bestellung telefonisch oder über das Formular; Abholung in Kochánov und Humpolec kostenlos. Lieferung extra.",
              "Jůzlová posiela zmesi po celom Česku. Objednávka telefónom alebo formulárom; odber v Kochánove a Humpolci zadarmo. Doprava zvlášť."),
            t("Objednávka po celém Česku: zavoláte nebo napíšete, my domluvíme vyzvednutí, rozvoz nebo balík",
              "Ordering from anywhere in Czechia",
              "Bestellung aus ganz Tschechien",
              "Objednávka z celého Česka"),
            t("E-shop nemáme a nechybí nám. Řeknete, co a kolik chcete a kde jste. Zbytek zařídíme.",
              "Five mixes from Kochánov 40, 582 53. Order by phone or the form. There is no web shop.",
              "Fünf Mischungen aus Kochánov 40, 582 53. Bestellung telefonisch oder über das Formular. Es gibt keinen Onlineshop.",
              "Päť zmesí z Kochánova 40, 582 53. Objednáte telefónom alebo formulárom. E-shop nemáme."),
            [
                ("p", t(
                    "Jůzlová vyrábí v Kochánově na Vysočině a zásobuje domácnosti v Čechách i na Moravě. Objednáte telefonem +420 728 466 141 nebo +420 607 629 931 nebo formulářem. Telefon bereme denně 8:00–19:00.",
                    "Jůzlová makes its mixes in Kochánov in the Vysočina Region and supplies households across Bohemia and Moravia. Order by phone on +420 728 466 141 or +420 607 629 931 or through the form. We take calls daily 8:00–19:00.",
                    "Jůzlová stellt die Mischungen in Kochánov in der Vysočina her und beliefert Haushalte in Böhmen und Mähren. Bestellung unter +420 728 466 141 oder +420 607 629 931 oder über das Formular. Telefonisch täglich 8:00–19:00 Uhr.",
                    "Jůzlová vyrába v Kochánove na Vysočine a zásobuje domácnosti v Čechách aj na Morave. Objednáte telefónom +420 728 466 141 alebo +420 607 629 931 alebo formulárom. Telefón berieme denne 8:00–19:00.",
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
                 t("Ano. Dílna je na Vysočině; zásilku nebo rozvoz domluvíme. Cena na webu je jen za zboží.",
                   "Yes. The workshop is in Vysočina; we arrange a parcel or a delivery. The website price is for the goods only.",
                   "Ja. Die Werkstatt ist in der Vysočina; Paket oder Lieferung vereinbaren wir. Der Website-Preis gilt nur für die Ware.",
                   "Áno. Dielňa je na Vysočine; zásielku alebo rozvoz dohodneme. Cena na webe je len za tovar.")),
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
            t("objednávka Jůzlová Česko, knedlíky v prášku po republice",
              "order Jůzlová Czechia, dumpling mix nationwide, no web shop",
              "Bestellung Jůzlová Tschechien, Knödelmischung",
              "objednávka Jůzlová Česko, knedle v prášku"),
        ),
        "vysocina": _page(
            t("Rozvoz po Vysočině — Jůzlová",
              "Vysočina delivery — Jůzlová",
              "Lieferung in der Vysočina — Jůzlová",
              "Rozvoz po Vysočine — Jůzlová"),
            t("Rozvoz našich směsí po Kraji Vysočina je zdarma od 5000 Kč, do Humpolce a Havlíčkova Brodu od 1000 Kč, do Jihlavy od 3000 Kč. Dílna Kochánov 40, 582 53.",
              "Jůzlová delivers across Vysočina free from 5000 Kč, to Humpolec and Havlíčkův Brod from 1000 Kč, to Jihlava from 3000 Kč. Workshop: Kochánov 40, 582 53.",
              "Jůzlová liefert in der Region Vysočina ab 5000 Kč kostenlos, nach Humpolec und Havlíčkův Brod ab 1000 Kč, nach Jihlava ab 3000 Kč. Werkstatt: Kochánov 40, 582 53.",
              "Rozvoz našich zmesí po kraji Vysočina je zadarmo od 5000 Kč, do Humpolca a Havlíčkovho Brodu od 1000 Kč, do Jihlavy od 3000 Kč. Dielňa Kochánov 40, 582 53."),
            t("Rozvoz po kraji Vysočina",
              "Delivery in the Vysočina Region",
              "Lieferung in der Region Vysočina",
              "Rozvoz po kraji Vysočina"),
            t("Od 5000 Kč vezeme po Vysočině zdarma. Dílna je Kochánov 40, 582 53.",
              "From 5000 Kč we deliver across Vysočina free of charge. The workshop is at Kochánov 40, 582 53.",
              "Ab 5000 Kč liefern wir in der Vysočina kostenlos. Die Werkstatt ist Kochánov 40, 582 53.",
              "Od 5000 Kč vezieme po Vysočine zadarmo. Dielňa je Kochánov 40, 582 53."),
            [
                ("p", t(
                    "Kraj Vysočina je náš domov. Asi 90 % zakázek je místních kolem Kochánova. Rozvoz po kraji je zdarma, když objednávka přesáhne 5000 Kč. Do Humpolce a Havlíčkova Brodu stačí 1000 Kč. Do Jihlavy stačí 3000 Kč.",
                    "The Vysočina Region is our home. About 90% of orders stay close to Kochánov. Regional delivery is free for orders over 5000 Kč. For Humpolec and Havlíčkův Brod the threshold is only 1000 Kč; for Jihlava it is 3000 Kč.",
                    "Die Region Vysočina ist unser Zuhause. Etwa 90 % der Aufträge bleiben um Kochánov. Die regionale Lieferung ist ab 5000 Kč kostenlos. Nach Humpolec und Havlíčkův Brod reichen 1000 Kč. Nach Jihlava reichen 3000 Kč.",
                    "Kraj Vysočina je náš domov. Asi 90 % zákaziek je miestnych okolo Kochánova. Rozvoz po kraji je zadarmo, keď objednávka presiahne 5000 Kč. Do Humpolca a Havlíčkovho Brodu stačí 1000 Kč. Do Jihlavy stačí 3000 Kč.",
                )),
                ("h2", t("Co vozíme", "What we deliver", "Was wir liefern", "Čo vozíme")),
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
                 t("Od 5000 Kč. Pod touto částkou dopravu naceníme.",
                   "From 5000 Kč. Below that we quote the delivery charge.",
                   "Ab 5000 Kč. Darunter nennen wir die Lieferkosten.",
                   "Od 5000 Kč. Pod touto sumou dopravu naceníme.")),
                (t("Platí to i o víkendu?", "Does this apply at weekends?", "Gilt das am Wochenende?", "Platí to aj cez víkend?"),
                 t("Telefon bereme denně 8:00–19:00. Termín rozvozu domluvíme.",
                   "We take calls daily 8:00–19:00 and agree a delivery date with you.",
                   "Telefon täglich 8:00–19:00 Uhr. Den Liefertag vereinbaren wir.",
                   "Telefón denne 8:00–19:00. Termín rozvozu dohodneme.")),
                (t("Je cena s dopravou?", "Is the price with delivery?", "Ist der Preis mit Lieferung?", "Je cena s dopravou?"),
                 t("Ne. Ceník je jen za zboží.", "No. The price list covers the goods only.", "Nein. Die Liste gilt nur für die Ware.", "Nie. Cenník je len za tovar.")),
                (t("Kde sídlíte na Vysočině?", "Where are you based in Vysočina?", "Wo sitzen Sie in der Vysočina?", "Kde sídlite na Vysočine?"),
                 t("Kochánov 40, 582 53, 12 km od Havlíčkova Brodu.",
                   "Kochánov 40, 582 53, 12 km from Havlíčkův Brod.",
                   "Kochánov 40, 582 53, 12 km von Havlíčkův Brod.",
                   "Kochánov 40, 582 53, 12 km od Havlíčkovho Brodu.")),
                (t("Vozíte kakaový puding?", "Do you deliver cocoa pudding?", "Liefern Sie Kakaopudding?", "Vozíte kakaový puding?"),
                 t("Ne. Máme vanilkový puding a kakao zvlášť.",
                   "No. We sell vanilla pudding and cocoa separately.",
                   "Nein. Vanillepudding und Kakao führen wir getrennt.",
                   "Nie. Máme vanilkový puding a kakao zvlášť.")),
            ],
            t("rozvoz Vysočina Jůzlová, knedlíky v prášku zdarma od 5000 Kč",
              "Vysočina delivery Jůzlová, free from 5000 Kč",
              "Lieferung Vysočina Jůzlová, kostenlos ab 5000 Kč",
              "rozvoz Vysočina Jůzlová, knedle zadarmo od 5000 Kč"),
        ),
        "havlickuv_brod": _page(
            t("Havlíčkův Brod — odběr a rozvoz Jůzlová",
              "Havlíčkův Brod — pick-up and delivery",
              "Havlíčkův Brod — Abholung und Lieferung",
              "Havlíčkův Brod — odber a rozvoz Jůzlová"),
            t("Do Havlíčkova Brodu vozíme zdarma od 1000 Kč. Dílna je 12 km daleko v Kochánově 40, 582 53. Nejdřív zavolejte, telefon bereme denně 8:00–19:00.",
              "Delivery to Havlíčkův Brod is free from 1000 Kč. The workshop is 12 km away at Kochánov 40, 582 53. Phone first; we take calls daily 8:00–19:00.",
              "Lieferung nach Havlíčkův Brod ist ab 1000 Kč kostenlos. Die Werkstatt liegt 12 km entfernt in Kochánov 40, 582 53. Bitte vorher anrufen, täglich 8:00–19:00 Uhr.",
              "Do Havlíčkovho Brodu vozíme zadarmo od 1000 Kč. Dielňa je 12 km ďaleko v Kochánove 40, 582 53. Najprv zavolajte, telefón berieme denne 8:00–19:00."),
            t("Havlíčkův Brod", "Havlíčkův Brod", "Havlíčkův Brod", "Havlíčkův Brod"),
            t("Město je 12 km od dílny. Rozvoz je od 1000 Kč zdarma. Mouka se značkou KLASA je z místního mlýna, který vlastní a vede naše širší rodina.",
              "The town is 12 km from the workshop. Delivery is free from 1000 Kč. Our KLASA-certified flour comes from the local mill, owned and run by our extended family.",
              "Die Stadt liegt 12 km von der Werkstatt entfernt. Lieferung ab 1000 Kč kostenlos. Das Mehl mit dem KLASA-Siegel kommt aus der örtlichen Mühle, die unserer erweiterten Familie gehört und von ihr geführt wird.",
              "Mesto je 12 km od dielne. Rozvoz je od 1000 Kč zadarmo. Múka so značkou KLASA je z miestneho mlyna, ktorý vlastní a vedie naša širšia rodina."),
            [
                ("p", t(
                    "Havlíčkův Brod je nejbližší větší město. Pšeničnou mouku se značkou KLASA bereme ze zdejšího mlýna, který vlastní a vede naše širší rodina, 12 km od Kochánova. Rozvoz do města je zdarma od 1000 Kč — nižší práh než pro zbytek Vysočiny.",
                    "Havlíčkův Brod is the nearest larger town. We buy KLASA-certified wheat flour from the mill here, owned and run by our extended family, 12 km from Kochánov. Delivery within the town is free from 1000 Kč — a lower threshold than for the rest of Vysočina.",
                    "Havlíčkův Brod ist die nächste größere Stadt. Das Weizenmehl mit dem KLASA-Siegel holen wir aus der hiesigen Mühle, die unsere erweiterte Familie besitzt und führt, 12 km von Kochánov. Die Lieferung in die Stadt ist ab 1000 Kč kostenlos — eine niedrigere Schwelle als in der übrigen Vysočina.",
                    "Havlíčkův Brod je najbližšie väčšie mesto. Pšeničnú múku so značkou KLASA berieme z tunajšieho mlyna, ktorý vlastní a vedie naša širšia rodina, 12 km od Kochánova. Rozvoz do mesta je zadarmo od 1000 Kč — nižší prah než pre zvyšok Vysočiny.",
                )),
                ("h2", t("Jak objednat z Brodu", "How to order from Brod", "Bestellung aus Brod", "Ako objednať z Brodu")),
                ("p", t(
                    "Zavolejte +420 728 466 141 nebo +420 607 629 931. Můžete jet do Kochánova 40, 582 53, nebo si nechat zboží přivézt. Ceník platí v dílně.",
                    "Call +420 728 466 141 or +420 607 629 931. You can drive to Kochánov 40, 582 53, or have the goods delivered. The price list applies at the workshop.",
                    "Rufen Sie +420 728 466 141 oder +420 607 629 931 an. Sie können nach Kochánov 40, 582 53 fahren oder liefern lassen. Die Preisliste gilt in der Werkstatt.",
                    "Zavolajte +420 728 466 141 alebo +420 607 629 931. Môžete ísť do Kochánova 40, 582 53, alebo si nechať tovar privezť. Cenník platí v dielni.",
                )),
                ("p", price),
                ("links", "geo"),
                ("form", None),
            ],
            [
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
                (t("Můžu jet do dílny?", "Can I drive to the workshop?", "Kann ich zur Werkstatt fahren?", "Môžem ísť do dielne?"),
                 t("Ano. Vyzvednutí v Kochánově je zdarma po telefonu.",
                   "Yes. Pick-up at the workshop is free; please phone first.",
                   "Ja. Die Abholung in Kochánov ist kostenlos; bitte vorher anrufen.",
                   "Áno. Vyzdvihnutie v Kochánove je zadarmo po telefóne.")),
            ],
            t("Havlíčkův Brod Jůzlová, rozvoz od 1000 Kč, mouka KLASA",
              "Havlíčkův Brod Jůzlová, free delivery from 1000 Kč, KLASA flour",
              "Havlíčkův Brod Jůzlová, Lieferung ab 1000 Kč",
              "Havlíčkův Brod Jůzlová, rozvoz od 1000 Kč"),
        ),
    }
    first.update(more_pages(lang, t, price, _page))
    return first


AEO_PAGES = {lg: _build_pages(lg) for lg in ("cs", "en", "de", "sk")}
