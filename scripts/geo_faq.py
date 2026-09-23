"""GEO-oriented FAQ copy. Direct answers first; one concept per Q&A.

Used on the FAQ page (full set), homepage (first HOME_COUNT items),
and recipe pages (two questions each) in all four languages.
"""

from cocoa_faq import b2b_cocoa_faq

HOME_COUNT = 6

# D2C only — never put kitchen/wholesale questions here.
SITE_FAQ = {
    "cs": [
        ("Objednání a odběr", [
            ("Jak u vás objednám, když nemáte e-shop?",
             "Zavoláte Jiřině (+420 728 466 141) nebo Jiřímu (+420 607 629 931), nebo vyplníte formulář. Řeknete, co a kolik chcete a kde jste; zbytek domluvíme."),
            ("Kde si zboží vyzvednu zdarma?",
             "V dílně Kochánov 40, 582 53, nebo v Humpolci v okolí Pivovaru Bernard. Vždy po telefonické domluvě, denně 8:00–19:00."),
            ("Dáváte vzorky nebo ochutnávky?",
             "Ne. Objednáváte hotová balení. Na první vyzkoušení se hodí puding ve 400 g balení za 30 Kč."),
            ("Platím předem, nebo při převzetí?",
             "Při vyzvednutí a rozvozu platíte při převzetí. Když zboží posíláme balíkem, řekneme celkovou částku předem a odešleme až po vašem souhlasu."),
        ]),
        ("Doprava", [
            ("Kdy je rozvoz zdarma?",
             "Do Humpolce a Havlíčkova Brodu od 1000 Kč, do Jihlavy od 3000 Kč, po zbytku Vysočiny od 5000 Kč."),
            ("Posíláte i balíkem?",
             "Na požádání ano, po Česku i do zahraničí. Většina zákazníků si ale pro zboží přijede. Poštovné, krabici a pojištění platíte celé vy a celkovou částku domluvíme předem. Můžete poslat i vlastního dopravce."),
        ]),
        ("Složení a alergeny", [
            ("Z čeho jsou knedlíky v prášku?",
             "Z pšeničné mouky z mlýna v Havlíčkově Brodě, který vede naše širší rodina, a ze sušených bramborových vloček. Zaděláváte jen vodou; vejce, mléko nebo strouhané brambory přidáte podle zvyku."),
            ("Je vanilkový puding opravdu bez lepku?",
             "Ano. Základem je kukuřičný škrob, který lepek neobsahuje. Kakaový puding jako hotovou směs nevedeme — čokoládový krém vznikne zamícháním našeho kakaa."),
            ("Kolik tuku má vaše kakao?",
             "20–22 % kakaového másla. Podle práva EU musí mít kakaový prášek nejméně 20 %; pod tím je to kakao se sníženým obsahem tuku. Bez přidaného cukru, bez 14 alergenů EU, lepek pod 20 ppm."),
            ("Je vanilínový cukr pravá vanilka?",
             "Ne. Je to jemně mletý cukr s vanilínovým aromatem. Říkáme to rovnou v názvu."),
        ]),
        ("Balení a skladování", [
            ("Kolik porcí je z 5 kg knedlíků?",
             "Zhruba 60–70 porcí přílohy. Jeden pytel vystačí na sezónu nedělních obědů."),
            ("Kolik pudingu dát na půl litru mléka?",
             "Zhruba 40 g na 500 ml mléka. Z kila uvaříte asi 25 pudingů."),
            ("Jak směsi skladovat?",
             "V suchu a zavřené. Kakao mimo silné pachy, ideálně při 15–20 °C."),
        ]),
    ],
    "en": [
        ("Ordering and pick-up", [
            ("How do I order without a web shop?",
             "Call Jiřina (+420 728 466 141) or Jiří (+420 607 629 931), or use the form. Tell us what you want, how much and where you are; we arrange the rest."),
            ("Where can I collect for free?",
             "At the workshop, Kochánov 40, 582 53, or in Humpolec near the Bernard brewery. Always by prior phone call, daily 8:00–19:00."),
            ("Do you give samples or tastings?",
             "No. You order finished packs. For a first try, the pudding comes in a 400 g pack for 30 Kč (CZK)."),
            ("Do I pay in advance or on collection?",
             "For pick-up and delivery you pay on hand-over. If we post a parcel, we give you the total first and send it only once you agree."),
        ]),
        ("Delivery", [
            ("When is delivery free?",
             "To Humpolec and Havlíčkův Brod from 1000 Kč, to Jihlava from 3000 Kč, across the rest of Vysočina from 5000 Kč."),
            ("Can you post a parcel?",
             "On request, within Czechia or abroad, though most customers come and collect. You pay the full postage, box and insurance, and we agree the total first. You may also send your own courier."),
        ]),
        ("Ingredients and allergens", [
            ("What is the dumpling mix made of?",
             "Wheat flour from the mill in Havlíčkův Brod run by our extended family, and dried potato flakes. You add only water; egg, milk or grated potato go in if that is how you like them."),
            ("Is the vanilla pudding really gluten-free?",
             "Yes. It is based on corn starch, which contains no gluten. We do not sell a cocoa pudding mix; for a chocolate cream, stir in our cocoa."),
            ("How much fat is in your cocoa?",
             "20–22 % cocoa butter. Under EU law, cocoa powder must contain at least 20 %; below that it counts as fat-reduced cocoa. No added sugar, none of the 14 EU allergens, gluten under 20 ppm."),
            ("Is the vanilla sugar real vanilla?",
             "No. It is finely ground sugar flavoured with vanillin, not with vanilla pods."),
        ]),
        ("Packs and storage", [
            ("How many portions from 5 kg of dumpling mix?",
             "About 60–70 side-dish portions. One bag covers a whole season of Sunday lunches."),
            ("How much pudding powder per half litre of milk?",
             "About 40 g for 500 ml of milk. One kilo makes about 25 puddings."),
            ("How do I store the mixes?",
             "Dry and sealed. Keep the cocoa away from strong smells, ideally at 15–20 °C."),
        ]),
    ],
    "de": [
        ("Bestellen und Abholen", [
            ("Wie bestelle ich ohne Onlineshop?",
             "Rufen Sie Jiřina (+420 728 466 141) oder Jiří (+420 607 629 931) an oder nutzen Sie das Formular. Sie sagen, was und wie viel Sie möchten und wo Sie sind; den Rest klären wir."),
            ("Wo kann ich kostenlos abholen?",
             "In der Werkstatt, Kochánov 40, 582 53, oder in Humpolec nahe der Brauerei Bernard. Immer nach telefonischer Absprache, täglich 8:00–19:00 Uhr."),
            ("Gibt es Muster oder Verkostung?",
             "Nein. Sie bestellen fertige Packungen. Zum Ausprobieren gibt es den Pudding als 400-g-Packung für 30 Kč."),
            ("Zahle ich vorab oder bei Übergabe?",
             "Abholung und Lieferung: bei Übergabe. Beim Paket nennen wir die Gesamtsumme vorab und versenden erst nach Ihrer Zusage."),
        ]),
        ("Lieferung", [
            ("Wann ist die Lieferung kostenlos?",
             "Nach Humpolec und Havlíčkův Brod ab 1000 Kč, nach Jihlava ab 3000 Kč, in der übrigen Vysočina ab 5000 Kč."),
            ("Verschicken Sie auch Pakete?",
             "Auf Wunsch ja, innerhalb Tschechiens oder ins Ausland; die meisten Kunden holen aber ab. Porto, Karton und Versicherung zahlen Sie vollständig, die Gesamtsumme vereinbaren wir vorab. Sie können auch einen eigenen Spediteur schicken."),
        ]),
        ("Zutaten und Allergene", [
            ("Woraus besteht die Knödelmischung?",
             "Aus Weizenmehl der Mühle in Havlíčkův Brod, die unsere erweiterte Familie führt, und getrockneten Kartoffelflocken. Sie geben nur Wasser dazu; Ei, Milch oder geriebene Kartoffeln nach Belieben."),
            ("Ist der Vanillepudding wirklich glutenfrei?",
             "Ja. Grundlage ist Maisstärke, die kein Gluten enthält. Eine Kakaopuddingmischung führen wir nicht — für Schokocreme rühren Sie unseren Kakao ein."),
            ("Wie viel Fett hat Ihr Kakao?",
             "20–22 % Kakaobutter. Nach EU-Recht braucht Kakaopulver mindestens 20 %; darunter ist es fettreduzierter Kakao. Ohne Zuckerzusatz, ohne die 14 EU-Allergene, Gluten unter 20 ppm."),
            ("Ist der Vanillinzucker echte Vanille?",
             "Nein. Es ist fein gemahlener Zucker mit Vanillinaroma. Das steht schon im Produktnamen."),
        ]),
        ("Packung und Lagerung", [
            ("Wie viele Portionen aus 5 kg Knödelmischung?",
             "Etwa 60–70 Beilagenportionen. Ein Beutel reicht für eine ganze Saison Sonntagsessen."),
            ("Wie viel Puddingpulver auf einen halben Liter Milch?",
             "Etwa 40 g auf 500 ml Milch. Aus einem Kilo werden rund 25 Puddings."),
            ("Wie lagere ich die Mischungen?",
             "Trocken und verschlossen. Kakao fern von starken Gerüchen, ideal bei 15–20 °C."),
        ]),
    ],
    "sk": [
        ("Objednanie a odber", [
            ("Ako objednám, keď nemáte e-shop?",
             "Zavoláte Jiřine (+420 728 466 141) alebo Jiřímu (+420 607 629 931), alebo vyplníte formulár. Poviete, čo a koľko chcete a kde ste; zvyšok dohodneme."),
            ("Kde si tovar vyzdvihnem zadarmo?",
             "V dielni Kochánov 40, 582 53, alebo v Humpolci v okolí Pivovaru Bernard. Vždy po telefonickej dohode, denne 8:00–19:00."),
            ("Dávate vzorky alebo ochutnávky?",
             "Nie. Objednávate hotové balenia. Na prvé vyskúšanie sa hodí puding v 400 g balení za 30 Kč."),
            ("Platím vopred, alebo pri prevzatí?",
             "Pri vyzdvihnutí a rozvoze platíte pri prevzatí. Keď tovar posielame balíkom, povieme celkovú sumu vopred a odošleme až po vašom súhlase."),
        ]),
        ("Doprava", [
            ("Kedy je rozvoz zadarmo?",
             "Do Humpolca a Havlíčkovho Brodu od 1000 Kč, do Jihlavy od 3000 Kč, po zvyšku Vysočiny od 5000 Kč."),
            ("Posielate aj balíkom, napríklad na Slovensko?",
             "Na požiadanie áno, hoci väčšina zákazníkov si pre tovar príde. Poštovné, krabicu a poistenie platíte celé vy a celkovú sumu dohodneme vopred."),
            ("Môžem poslať vlastného dopravcu?",
             "Áno. Často to vyjde lacnejšie."),
        ]),
        ("Zloženie a alergény", [
            ("Z čoho sú knedle v prášku?",
             "Z pšeničnej múky z mlyna v Havlíčkovom Brode, ktorý vedie naša širšia rodina, a zo sušených zemiakových vločiek. Zamiešate len s vodou; vajce, mlieko alebo strúhané zemiaky pridáte podľa zvyku."),
            ("Je vanilkový puding naozaj bez lepku?",
             "Áno. Základom je kukuričný škrob, ktorý lepok neobsahuje. Kakaový puding ako hotovú zmes nevedieme — čokoládový krém vznikne zamiešaním nášho kakaa."),
            ("Koľko tuku má vaše kakao?",
             "20–22 % kakaového masla. Podľa práva EÚ musí mať kakaový prášok najmenej 20 %; pod tým je to kakao so zníženým obsahom tuku. Bez pridaného cukru, bez 14 alergénov EÚ, lepok pod 20 ppm."),
            ("Je vanilínový cukor pravá vanilka?",
             "Nie. Je to jemne mletý cukor s vanilínovou arómou. Hovoríme to rovno v názve."),
        ]),
        ("Balenie a skladovanie", [
            ("Koľko porcií je z 5 kg knedieľ?",
             "Zhruba 60–70 porcií prílohy. Jedno vrece vystačí na sezónu nedeľných obedov."),
            ("Koľko pudingu dať na pol litra mlieka?",
             "Zhruba 40 g na 500 ml mlieka. Z kila uvaríte asi 25 pudingov."),
            ("Ako zmesi skladovať?",
             "V suchu a zatvorené. Kakao mimo silných pachov, ideálne pri 15–20 °C."),
        ]),
    ],
}

# B2B only — wholesale pages. Keep kitchens off D2C FAQs.
B2B_FAQ = {
    "cs": [
        ("Jaká je minimální objednávka v Praze?",
         "Do Prahy bereme smíšenou objednávku od 25 kg. Cenu podle množství řekneme po telefonu nebo e-mailu."),
        ("Můžu poslat vlastního dopravce?",
         "Ano. Často to vyjde levněji než náš rozvoz mimo bezplatné zóny."),
    ],
    "en": [
        ("What is the Prague minimum?",
         "A mixed order from 25 kg. We quote the quantity price by phone or e-mail."),
        ("Can I send my own courier?",
         "Yes. That is often cheaper than our delivery outside the free zones."),
    ],
    "de": [
        ("Was ist das Prager Minimum?",
         "Eine gemischte Bestellung ab 25 kg. Den Mengenpreis nennen wir telefonisch oder per E-Mail."),
        ("Kann ich einen eigenen Kurier schicken?",
         "Ja. Das ist oft günstiger als unsere Lieferung außerhalb der Gratiszonen."),
    ],
    "sk": [
        ("Aká je minimálna objednávka v Prahe?",
         "Do Prahy berieme zmiešanú objednávku od 25 kg. Cenu podľa množstva povieme po telefóne alebo e-maile."),
        ("Môžem poslať vlastného dopravcu?",
         "Áno. Často to vyjde lacnejšie než náš rozvoz mimo bezplatných zón."),
    ],
}

# Fix CS item 9 - I accidentally put a string instead of tuple. Need to fix SITE_FAQ cs.
# I'll fix in a follow-up replace.

RECIPE_FAQ = {
    "cs": {
        "sisky-s-makem-recept": [
            ("Jak se dělají šišky s mákem z knedlíků v prášku?",
             "Bramborové knedlíky v prášku smíchejte s vodou podle návodu, vytvarujte šišky, pečte na 200 °C dozlatova z obou stran, 5 minut spařte ve vroucí vodě a obalte v máku, cukru a másle."),
            ("Na kolik stupňů péct šišky s mákem?",
             "Na 200 °C uprostřed trouby, na vymaštěném plechu, s jedním otočením, aby měly zlatavou kůrku z obou stran."),
        ],
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept": [
            ("Jak dlouho se peče hruškový koláč s vanilkovým pudingem?",
             "20 minut přípravy a cca 45 minut pečení na 180 °C. Recept je na 8 porcí a funguje i s jablky, malinami nebo broskvemi."),
            ("Kolik pudingu patří do hruškového koláče?",
             "40 g našeho vanilkového pudingu v prášku do lité vrstvy se zakysanou smetanou, šlehačkou, cukrem a vejcem."),
        ],
        "strapacky-se-zelim-a-slaninou-recept": [
            ("Z čeho se dělají naše strapačky?",
             "Z chlupatých knedlíků v prášku protlačených na halušky do vroucí vody, s kysaným zelím, slaninou a jarní cibulkou."),
            ("Jak dlouho trvá příprava strapaček?",
             "Asi 30 minut: těsto podle návodu, halušky vařit, než vyplavou, zelí 10 minut povařit, slaninu osmažit."),
        ],
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": [
            ("Pečou se bebe řezy s čokoládovým pudingem?",
             "Ne. Jsou nepečené: vrstva světlých sušenek, uvařený puding, tmavé sušenky, šlehačka se zakysanou smetanou a kakao. Nejlépe přes noc v lednici."),
            ("Lze místo čokoládového pudingu použít vanilkový?",
             "Ano. Řez chutná výborně i s naším vanilkovým pudingem a skořicovým posypem."),
        ],
        "slehackova-rolada-recept": [
            ("Je šlehačková roláda bez lepku?",
             "Ano. Těsto je jen z vajec, moučkového cukru a kakaa holandského typu — bez mouky, tedy bez lepku. Hotová je za cca 30 minut."),
            ("Na kolik stupňů péct šlehačkovou roládu?",
             "8 minut na 180 °C, troubu neotevírejte. Po vychladnutí potřete šlehačkou a srolujte."),
        ],
        "domaci-pernik-recept-podle-jirina-juzlova": [
            ("Potřebuji k domácímu perníku váhu?",
             "Ne. Je to hrníčkový recept Jiřiny Jůzlové: 10 minut mísení, 20–25 minut pečení na 180 °C, 25–30 porcí. Do těsta patří vanilkový puding v prášku a kakao holandského typu."),
            ("Jak poznám, že je perník upečený?",
             "Dřevěným párátkem — po zapíchnutí musí zůstat čisté, bez přilepeného těsta."),
        ],
        "bramborovo-tvarohove-knedliky-s-jahodami": [
            ("Jak rychle jsou bramborovo-tvarohové knedlíky s jahodami hotové?",
             "Za 20 minut: těsto z bramborových knedlíků v prášku a tvarohu, jahoda dovnitř, 5 minut v páře."),
            ("Jaký tvaroh do ovocných knedlíků?",
             "Měkký tvaroh v kostce, ne ve vaničce — 250 g na 250 g naší směsi."),
        ],
        "rychle-venecky-ci-vetrnicky-recept": [
            ("Proč pečete věnečky na 250 °C?",
             "Horký start na 250 °C a vyšší podíl másla (90 g na 140 g mouky) těsto rychle nafouknou. Po 5 minutách snižte na 200 °C. Asi 80 kousků na dvou plechách."),
            ("Hodí se jedno těsto na věnečky i větrníčky?",
             "Ano. Stejné odpalované těsto: věnečky jako dva kroužky, větrníčky jako kopečky. Náplň volte podle chuti — šlehačka, vanilkový krém nebo karamel."),
        ],
        "venecky-s-vanilkovym-kremem-recept": [
            ("Čím se plní věnečky s vanilkovým krémem?",
             "Vanilkovým máslovým krémem z našeho pudingu, žloutků a másla, navrch rumová poleva. Asi 20 kousků."),
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
            ("Čím se plní minivětrníčky?",
             "Máslovo-pudingovým krémem s tvarohem z našeho vanilkového pudingu, navrch čokoládová poleva. Asi 40–45 kousků, pečení 20 minut na 200 °C."),
            ("Existuje lehčí letní varianta minivětrníčků?",
             "Ano: místo máslového krému a polevy plňte oslazenou šlehačkou a jahodami, posypte moučkovým cukrem."),
        ],
        "karamelove-vetrniky-recept": [
            ("Jak se skládají karamelové větrníky?",
             "Skořápka z odpalovaného těsta, vanilkový pudingový krém, kroužek karamelové šlehačky a karamelová poleva. Asi 24 středních kousků."),
            ("Proč připravit karamelovou šlehačku den předem?",
             "Karamel se smetanou musí v lednici ztuhnout, aby šlehačka držela tvar. Troubu při pečení skořápek neotevírejte — větrníky spadnou."),
        ],
        "irsky-sticky-toffee-pudding-recept": [
            ("Je v irském sticky toffee puddingu naše kakao?",
             "Ano. 60 g kakaa holandského typu a 100 ml Baileys v datlovém těstě, 6 porcí, 45–50 minut na 160 °C, slaná toffee omáčka."),
            ("Proč se Baileys přidává až po povaření datlí?",
             "Mimo plotnu — delší var by vyhnal alkohol a ztlumil chuť likéru. Vody je 180 ml (o 100 ml méně než v původním receptu), právě o množství Baileys."),
        ],
    },
    "en": {
        "sisky-s-makem-recept": [
            ("How do you make poppy-seed potato rolls with our dumpling mix?",
             "Mix the potato dumpling powder with water as directed on the pack, shape small rolls, bake at 200 °C until golden on both sides, blanch for 5 minutes in boiling water, then toss with poppy seed, sugar and butter."),
            ("What oven temperature for šišky s mákem?",
             "200 °C on the middle rack, on a greased tray; turn once so both sides brown."),
        ],
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept": [
            ("How long does the pear and vanilla-pudding cake bake?",
             "20 minutes prep and about 45 minutes at 180 °C. The recipe serves 8 and also works with apples, raspberries or peaches."),
            ("How much pudding mix goes into the pear cake?",
             "40 g of our vanilla pudding powder in the poured layer with sour cream, whipping cream, sugar and egg."),
        ],
        "strapacky-se-zelim-a-slaninou-recept": [
            ("What are our strapačky made from?",
             "Hairy-dumpling mix pressed through a colander into boiling water as halušky, served with sauerkraut, bacon and spring onion."),
            ("How long do strapačky take?",
             "About 30 minutes: mix the dough, boil the dumplings until they float, simmer cabbage 10 minutes, fry the bacon."),
        ],
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": [
            ("Do you bake the Bebe chocolate-pudding slices?",
             "No. They are no-bake: a layer of light biscuits, cooked pudding, dark biscuits, whipped cream with sour cream and a dusting of cocoa. Best left overnight in the fridge."),
            ("Can I use vanilla pudding instead of chocolate?",
             "Yes. The slice is excellent with our vanilla pudding and a dusting of cinnamon."),
        ],
        "slehackova-rolada-recept": [
            ("Is the cream roulade gluten-free?",
             "Yes. The sponge is only eggs, icing sugar and Dutch-process cocoa — no flour, so no gluten. Ready in about 30 minutes."),
            ("What temperature for the cream roll?",
             "8 minutes at 180 °C; do not open the oven. Cool, spread with whipped cream and roll up."),
        ],
        "domaci-pernik-recept-podle-jirina-juzlova": [
            ("Do I need scales for the cup gingerbread?",
             "No. Jiřina Jůzlová’s cup recipe: 10 minutes mixing, 20–25 minutes at 180 °C, 25–30 portions. The batter includes vanilla pudding powder and Dutch-process cocoa."),
            ("How do I know the gingerbread is done?",
             "A wooden skewer must come out clean, with no sticky batter."),
        ],
        "bramborovo-tvarohove-knedliky-s-jahodami": [
            ("How fast are the strawberry quark dumplings?",
             "In 20 minutes: a dough of potato dumpling mix and quark, a strawberry inside, 5 minutes in steam."),
            ("Which quark for fruit dumplings?",
             "Soft block quark, not the tub kind — 250 g to 250 g of our mix."),
        ],
        "rychle-venecky-ci-vetrnicky-recept": [
            ("Why bake cream puffs at 250 °C?",
             "A hot start at 250 °C and a higher butter ratio (90 g to 140 g flour) make the choux rise fast. After 5 minutes drop to 200 °C. About 80 pieces on two trays."),
            ("Can one dough make both rings and puffs?",
             "Yes. The same choux: pipe rings as two stacked circles and puffs as small mounds. Fill with whipped cream, vanilla custard or caramel as you like."),
        ],
        "venecky-s-vanilkovym-kremem-recept": [
            ("What fills the vanilla-cream rings?",
             "Vanilla buttercream made from our pudding, egg yolks and butter, with a rum glaze on top. About 20 pieces."),
            ("How do I bake choux shells so they do not collapse?",
             "10 minutes at 200 °C without opening the door, then 15–25 minutes at 180 °C until deep gold and dry. Cool fully before filling."),
        ],
        "kremrole-recept": [
            ("How many kremrole and what equipment?",
             "About 35–40 pieces. A butter pastry with an Italian-meringue filling. You need metal cream-horn tubes; foil tubes work in a pinch."),
            ("What oven temperature for kremrole?",
             "12–15 minutes at 180–200 °C until golden. For the meringue, cook a sugar syrup to 115–120 °C and pour it into the whipped whites."),
        ],
        "minivetrnicky-recept": [
            ("What fills the mini cream puffs?",
             "A butter-and-pudding cream with quark, made from our vanilla pudding, with a chocolate glaze on top. About 40–45 pieces, 20 minutes at 200 °C."),
            ("Is there a lighter summer version?",
             "Yes: skip the buttercream and glaze, fill with sweetened whipped cream and strawberries, dust with icing sugar."),
        ],
        "karamelove-vetrniky-recept": [
            ("How are the caramel cream puffs layered?",
             "A choux shell, vanilla pudding cream, a ring of caramel whipped cream and a caramel glaze. About 24 medium puffs."),
            ("Why make the caramel cream the day before?",
             "The caramel-and-cream mixture must chill until it whips stiff. Do not open the oven while the shells bake, or they will collapse."),
        ],
        "irsky-sticky-toffee-pudding-recept": [
            ("Does the sticky toffee pudding use our cocoa?",
             "Yes. 60 g Dutch-process cocoa and 100 ml Baileys in the date batter, 6 portions, 45–50 minutes at 160 °C, salted toffee sauce."),
            ("Why add Baileys after boiling the dates?",
             "Off the heat, because longer boiling would drive off the alcohol and mute the liqueur. The water is 180 ml, 100 ml less than in the original recipe, matching the volume of Baileys."),
        ],
    },
    "de": {
        "sisky-s-makem-recept": [
            ("Wie macht man Mohnnockerl aus unserer Knödelmischung?",
             "Kartoffelknödelpulver nach Packungsanleitung mit Wasser mischen, Nockerl formen, bei 200 °C beidseitig goldbraun backen, 5 Minuten in kochendem Wasser blanchieren und in Mohn, Zucker und Butter wenden."),
            ("Bei welcher Temperatur backt man Šišky s mákem?",
             "Bei 200 °C auf der mittleren Schiene, auf gefettetem Blech, einmal wenden."),
        ],
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept": [
            ("Wie lange backt der Birnenkuchen mit Vanillepudding?",
             "20 Minuten Vorbereitung und ca. 45 Minuten bei 180 °C. Das Rezept ergibt 8 Stücke und geht auch mit Äpfeln, Himbeeren oder Pfirsichen."),
            ("Wie viel Puddingpulver kommt in den Birnenkuchen?",
             "40 g unseres Vanillepuddingpulvers in die Gussmasse mit Sauerrahm, Sahne, Zucker und Ei."),
        ],
        "strapacky-se-zelim-a-slaninou-recept": [
            ("Woraus bestehen unsere Strapačky?",
             "Aus der Mischung für haarige Knödel, als Halušky ins kochende Wasser gedrückt, dazu Sauerkraut, Speck und Frühlingszwiebel."),
            ("Wie lange dauern Strapačky?",
             "Etwa 30 Minuten: Teig anrühren, Halušky kochen, bis sie aufschwimmen, Kraut 10 Minuten kochen, Speck ausbraten."),
        ],
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": [
            ("Backt man die Bebe-Schnitten mit Schokopudding?",
             "Nein. Sie werden nicht gebacken: helle Kekse, gekochter Pudding, dunkle Kekse, Sahne mit Sauerrahm, darüber Kakao. Am besten über Nacht kühlen."),
            ("Geht Vanillepudding statt Schokolade?",
             "Ja. Die Schnitte schmeckt auch mit unserem Vanillepudding und Zimt."),
        ],
        "slehackova-rolada-recept": [
            ("Ist die Sahnerolle glutenfrei?",
             "Ja. Der Biskuit besteht nur aus Eiern, Puderzucker und Kakao holländischer Art — ohne Mehl, also ohne Gluten. Fertig in ca. 30 Minuten."),
            ("Bei welcher Temperatur backt die Sahnerolle?",
             "8 Minuten bei 180 °C, Ofen nicht öffnen. Auskühlen lassen, mit Sahne bestreichen, aufrollen."),
        ],
        "domaci-pernik-recept-podle-jirina-juzlova": [
            ("Brauche ich für den Lebkuchen eine Waage?",
             "Nein. Tassenrezept von Jiřina Jůzlová: 10 Minuten rühren, 20–25 Minuten bei 180 °C, 25–30 Stücke. Im Teig: Vanillepuddingpulver und Kakao holländischer Art."),
            ("Wann ist der Lebkuchen fertig?",
             "Ein Holzstäbchen muss sauber herauskommen, ohne anhaftenden Teig."),
        ],
        "bramborovo-tvarohove-knedliky-s-jahodami": [
            ("Wie schnell sind die Erdbeer-Quark-Knödel fertig?",
             "In 20 Minuten: Teig aus Kartoffelknödelmischung und Quark, eine Erdbeere hinein, 5 Minuten dämpfen."),
            ("Welchen Quark für Obstknödel?",
             "Weichen Blockquark, nicht den Becherquark — 250 g auf 250 g unserer Mischung."),
        ],
        "rychle-venecky-ci-vetrnicky-recept": [
            ("Warum wird der Brandteig bei 250 °C gebacken?",
             "Der heiße Start bei 250 °C und mehr Butter (90 g auf 140 g Mehl) lassen den Teig schnell aufgehen. Nach 5 Minuten auf 200 °C zurückschalten. Etwa 80 Stück auf zwei Blechen."),
            ("Reicht ein Teig für Kränze und Windbeutel?",
             "Ja. Derselbe Brandteig: Kränze als zwei Ringe, Windbeutel als Häufchen. Die Füllung nach Wunsch."),
        ],
        "venecky-s-vanilkovym-kremem-recept": [
            ("Womit füllt man die Vanillecreme-Kränze?",
             "Vanille-Buttercreme aus unserem Pudding, Eigelb und Butter, darauf Rumglasur. Etwa 20 Stück."),
            ("Wie backt man Brandteigschalen, ohne dass sie fallen?",
             "10 Minuten bei 200 °C, ohne den Ofen zu öffnen, dann 15–25 Minuten bei 180 °C, bis sie sattgold und trocken sind. Vor dem Füllen vollständig auskühlen lassen."),
        ],
        "kremrole-recept": [
            ("Wie viele Schaumrollen ergibt das Rezept und was brauche ich?",
             "Etwa 35–40 Stück. Butterteig mit italienischer Meringue. Sie brauchen Metallhülsen; notfalls geht Alufolie."),
            ("Bei welcher Temperatur backt man Kremrole?",
             "12–15 Minuten bei 180–200 °C goldbraun. Meringue: Zuckersirup auf 115–120 °C kochen und in den steifen Eischnee gießen."),
        ],
        "minivetrnicky-recept": [
            ("Womit füllt man die Mini-Windbeutel?",
             "Mit Butter-Puddingcreme mit Quark aus unserem Vanillepudding, darauf Schokoglasur. Etwa 40–45 Stück, 20 Minuten bei 200 °C."),
            ("Gibt es eine leichtere Sommerversion?",
             "Ja: statt Buttercreme und Glasur gesüßte Sahne und Erdbeeren, darüber Puderzucker."),
        ],
        "karamelove-vetrniky-recept": [
            ("Wie sind die Karamell-Windbeutel geschichtet?",
             "Brandteigschale, Vanillepuddingcreme, ein Ring Karamellsahne, Karamellglasur. Etwa 24 mittelgroße Stück."),
            ("Warum die Karamellsahne am Vortag zubereiten?",
             "Die Karamell-Sahne-Mischung muss durchkühlen, bis sie sich steif schlagen lässt. Den Ofen beim Backen der Schalen nicht öffnen, sonst fallen die Windbeutel zusammen."),
        ],
        "irsky-sticky-toffee-pudding-recept": [
            ("Ist unser Kakao im Sticky-Toffee-Pudding?",
             "Ja. 60 g Kakao holländischer Art und 100 ml Baileys im Dattelteig, 6 Portionen, 45–50 Minuten bei 160 °C, gesalzene Toffeesauce."),
            ("Warum Baileys erst nach dem Kochen der Datteln?",
             "Vom Herd genommen — längeres Kochen würde den Alkohol austreiben und den Likörgeschmack dämpfen. Wasser: 180 ml, also 100 ml weniger als im Original, genau die Baileys-Menge."),
        ],
    },
    "sk": {
        "sisky-s-makem-recept": [
            ("Ako sa robia šišky s makom z knedieľ v prášku?",
             "Zemiakové knedle v prášku zmiešajte s vodou podľa návodu, vytvarujte šišky, pečte na 200 °C dozlatista z oboch strán, 5 minút sparte vo vriacej vode a obalte v maku, cukre a masle."),
            ("Na koľko stupňov piecť šišky s makom?",
             "Na 200 °C v strede rúry, na vymastenom plechu, s jedným otočením, aby mali zlatistú kôrku z oboch strán."),
        ],
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept": [
            ("Ako dlho sa pečie hruškový koláč s vanilkovým pudingom?",
             "20 minút prípravy a cca 45 minút pečenia na 180 °C. Recept je na 8 porcií a funguje aj s jablkami, malinami alebo broskyňami."),
            ("Koľko pudingu patrí do hruškového koláča?",
             "40 g nášho vanilkového pudingu v prášku do liatej vrstvy so zakysanou smotanou, šľahačkou, cukrom a vajcom."),
        ],
        "strapacky-se-zelim-a-slaninou-recept": [
            ("Z čoho sa robia naše strapačky?",
             "Z chlpatých knedieľ v prášku pretlačených na halušky do vriacej vody, s kyslou kapustou, slaninou a jarnou cibuľkou."),
            ("Ako dlho trvá príprava strapačiek?",
             "Asi 30 minút: cesto podľa návodu, halušky variť, kým vyplávajú, kapustu 10 minút povariť, slaninu opražiť."),
        ],
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": [
            ("Pečú sa bebe rezy s čokoládovým pudingom?",
             "Nie. Sú nepečené: vrstva svetlých sušienok, uvarený puding, tmavé sušienky, šľahačka so zakysanou smotanou a kakao. Najlepšie cez noc v chladničke."),
            ("Možno namiesto čokoládového pudingu použiť vanilkový?",
             "Áno. Rez chutí výborne aj s naším vanilkovým pudingom a škoricovým posypom."),
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
             "Dreveným špáradlom — po vpichnutí musí ostať čisté, bez prilepeného cesta."),
        ],
        "bramborovo-tvarohove-knedliky-s-jahodami": [
            ("Ako rýchlo sú zemiakovo-tvarohové knedle s jahodami hotové?",
             "Za 20 minút: cesto zo zemiakových knedieľ v prášku a tvarohu, jahoda dnu, 5 minút v pare."),
            ("Aký tvaroh do ovocných knedieľ?",
             "Mäkký tvaroh v kocke, nie vo vaničke — 250 g na 250 g našej zmesi."),
        ],
        "rychle-venecky-ci-vetrnicky-recept": [
            ("Prečo pečiete venčeky na 250 °C?",
             "Horúci štart na 250 °C a vyšší podiel masla (90 g na 140 g múky) cesto rýchlo nafúknu. Po 5 minútach znížte na 200 °C. Asi 80 kúskov na dvoch plechoch."),
            ("Hodí sa jedno cesto na venčeky aj vetrníčky?",
             "Áno. Rovnaké odpaľované cesto: venčeky ako dva krúžky, vetrníčky ako kôpky. Náplň podľa chuti — šľahačka, vanilkový krém alebo karamel."),
        ],
        "venecky-s-vanilkovym-kremem-recept": [
            ("Čím sa plnia venčeky s vanilkovým krémom?",
             "Vanilkovým maslovým krémom z nášho pudingu, žĺtkov a masla, navrch rumová poleva. Asi 20 kúskov."),
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
            ("Čím sa plnia minivetrníčky?",
             "Maslovo-pudingovým krémom s tvarohom z nášho vanilkového pudingu, navrch čokoládová poleva. Asi 40–45 kúskov, pečenie 20 minút na 200 °C."),
            ("Existuje ľahšia letná varianta minivetrníčkov?",
             "Áno: namiesto maslového krému a polevy plňte osladenou šľahačkou a jahodami, posypte práškovým cukrom."),
        ],
        "karamelove-vetrniky-recept": [
            ("Ako sa skladajú karamelové vetrníky?",
             "Škrupina z odpaľovaného cesta, vanilkový pudingový krém, krúžok karamelovej šľahačky a karamelová poleva. Asi 24 stredných kúskov."),
            ("Prečo pripraviť karamelovú šľahačku deň vopred?",
             "Karamel so smotanou musí v chladničke stuhnúť, aby šľahačka držala tvar. Rúru pri pečení škrupín neotvárajte — vetrníky by spadli."),
        ],
        "irsky-sticky-toffee-pudding-recept": [
            ("Je v írskom sticky toffee puddingu naše kakao?",
             "Áno. 60 g kakaa holandského typu a 100 ml Baileys v datľovom ceste, 6 porcií, 45–50 minút na 160 °C, slaná toffee omáčka."),
            ("Prečo sa Baileys pridáva až po povarení datlí?",
             "Mimo platne — dlhší var by vyhnal alkohol a stlmil chuť likéru. Vody je 180 ml (o 100 ml menej než v pôvodnom recepte), práve o množstvo Baileys."),
        ],
    },
}


def site_faq(lang):
    """Grouped FAQ page content: [(heading, [(q, a), ...]), ...]."""
    groups = SITE_FAQ.get(lang) or SITE_FAQ["cs"]
    return [(h, list(qas)) for h, qas in groups]


def b2b_faq(lang):
    items = list(B2B_FAQ.get(lang) or B2B_FAQ["cs"])
    seen = {q for q, _a in items}
    for q, a in b2b_cocoa_faq(lang):
        if q not in seen:
            items.append((q, a))
            seen.add(q)
    return items


def recipe_faq(lang, slug):
    pack = RECIPE_FAQ.get(lang) or RECIPE_FAQ["cs"]
    return pack.get(slug) or []
