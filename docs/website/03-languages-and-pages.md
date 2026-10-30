# 3. Languages and pages

[← Back to the handbook](README.md)

---

## The four languages

| Language | Address | Pages | Search-engine code | Notes |
|---|---|---|---|---|
| 🇨🇿 Czech | `/` | 39 | `cs-CZ` | **Main language.** All copy is written in Czech first |
| 🇬🇧 English | `/en/` | 28 | `en` | |
| 🇩🇪 German | `/de/` | 28 | `de-DE` and `de-AT` | One German page serves both Germany and Austria |
| 🇸🇰 Slovak | `/sk/` | 28 | `sk-SK` | |

The 11 extra Czech pages are **local landing pages** (Humpolec, Havlíčkův Brod,
Kochánov, Vysočina, wholesale in Prague/Brno…). They exist in Czech only and
have no translations.

Every page has a language switcher. Each translated page tells search engines
where its other-language versions are (hreflang). Visitors with no language
match get Czech (`x-default`).

## What the site contains

| Section | Czech | English | Pages per language |
|---|---|---|---|
| Home | `/` | `/en/` | 1 |
| Products | `/bramborove-knedliky-v-prasku/` … | `/en/potato-dumpling-mix/` … | 5: potato dumpling mix, raw-potato ("chlupaté") dumpling mix, gluten-free vanilla pudding, Dutch-process cocoa, vanilla sugar |
| Price list | `/cenik/` | `/en/prices/` | 1 |
| Recipes | `/recepty/` | `/en/recipes/` | 1 index + 14 recipes |
| About us | `/kdo-jsme/` | `/en/about-us/` | 1 |
| Where to find us | `/kde-nas-najdete/` | `/en/where-to-find-us/` | 1 |
| Contact | `/kontakt/` | `/en/contact/` | 1 |
| FAQ | `/caste-dotazy/` | `/en/faq/` | 1 |
| Wholesale | `/velkoobchod/` | `/en/wholesale/` | 1 (+5 local pages in Czech) |

👉 **The complete list of every page in every language is in the
[site map](generated/site-map.md)**, with a link from each address to that
page's full text.

## Address (URL) rules

- Each page has a fixed internal **page id**. Its public address is looked up
  per language in `SLUGS` in `scripts/build_site.py`.
- Addresses are plain keyword translations: lowercase, hyphens, no brand or
  personal names. Example: the potato dumpling mix is
  `/bramborove-knedliky-v-prasku/`, `/en/potato-dumpling-mix/`,
  `/de/kartoffelknoedel-mischung/`, `/sk/zemiakove-knedle-v-prasku/`.
- **Renaming an address:** change `SLUGS`, add the old address to
  `LEGACY_REDIRECTS`, rebuild. The old address then forwards permanently.
  Never delete an old folder by hand.

## Old addresses

The original WordPress site had different addresses. All of them are handled:

- **167 forward permanently (301)** to the matching new page.
- **Dead WordPress pages** (admin pages, feeds, theme demo posts, `/archive/`)
  answer **410 Gone** so search engines forget them.

Both lists are in the [site map](generated/site-map.md#redirects-301).

## Files for search engines and AI assistants

| File | For |
|---|---|
| `/sitemap.xml` | Search engines: index of the four language sitemaps |
| `/robots.txt` | Search engine crawl rules |
| `/llms.txt`, `/llms-full.txt`, `/llms-{cs,en,de,sk}.txt` | AI assistants (ChatGPT, Claude, Perplexity…): plain-text summary of the business |
| `/ai/` | Machine-readable facts: products, FAQ, entity data |
| `/site.webmanifest` | Phone home-screen icon and name |
