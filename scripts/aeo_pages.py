"""Multi-market AEO pages, extra FAQs, and UI strings.

Czech is the source of truth. DE / SK / EN are native, not relabeled Czech.
Do not invent reviews, wholesale rates, samples, or supplier brand names.

NEVER mention cocoa (or other ingredient) suppliers — not the brand name, and
not a FAQ that says we refuse to name them. Describe the product only
(Dutch-process / holandský typ, fat %, sugar, allergens, use).
"""

from aeo_more import more_pages

GEO_SLUGS = {
    "objednavka_cesko": "objednavka-cesko",
    "vysocina": "vysocina",
    "havlickuv_brod": "havlickuv-brod",
    "humpolec": "humpolec",
    "kochanov": "kochanov",
    "navstevnikum": "navstevnikum",
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
            "Tento formulář je jen pro provozovny. Domácnosti použijte stránku Kontakt. "
            "Do e-mailu majitelů jde české označení tématu."
        ),
        "de_tooltip": (
            "Německé stránky jsou hotové. Odpovědi z dílny bývají česky; "
            "němčinu si majitelé občas pomáhají překladačem."
        ),
        "lang_cs": "Čeština",
        "lang_en": "English",
        "lang_de": "Deutsch",
        "lang_sk": "Slovenčina",
        "lang_more": "Další jazyky",
        "lang_other": "Jiný jazyk? Napište nám — ozveme se.",
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
            "This form is for kitchens and shops only. Households use the Contact page. "
            "The owner inbox labels the topic in Czech."
        ),
        "de_tooltip": (
            "German pages are live. Workshop replies are usually in Czech; "
            "the owners sometimes use a translator for German."
        ),
        "lang_cs": "Čeština",
        "lang_en": "English",
        "lang_de": "Deutsch",
        "lang_sk": "Slovenčina",
        "lang_more": "More languages",
        "lang_other": "Another language? Write to us and we will reply.",
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
            "Dieses Formular ist nur für Betriebe. Haushalte nutzen die Kontaktseite. "
            "Im Postfach der Inhaber steht das Thema auf Tschechisch."
        ),
        "de_tooltip": (
            "Die deutschen Seiten sind fertig. Antworten aus der Werkstatt sind meist tschechisch; "
            "für Deutsch nutzen die Inhaber manchmal eine Übersetzungshilfe."
        ),
        "lang_cs": "Čeština",
        "lang_en": "English",
        "lang_de": "Deutsch",
        "lang_sk": "Slovenčina",
        "lang_more": "Weitere Sprachen",
        "lang_other": "Andere Sprache? Schreiben Sie uns — wir antworten.",
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
            "Tento formulár je len pre prevádzky. Domácnosti použite stránku Kontakt. "
            "Do e-mailu majiteľov ide české označenie témy."
        ),
        "de_tooltip": (
            "Nemecké stránky sú hotové. Odpovede z dielne bývajú po česky; "
            "nemčinu si majitelia občas pomáhajú prekladačom."
        ),
        "lang_cs": "Čeština",
        "lang_en": "English",
        "lang_de": "Deutsch",
        "lang_sk": "Slovenčina",
        "lang_more": "Ďalšie jazyky",
        "lang_other": "Iný jazyk? Napíšte nám — ozveme sa.",
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
            ("Co je Jůzlová?",
             "Rodinná dílna potravinářských směsí od roku 2004 v Kochánově 40, 582 53 na Vysočině. Pět výrobků: knedlíky v prášku, chlupaté knedlíky, vanilkový puding bez lepku, kakao holandského typu a vanilínový cukr."),
            ("Kdo firmu vede?",
             "Rod Jůzlových má v Kochánově kořeny asi 400 let. Kochánov je obec a vesnice s přibližně 200 obyvateli v okrese Havlíčkův Brod v kraji Vysočina. Rodinnou firmu vedou Jiřina Jůzlová a její manžel Jiří Jůzl. Dcera Lucie Kůželová pomáhá s výrobou, logistikou, balením, prodejem a zákazníky a často vyřizuje i poptávky na oficiální facebookové stránce. Její manžel Filip Kůžel ze Štoků, manželé 25 let, podporuje logistiku a zákazníky. Druhá dcera Jiřiny, Jířa Kennedy-Jůzlová, se stará o nákup surovin, regulační shodu, kvalitu surovin a kontrolu certifikací, aby kvalita držela od farmy po kuchyni. Její manžel Adam Kennedy zajišťuje marketing a vytvořil tento web, aby zákazníci mohli produkty snadno najít, prohlédnout a objednat."),
            ("Odkud berete mouku?",
             "Pšeničná mouka oceněná značkou KLASA pochází z mlýna v Havlíčkově Brodě, 12 km od dílny — mlýn vlastní a vede naše širší rodina."),
            ("Jak se jmenuje firma v papírech?",
             "Jůzlová s.r.o., IČO 45900124. Na mapách je zápis Juzlova - Potravinářské směsi, Kochánov 40, 582 53."),
        ],
        "kde_nas_najdete": [
            ("Kde přesně sídlíte?",
             "Dílna je Kochánov 40, 582 53, kraj Vysočina, 12 km od Havlíčkova Brodu. PSČ je vždy 582 53, nikoli 582 91."),
            ("Je vyzvednutí v Kochánově zdarma?",
             "Ano. V dílně nic za vyzvednutí neúčtujeme. Otevřeno denně 8:00–19:00 po telefonu."),
            ("Kde v Humpolci zboží vyzvednu?",
             "U dcery majitelky v okolí Pivovaru Bernard. Den a hodinu domluvíme. Ulice tu neuvádíme."),
            ("Kdy je rozvoz po Vysočině zdarma?",
             "Od 5000 Kč. Do Humpolce a Havlíčkova Brodu je rozvoz zdarma od 1000 Kč. Do Jihlavy je rozvoz zdarma od 3000 Kč."),
            ("Platí ceník i s dopravou?",
             "Ne. Cena na webu je jen za zboží. Sledovaná doprava, balení a pojištění se účtují zvlášť."),
            ("Najdu vás na mapě?",
             "Ano. Google: Juzlova - Potravinářské směsi. Seznam: mapy.cz, firma 12906730."),
        ],
        "kontakt": [
            ("Na jaké telefony volat?",
             "Jiřina Jůzlová +420 728 466 141, Jiří Jůzl +420 607 629 931. E-mail juzlj@seznam.cz."),
            ("Jste k zastižení i o víkendu?",
             "Ano. Denně 8:00–19:00 po telefonu, včetně soboty a neděle, vždy po předchozí domluvě."),
            ("Můžu objednat formulářem?",
             "Ano. Domácnosti vyplní kontaktní formulář. Provozovny mají samostatný velkoobchodní formulář."),
            ("Posíláte vzorky?",
             "Ne. Objednáváte hotové balení. Ochutnávku na místě nenabízíme."),
            ("Jaké je PSČ dílny?",
             "582 53. Číslo 582 91 patří jinému Kochánovu a u nás neplatí."),
        ],
        "ceny": [
            ("Kolik stojí knedlíky v prášku?",
             "Bramborové knedlíky 5 kg / 250 Kč, chlupaté knedlíky 5 kg / 260 Kč. Ceny platí při vyzvednutí v dílně."),
            ("Kolik stojí puding, cukr a kakao?",
             "Vanilkový puding 1 kg / 60 Kč nebo 400 g / 30 Kč. Vanilínový cukr 1 kg / 60 Kč. Kakao holandského typu 500 g / 270 Kč."),
            ("Je v ceně doprava?",
             "Ne. Uvedená cena je jen za zboží. Sledovaná doprava, balení a pojištění se účtují zvlášť."),
            ("Platí staré ceny z roku 2017?",
             "Ne. Platí jen aktuální ceník na této stránce."),
            ("Kde platím tyto ceny?",
             "Při vyzvednutí v Kochánově 40, 582 53. Po dohodě i v Humpolci."),
        ],
        "velkoobchod": [
            ("Dodáváte restauracím?",
             "Ano. Restauracím, pekárnám, kavárnám, školám i výrobcům zmrzliny. Značky zákazníků nejmenujeme."),
            ("Jaká je minimální objednávka v Praze?",
             "Do Prahy bereme smíšenou objednávku od 25 kg. Cenu podle množství řekneme po telefonu nebo e-mailu."),
            ("Zveřejňujete velkoobchodní ceník?",
             "Ne. Cenu podle množství domluvíme. Mezinárodní sazby na webu nejsou."),
            ("Jak provozovna objedná?",
             "Samostatným velkoobchodním formulářem, nebo na +420 728 466 141 a +420 607 629 931."),
            ("Je rozvoz do Brna zdarma?",
             "Do Brna je rozvoz zdarma od objednávky nad 5000 Kč, po domluvě termínu."),
            ("Můžu poslat vlastního dopravce?",
             "Ano. Často to vyjde levněji než náš rozvoz mimo bezplatné zóny."),
        ],
        "do_eu": [
            ("Posíláte Čechům v EU?",
             "Ano. Nejčastěji do Německa, Rakouska, Slovenska a Polska. Jinde v unii dopravu nacíníme."),
            ("Co platím kromě zboží?",
             "Dopravu, krabici, pojištění a bublinkovou fólii. Částku pošleme před odesláním."),
            ("Je cena na ceníku i s balíkem?",
             "Ne. Ceník platí při vyzvednutí v Kochánově. Uvedená cena je jen za zboží."),
            ("Posíláte vzorky do zahraničí?",
             "Ne. Objednáváte běžná balení. Nic neodesíláme, dokud odsouhlasíte cenu zásilky."),
            ("Jak objednat z Německa nebo Rakouska?",
             "Formulářem na této stránce, e-mailem juzlj@seznam.cz, nebo telefonem. Odpověď bývá česky."),
        ],
    },
    "en": {
        "kdo_jsme": [
            ("What is Jůzlová?",
             "A family food-mix workshop since 2004 at Kochánov 40, 582 53 in the Vysočina Region. Five products: potato dumpling mix, hairy dumplings, gluten-free vanilla pudding, Dutch-process cocoa and vanilla sugar."),
            ("Who runs the workshop?",
             "The Jůzl family traces about 400 years of roots in Kochánov, a municipality and village of roughly 200 inhabitants in Havlíčkův Brod District in the Vysočina Region of the Czech Republic. Jiřina Jůzlová and her husband Jiří Jůzl run the local family business. Their daughter Lucie Kůželová supports production, logistics, packaging, sales and customer contact, and often handles enquiries on the official Facebook page. Lucie’s husband of 25 years, Filip Kůžel from nearby Štoky, helps with logistics and customers. Jiřina’s second daughter, Jířa Kennedy-Jůzlová, supports ingredient sourcing, regulatory compliance, ingredient quality and certification checks so quality holds from farm to kitchen. Her husband, Adam Kennedy, manages marketing and developed this website so customers can find, view and order the products more easily."),
            ("Where does the flour come from?",
             "KLASA-awarded wheat flour from a mill in Havlíčkův Brod, 12 km from the workshop — owned and run by our extended family."),
            ("What is the legal name?",
             "Jůzlová s.r.o., company ID 45900124. Maps list Juzlova - Potravinářské směsi, Kochánov 40, 582 53."),
        ],
        "kde_nas_najdete": [
            ("Where exactly are you?",
             "The workshop is Kochánov 40, 582 53, Vysočina Region, 12 km from Havlíčkův Brod. The postcode is always 582 53, never 582 91."),
            ("Is pick-up in Kochánov free?",
             "Yes. Workshop collection is free. Open daily 8:00–19:00 by phone."),
            ("Where do I collect in Humpolec?",
             "At the owners’ daughter’s place near Pivovar Bernard. We agree the day and time. We do not publish the street."),
            ("When is Vysočina delivery free?",
             "From 5000 CZK. Delivery to Humpolec and Havlíčkův Brod is free from 1000 CZK. Delivery to Jihlava is free from 3000 CZK."),
            ("Does the price list include shipping?",
             "No. The listed price is for the goods only. Tracked delivery, packaging and insurance are extra."),
            ("Are you on a map?",
             "Yes. Google: Juzlova - Potravinářské směsi. Seznam: mapy.cz firm 12906730."),
        ],
        "kontakt": [
            ("Which numbers should I call?",
             "Jiřina Jůzlová +420 728 466 141, Jiří Jůzl +420 607 629 931. E-mail juzlj@seznam.cz."),
            ("Are you reachable at weekends?",
             "Yes. Daily 8:00–19:00 by phone, including Saturday and Sunday, after you arrange a time."),
            ("Can I order with the form?",
             "Yes. Households use the contact form. Kitchens use the separate wholesale form."),
            ("Do you send samples?",
             "No. You order finished packs. We do not offer tasting on site."),
            ("What is the workshop postcode?",
             "582 53. 582 91 belongs to a different Kochánov and is not ours."),
        ],
        "ceny": [
            ("What do the dumpling mixes cost?",
             "Potato dumpling mix 5 kg / 250 CZK, hairy dumplings 5 kg / 260 CZK at workshop pick-up."),
            ("What do pudding, sugar and cocoa cost?",
             "Vanilla pudding 1 kg / 60 CZK or 400 g / 30 CZK. Vanilla sugar 1 kg / 60 CZK. Dutch-process cocoa 500 g / 270 CZK."),
            ("Is shipping included?",
             "No. The listed price is for the goods only. Tracked delivery, packaging and insurance are extra."),
            ("Do 2017 prices still apply?",
             "No. Only the prices on this page apply."),
            ("Where do these prices apply?",
             "At pick-up in Kochánov 40, 582 53. In Humpolec by arrangement."),
        ],
        "velkoobchod": [
            ("Do you supply restaurants?",
             "Yes. Restaurants, bakeries, cafés, schools and ice-cream makers. We do not name customer brands."),
            ("What is the Prague minimum?",
             "A mixed order from 25 kg. We quote the quantity price by phone or e-mail."),
            ("Do you publish wholesale rates?",
             "No. We agree the price by quantity. International rates are not on the site."),
            ("How does a kitchen order?",
             "The separate wholesale form, or +420 728 466 141 and +420 607 629 931."),
            ("Is delivery to Brno free?",
             "Delivery to Brno is free for orders over 5000 CZK, by arrangement."),
            ("Can I send my own courier?",
             "Yes. That is often cheaper than our delivery outside the free zones."),
        ],
        "do_eu": [
            ("Do you ship to Czechs in the EU?",
             "Yes. Most often to Germany, Austria, Slovakia and Poland. Elsewhere in the Union we quote shipping."),
            ("What do I pay besides the goods?",
             "Shipping, a box, insurance and bubble wrap. We send the amount before dispatch."),
            ("Does the price list include the parcel?",
             "No. The list applies at pick-up in Kochánov. The listed price is for the goods only."),
            ("Do you send samples abroad?",
             "No. You order ordinary packs. Nothing leaves until you accept the parcel price."),
            ("How do I order from Germany or Austria?",
             "The form on this page, e-mail juzlj@seznam.cz, or phone. Replies are usually in Czech."),
        ],
    },
    "de": {
        "kdo_jsme": [
            ("Was ist Jůzlová?",
             "Familienwerkstatt für Lebensmittelmischungen seit 2004 in Kochánov 40, 582 53 in der Vysočina. Fünf Produkte: Knödelmischung, haarige Knödel, glutenfreier Vanillepudding, Kakao holländischer Art und Vanillinzucker."),
            ("Wer führt den Betrieb?",
             "Die Familie Jůzl ist seit etwa 400 Jahren in Kochánov verwurzelt — einer Gemeinde und einem Dorf mit rund 200 Einwohnern im Bezirk Havlíčkův Brod in der Region Vysočina in Tschechien. Das lokale Familienunternehmen führen Jiřina Jůzlová und ihr Ehemann Jiří Jůzl. Tochter Lucie Kůželová unterstützt Produktion, Logistik, Verpackung, Verkauf und Kundenkontakt und beantwortet oft Anfragen auch auf der offiziellen Facebook-Seite. Ihr Ehemann seit 25 Jahren, Filip Kůžel aus dem nahegelegenen Štoky, hilft bei Logistik und Kunden. Jiřinas zweite Tochter, Jířa Kennedy-Jůzlová, kümmert sich um Rohstoffeinkauf, regulatorische Vorgaben, Rohstoffqualität und Zertifizierungsprüfungen, damit die Qualität vom Hof bis in die Küche hält. Ihr Ehemann Adam Kennedy betreut das Marketing und hat diese Website aufgebaut, damit Kunden die Produkte leichter finden, ansehen und bestellen können."),
            ("Woher kommt das Mehl?",
             "KLASA-Weizenmehl aus einer Mühle in Havlíčkův Brod, 12 km von der Werkstatt — im Besitz und Betrieb unserer erweiterten Familie."),
            ("Wie heißt die Firma rechtlich?",
             "Jůzlová s.r.o., IČO 45900124. Auf Karten: Juzlova - Potravinářské směsi, Kochánov 40, 582 53."),
        ],
        "kde_nas_najdete": [
            ("Wo genau sitzen Sie?",
             "Die Werkstatt ist Kochánov 40, 582 53, Region Vysočina, 12 km von Havlíčkův Brod. PLZ immer 582 53, niemals 582 91."),
            ("Ist die Abholung in Kochánov kostenlos?",
             "Ja. In der Werkstatt berechnen wir nichts. Täglich 8:00–19:00 Uhr telefonisch."),
            ("Wo hole ich in Humpolec ab?",
             "Bei der Tochter der Inhaber in der Nähe von Pivovar Bernard. Tag und Uhrzeit vereinbaren wir. Die Straße nennen wir hier nicht."),
            ("Wann ist die Lieferung in der Vysočina kostenlos?",
             "Ab 5000 Kč. Nach Humpolec und Havlíčkův Brod ab 1000 Kč. Nach Jihlava ab 3000 Kč."),
            ("Enthält die Preisliste die Lieferung?",
             "Nein. Der angegebene Preis gilt nur für die Ware. Nachverfolgbare Lieferung, Verpackung und Versicherung kommen hinzu."),
            ("Sind Sie auf einer Karte?",
             "Ja. Google: Juzlova - Potravinářské směsi. Seznam: mapy.cz, Firma 12906730."),
        ],
        "kontakt": [
            ("Welche Nummern soll ich anrufen?",
             "Jiřina Jůzlová +420 728 466 141, Jiří Jůzl +420 607 629 931. E-Mail juzlj@seznam.cz."),
            ("Erreichen wir Sie am Wochenende?",
             "Ja. Täglich 8:00–19:00 Uhr telefonisch, auch samstags und sonntags, nach Absprache."),
            ("Kann ich über das Formular bestellen?",
             "Ja. Haushalte nutzen das Kontaktformular. Betriebe das separate Großhandelsformular."),
            ("Schicken Sie Muster?",
             "Nein. Sie bestellen fertige Packungen. Verkostung vor Ort bieten wir nicht."),
            ("Welche PLZ hat die Werkstatt?",
             "582 53. 582 91 gehört zu einem anderen Kochánov und gilt bei uns nicht."),
        ],
        "ceny": [
            ("Was kosten die Knödelmischungen?",
             "Kartoffelknödel 5 kg / 250 Kč, haarige Knödel 5 kg / 260 Kč bei Abholung in der Werkstatt."),
            ("Was kosten Pudding, Zucker und Kakao?",
             "Vanillepudding 1 kg / 60 Kč oder 400 g / 30 Kč. Vanillinzucker 1 kg / 60 Kč. Kakao holländischer Art 500 g / 270 Kč."),
            ("Ist die Lieferung im Preis?",
             "Nein. Der angegebene Preis gilt nur für die Ware. Nachverfolgbare Lieferung, Verpackung und Versicherung kommen hinzu."),
            ("Gelten die Preise von 2017?",
             "Nein. Es gelten nur die Preise auf dieser Seite."),
            ("Wo gelten diese Preise?",
             "Bei Abholung in Kochánov 40, 582 53. In Humpolec nach Absprache."),
        ],
        "velkoobchod": [
            ("Beliefern Sie Restaurants?",
             "Ja. Restaurants, Bäckereien, Cafés, Schulen und Speiseeishersteller. Kundennamen nennen wir nicht."),
            ("Was ist das Minimum für Prag?",
             "Eine gemischte Bestellung ab 25 kg. Den Mengenpreis nennen wir telefonisch oder per E-Mail."),
            ("Veröffentlichen Sie Großhandelspreise?",
             "Nein. Den Preis vereinbaren wir nach Menge. Internationale Sätze stehen nicht auf der Website."),
            ("Wie bestellt ein Betrieb?",
             "Über das separate Großhandelsformular oder +420 728 466 141 und +420 607 629 931."),
            ("Ist die Lieferung nach Brünn kostenlos?",
             "Nach Brünn ist die Lieferung ab Bestellungen über 5000 Kč kostenlos, nach Terminabsprache."),
            ("Kann ich einen eigenen Kurier schicken?",
             "Ja. Das ist oft günstiger als unsere Lieferung außerhalb der Gratiszonen."),
        ],
        "do_eu": [
            ("Schicken Sie an Tschechen in der EU?",
             "Ja. Am häufigsten nach Deutschland, Österreich, Slowakei und Polen. Anderswo in der Union nennen wir die Fracht."),
            ("Was zahle ich außer der Ware?",
             "Versand, Karton, Versicherung und Luftpolsterfolie. Den Betrag schicken wir vor dem Versand."),
            ("Gilt die Preisliste auch fürs Paket?",
             "Nein. Die Liste gilt bei Abholung in Kochánov. Der angegebene Preis gilt nur für die Ware."),
            ("Schicken Sie Muster ins Ausland?",
             "Nein. Sie bestellen normale Packungen. Nichts geht raus, bevor Sie den Paketpreis annehmen."),
            ("Wie bestelle ich aus Deutschland oder Österreich?",
             "Über das Formular, E-Mail juzlj@seznam.cz oder telefonisch. Antworten sind meist tschechisch."),
        ],
    },
    "sk": {
        "kdo_jsme": [
            ("Čo je Jůzlová?",
             "Rodinná dielňa potravinárskych zmesí od roku 2004 v Kochánove 40, 582 53 na Vysočine. Päť výrobkov: knedle v prášku, chlpaté knedle, vanilkový puding bez lepku, kakao holandského typu a vanilínový cukor."),
            ("Kto firmu vedie?",
             "Rod Jůzlových má v Kochánove korene asi 400 rokov. Kochánov je obec a dedina s približne 200 obyvateľmi v okrese Havlíčkův Brod v kraji Vysočina. Rodinnú firmu vedú Jiřina Jůzlová a jej manžel Jiří Jůzl. Dcéra Lucie Kůželová pomáha s výrobou, logistikou, balením, predajom a zákazníkmi a často vybavuje aj dopyty na oficiálnej facebookovej stránke. Jej manžel Filip Kůžel zo Štokov, manželia 25 rokov, podporuje logistiku a zákazníkov. Druhá dcéra Jiřiny, Jířa Kennedy-Jůzlová, sa stará o nákup surovín, regulačnú zhodu, kvalitu surovín a kontrolu certifikácií, aby kvalita držala od farmy po kuchyňu. Jej manžel Adam Kennedy zabezpečuje marketing a vytvoril tento web, aby zákazníci mohli produkty ľahko nájsť, prezrieť a objednať."),
            ("Odkiaľ beriete múku?",
             "Pšeničná múka ocenená značkou KLASA pochádza z mlyna v Havlíčkovom Brode, 12 km od dielne — mlyn vlastní a vedie naša širšia rodina."),
            ("Ako sa volá firma v papieroch?",
             "Jůzlová s.r.o., IČO 45900124. Na mapách je zápis Juzlova - Potravinářské směsi, Kochánov 40, 582 53."),
        ],
        "kde_nas_najdete": [
            ("Kde presne sídlite?",
             "Dielňa je Kochánov 40, 582 53, kraj Vysočina, 12 km od Havlíčkovho Brodu. PSČ je vždy 582 53, nie 582 91."),
            ("Je vyzdvihnutie v Kochánove zadarmo?",
             "Áno. V dielni za vyzdvihnutie nič neúčtujeme. Otvorené denne 8:00–19:00 po telefóne."),
            ("Kde v Humpolci tovar vyzdvihnem?",
             "U dcéry majiteľky v okolí Pivovaru Bernard. Deň a hodinu dohodneme. Ulicu tu neuvádzame."),
            ("Kedy je rozvoz po Vysočine zadarmo?",
             "Od 5000 Kč. Do Humpolca a Havlíčkovho Brodu je rozvoz zadarmo od 1000 Kč. Do Jihlavy je rozvoz zadarmo od 3000 Kč."),
            ("Platí cenník aj s dopravou?",
             "Nie. Cena na webe je len za tovar. Sledovaná doprava, balenie a poistenie sa účtujú zvlášť."),
            ("Nájdem vás na mape?",
             "Áno. Google: Juzlova - Potravinářské směsi. Seznam: mapy.cz, firma 12906730."),
        ],
        "kontakt": [
            ("Na aké telefóny volať?",
             "Jiřina Jůzlová +420 728 466 141, Jiří Jůzl +420 607 629 931. E-mail juzlj@seznam.cz."),
            ("Ste k dispozícii aj cez víkend?",
             "Áno. Denne 8:00–19:00 po telefóne, vrátane soboty a nedele, vždy po predchádzajúcej dohode."),
            ("Môžem objednať formulárom?",
             "Áno. Domácnosti vyplnia kontaktný formulár. Prevádzky majú samostatný veľkoobchodný formulár."),
            ("Posielate vzorky?",
             "Nie. Objednávate hotové balenia. Ochutnávku na mieste neponúkame."),
            ("Aké je PSČ dielne?",
             "582 53. Číslo 582 91 patrí inému Kochánovu a u nás neplatí."),
        ],
        "ceny": [
            ("Koľko stoja knedle v prášku?",
             "Zemiakové knedle 5 kg / 250 Kč, chlpaté knedle 5 kg / 260 Kč. Ceny platia pri vyzdvihnutí v dielni."),
            ("Koľko stoja puding, cukor a kakao?",
             "Vanilkový puding 1 kg / 60 Kč alebo 400 g / 30 Kč. Vanilínový cukor 1 kg / 60 Kč. Kakao holandského typu 500 g / 270 Kč."),
            ("Je v cene doprava?",
             "Nie. Uvedená cena je len za tovar. Sledovaná doprava, balenie a poistenie sa účtujú zvlášť."),
            ("Platía staré ceny z roku 2017?",
             "Nie. Platí len aktuálny cenník na tejto stránke."),
            ("Kde platím tieto ceny?",
             "Pri vyzdvihnutí v Kochánove 40, 582 53. Po dohode aj v Humpolci."),
        ],
        "velkoobchod": [
            ("Dodávate reštauráciám?",
             "Áno. Reštauráciám, pekárňam, kaviarňam, školám aj výrobcom zmrzliny. Značky zákazníkov nemenujeme."),
            ("Aká je minimálna objednávka v Prahe?",
             "Do Prahy berieme zmiešanú objednávku od 25 kg. Cenu podľa množstva povieme po telefóne alebo e-mailom."),
            ("Zverejňujete veľkoobchodný cenník?",
             "Nie. Cenu podľa množstva dohodneme. Medzinárodné sadzby na webe nie sú."),
            ("Ako prevádzka objedná?",
             "Samostatným veľkoobchodným formulárom, alebo na +420 728 466 141 a +420 607 629 931."),
            ("Je rozvoz do Brna zadarmo?",
             "Do Brna je rozvoz zadarmo od objednávky nad 5000 Kč, po dohode termínu."),
            ("Môžem poslať vlastného dopravcu?",
             "Áno. Často to vyjde lacnejšie než náš rozvoz mimo bezplatných zón."),
        ],
        "do_eu": [
            ("Posielate Čechom v EÚ?",
             "Áno. Najčastejšie do Nemecka, Rakúska, Slovenska a Poľska. Inde v únii dopravu nacíníme."),
            ("Čo platím okrem tovaru?",
             "Dopravu, krabicu, poistenie a bublinkovú fóliu. Sumu pošleme pred odoslaním."),
            ("Je cena na cenníku aj s balíkom?",
             "Nie. Cenník platí pri vyzdvihnutí v Kochánove. Uvedená cena je len za tovar."),
            ("Posielate vzorky do zahraničia?",
             "Nie. Objednávate bežné balenia. Nič neodosielame, kým neodsúhlasíte cenu zásielky."),
            ("Ako objednať z Nemecka alebo Rakúska?",
             "Formulárom na tejto stránke, e-mailom juzlj@seznam.cz, alebo telefónom. Odpoveď býva po česky."),
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
             "Ne. Máme jen vanilkový puding bez lepku. Čokoládovou chuť smícháte s kakaem holandského typu."),
        ],
        "chlupate_knedliky": [
            ("Jak rychle jsou chlupaté knedlíky hotové?",
             "Za 15 minut: směs s vodou, vytvarovat, povařit."),
            ("Je 260 Kč s dopravou?",
             "Ne. Cena 5 kg / 260 Kč je jen za zboží při vyzvednutí v dílně."),
            ("Jsou to bosáky?",
             "Ano. Říkáme jim chlupaté knedlíky i bosáky. Hodí se na strapačky a halušky."),
        ],
        "vanilkovy_pudink": [
            ("Jaké jsou balení?",
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
             "Ne. Kakao je 500 g prášek holandského typu, 270 Kč. Puding je samostatná vanilková směs."),
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
             "Ne. Je to vanilínový cukr — jemně mletý cukr s vanilínovým aroma."),
        ],
    },
    "en": {
        "bramborove_knedliky": [
            ("Does 250 CZK include delivery?",
             "No. 250 CZK for 5 kg applies at workshop pick-up. Tracked delivery, packaging and insurance are extra."),
            ("Where do I collect the mix?",
             "At Kochánov 40, 582 53, or in Humpolec near Pivovar Bernard by arrangement."),
            ("Do you make cocoa pudding?",
             "No. We only sell gluten-free vanilla pudding. Chocolate taste comes from Dutch-process cocoa."),
        ],
        "chlupate_knedliky": [
            ("How fast are hairy dumplings ready?",
             "In 15 minutes: mix with water, shape, boil."),
            ("Is 260 CZK with delivery?",
             "No. 5 kg / 260 CZK is for the goods only at workshop pick-up."),
            ("Are these bosáky?",
             "Yes. We call them hairy dumplings and bosáky. They work for strapačky and halušky."),
        ],
        "vanilkovy_pudink": [
            ("What pack sizes are there?",
             "1 kg / 60 CZK and 400 g / 30 CZK at pick-up in Kochánov 40, 582 53."),
            ("Is shipping included?",
             "No. The listed price is for the goods only. Tracked delivery, packaging and insurance are extra."),
            ("Can I make a chocolate cream from it?",
             "Yes. Stir in our Dutch-process cocoa. We do not sell a ready-made cocoa pudding mix."),
            ("Does it work in baking?",
             "Yes. It is in the pear cake, gingerbread and cream-puff recipes on this site."),
        ],
        "kakao_holandskeho_typu": [
            ("Is the cocoa the same as pudding?",
             "No. Cocoa is a 500 g Dutch-process powder at 270 CZK. Pudding is a separate vanilla mix."),
            ("Does 270 CZK include delivery?",
             "No. The price applies at pick-up. Tracked delivery, packaging and insurance are extra."),
        ],
        "vanilkovy_cukr": [
            ("What does a kilogram cost?",
             "60 CZK at pick-up in Kochánov 40, 582 53."),
            ("Is delivery included?",
             "No. The listed price is for the goods only."),
            ("Do your website recipes use it?",
             "Yes. It belongs in dough and as a dusting on biscuits and cakes."),
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
             "Nein. Wir führen nur glutenfreien Vanillepudding. Schokoladengeschmack gibt Kakao holländischer Art."),
        ],
        "chlupate_knedliky": [
            ("Wie schnell sind haarige Knödel fertig?",
             "In 15 Minuten: Mischung mit Wasser, formen, kochen."),
            ("Sind 260 Kč mit Lieferung?",
             "Nein. 5 kg / 260 Kč gelten nur für die Ware bei Abholung."),
            ("Sind das Bosáky?",
             "Ja. Wir sagen haarige Knödel und Bosáky. Sie eignen sich für Strapačky und Halušky."),
        ],
        "vanilkovy_pudink": [
            ("Welche Packungen gibt es?",
             "1 kg / 60 Kč und 400 g / 30 Kč bei Abholung in Kochánov 40, 582 53."),
            ("Ist die Lieferung im Preis?",
             "Nein. Der angegebene Preis gilt nur für die Ware."),
            ("Kann ich daraus Schokocreme machen?",
             "Ja. Mit unserem Kakao holländischer Art. Eine fertige Kakaopuddingmischung führen wir nicht."),
            ("Geht er auch zum Backen?",
             "Ja. Er steckt im Birnenkuchen, Lebkuchen und in den Brandteig-Rezepten auf dieser Website."),
        ],
        "kakao_holandskeho_typu": [
            ("Ist Kakao dasselbe wie Pudding?",
             "Nein. Kakao ist 500 g Pulver holländischer Art für 270 Kč. Pudding ist eine eigene Vanillemischung."),
            ("Sind 270 Kč inklusive Lieferung?",
             "Nein. Der Preis gilt bei Abholung. Lieferung, Verpackung und Versicherung kommen hinzu."),
        ],
        "vanilkovy_cukr": [
            ("Was kostet ein Kilogramm?",
             "60 Kč bei Abholung in Kochánov 40, 582 53."),
            ("Ist die Lieferung im Preis?",
             "Nein. Der angegebene Preis gilt nur für die Ware."),
            ("Steckt er in den Rezepten auf der Website?",
             "Ja. In den Teig und als Bestreuung auf Gebäck und Kuchen."),
            ("Ist das eine Vanilleschote?",
             "Nein. Es ist Vanillinzucker — fein gemahlener Zucker mit Vanillearoma."),
        ],
    },
    "sk": {
        "bramborove_knedliky": [
            ("Je v cene 250 Kč aj doprava?",
             "Nie. 250 Kč za 5 kg platí pri vyzdvihnutí v dielni. Sledovaná doprava, balenie a poistenie sa účtujú zvlášť."),
            ("Kde zmes vyzdvihnem?",
             "V Kochánove 40, 582 53, alebo po dohode v Humpolci pri Pivovare Bernard."),
            ("Vyrábate kakaový puding?",
             "Nie. Máme len vanilkový puding bez lepku. Čokoládovú chuť zmiešate s kakaom holandského typu."),
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
        "vanilkovy_pudink": [
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
             "Nie. Kakao je 500 g prášok holandského typu, 270 Kč. Puding je samostatná vanilková zmes."),
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
             "Nie. Je to vanilínový cukor — jemne mletý cukor s vanilínovým aróma."),
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
    return out[:8]


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
            t("Objednávka po Česku — Jůzlová Kochánov",
              "Order across Czechia — Jůzlová Kochánov",
              "Bestellung in Tschechien — Jůzlová Kochánov",
              "Objednávka po Česku — Jůzlová Kochánov"),
            t("Jůzlová posílá směsi po celé České republice. Objednávka telefonem nebo formulářem. Ceník platí v dílně; doprava zvlášť.",
              "Jůzlová supplies mixes across Czechia. Order by phone or form. Price list applies at the workshop; shipping is extra.",
              "Jůzlová liefert Mischungen in ganz Tschechien. Bestellung telefonisch oder per Formular. Preisliste gilt in der Werkstatt; Lieferung extra.",
              "Jůzlová posiela zmesi po celom Česku. Objednávka telefónom alebo formulárom. Cenník platí v dielni; doprava zvlášť."),
            t("Objednávka po celé České republice",
              "Ordering from anywhere in Czechia",
              "Bestellung aus ganz Tschechien",
              "Objednávka z celého Česka"),
            t("Pět směsí z Kochánova 40, 582 53. Objednáte telefonem, e-mailem nebo formulářem. E-shop nemáme.",
              "Five mixes from Kochánov 40, 582 53. Order by phone, e-mail or the form. There is no web shop.",
              "Fünf Mischungen aus Kochánov 40, 582 53. Bestellung telefonisch, per E-Mail oder Formular. Es gibt keinen Onlineshop.",
              "Päť zmesí z Kochánova 40, 582 53. Objednáte telefónom, e-mailom alebo formulárom. E-shop nemáme."),
            [
                ("p", t(
                    "Jůzlová vyrábí v Kochánově na Vysočině a zásobuje domácnosti v Čechách i na Moravě. Objednávka je telefon +420 728 466 141 nebo +420 607 629 931, e-mail juzlj@seznam.cz, nebo formulář. Denně 8:00–19:00 po telefonu.",
                    "Jůzlová makes mixes in Kochánov in the Vysočina Region and supplies households in Bohemia and Moravia. Order by phone +420 728 466 141 or +420 607 629 931, e-mail juzlj@seznam.cz, or the form. Daily 8:00–19:00 by phone.",
                    "Jůzlová stellt in Kochánov in der Vysočina her und beliefert Haushalte in Böhmen und Mähren. Bestellung unter +420 728 466 141 oder +420 607 629 931, E-Mail juzlj@seznam.cz oder Formular. Täglich 8:00–19:00 Uhr telefonisch.",
                    "Jůzlová vyrába v Kochánove na Vysočine a zásobuje domácnosti v Čechách aj na Morave. Objednávka je telefón +420 728 466 141 alebo +420 607 629 931, e-mail juzlj@seznam.cz, alebo formulár. Denne 8:00–19:00 po telefóne.",
                )),
                ("h2", t("Jak to probíhá", "How it works", "So läuft es", "Ako to prebieha")),
                ("ol", [
                    t("Zavoláte nebo napíšete, které směsi a kolik balení chcete.",
                      "Call or write which mixes and how many packs you want.",
                      "Sie rufen an oder schreiben, welche Mischungen und wie viele Packungen Sie möchten.",
                      "Zavoláte alebo napíšete, ktoré zmesi a koľko balení chcete."),
                    t("Domluvíme vyzvednutí v dílně, Humpolec, nebo rozvoz.",
                      "We agree workshop pick-up, Humpolec, or delivery.",
                      "Wir vereinbaren Abholung in der Werkstatt, Humpolec oder Lieferung.",
                      "Dohodneme vyzdvihnutie v dielni, Humpolec, alebo rozvoz."),
                    t("Ceník 250 / 260 / 60 / 30 / 270 Kč platí v dílně. Doprava mimo bezplatné zóny se nacíní zvlášť.",
                      "The 250 / 260 / 60 / 30 / 270 CZK list applies at the workshop. Delivery outside free zones is quoted separately.",
                      "Die Preise 250 / 260 / 60 / 30 / 270 Kč gelten in der Werkstatt. Lieferung außerhalb der Gratiszonen wird extra angeboten.",
                      "Cenník 250 / 260 / 60 / 30 / 270 Kč platí v dielni. Doprava mimo bezplatných zón sa nacíni zvlášť."),
                ]),
                ("p", price),
                ("links", "geo"),
                ("form", None),
            ],
            [
                (t("Objednáváte po celém Česku?", "Do you take orders from all of Czechia?", "Nehmen Sie Bestellungen aus ganz Tschechien an?", "Objednávate z celého Česka?"),
                 t("Ano. Dílna je na Vysočině; zásilku nebo rozvoz domluvíme. Cena na webu je jen za zboží.",
                   "Yes. The workshop is in Vysočina; we arrange a parcel or delivery. The website price is for the goods only.",
                   "Ja. Die Werkstatt ist in der Vysočina; Paket oder Lieferung vereinbaren wir. Der Website-Preis gilt nur für die Ware.",
                   "Áno. Dielňa je na Vysočine; zásielku alebo rozvoz dohodneme. Cena na webe je len za tovar.")),
                (t("Máte e-shop?", "Is there a web shop?", "Gibt es einen Onlineshop?", "Máte e-shop?"),
                 t("Ne. Objednávka telefonem, e-mailem nebo formulářem.",
                   "No. Order by phone, e-mail or the form.",
                   "Nein. Bestellung telefonisch, per E-Mail oder Formular.",
                   "Nie. Objednávka telefónom, e-mailom alebo formulárom.")),
                (t("Kdy je rozvoz zdarma?", "When is delivery free?", "Wann ist die Lieferung kostenlos?", "Kedy je rozvoz zadarmo?"),
                 t("Po Vysočině od 5000 Kč. Do Humpolce a Havlíčkova Brodu od 1000 Kč. Do Jihlavy od 3000 Kč.",
                   "Across Vysočina from 5000 CZK. To Humpolec and Havlíčkův Brod from 1000 CZK. To Jihlava from 3000 CZK.",
                   "In der Vysočina ab 5000 Kč. Nach Humpolec und Havlíčkův Brod ab 1000 Kč. Nach Jihlava ab 3000 Kč.",
                   "Po Vysočine od 5000 Kč. Do Humpolca a Havlíčkovho Brodu od 1000 Kč. Do Jihlavy od 3000 Kč.")),
                (t("Posíláte vzorky?", "Do you send samples?", "Schicken Sie Muster?", "Posielate vzorky?"),
                 t("Ne. Objednáváte hotová balení.", "No. You order finished packs.", "Nein. Sie bestellen fertige Packungen.", "Nie. Objednávate hotové balenia.")),
                (t("Jaké je PSČ?", "What is the postcode?", "Welche PLZ?", "Aké je PSČ?"),
                 t("582 53. Nikoli 582 91.", "582 53. Never 582 91.", "582 53. Niemals 582 91.", "582 53. Nie 582 91.")),
            ],
            t("objednávka Jůzlová Česko, knedlíky v prášku po republice",
              "order Jůzlová Czechia, dumpling mix nationwide",
              "Bestellung Jůzlová Tschechien, Knödelmischung",
              "objednávka Jůzlová Česko, knedle v prášku"),
        ),
        "vysocina": _page(
            t("Rozvoz po Vysočině — Jůzlová",
              "Vysočina delivery — Jůzlová",
              "Lieferung in der Vysočina — Jůzlová",
              "Rozvoz po Vysočine — Jůzlová"),
            t("Rozvoz směsí Jůzlová po kraji Vysočina je zdarma od 5000 Kč. Dílna Kochánov 40, 582 53.",
              "Jůzlová delivery across the Vysočina Region is free from 5000 CZK. Workshop Kochánov 40, 582 53.",
              "Lieferung der Jůzlová-Mischungen in der Region Vysočina ist ab 5000 Kč kostenlos. Werkstatt Kochánov 40, 582 53.",
              "Rozvoz zmesí Jůzlová po kraji Vysočina je zadarmo od 5000 Kč. Dielňa Kochánov 40, 582 53."),
            t("Rozvoz po kraji Vysočina",
              "Delivery in the Vysočina Region",
              "Lieferung in der Region Vysočina",
              "Rozvoz po kraji Vysočina"),
            t("Od 5000 Kč vezeme po Vysočině zdarma. Dílna je Kochánov 40, 582 53.",
              "From 5000 CZK we deliver across Vysočina free. The workshop is Kochánov 40, 582 53.",
              "Ab 5000 Kč liefern wir in der Vysočina kostenlos. Die Werkstatt ist Kochánov 40, 582 53.",
              "Od 5000 Kč vezieme po Vysočine zadarmo. Dielňa je Kochánov 40, 582 53."),
            [
                ("p", t(
                    "Kraj Vysočina je náš domov. Asi 90 % zakázek je místních kolem Kochánova. Rozvoz po kraji je zdarma, když objednávka přesáhne 5000 Kč. Do Humpolce a Havlíčkova Brodu stačí 1000 Kč. Do Jihlavy stačí 3000 Kč.",
                    "The Vysočina Region is home. About 90% of orders stay near Kochánov. Regional delivery is free above 5000 CZK. Humpolec and Havlíčkův Brod need only 1000 CZK. Jihlava needs 3000 CZK.",
                    "Die Region Vysočina ist unser Zuhause. Etwa 90 % der Aufträge bleiben um Kochánov. Die regionale Lieferung ist ab 5000 Kč kostenlos. Nach Humpolec und Havlíčkův Brod reichen 1000 Kč. Nach Jihlava reichen 3000 Kč.",
                    "Kraj Vysočina je náš domov. Asi 90 % zákaziek je miestnych okolo Kochánova. Rozvoz po kraji je zadarmo, keď objednávka presiahne 5000 Kč. Do Humpolca a Havlíčkovho Brodu stačí 1000 Kč. Do Jihlavy stačí 3000 Kč.",
                )),
                ("h2", t("Co vozíme", "What we deliver", "Was wir liefern", "Čo vozíme")),
                ("ul", [
                    t("bramborové knedlíky v prášku 5 kg / 250 Kč",
                      "potato dumpling mix 5 kg / 250 CZK",
                      "Kartoffelknödelmischung 5 kg / 250 Kč",
                      "zemiakové knedle v prášku 5 kg / 250 Kč"),
                    t("chlupaté knedlíky 5 kg / 260 Kč",
                      "hairy dumplings 5 kg / 260 CZK",
                      "haarige Knödel 5 kg / 260 Kč",
                      "chlpaté knedle 5 kg / 260 Kč"),
                    t("vanilkový puding 60 Kč / 30 Kč, vanilínový cukr 60 Kč, kakao 270 Kč",
                      "vanilla pudding 60 / 30 CZK, vanilla sugar 60 CZK, cocoa 270 CZK",
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
                   "From 5000 CZK. Below that we quote delivery.",
                   "Ab 5000 Kč. Darunter nennen wir die Lieferkosten.",
                   "Od 5000 Kč. Pod touto sumou dopravu nacíníme.")),
                (t("Platí to i o víkendu?", "Does this apply at weekends?", "Gilt das am Wochenende?", "Platí to aj cez víkend?"),
                 t("Telefon denně 8:00–19:00. Termín rozvozu domluvíme.",
                   "Phone daily 8:00–19:00. We agree a delivery slot.",
                   "Telefon täglich 8:00–19:00 Uhr. Den Liefertag vereinbaren wir.",
                   "Telefón denne 8:00–19:00. Termín rozvozu dohodneme.")),
                (t("Je cena s dopravou?", "Is the price with delivery?", "Ist der Preis mit Lieferung?", "Je cena s dopravou?"),
                 t("Ne. Ceník je jen za zboží.", "No. The list is for the goods only.", "Nein. Die Liste gilt nur für die Ware.", "Nie. Cenník je len za tovar.")),
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
              "Vysočina delivery Jůzlová, free from 5000 CZK",
              "Lieferung Vysočina Jůzlová, kostenlos ab 5000 Kč",
              "rozvoz Vysočina Jůzlová, knedle zadarmo od 5000 Kč"),
        ),
        "havlickuv_brod": _page(
            t("Havlíčkův Brod — odběr a rozvoz Jůzlová",
              "Havlíčkův Brod — pick-up and delivery",
              "Havlíčkův Brod — Abholung und Lieferung",
              "Havlíčkův Brod — odber a rozvoz Jůzlová"),
            t("Do Havlíčkova Brodu vozíme zdarma od 1000 Kč. Dílna je 12 km v Kochánově 40, 582 53.",
              "Delivery to Havlíčkův Brod is free from 1000 CZK. The workshop is 12 km away at Kochánov 40, 582 53.",
              "Lieferung nach Havlíčkův Brod ist ab 1000 Kč kostenlos. Die Werkstatt ist 12 km entfernt in Kochánov 40, 582 53.",
              "Do Havlíčkovho Brodu vozíme zadarmo od 1000 Kč. Dielňa je 12 km v Kochánove 40, 582 53."),
            t("Havlíčkův Brod", "Havlíčkův Brod", "Havlíčkův Brod", "Havlíčkův Brod"),
            t("Město je 12 km od dílny. Rozvoz od 1000 Kč zdarma. Mouka KLASA je z místního mlýna, který vlastní a vede naše širší rodina.",
              "The town is 12 km from the workshop. Delivery from 1000 CZK is free. KLASA flour comes from the local mill, owned and run by our extended family.",
              "Die Stadt ist 12 km von der Werkstatt. Lieferung ab 1000 Kč kostenlos. Das KLASA-Mehl kommt aus der örtlichen Mühle, die unserer erweiterten Familie gehört und von ihr geführt wird.",
              "Mesto je 12 km od dielne. Rozvoz od 1000 Kč zadarmo. Múka KLASA je z miestneho mlyna, ktorý vlastní a vedie naša širšia rodina."),
            [
                ("p", t(
                    "Havlíčkův Brod je nejbližší větší město. Pšeničnou mouku KLASA bereme z mlýna tady, který vlastní a vede naše širší rodina, 12 km od Kochánova. Rozvoz do města je zdarma od 1000 Kč — nižší práh než zbytek Vysočiny.",
                    "Havlíčkův Brod is the nearest larger town. We buy KLASA wheat flour from the mill here — owned and run by our extended family — 12 km from Kochánov. Town delivery is free from 1000 CZK — a lower threshold than the rest of Vysočina.",
                    "Havlíčkův Brod ist die nächste größere Stadt. Das KLASA-Weizenmehl holen wir aus der Mühle hier — im Besitz und Betrieb unserer erweiterten Familie —, 12 km von Kochánov. Die Stadtlieferung ist ab 1000 Kč kostenlos — niedriger als in der übrigen Vysočina.",
                    "Havlíčkův Brod je najbližšie väčšie mesto. Pšeničnú múku KLASA berieme z mlyna tu, ktorý vlastní a vedie naša širšia rodina, 12 km od Kochánova. Rozvoz do mesta je zadarmo od 1000 Kč — nižší prah než zvyšok Vysočiny.",
                )),
                ("h2", t("Jak objednat z Brodu", "How to order from Brod", "Bestellung aus Brod", "Ako objednať z Brodu")),
                ("p", t(
                    "Zavolejte +420 728 466 141 nebo +420 607 629 931. Můžete jet do Kochánova 40, 582 53, nebo si nechat zboží přivézt. Ceník platí v dílně.",
                    "Call +420 728 466 141 or +420 607 629 931. You can drive to Kochánov 40, 582 53, or have the goods brought. The price list applies at the workshop.",
                    "Rufen Sie +420 728 466 141 oder +420 607 629 931 an. Sie können nach Kochánov 40, 582 53 fahren oder liefern lassen. Die Preisliste gilt in der Werkstatt.",
                    "Zavolajte +420 728 466 141 alebo +420 607 629 931. Môžete ísť do Kochánova 40, 582 53, alebo si nechať tovar privezť. Cenník platí v dielni.",
                )),
                ("p", price),
                ("links", "geo"),
                ("form", None),
            ],
            [
                (t("Od kolika je rozvoz do Havlíčkova Brodu zdarma?", "From what amount is Havlíčkův Brod delivery free?", "Ab wann ist die Lieferung nach Havlíčkův Brod kostenlos?", "Od koľkého je rozvoz do Havlíčkovho Brodu zadarmo?"),
                 t("Od 1000 Kč.", "From 1000 CZK.", "Ab 1000 Kč.", "Od 1000 Kč.")),
                (t("Jak daleko je dílna?", "How far is the workshop?", "Wie weit ist die Werkstatt?", "Ako ďaleko je dielňa?"),
                 t("12 km, Kochánov 40, 582 53.", "12 km, Kochánov 40, 582 53.", "12 km, Kochánov 40, 582 53.", "12 km, Kochánov 40, 582 53.")),
                (t("Odkud je mouka?", "Where is the flour from?", "Woher kommt das Mehl?", "Odkiaľ je múka?"),
                 t("Z mlýna v Havlíčkově Brodě, značka KLASA — mlýn vlastní a vede naše širší rodina.",
                   "From the mill in Havlíčkův Brod, KLASA mark — owned and run by our extended family.",
                   "Aus der Mühle in Havlíčkův Brod, Marke KLASA — im Besitz und Betrieb unserer erweiterten Familie.",
                   "Z mlyna v Havlíčkovom Brode, značka KLASA — mlyn vlastní a vedie naša širšia rodina.")),
                (t("Je v ceně doprava?", "Is delivery included?", "Ist die Lieferung im Preis?", "Je v cene doprava?"),
                 t("Ne. Cena na webu je jen za zboží.", "No. The website price is for the goods only.", "Nein. Der Website-Preis gilt nur für die Ware.", "Nie. Cena na webe je len za tovar.")),
                (t("Můžu jet do dílny?", "Can I drive to the workshop?", "Kann ich zur Werkstatt fahren?", "Môžem ísť do dielne?"),
                 t("Ano. Vyzvednutí v Kochánově je zdarma po telefonu.",
                   "Yes. Workshop pick-up is free after you phone.",
                   "Ja. Die Abholung in Kochánov ist nach dem Anruf kostenlos.",
                   "Áno. Vyzdvihnutie v Kochánove je zadarmo po telefóne.")),
            ],
            t("Havlíčkův Brod Jůzlová, rozvoz od 1000 Kč, mouka KLASA",
              "Havlíčkův Brod Jůzlová, free delivery from 1000 CZK",
              "Havlíčkův Brod Jůzlová, Lieferung ab 1000 Kč",
              "Havlíčkův Brod Jůzlová, rozvoz od 1000 Kč"),
        ),
    }
    first.update(more_pages(lang, t, price, _page))
    return first


AEO_PAGES = {lg: _build_pages(lg) for lg in ("cs", "en", "de", "sk")}
