#!/usr/bin/env python3
"""Last pass: remaining labels and keywords after the settlement."""
import pathlib

E = [
    ("scripts/content_de.py", ' Gratis-Lieferung in der Vysočina ab Mindestbestellwert.', ' Nach Humpolec und Havlíčkův Brod liefern wir.'),
    ("scripts/content_de.py", '"nav_d2c": "Versand auf Anfrage"', '"nav_d2c": "Wohnen im Ausland"'),
    ("scripts/content_en.py", '; free delivery in Vysočina from set amounts.', '. We deliver to Humpolec and Havlíčkův Brod.'),
    ("scripts/content_en.py", '"nav_d2c": "Posting abroad"', '"nav_d2c": "Living abroad"'),
    ("scripts/content_en.py", 'Potato dough from water alone: no peeling', 'Potato dough, just add water: no peeling'),
    ("scripts/content_sk.py", '"nav_d2c": "Zaslanie po dohode"', '"nav_d2c": "Bývate v zahraničí"'),
    ("scripts/content_sk.py", '("h2", "Rozvoz po Vysočine a iné možnosti")', '("h2", "Rozvoz")'),
    ("scripts/cocoa_faq.py", ' Quantity prices are agreed case by case.', ''),
    ("scripts/seo_data.py", ', quantity pricing"', '"'),
    ("scripts/seo_data.py", ', Mengenpreis"', '"'),
    ("scripts/seo_data.py", ', cena podľa množstva"', '"'),
]
for f, a, b in E:
    p = pathlib.Path(f)
    s = p.read_text()
    assert s.count(a) == 1, (f, a, s.count(a))
    p.write_text(s.replace(a, b))
print("post ok")
