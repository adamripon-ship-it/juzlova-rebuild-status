---
title: SEO Technical & GEO Readiness Audit — juzlova.cz
date: 2026-09-17
scope: Live site https://www.juzlova.cz (read-only, source inspection, no browser rendering)
score: 74/100
---

# SEO Technical & GEO Readiness Audit

Sampled: home pages (cs/en/de/sk), one product page per language, robots.txt, sitemap.xml + 4 language sitemaps, llms.txt family. Evidence is quoted from live HTTP responses fetched during this audit. Items not directly verified are listed as "Not checked" at the end rather than assumed.

## Critical

**1. The four product URLs specified for this audit all 404 — real pages use an untranslated, different slug**
- URL: `https://www.juzlova.cz/bramborove-knedliky-v-prasku/`, `/en/potato-dumpling-mix/`, `/de/kartoffelknoedel-mischung/`, `/sk/zemiakove-knedle-v-prasku/`
- Evidence: all four return `HTTP_CODE:404` (`content-length: 153`, generic error page). The actual live, canonical, sitemap-listed product page is `/bramborove_knedliky/` — and it is **not translated per language**: EN/DE/SK mirrors live at `/en/bramborove_knedliky/`, `/de/bramborove_knedliky/`, `/sk/bramborove_knedliky/` (same Czech slug, confirmed `200`, self-referencing canonical + hreflang). Confirmed via direct status check: `https://www.juzlova.cz/bramborove_knedliky/ -> 200`.
- Fix: Decide and act on one of two paths: (a) implement translated slugs (e.g. `/en/potato-dumpling-mix/`) with 301s from the current underscore URLs, updating canonical/hreflang/sitemap together, matching the URL/hreflang plan referenced in the messaging deliverable; or (b) if the current shared-slug structure is intentional, stop citing translated slugs anywhere (briefs, ads, social) so no inbound link 404s. Right now anything pointing at the "expected" translated URLs is dead.

## High

**2. hreflang uses generic language codes only — no regional targeting, `de-AT` missing entirely**
- URL: all sampled pages, e.g. `https://www.juzlova.cz/` and `/de/bramborove_knedliky/`; also `sitemap-cs.xml`
- Evidence: every page emits exactly `hreflang="cs"`, `"en"`, `"de"`, `"sk"`, `"x-default"` — e.g. `<link rel="alternate" hreflang="de" href="https://www.juzlova.cz/de/">`. No `cs-CZ`, `sk-SK`, `de-DE`, or `de-AT` variant exists anywhere (HTML or sitemap XML agree with each other, so internally consistent, but neither matches the required set). Generic codes are technically valid per Google's spec and will still serve DE to both Germany and Austria, but they don't let the business ever differentiate AT from DE messaging/shipping/pricing later, and don't match spec.
- Fix: add the full regional set (`cs-CZ`, `sk-SK`, `de-DE`, `de-AT`, `en`, `x-default`) to both the HTML `<head>` and the sitemap XML on every page, with `de-DE` and `de-AT` both pointing at the same `/de/...` URL until/unless AT gets its own page. Defer full hreflang-matrix validation to the `seo-hreflang` sub-skill.

**3. Five homepage product-grid images ship without width/height — CLS risk**
- URL: `https://www.juzlova.cz/` (same template on `/en/`, `/de/`, `/sk/`)
- Evidence: `<img class="thumb" src="img/produkt-bramborove-knedliky.webp" alt="Bramborové knedlíky v prášku" loading="lazy">` — no `width`/`height` — repeated for `produkt-chlupate-knedliky.webp`, `produkt-vanilkovy-puding.webp`, `produkt-kakao.webp`, `vanilkovy-cukr.webp`. By contrast, every other image on the same page (logo, hero `kochanov-letecky.webp`, `workshop.webp`, all 7 recipe thumbs, footer marks) does declare `width`/`height`.
- Fix: add explicit `width`/`height` (or `aspect-ratio` CSS) to these 5 `<img>` tags to reserve layout space before the WebP loads.

**4. No security response headers on the page load checked**
- URL: `https://www.juzlova.cz/` (GET, full header dump)
- Evidence: headers present were only `content-type`, `last-modified`, `etag`, `cache-control`, `accept-ranges`, `server: Google Frontend`, `date`, `x-cloud-trace-context`. No `Strict-Transport-Security`, `Content-Security-Policy`, `X-Content-Type-Options`, `X-Frame-Options`, or `Referrer-Policy`.
- Fix: add at minimum `Strict-Transport-Security` (HSTS), `X-Content-Type-Options: nosniff`, and a baseline CSP at the hosting edge (`Google Frontend` suggests Firebase Hosting/GCS+LB — set via `firebase.json` `headers` or the load balancer's header policy).

## Medium

**5. HTTP→HTTPS redirect is two hops and mixes 302/301**
- URL: `http://juzlova.cz/`, `http://www.juzlova.cz/`
- Evidence: `http://juzlova.cz/` → `302` → `https://juzlova.cz/` → `301` → `https://www.juzlova.cz/` (two hops). `http://www.juzlova.cz/` → `302` → `https://www.juzlova.cz/` (should be `301`, it's permanent).
- Fix: make the HTTP→HTTPS upgrade a single-hop `301` straight to `https://www.juzlova.cz/`, and add HSTS (ties into #4) so browsers skip the HTTP round-trip entirely on repeat visits.

**6. Single render-blocking stylesheet, no preload**
- URL: `https://www.juzlova.cz/` — `<link rel="stylesheet" href="assets/site.css?v=20260907a">`
- Evidence: only one CSS file, loaded synchronously with no `rel="preload"`/media-split; both `<script>` tags (`assets/site.js`, Cloudflare Insights beacon) correctly use `defer`, so JS is not a render-blocking concern.
- Fix: inline critical above-the-fold CSS in `<head>` and load the rest via `rel="preload"` + `onload` swap (or `media="print" onload="this.media='all'"`).

**7. Inconsistent slug style (underscores vs hyphens)**
- URL: `/bramborove_knedliky/`, `/vanilkovy_pudink/` vs `/chlupate-knedliky/`, `/kakao-holandskeho-typu/`, `/vanilkovy-cukr/` (from `sitemap-cs.xml`)
- Evidence: two of five product slugs use `_`, three use `-`. Google treats `_` as a word-joiner and `-` as a word separator, so underscore slugs are effectively single unbroken tokens for keyword matching.
- Fix: standardize on hyphens site-wide with 301s, ideally as part of the same pass as fix #1.

**8. Currency label inconsistent across languages**
- URL: `/en/bramborove_knedliky/` title vs `/de/`, `/sk/` equivalents
- Evidence: EN title reads `"...5 kg / 250 CZK..."`; DE and SK keep the Czech symbol verbatim — DE meta description: `"Knödelmischung 5 kg/250 Kč..."`, SK: `"...250 Kč..."`.
- Fix: pick one convention (most defensible: keep `Kč` everywhere since that's the only currency actually charged at pickup) and apply it consistently, including on the EN pages.

## Low

**9. HTTP `Content-Type` header omits charset**
- URL: `https://www.juzlova.cz/` — header reads `content-type: text/html` (no `; charset=utf-8`)
- Evidence: the in-document `<meta charset="utf-8">` is present and all diacritics (č, ř, ě, š, ů, ö) render correctly in every sampled page, so this is not causing visible breakage today.
- Fix: set `Content-Type: text/html; charset=utf-8` at the server config as defense-in-depth.

**10. Product schema has minor gaps**
- URL: `/bramborove_knedliky/` — `Product` JSON-LD
- Evidence: `sku` is the URL slug string (`bramborove_knedliky`), not a real SKU/GTIN; `offers` has no `priceValidUntil`. Not required for validity, both are nice-to-haves for Merchant Listing eligibility.
- Fix: add a real SKU if one exists and a rolling `priceValidUntil`.

## What's working (evidence, no action needed)

- `robots.txt` is clean and explicit: `Allow: /` plus named allow rules for OAI-SearchBot, ClaudeBot, Claude-SearchBot, PerplexityBot, GPTBot, ChatGPT-User, Google-Extended, Googlebot, Bingbot, Applebot-Extended, Bytespider, Amazonbot, meta-externalagent, FacebookBot, cohere-ai; correctly declares all 5 sitemaps.
- `sitemap_discovery.py --json` confirms `sitemap.xml` (sitemapindex) and all 4 language sitemaps return `200`/`valid: true`; common fallback paths (`sitemap_index.xml`, `sitemap-index.xml`, `wp-sitemap.xml`) correctly 404, so nothing stray.
- Page-count parity across languages: `sitemap-cs.xml` has 44 entries (6 llms.txt discovery + 38 pages), `sitemap-en.xml`/`sitemap-de.xml`/`sitemap-sk.xml` each have exactly 38 `<url>` entries — consistent with full 1:1 page coverage (slug-by-slug diff not run, see Not checked).
- Canonical tags are correct and self-referential on all 8 sampled pages; `robots` meta is `index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1` everywhere sampled — no accidental noindex.
- Apex→www works end-to-end: `https://juzlova.cz/` → `301` → `https://www.juzlova.cz/` (`200`). All 4 home pages return `200`.
- JSON-LD is rich and well-formed: home has `Organization+LocalBusiness+FoodEstablishment` (full NAP, `geo`, `openingHoursSpecification`, `sameAs`), `WebSite`, `WebPage`, `ItemList` (5 products, URLs match sitemap exactly), `FAQPage`; product page adds `Product`+`Offer` (all required fields — `priceCurrency`, `price`, `availability`, `url`, `seller` — present) and `BreadcrumbList`. No required properties missing on any type checked.
- FAQ content is genuinely passage-level citable: each `FAQPage` Q&A is one short question + one direct, self-contained answer, e.g. Q "Kolik porcí je z 5kg balení?" / A "Z pětikilogramového balení připravíte přílohu zhruba pro 60–70 porcí." (69–104 characters per answer) — good shape for AI answer-engine extraction.
- `llms.txt`, `llms-full.txt`, `llms-cs.txt`, `llms-en.txt`, `llms-de.txt`, `llms-sk.txt` all return `200`; `llms.txt` is byte-identical to `llms-cs.txt` (Czech as default), so no drift between the two.
- Mobile: `<meta name="viewport" content="width=device-width,initial-scale=1">` present and correct on all 8 sampled pages.
- No mixed content found (`0` `http://` resource references) on `home-cs.html`/`product-cs.html`.
- One `rel="preload"` hint targets the homepage hero image with a responsive `imagesrcset` — good LCP practice.
- No `@font-face`/Google Fonts reference in any sampled HTML — consistent with the stated system-font strategy (actual rules live in `assets/site.css`, not fetched this pass).
- Titles: 43–54 characters across all 8 sampled pages; meta descriptions: 142–159 characters. No Czech text found leaking into EN/DE/SK titles or descriptions.

## Not checked (flagged rather than guessed, per scope limit on this pass)

- Full site-wide duplicate-title/meta-description scan (only the 8 sampled pages checked; sitemap lists 38 URLs × 4 languages = up to 152 pages not crawled).
- Broken internal link crawl beyond the sampled pages.
- Mixed content on `/en/`, `/de/`, `/sk/` variants (only `home-cs.html`/`product-cs.html` scanned; same template makes this low-risk but unverified).
- Contents of `assets/site.css` and `assets/site.js` (actual font-family rules, full render-blocking/critical-CSS analysis) — not fetched.
- Field or lab Core Web Vitals data (LCP/INP/CLS) — this pass is source inspection only; no PageSpeed Insights/CrUX run.
- JSON-LD parity on `/en/`, `/de/`, `/sk/` product and home pages beyond the hreflang/canonical/title/description tags already sampled.
- IndexNow protocol support (Bing/Yandex/Naver key file or ping endpoint) — not checked this pass.
- `claude-seo run render_page.py --mode auto` SPA detection was not executed; SSR/no-JS-required conclusion above is inferred from curl-fetched HTML already containing full text content, FAQ answers, and JSON-LD with no empty app-root div.
