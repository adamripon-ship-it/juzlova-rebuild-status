#!/usr/bin/env python3
"""Validate the sitemap against both route source and generated canonical HTML.

No network, dependencies or writes. Run after build_site.py. This verifies the
build, not whether the production revision has been deployed or indexed.
"""
from collections import Counter
from html.parser import HTMLParser
from urllib.parse import urlsplit
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET
import build_site as site

NS = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9',
      'h': 'http://www.w3.org/1999/xhtml',
      'i': 'http://www.google.com/schemas/sitemap-image/1.1'}


class Head(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.canonical = []
        self.alternates = {}
        self.noindex = False
        self.redirect = False
        self.language = ''
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html':
            self.language = a.get('lang', '')
        if tag == 'link':
            if a.get('rel') == 'canonical':
                self.canonical.append(a.get('href'))
            if a.get('rel') == 'alternate' and a.get('hreflang'):
                assert a['hreflang'] not in self.alternates, 'Duplicate HTML hreflang'
                self.alternates[a['hreflang']] = a.get('href')
        if tag == 'meta':
            if a.get('name', '').lower() in ('robots', 'googlebot', 'bingbot'):
                self.noindex |= 'noindex' in a.get('content', '').lower()
            self.redirect |= a.get('http-equiv', '').lower() == 'refresh'


def verify():
    root = site.ROOT
    data = {lg: site.load(lg) for lg in site.LANGS}
    dates = site.sitemap_content_dates(data)
    expected = {site.url_of(lg, pid): (lg, pid)
                for lg in site.LANGS for pid in site.page_ids(lg, data)}
    html_pages = {}
    # Independently enumerate actual served canonical HTML, not just page_ids().
    for path in root.rglob('index.html'):
        rel = path.relative_to(root)
        if any(x in {'.git', 'archive', 'docs', 'scripts', 'node_modules', 'brand'} for x in rel.parts):
            continue
        head = Head(path.read_text(encoding='utf-8'))
        if head.noindex or head.redirect:
            continue
        uri = rel.as_posix().removesuffix('index.html')
        url = site.BASE + '/' + uri
        assert head.canonical == [url], f'Canonical mismatch: {rel}'
        assert url not in html_pages, f'Duplicate page: {url}'
        html_pages[url] = head
    assert html_pages.keys() == expected.keys(), (
        f'Route/HTML coverage mismatch: missing={expected.keys()-html_pages.keys()}, '
        f'unexpected={html_pages.keys()-expected.keys()}')

    robot = RobotFileParser()
    robot.parse((root / 'robots.txt').read_text().splitlines())
    assert robot.site_maps() == [site.BASE + '/sitemap.xml']
    index = ET.parse(root / 'sitemap.xml').getroot()
    assert index.tag == '{' + NS['s'] + '}sitemapindex'
    children = [n.text for n in index.findall('s:sitemap/s:loc', NS)]
    expected_children = {site.BASE + f'/sitemap-{lg}.xml' for lg in site.LANGS} | {site.BASE + '/sitemap-resources.xml'}
    assert set(children) == expected_children and len(children) == len(expected_children)
    resources = {site.BASE + '/' + n for n in ['llms.txt', 'llms-full.txt'] + [f'llms-{lg}.txt' for lg in site.LANGS]}
    seen = {}; images = set(); counts = Counter()
    for child in children:
        path = root / urlsplit(child).path.lstrip('/')
        assert path.stat().st_size <= 50 * 1024 * 1024
        tree = ET.parse(path).getroot()
        assert tree.tag == '{' + NS['s'] + '}urlset'
        entries = tree.findall('s:url', NS)
        assert len(entries) <= 50000
        for node in entries:
            url = node.find('s:loc', NS).text
            assert url not in seen, f'Duplicate sitemap URL: {url}'
            assert not urlsplit(url).query and not urlsplit(url).fragment
            assert url.startswith(site.BASE + '/')
            assert node.find('s:priority', NS) is None
            assert node.find('s:changefreq', NS) is None
            assert node.find('.//i:title', NS) is None and node.find('.//i:caption', NS) is None
            links = node.findall('h:link', NS)
            alts = {a.get('hreflang'): a.get('href') for a in links}
            assert len(alts) == len(links)
            assert all(a.get('rel') == 'alternate' for a in links)
            if url in resources:
                assert child.endswith('/sitemap-resources.xml') and not alts
                assert (root / urlsplit(url).path.lstrip('/')).is_file()
                assert node.find('s:lastmod', NS) is None
                counts['resources'] += 1
            else:
                assert url in html_pages, f'Noncanonical or unknown URL: {url}'
                lg, pid = expected[url]
                assert child.endswith(f'/sitemap-{lg}.xml')
                assert html_pages[url].language == lg
                assert alts == html_pages[url].alternates, f'HTML/XML alternate mismatch: {url}'
                assert node.findtext('s:lastmod', default=None, namespaces=NS) == dates.get(lg, {}).get(pid)
                counts[lg] += 1
                if site.is_local_page(pid):
                    assert lg == 'cs' and not alts
                else:
                    assert set(alts) == {code for _, code in site.HREFLANG_CODES} | {'x-default'}
                    assert url in alts.values()
                    assert alts['x-default'] == site.url_of('cs', pid)
                for target in alts.values():
                    assert target in html_pages
                    assert html_pages[target].alternates == alts, f'Nonreciprocal alternate: {url}'
            for image in node.findall('i:image/i:loc', NS):
                assert image.text.startswith(site.BASE + '/img/')
                asset = root / urlsplit(image.text).path.lstrip('/')
                assert asset.is_file(), f'Missing image: {image.text}'
                images.add(image.text)
            for bot in ['Googlebot', 'Bingbot', 'OAI-SearchBot', 'Claude-SearchBot', 'PerplexityBot']:
                assert robot.can_fetch(bot, url), f'Blocked URL: {bot} {url}'
            seen[url] = True
    assert set(seen) == set(expected) | resources, 'Sitemap coverage incomplete'
    for bot in ['Googlebot', 'Bingbot', 'OAI-SearchBot', 'Claude-SearchBot', 'PerplexityBot']:
        for path in ['/archive/test/', '/status.html', '/__forms.html']:
            assert not robot.can_fetch(bot, site.BASE + path), f'Exclusion bypassed: {bot} {path}'
    for name in ['llms.txt'] + [f'llms-{lg}.txt' for lg in site.LANGS]:
        text = (root / name).read_text()
        assert site.BASE + '/sitemap.xml' in text and site.BASE + '/llms-full.txt' in text
    assert site.BASE + '/llms.txt' in (root / 'llms-full.txt').read_text()
    print(f'PASS: {len(expected)} canonical HTML pages, {len(resources)} text resources, '
          f'{len(images)} image URLs; {dict(counts)}; full route coverage, reciprocal '
          'hreflang, canonical/language consistency, dates, local assets and robots policy.')


if __name__ == '__main__':
    verify()
