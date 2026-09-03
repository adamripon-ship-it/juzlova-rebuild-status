"""Label data for the packaged mixes, transcribed from the printed sacks.

Every figure here is read off the label a customer actually receives; the
transcription and its provenance are in docs/PRODUCT-LABELS.md. Nothing in
this file may be inferred, rounded to look tidier, or filled in by analogy
with another product — a wrong allergen line is the one mistake on a food
site that can hurt somebody.

Only the products whose labels have been photographed appear in SPEC. The
vanilla pudding, cocoa and vanilla sugar are absent because nobody has sent
a photograph of their sacks yet, and the page renders without the section
rather than showing invented numbers. Adding one is a matter of
photographing the label and filling in an entry.

Numbers are stored with a decimal point and formatted per language at render
time, so the page shows "71,53" in Czech and "71.53" in English from one
source. Energy in kcal is derived from the printed kJ (1 kcal = 4.184 kJ);
the labels print kJ only.
"""

# ── language-neutral figures, per 100 g unless stated ───────────────────────

SPEC = {
    "bramborove_knedliky": {
        "net_weight_g": 5000,
        "nutrition": {
            "energy_kj": "1432.7",
            "carbohydrate_g": "71.53",
            "protein_g": "9.55",
            "fat_g": "1.42",
            "salt_g": "2",
        },
        # For HowTo totalTime: 2-3 min resting plus 15-20 min boiling.
        "prep_time": "PT3M",
        "cook_time": "PT20M",
        "total_time": "PT23M",
    },
    "chlupate_knedliky": {
        "net_weight_g": 5000,
        "nutrition": {
            "energy_kj": "1459.4",
            "carbohydrate_g": "76.49",
            "protein_g": "8.83",
            "fat_g": "1.43",
            "salt_g": "2",
        },
        # 10 min swelling plus 5-8 min boiling.
        "prep_time": "PT10M",
        "cook_time": "PT8M",
        "total_time": "PT18M",
    },
}

# ── translated label text ───────────────────────────────────────────────────
# Czech is the printed original; the rest are translations of it.

TEXT = {
    "cs": {
        "bramborove_knedliky": {
            "ingredients": "pšeničná mouka, sušená bramborová kaše (přírodní barvivo E 100, antioxidant E 304, E 223, emulgátor E 471), sůl, sušená vejce, kypřidlo, škrob",
            "allergens": "lepek, sušená vejce",
            "storage": "Uschovejte v suchu a chladu.",
            "steps": [
                "1 kg směsi nasypeme do misky a přelijeme 1 litrem vody.",
                "Řádně prohněteme a těsto necháme 2 až 3 minuty odležet.",
                "Z těsta vypracujeme válečky o průměru cca 6 cm.",
                "Vložíme je do vroucí vody a vaříme 15 až 20 minut podle velikosti knedlíků.",
            ],
        },
        "chlupate_knedliky": {
            "ingredients": "pšeničná mouka, sušená bramborová kaše, sušené brambory, bramborový škrob, sůl, sušená vejce",
            "allergens": "lepek",
            "storage": "Uschovejte v suchu a chladu.",
            "steps": [
                "1 kg směsi nasypeme do misky a přelijeme 1,2 litru vody.",
                "Řádně promícháme a těsto necháme 10 minut nabobtnat.",
                "Lžící tvarujeme knedlíky a vkládáme je do vroucí vody.",
                "Vaříme, až vyplavou — asi 5 až 8 minut podle velikosti.",
            ],
        },
    },
    "en": {
        "bramborove_knedliky": {
            "ingredients": "wheat flour, dried mashed potato (natural colour E 100, antioxidants E 304 and E 223, emulsifier E 471), salt, dried egg, raising agent, starch",
            "allergens": "gluten, dried egg",
            "storage": "Store in a dry, cool place.",
            "steps": [
                "Tip 1 kg of the mix into a bowl and pour over 1 litre of water.",
                "Knead thoroughly and let the dough rest for 2 to 3 minutes.",
                "Roll the dough into cylinders about 6 cm across.",
                "Lower them into boiling water and cook for 15 to 20 minutes, depending on the size of the dumplings.",
            ],
        },
        "chlupate_knedliky": {
            "ingredients": "wheat flour, dried mashed potato, dried potato, potato starch, salt, dried egg",
            "allergens": "gluten",
            "storage": "Store in a dry, cool place.",
            "steps": [
                "Tip 1 kg of the mix into a bowl and pour over 1.2 litres of water.",
                "Stir thoroughly and leave the dough to swell for 10 minutes.",
                "Shape the dumplings with a spoon and drop them into boiling water.",
                "Cook until they float — about 5 to 8 minutes, depending on size.",
            ],
        },
    },
    "de": {
        "bramborove_knedliky": {
            "ingredients": "Weizenmehl, Kartoffelpüreepulver (natürlicher Farbstoff E 100, Antioxidationsmittel E 304 und E 223, Emulgator E 471), Salz, Trockenei, Backtriebmittel, Stärke",
            "allergens": "Gluten, Trockenei",
            "storage": "Trocken und kühl lagern.",
            "steps": [
                "1 kg der Mischung in eine Schüssel geben und mit 1 Liter Wasser übergießen.",
                "Gründlich durchkneten und den Teig 2 bis 3 Minuten ruhen lassen.",
                "Aus dem Teig Rollen von etwa 6 cm Durchmesser formen.",
                "In kochendes Wasser geben und je nach Größe der Knödel 15 bis 20 Minuten garen.",
            ],
        },
        "chlupate_knedliky": {
            "ingredients": "Weizenmehl, Kartoffelpüreepulver, Trockenkartoffeln, Kartoffelstärke, Salz, Trockenei",
            "allergens": "Gluten",
            "storage": "Trocken und kühl lagern.",
            "steps": [
                "1 kg der Mischung in eine Schüssel geben und mit 1,2 Litern Wasser übergießen.",
                "Gründlich verrühren und den Teig 10 Minuten quellen lassen.",
                "Mit einem Löffel Knödel formen und in kochendes Wasser geben.",
                "Garen, bis sie an die Oberfläche steigen — je nach Größe etwa 5 bis 8 Minuten.",
            ],
        },
    },
    "sk": {
        "bramborove_knedliky": {
            "ingredients": "pšeničná múka, sušená zemiaková kaša (prírodné farbivo E 100, antioxidant E 304, E 223, emulgátor E 471), soľ, sušené vajcia, kypriaci prášok, škrob",
            "allergens": "lepok, sušené vajcia",
            "storage": "Uchovávajte v suchu a chlade.",
            "steps": [
                "1 kg zmesi nasypeme do misky a zalejeme 1 litrom vody.",
                "Dôkladne premiesime a cesto necháme 2 až 3 minúty odležať.",
                "Z cesta vypracujeme valčeky s priemerom asi 6 cm.",
                "Vložíme ich do vriacej vody a varíme 15 až 20 minút podľa veľkosti knedlí.",
            ],
        },
        "chlupate_knedliky": {
            "ingredients": "pšeničná múka, sušená zemiaková kaša, sušené zemiaky, zemiakový škrob, soľ, sušené vajcia",
            "allergens": "lepok",
            "storage": "Uchovávajte v suchu a chlade.",
            "steps": [
                "1 kg zmesi nasypeme do misky a zalejeme 1,2 litra vody.",
                "Dôkladne premiešame a cesto necháme 10 minút napučať.",
                "Lyžicou tvarujeme knedle a vkladáme ich do vriacej vody.",
                "Varíme, kým nevyplávajú — asi 5 až 8 minút podľa veľkosti.",
            ],
        },
    },
}

# ── section and row labels ──────────────────────────────────────────────────

UI = {
    "cs": {
        "spec_h": "Složení a výživové údaje",
        "net_weight": "Hmotnost",
        "ingredients": "Složení",
        "allergens": "Alergenní složky",
        "storage": "Skladování",
        "nutrition": "Výživové údaje na 100 g",
        "prep_h": "Návod k použití",
        "energy": "Energetická hodnota",
        "carbohydrate": "Sacharidy",
        "protein": "Bílkoviny",
        "fat": "Tuky",
        "salt": "Sůl",
        "source": "Údaje odpovídají textu vytištěnému na obalu 5kg balení.",
    },
    "en": {
        "spec_h": "Ingredients and nutrition",
        "net_weight": "Net weight",
        "ingredients": "Ingredients",
        "allergens": "Allergens",
        "storage": "Storage",
        "nutrition": "Nutrition per 100 g",
        "prep_h": "How to prepare",
        "energy": "Energy",
        "carbohydrate": "Carbohydrate",
        "protein": "Protein",
        "fat": "Fat",
        "salt": "Salt",
        "source": "These figures are transcribed from the label printed on the 5 kg sack.",
    },
    "de": {
        "spec_h": "Zutaten und Nährwerte",
        "net_weight": "Füllmenge",
        "ingredients": "Zutaten",
        "allergens": "Allergene",
        "storage": "Lagerung",
        "nutrition": "Nährwerte je 100 g",
        "prep_h": "Zubereitung",
        "energy": "Energie",
        "carbohydrate": "Kohlenhydrate",
        "protein": "Eiweiß",
        "fat": "Fett",
        "salt": "Salz",
        "source": "Die Angaben entsprechen dem Etikett auf dem 5-kg-Sack.",
    },
    "sk": {
        "spec_h": "Zloženie a výživové údaje",
        "net_weight": "Hmotnosť",
        "ingredients": "Zloženie",
        "allergens": "Alergénne zložky",
        "storage": "Skladovanie",
        "nutrition": "Výživové údaje na 100 g",
        "prep_h": "Návod na použitie",
        "energy": "Energetická hodnota",
        "carbohydrate": "Sacharidy",
        "protein": "Bielkoviny",
        "fat": "Tuky",
        "salt": "Soľ",
        "source": "Údaje zodpovedajú textu vytlačenému na obale 5 kg balenia.",
    },
}

# Languages that write decimals with a comma.
_COMMA = {"cs", "de", "sk"}


def num(lang, value):
    """Format a stored dot-decimal for display in `lang`."""
    return value.replace(".", ",") if lang in _COMMA else value


def kcal(energy_kj):
    """kcal from the printed kJ. The labels give kJ only; 1 kcal = 4.184 kJ."""
    return str(round(float(energy_kj) / 4.184))


def spec_for(lang, key):
    """Merged figures and translated text for one product, or None."""
    base = SPEC.get(key)
    text = TEXT.get(lang, {}).get(key)
    if not base or not text:
        return None
    return {**base, **text, "ui": UI[lang]}
