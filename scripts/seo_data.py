"""Language-independent SEO / GEO facts used by the site generator.

Recipe times are ISO-8601 duration strings for schema.org Recipe.
Seed ratings are stored as integer tenths so averages stay exact (4.7 → 47).
"""

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

# Cycle requested: 4.7, 4.5, 4.8, 4.4. Counts 50–100.
_RATING_CYCLE = (4.7, 4.5, 4.8, 4.4)
_RATING_COUNTS = (87, 64, 92, 71, 55, 98, 76, 53, 81, 69, 58, 94, 62)

RECIPE_RATINGS = {}
for _i, _slug in enumerate(RECIPE_SLUGS):
    _rating = _RATING_CYCLE[_i % 4]
    _count = _RATING_COUNTS[_i]
    _tenths = int(round(_rating * 10))
    RECIPE_RATINGS[_slug] = {
        "rating": _rating,
        "count": _count,
        "sum_tenths": _tenths * _count,
    }

RECIPE_TIMES = {
    "sisky-s-makem-recept": {
        "prepTime": "PT15M", "cookTime": "PT25M", "totalTime": "PT40M",
        "recipeYield": "4", "datePublished": "2017-04-15",
    },
    "hruskovy-kolac-s-vanilkovym-pudinkem-recept": {
        "prepTime": "PT20M", "cookTime": "PT45M", "totalTime": "PT65M",
        "recipeYield": "8", "datePublished": "2017-04-15",
    },
    "strapacky-se-zelim-a-slaninou-recept": {
        "prepTime": "PT10M", "cookTime": "PT20M", "totalTime": "PT30M",
        "recipeYield": "4", "datePublished": "2017-04-15",
    },
    "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": {
        "prepTime": "PT25M", "cookTime": "PT0M", "totalTime": "PT25M",
        "recipeYield": "12", "datePublished": "2017-04-15",
    },
    "slehackova-rolada-recept": {
        "prepTime": "PT20M", "cookTime": "PT8M", "totalTime": "PT30M",
        "recipeYield": "8", "datePublished": "2017-04-15",
        "suitableForDiet": "https://schema.org/GlutenFreeDiet",
    },
    "domaci-pernik-recept-podle-jirina-juzlova": {
        "prepTime": "PT10M", "cookTime": "PT25M", "totalTime": "PT35M",
        "recipeYield": "28", "datePublished": "2017-04-15",
    },
    "bramborovo-tvarohove-knedliky-s-jahodami": {
        "prepTime": "PT15M", "cookTime": "PT5M", "totalTime": "PT20M",
        "recipeYield": "4", "datePublished": "2017-04-15",
    },
    "rychle-venecky-ci-vetrnicky-recept": {
        "prepTime": "PT45M", "cookTime": "PT15M", "totalTime": "PT60M",
        "recipeYield": "80", "datePublished": "2026-09-02",
    },
    "venecky-s-vanilkovym-kremem-recept": {
        "prepTime": "PT60M", "cookTime": "PT35M", "totalTime": "PT95M",
        "recipeYield": "20", "datePublished": "2026-09-02",
    },
    "kremrole-recept": {
        "prepTime": "PT90M", "cookTime": "PT15M", "totalTime": "PT105M",
        "recipeYield": "38", "datePublished": "2026-09-02",
    },
    "minivetrnicky-recept": {
        "prepTime": "PT50M", "cookTime": "PT20M", "totalTime": "PT70M",
        "recipeYield": "42", "datePublished": "2026-09-02",
    },
    "karamelove-vetrniky-recept": {
        "prepTime": "PT90M", "cookTime": "PT30M", "totalTime": "PT120M",
        "recipeYield": "24", "datePublished": "2026-09-02",
    },
    "irsky-sticky-toffee-pudding-recept": {
        "prepTime": "PT25M", "cookTime": "PT50M", "totalTime": "PT75M",
        "recipeYield": "6", "datePublished": "2026-09-02",
    },
}

RECIPE_CATEGORY = {
    "cs": {
        "sisky-s-makem-recept": "Hlavní jídlo",
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept": "Dezerty",
        "strapacky-se-zelim-a-slaninou-recept": "Hlavní jídlo",
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": "Dezerty",
        "slehackova-rolada-recept": "Dezerty",
        "domaci-pernik-recept-podle-jirina-juzlova": "Dezerty",
        "bramborovo-tvarohove-knedliky-s-jahodami": "Hlavní jídlo",
        "rychle-venecky-ci-vetrnicky-recept": "Cukrářské pečivo",
        "venecky-s-vanilkovym-kremem-recept": "Cukrářské pečivo",
        "kremrole-recept": "Cukrářské pečivo",
        "minivetrnicky-recept": "Cukrářské pečivo",
        "karamelove-vetrniky-recept": "Cukrářské pečivo",
        "irsky-sticky-toffee-pudding-recept": "Dezerty",
    },
    "en": {
        "sisky-s-makem-recept": "Main course",
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept": "Dessert",
        "strapacky-se-zelim-a-slaninou-recept": "Main course",
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": "Dessert",
        "slehackova-rolada-recept": "Dessert",
        "domaci-pernik-recept-podle-jirina-juzlova": "Dessert",
        "bramborovo-tvarohove-knedliky-s-jahodami": "Main course",
        "rychle-venecky-ci-vetrnicky-recept": "Pastry",
        "venecky-s-vanilkovym-kremem-recept": "Pastry",
        "kremrole-recept": "Pastry",
        "minivetrnicky-recept": "Pastry",
        "karamelove-vetrniky-recept": "Pastry",
        "irsky-sticky-toffee-pudding-recept": "Dessert",
    },
    "de": {
        "sisky-s-makem-recept": "Hauptgericht",
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept": "Dessert",
        "strapacky-se-zelim-a-slaninou-recept": "Hauptgericht",
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": "Dessert",
        "slehackova-rolada-recept": "Dessert",
        "domaci-pernik-recept-podle-jirina-juzlova": "Dessert",
        "bramborovo-tvarohove-knedliky-s-jahodami": "Hauptgericht",
        "rychle-venecky-ci-vetrnicky-recept": "Konditorei",
        "venecky-s-vanilkovym-kremem-recept": "Konditorei",
        "kremrole-recept": "Konditorei",
        "minivetrnicky-recept": "Konditorei",
        "karamelove-vetrniky-recept": "Konditorei",
        "irsky-sticky-toffee-pudding-recept": "Dessert",
    },
    "sk": {
        "sisky-s-makem-recept": "Hlavné jedlo",
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept": "Dezerty",
        "strapacky-se-zelim-a-slaninou-recept": "Hlavné jedlo",
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": "Dezerty",
        "slehackova-rolada-recept": "Dezerty",
        "domaci-pernik-recept-podle-jirina-juzlova": "Dezerty",
        "bramborovo-tvarohove-knedliky-s-jahodami": "Hlavné jedlo",
        "rychle-venecky-ci-vetrnicky-recept": "Cukrárske pečivo",
        "venecky-s-vanilkovym-kremem-recept": "Cukrárske pečivo",
        "kremrole-recept": "Cukrárske pečivo",
        "minivetrnicky-recept": "Cukrárske pečivo",
        "karamelove-vetrniky-recept": "Cukrárske pečivo",
        "irsky-sticky-toffee-pudding-recept": "Dezerty",
    },
}

CUISINE = {"cs": "Česká", "en": "Czech", "de": "Tschechisch", "sk": "Česká"}

KEYWORDS = {
    "cs": {
        "home": "Jůzlová, knedlíky v prášku, chlupaté knedlíky, bosáky, vanilkový puding bez lepku, kakao holandského typu, vanilínový cukr, Kochánov, Vysočina, potravinářské směsi",
        "kdo_jsme": "Jůzlová, kdo jsme, rodinná dílna, Kochánov, výroba od 2004, KLASA mouka",
        "kde_nas_najdete": "odběr Kochánov, Humpolec, rozvoz Vysočina, Havlíčkův Brod, Jihlava, dodání zboží Jůzlová",
        "kontakt": "kontakt Jůzlová, Jiřina Jůzlová, Jiří Jůzl, telefon, Kochánov 40, juzlj@seznam.cz",
        "ceny": "ceník Jůzlová, cena knedlíků v prášku, puding 34 Kč, kakao 100 Kč",
        "recepty": "recepty Jůzlová, šišky s mákem, strapačky, perník, věnečky, pudinkové recepty",
        "faq": "Jůzlová FAQ, jak objednat knedlíky v prášku, bezlepkový puding, rozvoz Vysočina",
        "products": {
            "bramborove_knedliky": "bramborové knedlíky v prášku, bramborové těsto, šišky, gnocchi, KLASA, 5 kg 165 Kč",
            "chlupate_knedliky": "chlupaté knedlíky, bosáky, halušky, strapačky, 15 minut, 5 kg 185 Kč",
            "vanilkovy_pudink": "vanilkový puding bez lepku, kukuřičný škrob, 1 kg 34 Kč, Jůzlová pudink",
            "kakao_holandskeho_typu": "kakao holandského typu, 21 % tuku, cukrářské kakao, bez cukru, 500 g 100 Kč",
            "vanilkovy_cukr": "vanilínový cukr, vanilin, posyp cukroví, 1 kg 38 Kč, Jůzlová",
        },
    },
    "en": {
        "home": "Jůzlová, potato dumpling mix, hairy dumplings, gluten-free vanilla pudding, Dutch-process cocoa, vanilla sugar, Kochánov, Czech food mixes",
        "kdo_jsme": "Jůzlová about, family workshop, Kochánov, since 2004, KLASA flour",
        "kde_nas_najdete": "Jůzlová pickup Kochánov Humpolec, Vysočina delivery, Havlíčkův Brod, Jihlava",
        "kontakt": "Jůzlová contact, Jiřina Jůzlová, Jiří Jůzl, Kochánov 40, juzlj@seznam.cz",
        "ceny": "Jůzlová price list, dumpling mix price, pudding 34 CZK, cocoa 100 CZK",
        "recepty": "Jůzlová recipes, poppy-seed rolls, strapačky, gingerbread, cream puffs, pudding desserts",
        "faq": "Jůzlová FAQ, how to order dumpling mix, gluten-free pudding, Vysočina delivery",
        "products": {
            "bramborove_knedliky": "potato dumpling mix, potato dough, gnocchi, KLASA flour, 5 kg 165 CZK",
            "chlupate_knedliky": "hairy dumplings, bosáky, halušky, strapačky, 15 minutes, 5 kg 185 CZK",
            "vanilkovy_pudink": "gluten-free vanilla pudding, corn starch, 1 kg 34 CZK",
            "kakao_holandskeho_typu": "Dutch-process cocoa, 21% fat, unsweetened cocoa, 500 g 100 CZK",
            "vanilkovy_cukr": "vanilla sugar, vanillin, dusting sugar, 1 kg 38 CZK",
        },
    },
    "de": {
        "home": "Jůzlová, Kartoffelknödelmischung, Haarige Knödel, glutenfreier Vanillepudding, Kakao holländischer Art, Vanillinzucker, Kochánov",
        "kdo_jsme": "Jůzlová über uns, Familienbetrieb, Kochánov, seit 2004, KLASA Mehl",
        "kde_nas_najdete": "Abholung Kochánov Humpolec, Lieferung Vysočina, Havlíčkův Brod, Jihlava",
        "kontakt": "Jůzlová Kontakt, Jiřina Jůzlová, Jiří Jůzl, Kochánov 40, juzlj@seznam.cz",
        "ceny": "Jůzlová Preisliste, Knödelmischung Preis, Pudding 34 Kč, Kakao 100 Kč",
        "recepty": "Jůzlová Rezepte, Mohnnockerl, Strapačky, Lebkuchen, Brandteig, Puddingdesserts",
        "faq": "Jůzlová FAQ, Knödelmischung bestellen, glutenfreier Pudding, Lieferung Vysočina",
        "products": {
            "bramborove_knedliky": "Kartoffelknödelmischung, Kartoffelteig, Gnocchi, KLASA, 5 kg 165 Kč",
            "chlupate_knedliky": "Haarige Knödel, Bosáky, Halušky, Strapačky, 15 Minuten, 5 kg 185 Kč",
            "vanilkovy_pudink": "glutenfreier Vanillepudding, Maisstärke, 1 kg 34 Kč",
            "kakao_holandskeho_typu": "Kakao holländischer Art, 21 % Fett, ungesüßt, 500 g 100 Kč",
            "vanilkovy_cukr": "Vanillinzucker, Vanillin, Puder, 1 kg 38 Kč",
        },
    },
    "sk": {
        "home": "Jůzlová, zemiakové knedle v prášku, chlpaté knedle, vanilkový puding bez lepku, kakao holandského typu, vanilínový cukor, Kochánov",
        "kdo_jsme": "Jůzlová kto sme, rodinná dielňa, Kochánov, od 2004, KLASA múka",
        "kde_nas_najdete": "odber Kochánov Humpolec, rozvoz Vysočina, Havlíčkův Brod, Jihlava",
        "kontakt": "kontakt Jůzlová, Jiřina Jůzlová, Jiří Jůzl, Kochánov 40, juzlj@seznam.cz",
        "ceny": "cenník Jůzlová, cena knedieľ v prášku, puding 34 Kč, kakao 100 Kč",
        "recepty": "recepty Jůzlová, šišky s makom, strapačky, perník, venčeky, pudingové recepty",
        "faq": "Jůzlová FAQ, ako objednať knedle v prášku, bezlepkový puding, rozvoz Vysočina",
        "products": {
            "bramborove_knedliky": "zemiakové knedle v prášku, zemiakové cesto, gnocchi, KLASA, 5 kg 165 Kč",
            "chlupate_knedliky": "chlpaté knedle, bosáky, halušky, strapačky, 15 minút, 5 kg 185 Kč",
            "vanilkovy_pudink": "vanilkový puding bez lepku, kukuričný škrob, 1 kg 34 Kč",
            "kakao_holandskeho_typu": "kakao holandského typu, 21 % tuku, bez cukru, 500 g 100 Kč",
            "vanilkovy_cukr": "vanilínový cukor, vanilín, posyp, 1 kg 38 Kč",
        },
    },
}

RECIPE_KEYWORDS = {
    "cs": {
        "sisky-s-makem-recept": "šišky s mákem, bramborové šišky, recept Jůzlová, mák cukr máslo",
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept": "hruškový koláč, vanilkový pudink, recept Lucie Kůželová",
        "strapacky-se-zelim-a-slaninou-recept": "strapačky, chlupaté knedlíky, halušky se zelím, slanina",
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": "bebe řezy, čokoládový puding, nepečený dezert",
        "slehackova-rolada-recept": "šlehačková roláda, bezlepková roláda, kakao holandského typu",
        "domaci-pernik-recept-podle-jirina-juzlova": "domácí perník, hrníčkový perník, Jiřina Jůzlová",
        "bramborovo-tvarohove-knedliky-s-jahodami": "ovocné knedlíky, jahody, tvaroh, bramborové těsto",
        "rychle-venecky-ci-vetrnicky-recept": "věnečky, větrníčky, odpalované těsto, 250 °C",
        "venecky-s-vanilkovym-kremem-recept": "věnečky s krémem, vanilkový máslový krém, rumová poleva",
        "kremrole-recept": "kremrole, italský sníh, máslové těsto, trubičky",
        "minivetrnicky-recept": "minivětrníčky, pudinkový krém, čokoládová poleva",
        "karamelove-vetrniky-recept": "karamelové větrníky, karamelová šlehačka, vanilkový pudink",
        "irsky-sticky-toffee-pudding-recept": "sticky toffee pudding, Baileys, kakao holandského typu, datle",
    },
    "en": {
        "sisky-s-makem-recept": "poppy seed potato rolls, šišky s mákem, Jůzlová recipe",
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept": "pear cake vanilla pudding, Czech cake recipe",
        "strapacky-se-zelim-a-slaninou-recept": "strapačky, sauerkraut dumplings, hairy dumpling mix",
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": "no-bake biscuit cake, chocolate pudding slices",
        "slehackova-rolada-recept": "gluten-free cream roll, Dutch-process cocoa roulade",
        "domaci-pernik-recept-podle-jirina-juzlova": "Czech gingerbread, cup gingerbread, Jiřina Jůzlová",
        "bramborovo-tvarohove-knedliky-s-jahodami": "strawberry dumplings, quark, potato dough",
        "rychle-venecky-ci-vetrnicky-recept": "cream puffs, choux pastry, věnečky větrníčky",
        "venecky-s-vanilkovym-kremem-recept": "vanilla cream rings, rum glaze, choux",
        "kremrole-recept": "kremrole, Italian meringue, cream horns",
        "minivetrnicky-recept": "mini cream puffs, pudding cream, chocolate glaze",
        "karamelove-vetrniky-recept": "caramel cream puffs, caramel whipped cream",
        "irsky-sticky-toffee-pudding-recept": "sticky toffee pudding, Baileys, Dutch-process cocoa",
    },
    "de": {
        "sisky-s-makem-recept": "Mohnnockerl, Kartoffelteig, Jůzlová Rezept",
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept": "Birnenkuchen Vanillepudding, tschechischer Kuchen",
        "strapacky-se-zelim-a-slaninou-recept": "Strapačky, Sauerkraut, Haarige Knödel",
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": "Keksschnitte, Schokopudding, ohne Backen",
        "slehackova-rolada-recept": "Sahnerolle glutenfrei, Kakao holländischer Art",
        "domaci-pernik-recept-podle-jirina-juzlova": "Lebkuchen, Tassenrezept, Jiřina Jůzlová",
        "bramborovo-tvarohove-knedliky-s-jahodami": "Erdbeerknödel, Quark, Kartoffelteig",
        "rychle-venecky-ci-vetrnicky-recept": "Brandteig, Windbeutel, Kränze",
        "venecky-s-vanilkovym-kremem-recept": "Vanillecreme Kränze, Rumglasur",
        "kremrole-recept": "Schaumrollen, italienische Meringue",
        "minivetrnicky-recept": "Mini-Windbeutel, Puddingcreme, Schokoglasur",
        "karamelove-vetrniky-recept": "Karamell-Windbeutel, Karamellsahne",
        "irsky-sticky-toffee-pudding-recept": "Sticky Toffee Pudding, Baileys, Kakao",
    },
    "sk": {
        "sisky-s-makem-recept": "šišky s makom, zemiakové šišky, recept Jůzlová",
        "hruskovy-kolac-s-vanilkovym-pudinkem-recept": "hruškový koláč, vanilkový puding",
        "strapacky-se-zelim-a-slaninou-recept": "strapačky, chlpaté knedle, halušky so zelím",
        "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": "bebe rezy, čokoládový puding, nepečený dezert",
        "slehackova-rolada-recept": "šľahačková roláda, bezlepková roláda, kakao",
        "domaci-pernik-recept-podle-jirina-juzlova": "domáci perník, hrnčekový perník, Jiřina Jůzlová",
        "bramborovo-tvarohove-knedliky-s-jahodami": "ovocné knedle, jahody, tvaroh",
        "rychle-venecky-ci-vetrnicky-recept": "venčeky, vetrníčky, odpaľované cesto",
        "venecky-s-vanilkovym-kremem-recept": "venčeky s krémom, vanilkový maslový krém",
        "kremrole-recept": "kremrole, taliansky sneh, trubičky",
        "minivetrnicky-recept": "minivetrníčky, pudingový krém, čokoládová poleva",
        "karamelove-vetrniky-recept": "karamelové vetrníky, karamelová šľahačka",
        "irsky-sticky-toffee-pudding-recept": "sticky toffee pudding, Baileys, kakao holandského typu",
    },
}

SITEMAP_PRIORITY = {
    "": 1.0,
    "faq/": 0.9,
    "recepty/": 0.9,
    "ceny/": 0.8,
    "kdo_jsme/": 0.7,
    "kde-nas-najdete/": 0.7,
    "kontakt/": 0.7,
}

PRODUCT_PRIORITY = 0.9
RECIPE_PRIORITY = 0.8


def keywords_for(lang, kind, key=""):
    pack = KEYWORDS.get(lang) or KEYWORDS["cs"]
    if kind == "product":
        return pack["products"].get(key, pack["home"])
    if kind == "recipe":
        return (RECIPE_KEYWORDS.get(lang) or RECIPE_KEYWORDS["cs"]).get(key, pack["recepty"])
    return pack.get(kind, pack["home"])


def rating_payload(slug):
    row = RECIPE_RATINGS[slug]
    value = round(row["sum_tenths"] / 10 / row["count"], 1)
    return {
        "ratingValue": value,
        "ratingCount": row["count"],
        "bestRating": 5,
        "worstRating": 1,
    }


def seed_store():
    recipes = {}
    for slug, row in RECIPE_RATINGS.items():
        recipes[slug] = {"sum_tenths": row["sum_tenths"], "count": row["count"]}
    return {"version": 1, "recipes": recipes}
