#!/usr/bin/env python3
"""Check actual generated product markup against the existing published prices."""
import json
import re
from urllib.parse import urlsplit
import build_site as site

expected = {'bramborove_knedliky': [(5, 'KGM', '250')],
            'chlupate_knedliky': [(5, 'KGM', '260')],
            'vanilkovy_pudink': [(1, 'KGM', '60'), (400, 'GRM', '30')],
            'kakao_holandskeho_typu': [(500, 'GRM', '270')],
            'vanilkovy_cukr': [(1, 'KGM', '60')]}
data = {lg: site.load(lg) for lg in site.LANGS}
count = 0
for lg in site.LANGS:
    for pid in site.page_ids(lg, data):
        text = (site.ROOT / urlsplit(site.url_of(lg, pid)).path.lstrip('/') / 'index.html').read_text()
        blocks = [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S)]
        org = next(x for x in blocks if x.get('@id') == site.BASE + '/#org')
        assert 'FoodManufacturer' not in org['@type']
        assert 'aggregateRating' not in org, 'Self-serving organization ratings must not be marked up'
        page = next(x for x in blocks if x.get('@type') == 'WebPage')
        assert 'dateModified' not in page, 'Do not assign a global date to every page'
        if pid not in expected: continue
        product = next(x for x in blocks if x.get('@type') == 'Product')
        actual = []
        for offer in product['offers']:
            ref = offer['priceSpecification']['referenceQuantity']
            actual.append((ref['value'], ref['unitCode'], offer['price']))
            assert offer['priceCurrency'] == 'CZK' and offer['url'] == site.url_of(lg, pid)
            assert 'availability' not in offer, 'Do not invent live stock availability'
        assert actual == expected[pid], (lg, pid, actual)
        assert product['brand']['@id'] != product['manufacturer']['@id']
        count += 1
print(f'PASS: {count} localized product pages, all six pack offers per language, no false stock or business rating markup')
