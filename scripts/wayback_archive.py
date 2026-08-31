#!/usr/bin/env python3
"""Mirror everything the Wayback Machine holds for juzlova.cz into archive/.

For every URL ever captured (per the CDX index) this fetches the LAST
successful (HTTP 200) capture:
  - HTML pages   -> archive/pages_html/<slug>.html   (raw original via id_)
                    archive/pages_text/<slug>.txt    (editorial text)
                    archive/seo/<slug>.json          (title, metas, canonical,
                                                      JSON-LD, h1/h2, images)
  - images       -> archive/images/<slug>            (original bytes via im_)
  - robots/feeds -> archive/other/<slug>
  - CDX dumps    -> archive/cdx/  (full capture index + homepage history)
  - manifest     -> archive/manifest.json

The Internet Archive intermittently serves a "Temporarily Offline" page;
every fetch retries through it.
"""
import hashlib
import html as htmllib
import json
import os
import re
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = os.path.join(os.path.dirname(__file__), "..", "archive")
HDR = {"User-Agent": "Mozilla/5.0 (juzlova.cz archive recovery)"}


def fetch(url, tries=12):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=HDR)
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            head = data[:4000]
            if b"Temporarily Offline" in head and b"Internet Archive" in head:
                time.sleep(4 + i * 3)
                continue
            return data
        except Exception:
            time.sleep(4 + i * 3)
    return None


def safe(orig):
    path = re.sub(r"^https?://(www\.)?juzlova\.cz", "", orig).strip("/")
    if not path:
        path = "home"
    s = re.sub(r"[^A-Za-z0-9._-]", "_", urllib.request.unquote(path))
    if len(s) > 140:
        s = s[:140] + "_" + hashlib.md5(orig.encode()).hexdigest()[:8]
    return s


def strip_html(h):
    h = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?is)<br[^>]*>", "\n", h)
    h = re.sub(r"(?is)</(p|div|h[1-6]|li|tr|section|article)>", "\n", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    h = htmllib.unescape(h)
    return re.sub(r"\n\s*\n+", "\n\n", re.sub(r"[ \t]+", " ", h)).strip()


def main():
    for d in ["cdx", "pages_html", "pages_text", "seo", "images", "other"]:
        os.makedirs(os.path.join(BASE, d), exist_ok=True)

    cdx = fetch(
        "https://web.archive.org/cdx/search/cdx?url=juzlova.cz*&limit=100000"
        "&fl=urlkey,timestamp,original,mimetype,statuscode,digest,length"
    )
    if not cdx:
        raise SystemExit("CDX index unreachable")
    open(os.path.join(BASE, "cdx", "all-captures.txt"), "wb").write(cdx)
    hp = fetch(
        "https://web.archive.org/cdx/search/cdx?url=juzlova.cz&limit=10000"
        "&fl=timestamp,statuscode,length,digest"
    )
    if hp:
        open(os.path.join(BASE, "cdx", "homepage-captures.txt"), "wb").write(hp)

    last = {}
    for ln in cdx.decode("utf-8", "replace").splitlines():
        p = ln.split(" ")
        if len(p) < 7 or p[4] != "200":
            continue
        key, ts, orig, mime = p[0], p[1], p[2], p[3]
        cur = last.get(key)
        if not cur or ts > cur[0]:
            last[key] = (ts, orig, mime)

    results = {"pages": [], "images": [], "other": [], "failed": []}

    def do_page(item):
        ts, orig, mime = item
        s = safe(orig)
        data = fetch(f"https://web.archive.org/web/{ts}id_/{orig}")
        if not data:
            results["failed"].append(["page", orig, ts])
            return
        open(os.path.join(BASE, "pages_html", s + ".html"), "wb").write(data)
        h = data.decode("utf-8", "replace")
        seo = {"url": orig, "wayback_timestamp": ts, "slug": s}
        m = re.search(r"(?is)<title[^>]*>(.*?)</title>", h)
        seo["title"] = m.group(1).strip() if m else None
        seo["meta"] = {}
        for mm in re.finditer(r"(?is)<meta\s+[^>]*>", h):
            tag = mm.group(0)
            nm = re.search(r'(?:name|property)=["\']([^"\']+)', tag)
            ct = re.search(r'content=["\']([^"\']*)', tag)
            if nm and ct:
                seo["meta"][nm.group(1)] = ct.group(1)
        c = re.search(r'(?is)<link[^>]+rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', h)
        seo["canonical"] = c.group(1) if c else None
        seo["jsonld"] = [x.strip() for x in re.findall(
            r"(?is)<script[^>]+ld\+json[^>]*>(.*?)</script>", h)]
        seo["h1"] = [strip_html(x) for x in re.findall(r"(?is)<h1[^>]*>(.*?)</h1>", h)]
        seo["h2"] = [strip_html(x) for x in re.findall(r"(?is)<h2[^>]*>(.*?)</h2>", h)]
        seo["images_referenced"] = sorted(set(re.findall(
            r'(?i)src=["\']([^"\']*wp-content/uploads[^"\']+)', h)))
        json.dump(seo, open(os.path.join(BASE, "seo", s + ".json"), "w"),
                  ensure_ascii=False, indent=1)
        open(os.path.join(BASE, "pages_text", s + ".txt"), "w").write(strip_html(h))
        results["pages"].append([orig, ts, s])

    def do_img(item):
        ts, orig, mime = item
        s = safe(orig)
        data = fetch(f"https://web.archive.org/web/{ts}im_/{orig}")
        if not data or data[:6] == b"<html>":
            results["failed"].append(["image", orig, ts])
            return
        open(os.path.join(BASE, "images", s), "wb").write(data)
        results["images"].append([orig, ts, s, len(data)])

    def do_other(item):
        ts, orig, mime = item
        s = safe(orig)
        data = fetch(f"https://web.archive.org/web/{ts}id_/{orig}")
        if data:
            open(os.path.join(BASE, "other", s), "wb").write(data)
            results["other"].append([orig, ts, s])
        else:
            results["failed"].append(["other", orig, ts])

    pages, imgs, other = [], [], []
    for key, (ts, orig, mime) in last.items():
        if "/wp-content/cache/" in orig or "/wp-includes/" in orig:
            continue
        if mime == "text/html" and not any(
                x in orig for x in ["?p=", "?page_id=", "xmlrpc", "wp-json"]):
            pages.append((ts, orig, mime))
        elif mime.startswith("image/") and "/wp-content/uploads/" in orig:
            imgs.append((ts, orig, mime))
        elif (any(orig.endswith(x) for x in ["robots.txt", "favicon.ico", "wlwmanifest.xml"])
              or "/feed/" in orig or mime == "text/xml"):
            other.append((ts, orig, mime))

    with ThreadPoolExecutor(6) as ex:
        list(ex.map(do_page, pages))
        list(ex.map(do_img, imgs))
        list(ex.map(do_other, other))

    json.dump(results, open(os.path.join(BASE, "manifest.json"), "w"),
              ensure_ascii=False, indent=1)
    print("pages=%d images=%d other=%d failed=%d" % (
        len(results["pages"]), len(results["images"]),
        len(results["other"]), len(results["failed"])))
    for f in results["failed"]:
        print("FAILED", *f)


if __name__ == "__main__":
    main()
