#!/usr/bin/env python3
"""Read-only checks against the real deployment, including its revision."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import urllib.request
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument('--base', required=True)
parser.add_argument('--expected-revision', required=True)
args = parser.parse_args()
base = args.base.rstrip('/')
root = Path(__file__).resolve().parents[1]
ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

def get(path):
    req = urllib.request.Request(base + path, headers={'User-Agent': 'JuzlovaDeploymentCheck/1.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        assert r.status == 200 and r.url == base + path, f'Unexpected status/redirect: {path}'
        return r.read()

config = json.loads(get('/api/config'))
assert config.get('revision') == args.expected_revision, 'Custom domain serves a different revision'
files = ['sitemap.xml', 'robots.txt', 'llms.txt', 'llms-full.txt']
files += [f'sitemap-{lg}.xml' for lg in ['cs', 'en', 'de', 'sk', 'resources']]
files += [f'llms-{lg}.txt' for lg in ['cs', 'en', 'de', 'sk']]
for name in files:
    assert get('/' + name) == (root / name).read_bytes(), f'Stale discovery file: {name}'
paths = []
for lg in ['cs', 'en', 'de', 'sk']:
    xml = ET.parse(root / f'sitemap-{lg}.xml')
    from urllib.parse import urlsplit
    paths += [urlsplit(n.text).path for n in xml.findall('s:url/s:loc', ns)]
with ThreadPoolExecutor(max_workers=5) as pool:
    for path, body in zip(paths, pool.map(get, paths)):
        assert b'<html' in body.lower(), f'Not an HTML page: {path}'
        assert b'assets/measurement.js' in body, f'Missing measurement asset: {path}'
        assert b'FoodManufacturer' not in body, f'Old organization markup: {path}'
assert get('/assets/measurement.js') == (root / 'assets/measurement.js').read_bytes()
print(f'PASS deployed revision, {len(files)} discovery files, {len(paths)} canonical pages and measurement asset at {base}')
