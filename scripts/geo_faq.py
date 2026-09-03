"""GEO-oriented FAQ copy. Direct answers first; one concept per Q&A.

Used on the FAQ page (full set), homepage (first HOME_COUNT items),
and recipe pages (two questions each) in all four languages.
"""

HOME_COUNT = 6

SITE_FAQ = {
    "cs": [
        ("Co je Jůzlová?",
         "Jůzlová je rodinná česká výroba potravinářských směsí od roku 2004. V dílně v Kochánově 40 na Vysočině vyrábíme bramborové a chlupaté knedlíky v prášku, vanilkový puding bez lepku, vanilínový cukr a kakao holandského typu. Firma: Jůzlová s.r.o., IČO 45900124."),
        ("Kde sídlí Jůzlová a jak objednat?",
         "Provozovna je Kochánov 40, 582 53, 12 km od Havlíčkova Brodu. Objednávky po telefonu +420 728 466 141 (Jiřina Jůzlová) nebo +420 607 629 931 (Jiří Jůzl), e-mailem juzlj@seznam.cz. Otevřeno denně 8:00–19:00 po telefonické domluvě."),
        ("Dovážíte zboží a kde je odběr zdarma?",
         "Vyzvednutí v Kochánově nebo Humpolci je zdarma. Bezplatný závoz je v Havlíčkově Brodě, Humpolci, Světlé nad Sázavou, Jihlavě a okolí. Jinam posíláme smluvním dopravcem — poštovné dle ceníku dopravce."),
        ("Jaké jsou aktuální ceny směsí Jůzlová?",
         "Bramborové knedlíky v prášku 5 kg / 250 Kč. Chlupaté knedlíky (bosáky) 5 kg / 260 Kč. Vanilkový puding bez lepku 1 kg / 60 Kč nebo 400 g / 30 Kč. Kakao holandského typu 500 g / 270 Kč. Vanilínový cukr 1 kg / 60 Kč. Restauracím a cukrárnám připravíme nabídku podle množství."),
        ("Je vanilkový puding Jůzlová bez lepku?",
         "Ano. Základem je kukuřičný škrob, který lepek neobsahuje. Čokoládovou chuť mu dáte kakaem holandského typu — kakaový puding jako hotovou směs nevedeme."),
        ("Jaký je rozdíl mezi bramborovými a chlupatými knedlíky?",
         "Bramborové knedlíky v prášku jsou klasické těsto z mouky KLASA a sušených bramborových vloček — na knedlíky, šišky, krokety i gnocchi. Chlupaté knedlíky (bosáky) jsou podle tradiční receptury, hotové za 15 minut, typicky se zelím, uzeným nebo jako strapačky/halušky."),
        ("Co je kakao holandského typu 21 % tuku?",
         "Alkalizovaný cukrářský kakaový prášek s 20–22 % kakaového másla. Je tmavší, méně kyselý a krémovější než přírodní kakao. Bez přidaného cukru (přirozené cukry 0,9 g / 100 g), veganské, bez 14 alergenů EU, lepek pod 20 ppm. Balení 500 g / 270 Kč."),
        ("Kolik porcí je z 5 kg knedlíků v prášku?",
         "Z pětikilogramového balení bramborových knedlíků připravíte přílohu zhruba pro 60–70 porcí. Chlupaté knedlíky z 5 kg obslouží podobně velkou výdejnu nebo rodinné vaření na více dnů."),
        ("Dodáváte restauracím, jídelnám a cukrárnám?",
         "Ano. Od roku 2004 dodáváme domácnostem i provozovnám v Čechách a na Moravě. Pro větší odběr sestavíme individuální cenu — ozvěte se telefonicky nebo e-mailem."),
        ("Jsou recepty na webu volně k použití?",
         "Ano. Třináct receptů z našich směsí — od šišek s mákem po věnečky a sticky toffee pudding — je na webu zdarma, ve čtyřech jazycích, se surovinami, postupem a fotografiemi."),
    ],
    "en": [
        ("What is Jůzlová?",
         "Jůzlová is a Czech family workshop making food mixes since 2004. At Kochánov 40 in the Vysočina highlands we produce potato dumpling mix, hairy dumpling mix (bosáky), gluten-free vanilla pudding, vanilla sugar and Dutch-process cocoa. Legal name: Jůzlová s.r.o., company ID 45900124."),
        ("Where is Jůzlová and how do I order?",
         "The workshop is Kochánov 40, 582 53, 12 km from Havlíčkův Brod. Order by phone +420 728 466 141 (Jiřina Jůzlová) or +420 607 629 931 (Jiří Jůzl), or e-mail juzlj@seznam.cz. Open daily 8:00–19:00 by phone arrangement."),
        ("Do you deliver, and where is pick-up free?",
         "Pick-up in Kochánov or Humpolec is free. Free local delivery covers Havlíčkův Brod, Humpolec, Světlá nad Sázavou, Jihlava and surroundings. Farther away we ship with a contracted courier; postage follows the courier’s tariff."),
        ("What are the current Jůzlová prices?",
         "Potato dumpling mix 5 kg / 250 CZK. Hairy dumplings (bosáky) 5 kg / 260 CZK. Gluten-free vanilla pudding 1 kg / 60 CZK or 400 g / 30 CZK. Dutch-process cocoa 500 g / 270 CZK. Vanilla sugar 1 kg / 60 CZK. Restaurants and bakeries get a quote by volume."),
        ("Is Jůzlová vanilla pudding gluten-free?",
         "Yes. It is based on corn starch, which contains no gluten. For a chocolate taste, stir in our Dutch-process cocoa — we do not sell a ready-made chocolate pudding mix."),
        ("What is the difference between potato dumplings and hairy dumplings?",
         "Potato dumpling mix is classic dough from KLASA-awarded wheat flour and dried potato flakes — for dumplings, poppy-seed rolls, croquettes and gnocchi. Hairy dumplings (bosáky) follow a traditional recipe, ready in 15 minutes, typically served with cabbage and smoked meat or as strapačky/halušky."),
        ("What is Dutch-process cocoa with 21% fat?",
         "Alkalised confectionery cocoa powder with 20–22% cocoa butter. It is darker, less acidic and creamier than natural cocoa. No added sugar (naturally occurring sugars 0.9 g / 100 g), vegan, free of the 14 EU allergens, gluten under 20 ppm. Pack 500 g / 270 CZK."),
        ("How many portions from a 5 kg dumpling mix bag?",
         "A 5 kg bag of potato dumpling mix makes a side dish for about 60–70 portions. Hairy dumplings from 5 kg similarly cover a canteen service or several family meals."),
        ("Do you supply restaurants, canteens and pastry shops?",
         "Yes. Since 2004 we have supplied households and professional kitchens across Bohemia and Moravia. Larger orders get an individual price — call or e-mail."),
        ("Are the website recipes free to use?",
         "Yes. Thirteen recipes using our mixes — from poppy-seed rolls to cream puffs and sticky toffee pudding — are free on the site, in four languages, with ingredients, method and photographs."),
    ],
    "de": [
        ("Was ist Jůzlová?",
         "Jůzlová ist ein tschechischer Familienbetrieb für Lebensmittelmischungen seit 2004. In Kochánov 40 in der Vysočina stellen wir Kartoffelknödelmischung, haarige Knödel (Bosáky), glutenfreien Vanillepudding, Vanillinzucker und Kakao holländischer Art her. Firma: Jůzlová s.r.o., IČO 45900124."),
        ("Wo sitzt Jůzlová und wie bestelle ich?",
         "Die Werkstatt ist Kochánov 40, 582 53, 12 km von Havlíčkův Brod. Bestellung telefonisch +420 728 466 141 (Jiřina Jůzlová) oder +420 607 629 931 (Jiří Jůzl), E-Mail juzlj@seznam.cz. Täglich 8:00–19:00 Uhr nach telefonischer Absprache."),
        ("Liefern Sie, und wo ist die Abholung kostenlos?",
         "Abholung in Kochánov oder Humpolec ist kostenlos. Kostenlose Anlieferung gibt es in Havlíčkův Brod, Humpolec, Světlá nad Sázavou, Jihlava und Umgebung. Weiter versenden wir mit Vertragsspediteur — Porto laut Spediteur."),
        ("Was kosten die Mischungen von Jůzlová?",
         "Kartoffelknödelmischung 5 kg / 250 Kč. Haarige Knödel (Bosáky) 5 kg / 260 Kč. Glutenfreier Vanillepudding 1 kg / 60 Kč oder 400 g / 30 Kč. Kakao holländischer Art 500 g / 270 Kč. Vanillinzucker 1 kg / 60 Kč. Gastronomie erhält ein Angebot nach Menge."),
        ("Ist der Vanillepudding von Jůzlová glutenfrei?",
         "Ja. Grundlage ist Maisstärke ohne Gluten. Schokoladengeschmack geben Sie mit Kakao holländischer Art — eine fertige Schokopuddingmischung führen wir nicht."),
        ("Worin unterscheiden sich Kartoffelknödel und haarige Knödel?",
         "Die Kartoffelknödelmischung ist klassischer Teig aus KLASA-Weizenmehl und getrockneten Kartoffelflocken — für Knödel, Mohnnockerl, Kroketten und Gnocchi. Haarige Knödel (Bosáky) folgen einem traditionellen Rezept, fertig in 15 Minuten, typisch mit Kraut und Rauchfleisch oder als Strapačky/Halušky."),
        ("Was ist Kakao holländischer Art mit 21 % Fett?",
         "Alkalisierter Konditor-Kakaopulver mit 20–22 % Kakaobutter. Dunkler, weniger sauer und cremiger als Naturkakao. Ohne Zuckerzusatz (natürliche Zucker 0,9 g / 100 g), vegan, ohne die 14 EU-Allergene, Gluten unter 20 ppm. Packung 500 g / 270 Kč."),
        ("Wie viele Portionen aus 5 kg Knödelmischung?",
         "Aus 5 kg Kartoffelknödelmischung bereiten Sie Beilage für etwa 60–70 Portionen. Haarige Knödel aus 5 kg reichen ähnlich für eine Kantine oder mehrere Familientage."),
        ("Liefern Sie an Restaurants, Kantinen und Konditoreien?",
         "Ja. Seit 2004 beliefern wir Haushalte und Betriebe in Böhmen und Mähren. Für größere Abnahme machen wir einen individuellen Preis — bitte anrufen oder schreiben."),
        ("Sind die Rezepte auf der Website frei nutzbar?",
         "Ja. Dreizehn Rezepte mit unseren Mischungen — von Mohnnockerl bis Windbeutel und Sticky-Toffee-Pudding — stehen kostenlos in vier Sprachen mit Zutaten, Zubereitung und Fotos."),
    ],
    "sk": [
        ("Čo je Jůzlová?",
         "Jůzlová je rodinná česká výroba potravinárskych zmesí od roku 2004. V dielni v Kochánove 40 na Vysočine vyrábame zemiakové a chlpaté knedle v prášku, vanilkový puding bez lepku, vanilínový cukor a kakao holandského typu. Firma: Jůzlová s.r.o., IČO 45900124."),
        ("Kde sídli Jůzlová a ako objednať?",
         "Prevádzka je Kochánov 40, 582 53, 12 km od Havlíčkovho Brodu. Objednávky na +420 728 466 141 (Jiřina Jůzlová) alebo +420 607 629 931 (Jiří Jůzl), e-mail juzlj@seznam.cz. Otvorené denne 8:00–19:00 po telefonickom dohovore."),
        ("Dovážate tovar a kde je odber zadarmo?",
         "Vyzdvihnutie v Kochánove alebo Humpolci je zadarmo. Bezplatný závoz je v Havlíčkovom Brode, Humpolci, Světlej nad Sázavou, Jihlave a okolí. Ďalej posielame zmluvným dopravcom — poštovné podľa cenníka dopravcu."),
        ("Aké sú aktuálne ceny zmesí Jůzlová?",
         "Zemiakové knedle v prášku 5 kg / 250 Kč. Chlpaté knedle (bosáky) 5 kg / 260 Kč. Vanilkový puding bez lepku 1 kg / 60 Kč alebo 400 g / 30 Kč. Kakao holandského typu 500 g / 270 Kč. Vanilínový cukor 1 kg / 60 Kč. Reštauráciám a cukrárňam pripravíme ponuku podľa množstva."),
        ("Je vanilkový puding Jůzlová bez lepku?",
         "Áno. Základom je kukuričný škrob, ktorý lepok neobsahuje. Čokoládovú chuť mu dáte kakaom holandského typu — kakaový puding ako hotovú zmes nevedieme."),
        ("Aký je rozdiel medzi zemiakovými a chlpatými knedľami?",
         "Zemiakové knedle v prášku sú klasické cesto z múky KLASA a sušených zemiakových vločiek — na knedle, šišky, krokety aj gnocchi. Chlpaté knedle (bosáky) sú podľa tradičnej receptúry, hotové za 15 minút, typicky so zelím, údeným alebo ako strapačky/halušky."),
        ("Čo je kakao holandského typu 21 % tuku?",
         "Alkalizovaný cukrársky kakaový prášok s 20–22 % kakaového masla. Je tmavšie, menej kyslé a krémovejšie než prírodné kakao. Bez pridaného cukru (prirodzené cukry 0,9 g / 100 g), vegánske, bez 14 alergénov EÚ, lepok pod 20 ppm. Balenie 500 g / 270 Kč."),
        ("Koľko porcií je z 5 kg knedieľ v prášku?",
         "Z päťkilogramového balenia zemiakových knedieľ pripravíte prílohu zhruba pre 60–70 porcií. Chlpaté knedle z 5 kg obslúžia podobne veľkú výdajňu alebo rodinné varenie na viac dní."),
        ("Dodávate reštauráciám, jedálňam a cukrárňam?",
         "Áno. Od roku 2004 dodávame domácnostiam aj prevádzkam v Čechách a na Morave. Pre väčší odber zostavíme individuálnu cenu — ozvite sa telefonicky alebo e-mailom."),
        ("Sú recepty na webe voľne na použitie?",
         "Áno. Trinásť receptov z našich zmesí — od šišiek s makom po venčeky a sticky toffee pudding — je na webe zadarmo, v štyroch jazykoch, so surovinami, postupom a fotografiami."),
    ],
}

# Fix CS item 9 - I accidentally put a string instead of tuple. Need to fix SITE_FAQ cs.
# I'll fix in a follow-up replace.

RECIPE_FAQ = {
    "cs": {
        "sisky-s-makem-recept": [
            ("Jak se dělají šišky s mákem z těsta Jůzlová?",
             "Bramborové knedlíky v prášku smíchejte s vodou dle návodu, vytvarujte šišky, pečte na 200 °C dozlatova z obou stran, 5 minut spařte ve vroucí vodě a obalte v máku, cukru a másle."),
            ("Na kolik stupňů péct šišky s mákem?",
             "Na 200 °C uprostřed trouby, na vymaštěném plechu, s jedním otočením, aby měly zlatavou kůrku z obou stran."),
        ],
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept": [
            ("Jak dlouho se peče hruškový koláč s vanilkovým pudinkem?",
             "20 minut přípravy a cca 45 minut pečení na 180 °C. Recept je na 8 porcí a funguje i s jablky, malinami nebo broskvemi."),
            ("Kolik pudinku patří do hruškového koláče?",
             "40 g vanilkového pudinku v prášku Jůzlová do lité vrstvy se zakysanou smetanou, šlehačkou, cukrem a vejcem."),
        ],
        "strapacky-se-zelim-a-slaninou-recept": [
            ("Z čeho se dělají strapačky Jůzlová?",
             "Z chlupatých knedlíků v prášku protlačených na halušky do vroucí vody, s kysaným zelím, slaninou a jarní cibulkou."),
            ("Jak dlouho trvá příprava strapaček?",
             "Asi 30 minut: těsto podle návodu, halušky vařit než vyplavou, zelí 10 minut povařit, slaninu osmažit."),
        ],
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": [
            ("Pečou se bebe řezy s čokoládovým pudingem?",
             "Ne. Jsou nepečené: vrstva světlých sušenek, uvařený puding, tmavé sušenky, šlehačka se zakysanou smetanou a kakao. Nejlépe přes noc v lednici."),
            ("Lze místo čokoládového pudingu použít vanilkový?",
             "Ano. Řez chutná výborně i s vanilkovým pudinkem Jůzlová a skořicovým posypem."),
        ],
        "slehackova-rolada-recept": [
            ("Je šlehačková roláda bez lepku?",
             "Ano. Těsto je jen z vajec, moučkového cukru a kakaa holandského typu — bez mouky, tedy bez lepku. Hotová je za cca 30 minut."),
            ("Na kolik stupňů péct šlehačkovou roládu?",
             "8 minut na 180 °C, troubu neotevírejte. Po vychladnutí potřete šlehačkou a srolujte."),
        ],
        "domaci-pernik-recept-podle-jirina-juzlova": [
            ("Potřebuji k domácímu perníku váhu?",
             "Ne. Je to hrníčkový recept Jiřiny Jůzlové: 10 minut mísení, 20–25 minut pečení na 180 °C, 25–30 porcí. Do těsta patří vanilkový pudink v prášku a kakao holandského typu."),
            ("Jak poznám, že je perník upečený?",
             "Dřevěným párátkem — po zapíchnutí musí zůstat čisté, bez přilepeného těsta."),
        ],
        "bramborovo-tvarohove-knedliky-s-jahodami": [
            ("Jak rychle jsou bramborovo-tvarohové knedlíky s jahodami hotové?",
             "Za 20 minut: těsto z bramborových knedlíků v prášku a tvarohu, jahoda dovnitř, 5 minut v páře."),
            ("Jaký tvaroh do ovocných knedlíků?",
             "Měkký tvaroh v kostce, ne ve vaničce — 250 g na 250 g směsi Jůzlová."),
        ],
        "rychle-venecky-ci-vetrnicky-recept": [
            ("Proč pečete věnečky na 250 °C?",
             "Horký start 250 °C a vyšší podíl másla (90 g na 140 g mouky) těsto rychle vykynou. Po 5 minutách snižte na 200 °C. Asi 80 kousků na dvou plechách."),
            ("Hodí se jedno těsto na věnečky i větrníčky?",
             "Ano. Stejné odpalované těsto: věnečky jako dva kroužky, větrníčky jako kopečky. Náplň volte podle chuti — šlehačka, vanilkový krém nebo karamel."),
        ],
        "venecky-s-vanilkovym-kremem-recept": [
            ("Čím se plní věnečky s vanilkovým krémem?",
             "Vanilkovým máslovým krémem z pudinku Jůzlová, žloutků a másla, navrch rumová poleva. Asi 20 kousků."),
            ("Jak péct skořápky věnečků, aby nespadly?",
             "10 minut na 200 °C bez otevírání dvířek, pak 15–25 minut na 180 °C, až jsou sytě zlatavé a suché. Před plněním úplně vychladit."),
        ],
        "kremrole-recept": [
            ("Kolik kremrolí je z receptu a co k nim potřebuji?",
             "Asi 35–40 kousků. Těsto z mouky, másla a smetany, náplň italský sníh. Potřebujete kovové trubičky — nouzově stačí alobal."),
            ("Na kolik stupňů péct kremrole?",
             "12–15 minut na 180–200 °C dozlatova. Sníh: cukr s vodou na 115–120 °C, vlít do ušlehaných bílků."),
        ],
        "minivetrnicky-recept": [
            ("Čím se plní minivětrníčky Jůzlová?",
             "Máslovo-pudinkovým krémem s tvarohem z vanilkového pudinku Jůzlová, vršek čokoládová poleva. Asi 40–45 kousků, pečení 20 minut na 200 °C."),
            ("Existuje lehčí letní varianta minivětrníčků?",
             "Ano: místo máslového krému a polevy plňte oslazenou šlehačkou a jahodami, posypte moučkovým cukrem."),
        ],
        "karamelove-vetrniky-recept": [
            ("Jak se skládají karamelové větrníky?",
             "Skořápka z odpalovaného těsta, vanilkový pudinkový krém, kroužek karamelové šlehačky a karamelová poleva. Asi 24 středních kousků."),
            ("Proč připravit karamelovou šlehačku den předem?",
             "Karamel se smetanou musí v lednici ztuhnout, až šlehačka drží tvar. Troubu při pečení skořápek neotevírejte — větrníky spadnou."),
        ],
        "irsky-sticky-toffee-pudding-recept": [
            ("Je v irském sticky toffee puddingu kakao Jůzlová?",
             "Ano. 60 g kakaa holandského typu a 100 ml Baileys v datlovém těstě, 6 porcí, 45–50 minut na 160 °C, slaná toffee omáčka."),
            ("Proč se Baileys přidává až po povaření datlí?",
             "Mimo plotnu — delší var by vyhnal alkohol a ztlumil chuť likéru. Vody je 180 ml (o 100 ml méně než v původním receptu), právě o množství Baileys."),
        ],
    },
    "en": {
        "sisky-s-makem-recept": [
            ("How do you make poppy-seed potato rolls with Jůzlová mix?",
             "Mix the potato dumpling powder with water as on the pack, shape small rolls, bake at 200 °C until golden on both sides, blanch 5 minutes in boiling water, then toss with poppy seed, sugar and butter."),
            ("What oven temperature for šišky s mákem?",
             "200 °C, middle rack, greased tray, turn once so both sides brown."),
        ],
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept": [
            ("How long does the pear and vanilla-pudding cake bake?",
             "20 minutes prep and about 45 minutes at 180 °C. The recipe serves 8 and also works with apples, raspberries or peaches."),
            ("How much pudding mix goes into the pear cake?",
             "40 g of Jůzlová vanilla pudding powder in the poured layer with sour cream, whipping cream, sugar and egg."),
        ],
        "strapacky-se-zelim-a-slaninou-recept": [
            ("What are Jůzlová strapačky made from?",
             "Hairy dumpling mix pressed through a colander as halušky into boiling water, with sauerkraut, bacon and spring onion."),
            ("How long do strapačky take?",
             "About 30 minutes: mix the dough, boil the dumplings until they float, simmer cabbage 10 minutes, fry the bacon."),
        ],
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": [
            ("Do you bake the Bebe chocolate-pudding slices?",
             "No. They are no-bake: light biscuits, cooked pudding, dark biscuits, whipped cream with sour cream, cocoa dusting. Best overnight in the fridge."),
            ("Can I use vanilla pudding instead of chocolate?",
             "Yes. The slice is excellent with Jůzlová vanilla pudding and a cinnamon dusting."),
        ],
        "slehackova-rolada-recept": [
            ("Is the cream roulade gluten-free?",
             "Yes. The sponge is only eggs, icing sugar and Dutch-process cocoa — no flour, so no gluten. Ready in about 30 minutes."),
            ("What temperature for the cream roll?",
             "8 minutes at 180 °C; do not open the oven. Cool, spread whipped cream, roll."),
        ],
        "domaci-pernik-recept-podle-jirina-juzlova": [
            ("Do I need scales for the cup gingerbread?",
             "No. Jiřina Jůzlová’s cup recipe: 10 minutes mixing, 20–25 minutes at 180 °C, 25–30 portions. The batter includes vanilla pudding powder and Dutch-process cocoa."),
            ("How do I know the gingerbread is done?",
             "A wooden skewer must come out clean, with no sticky batter."),
        ],
        "bramborovo-tvarohove-knedliky-s-jahodami": [
            ("How fast are the strawberry quark dumplings?",
             "20 minutes: potato mix plus quark dough, a strawberry inside, 5 minutes in steam."),
            ("Which quark for fruit dumplings?",
             "Soft block quark, not the tub kind — 250 g to 250 g of Jůzlová mix."),
        ],
        "rychle-venecky-ci-vetrnicky-recept": [
            ("Why bake cream puffs at 250 °C?",
             "A hot start at 250 °C and a higher butter ratio (90 g to 140 g flour) make the choux rise fast. After 5 minutes drop to 200 °C. About 80 pieces on two trays."),
            ("Can one dough make both rings and puffs?",
             "Yes. Same choux: rings as two stacked circles, puffs as small mounds. Fill with cream, vanilla custard or caramel as you like."),
        ],
        "venecky-s-vanilkovym-kremem-recept": [
            ("What fills the vanilla-cream rings?",
             "Vanilla buttercream from Jůzlová pudding, egg yolks and butter, with a rum glaze on top. About 20 pieces."),
            ("How do I bake choux shells so they do not collapse?",
             "10 minutes at 200 °C without opening the door, then 15–25 minutes at 180 °C until deep gold and dry. Cool fully before filling."),
        ],
        "kremrole-recept": [
            ("How many kremrole and what equipment?",
             "About 35–40 pieces. Butter pastry and Italian meringue. You need metal cream-horn tubes — foil tubes work in a pinch."),
            ("What oven temperature for kremrole?",
             "12–15 minutes at 180–200 °C until golden. Meringue: sugar syrup to 115–120 °C poured into whipped whites."),
        ],
        "minivetrnicky-recept": [
            ("What fills Jůzlová mini cream puffs?",
             "Butter-pudding cream with quark from Jůzlová vanilla pudding, chocolate glaze on top. About 40–45 pieces, 20 minutes at 200 °C."),
            ("Is there a lighter summer version?",
             "Yes: skip the buttercream and glaze, fill with sweetened whipped cream and strawberries, dust with icing sugar."),
        ],
        "karamelove-vetrniky-recept": [
            ("How are the caramel cream puffs layered?",
             "Choux shell, vanilla pudding cream, a ring of caramel whipped cream, caramel glaze. About 24 medium puffs."),
            ("Why make the caramel cream the day before?",
             "The caramel-and-cream mix must chill until it whips stiff. Do not open the oven while the shells bake or they collapse."),
        ],
        "irsky-sticky-toffee-pudding-recept": [
            ("Does the sticky toffee pudding use Jůzlová cocoa?",
             "Yes. 60 g Dutch-process cocoa and 100 ml Baileys in the date batter, 6 portions, 45–50 minutes at 160 °C, salted toffee sauce."),
            ("Why add Baileys after boiling the dates?",
             "Off the heat — longer boiling would drive off alcohol and mute the liqueur. Water is 180 ml (100 ml less than the original), matching the Baileys volume."),
        ],
    },
    "de": {
        "sisky-s-makem-recept": [
            ("Wie macht man Mohnnockerl mit Jůzlová-Teig?",
             "Kartoffelknödelpulver mit Wasser nach Packung mischen, Nockerl formen, bei 200 °C beidseitig goldbraun backen, 5 Minuten blanchieren, mit Mohn, Zucker und Butter wenden."),
            ("Bei welcher Temperatur backt man Šišky s mákem?",
             "200 °C, mittlere Schiene, gefettetes Blech, einmal wenden."),
        ],
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept": [
            ("Wie lange backt der Birnenkuchen mit Vanillepudding?",
             "20 Minuten Vorbereitung und ca. 45 Minuten bei 180 °C. Das Rezept ergibt 8 Stücke und geht auch mit Äpfeln, Himbeeren oder Pfirsichen."),
            ("Wie viel Puddingpulver kommt in den Birnenkuchen?",
             "40 g Jůzlová-Vanillepuddingpulver in die Gussmasse mit Sauerrahm, Sahne, Zucker und Ei."),
        ],
        "strapacky-se-zelim-a-slaninou-recept": [
            ("Woraus bestehen Jůzlová-Strapačky?",
             "Aus Haarige-Knödel-Mischung, als Halušky ins kochende Wasser gedrückt, mit Sauerkraut, Speck und Frühlingszwiebel."),
            ("Wie lange dauern Strapačky?",
             "Etwa 30 Minuten: Teig anrühren, kochen bis sie aufschwimmen, Kraut 10 Minuten, Speck ausbraten."),
        ],
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": [
            ("Backt man die Bebe-Schnitten mit Schokopudding?",
             "Nein. Ohne Backen: helle Kekse, gekochter Pudding, dunkle Kekse, Sahne mit Sauerrahm, Kakao. Am besten über Nacht kühlen."),
            ("Geht Vanillepudding statt Schokolade?",
             "Ja. Die Schnitte schmeckt auch mit Jůzlová-Vanillepudding und Zimt."),
        ],
        "slehackova-rolada-recept": [
            ("Ist die Sahnerolle glutenfrei?",
             "Ja. Der Biskuit besteht nur aus Eiern, Puderzucker und Kakao holländischer Art — ohne Mehl, also ohne Gluten. Fertig in ca. 30 Minuten."),
            ("Bei welcher Temperatur die Sahnerolle?",
             "8 Minuten bei 180 °C, Ofen nicht öffnen. Auskühlen, mit Sahne bestreichen, rollen."),
        ],
        "domaci-pernik-recept-podle-jirina-juzlova": [
            ("Brauche ich für den Lebkuchen eine Waage?",
             "Nein. Tassenrezept von Jiřina Jůzlová: 10 Minuten rühren, 20–25 Minuten bei 180 °C, 25–30 Stücke. Im Teig: Vanillepuddingpulver und Kakao holländischer Art."),
            ("Wann ist der Lebkuchen fertig?",
             "Ein Holzstäbchen muss sauber herauskommen, ohne Teig."),
        ],
        "bramborovo-tvarohove-knedliky-s-jahodami": [
            ("Wie schnell sind die Erdbeer-Quark-Knödel fertig?",
             "In 20 Minuten: Kartoffelmischung plus Quark, Erdbeere hinein, 5 Minuten dämpfen."),
            ("Welchen Quark für Obstknödel?",
             "Weichen Blockquark, nicht den Becherquark — 250 g auf 250 g Jůzlová-Mischung."),
        ],
        "rychle-venecky-ci-vetrnicky-recept": [
            ("Warum Brandteig bei 250 °C?",
             "Heißer Start bei 250 °C und mehr Butter (90 g auf 140 g Mehl) lassen den Teig schnell aufgehen. Nach 5 Minuten auf 200 °C. Etwa 80 Stück auf zwei Blechen."),
            ("Ein Teig für Kränze und Windbeutel?",
             "Ja. Gleicher Brandteig: Kränze als zwei Ringe, Windbeutel als Häufchen. Füllung nach Wunsch."),
        ],
        "venecky-s-vanilkovym-kremem-recept": [
            ("Womit füllt man die Vanillecreme-Kränze?",
             "Vanille-Buttercreme aus Jůzlová-Pudding, Eigelben und Butter, dazu Rumglasur. Etwa 20 Stück."),
            ("Wie backt man Brandteigschalen, ohne dass sie fallen?",
             "10 Minuten bei 200 °C ohne Öffnen, dann 15–25 Minuten bei 180 °C bis sattgold und trocken. Vor dem Füllen vollständig auskühlen."),
        ],
        "kremrole-recept": [
            ("Wie viele Schaumrollen und welches Gerät?",
             "Etwa 35–40 Stück. Butterteig und italienische Meringue. Metallhülsen — notfalls Alufolie."),
            ("Backtemperatur für Kremrole?",
             "12–15 Minuten bei 180–200 °C. Meringue: Zuckersirup auf 115–120 °C in steifen Eischnee."),
        ],
        "minivetrnicky-recept": [
            ("Womit füllt man Mini-Windbeutel von Jůzlová?",
             "Butter-Puddingcreme mit Quark aus Jůzlová-Vanillepudding, Schokoglasur. Etwa 40–45 Stück, 20 Minuten bei 200 °C."),
            ("Gibt es eine leichtere Sommerversion?",
             "Ja: statt Buttercreme und Glasur süße Sahne und Erdbeeren, Puderzucker."),
        ],
        "karamelove-vetrniky-recept": [
            ("Wie sind die Karamell-Windbeutel geschichtet?",
             "Brandteigschale, Vanillepuddingcreme, Ring Karamellsahne, Karamellglasur. Etwa 24 mittlere Stück."),
            ("Warum Karamellsahne am Vortag?",
             "Die Karamell-Sahne-Mischung muss kalt werden, bis sie steif schlägt. Ofen beim Backen der Schalen nicht öffnen."),
        ],
        "irsky-sticky-toffee-pudding-recept": [
            ("Ist Jůzlová-Kakao im Sticky-Toffee-Pudding?",
             "Ja. 60 g Kakao holländischer Art und 100 ml Baileys im Dattelteig, 6 Portionen, 45–50 Minuten bei 160 °C, gesalzene Toffeesauce."),
            ("Warum Baileys erst nach dem Kochen der Datteln?",
             "Abseits der Hitze — langes Kochen würde Alkohol und Geschmack austreiben. Wasser 180 ml (100 ml weniger als im Original), genau die Baileys-Menge."),
        ],
    },
    "sk": {
        "sisky-s-makem-recept": [
            ("Ako sa robia šišky s makom z cesta Jůzlová?",
             "Zemiakové knedle v prášku zmiešajte s vodou podľa návodu, vytvarujte šišky, pečte na 200 °C dozlatista z oboch strán, 5 minút sparte vo vriacej vode a obalte v maku, cukre a masle."),
            ("Na koľko stupňov piecť šišky s makom?",
             "Na 200 °C v strede rúry, na vymazanom plechu, s jedným otočením."),
        ],
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept": [
            ("Ako dlho sa pečie hruškový koláč s vanilkovým pudingom?",
             "20 minút prípravy a cca 45 minút pečenia na 180 °C. Recept je na 8 porcií a funguje aj s jablkami, malinami alebo broskyňami."),
            ("Koľko pudingu patrí do hruškového koláča?",
             "40 g vanilkového pudingu v prášku Jůzlová do liatej vrstvy so zakysanou smotanou, šľahačkou, cukrom a vajcom."),
        ],
        "strapacky-se-zelim-a-slaninou-recept": [
            ("Z čoho sa robia strapačky Jůzlová?",
             "Z chlpatých knedieľ v prášku pretlačených na halušky do vriacej vody, s kyslou kapustou, slaninou a jarnou cibuľkou."),
            ("Ako dlho trvá príprava strapačiek?",
             "Asi 30 minút: cesto podľa návodu, halušky variť kým vyplávajú, kapustu 10 minút, slaninu opražiť."),
        ],
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": [
            ("Pečú sa bebe rezy s čokoládovým pudingom?",
             "Nie. Sú nepečené: vrstva svetlých sušienok, uvarený puding, tmavé sušienky, šľahačka so zakysanou smotanou a kakao. Najlepšie cez noc v chladničke."),
            ("Možno namiesto čokoládového pudingu použiť vanilkový?",
             "Áno. Rez chutí výborne aj s vanilkovým pudingom Jůzlová a škoricovým posypom."),
        ],
        "slehackova-rolada-recept": [
            ("Je šľahačková roláda bez lepku?",
             "Áno. Cesto je len z vajec, práškového cukru a kakaa holandského typu — bez múky, teda bez lepku. Hotová je za cca 30 minút."),
            ("Na koľko stupňov piecť šľahačkovú roládu?",
             "8 minút na 180 °C, rúru neotvárajte. Po vychladnutí potrite šľahačkou a zrolujte."),
        ],
        "domaci-pernik-recept-podle-jirina-juzlova": [
            ("Potrebujem k domácemu perníku váhu?",
             "Nie. Je to hrnčekový recept Jiřiny Jůzlovej: 10 minút miešania, 20–25 minút pečenia na 180 °C, 25–30 porcií. Do cesta patrí vanilkový puding v prášku a kakao holandského typu."),
            ("Ako spoznám, že je perník upečený?",
             "Drevenou špáradlou — po vpichnutí musí ostať čisté, bez prilepeného cesta."),
        ],
        "bramborovo-tvarohove-knedliky-s-jahodami": [
            ("Ako rýchlo sú zemiakovo-tvarohové knedle s jahodami hotové?",
             "Za 20 minút: cesto zo zemiakových knedieľ v prášku a tvarohu, jahoda dnu, 5 minút v pare."),
            ("Aký tvaroh do ovocných knedieľ?",
             "Mäkký tvaroh v kocke, nie vo vaničke — 250 g na 250 g zmesi Jůzlová."),
        ],
        "rychle-venecky-ci-vetrnicky-recept": [
            ("Prečo pečiete venčeky na 250 °C?",
             "Horúci štart 250 °C a vyšší podiel masla (90 g na 140 g múky) cesto rýchlo vykysnú. Po 5 minútach znížte na 200 °C. Asi 80 kúskov na dvoch plechoch."),
            ("Hodí sa jedno cesto na venčeky aj vetrníčky?",
             "Áno. Rovnaké odpaľované cesto: venčeky ako dva krúžky, vetrníčky ako kopečky."),
        ],
        "venecky-s-vanilkovym-kremem-recept": [
            ("Čím sa plnia venčeky s vanilkovým krémom?",
             "Vanilkovým maslovým krémom z pudingu Jůzlová, žĺtkov a masla, navrch rumová poleva. Asi 20 kúskov."),
            ("Ako piecť škrupiny venčekov, aby nespadli?",
             "10 minút na 200 °C bez otvárania dvierok, potom 15–25 minút na 180 °C, kým sú sýto zlatisté a suché. Pred plnením úplne vychladiť."),
        ],
        "kremrole-recept": [
            ("Koľko kremrolí je z receptu a čo k nim potrebujem?",
             "Asi 35–40 kúskov. Cesto z múky, masla a smotany, náplň taliansky sneh. Potrebujete kovové trubičky — núdzovo stačí alobal."),
            ("Na koľko stupňov piecť kremrole?",
             "12–15 minút na 180–200 °C dozlatista. Sneh: cukor s vodou na 115–120 °C do ušľahaných bielok."),
        ],
        "minivetrnicky-recept": [
            ("Čím sa plnia minivetrníčky Jůzlová?",
             "Maslovo-pudingovým krémom s tvarohom z vanilkového pudingu Jůzlová, vrch čokoládová poleva. Asi 40–45 kúskov, pečenie 20 minút na 200 °C."),
            ("Existuje ľahšia letná varianta minivetrníčkov?",
             "Áno: namiesto maslového krému a polevy plňte osladenou šľahačkou a jahodami, posypte práškovým cukrom."),
        ],
        "karamelove-vetrniky-recept": [
            ("Ako sa skladajú karamelové vetrníky?",
             "Škrupina z odpaľovaného cesta, vanilkový pudingový krém, krúžok karamelovej šľahačky a karamelová poleva. Asi 24 stredných kúskov."),
            ("Prečo pripraviť karamelovú šľahačku deň vopred?",
             "Karamel so smotanou musí v chladničke stuhnúť, kým šľahačka drží tvar. Rúru pri pečení škrupín neotvárajte."),
        ],
        "irsky-sticky-toffee-pudding-recept": [
            ("Je v írskom sticky toffee pudingu kakao Jůzlová?",
             "Áno. 60 g kakaa holandského typu a 100 ml Baileys v datľovom ceste, 6 porcií, 45–50 minút na 160 °C, slaná toffee omáčka."),
            ("Prečo sa Baileys pridáva až po povarení datlí?",
             "Mimo platne — dlhší var by vyhnal alkohol a stlmil chuť likéru. Vody je 180 ml (o 100 ml menej než v pôvodnom recepte), práve o množstvo Baileys."),
        ],
    },
}


def site_faq(lang):
    items = SITE_FAQ.get(lang) or SITE_FAQ["cs"]
    return [(q, a) for q, a in items]


def home_faq(lang):
    return site_faq(lang)[:HOME_COUNT]


def recipe_faq(lang, slug):
    pack = RECIPE_FAQ.get(lang) or RECIPE_FAQ["cs"]
    return pack.get(slug) or []
