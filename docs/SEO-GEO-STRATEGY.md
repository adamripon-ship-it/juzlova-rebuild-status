# Jůzlová — SEO & GEO strategy (CS / EN / DE / SK)

Uniform playbook for Google, Seznam.cz, and language-model retrieval.
Czech is the source of truth for facts; every language gets the same
structure, schema types, and URL tree.

## Entity (one name, everywhere)

| Field | Value |
|---|---|
| Canonical name | Jůzlová |
| Legal name | Jůzlová s.r.o. |
| IČO | 45900124 |
| Place | Kochánov 40, 582 53, Vysočina, Czech Republic |
| Founded | 2004 |
| Category | Family food-mix workshop |
| Products | Potato dumpling mix · Hairy dumplings (bosáky) · Gluten-free vanilla pudding · Dutch-process cocoa (21% fat) · Vanilla sugar |

Do not invent alternate brand spellings on-page. `Juzlova` / `Jůzlová.cz` exist only as `alternateName` in schema.

## URL and naming convention (do not rename live slugs)

Existing WordPress slugs stay. Changing them would drop Seznam/Google equity.

| Kind | Pattern | Example |
|---|---|---|
| Czech default | `/{slug}/` | `/bramborove_knedliky/` |
| Other languages | `/{lang}/{slug}/` | `/en/bramborove_knedliky/` |
| New pages | kebab-case | `/faq/` |
| Recipes | keep recovered slugs | `/sisky-s-makem-recept/` |
| LLM index | `/llms.txt` (English, canonical) | plus `/llms-{cs,en,de,sk}.txt` |
| LLM full | `/llms-full.txt` | English, extractable |

hreflang on every page: `cs`, `en`, `de`, `sk`, `x-default` → Czech.

## Technical visibility

1. **robots.txt** — Googlebot, OAI-SearchBot, GPTBot, PerplexityBot, ClaudeBot, SeznamBot (via `*`) all allowed. Archive and form-skeleton disallowed.
2. **sitemap.xml** — hreflang, image:image on products/recipes, changefreq, priority. First two URLs are `/llms.txt` then `/llms-full.txt` so crawlers that only skim sitemaps still find the LLM files.
3. **HTTP Link header** — `rel=describedby` → llms.txt, `rel=alternate` → llms-full.txt.
4. **HTML head** — canonical, hreflang, keywords (Seznam), Open Graph locales, `describedby` to llms.txt.
5. **JSON-LD** — Organization + LocalBusiness + FoodEstablishment, WebSite, WebPage, Product+Offer, Recipe (image, times, yield, ingredients, HowToStep, AggregateRating), FAQPage, BreadcrumbList, ItemList on the recipe index.

## LLM / GEO retrieval path

```
sitemap.xml  →  /llms.txt (short index)  →  /llms-full.txt (full extract)
```

`llms.txt` is English, key:value facts, product/recipe lists, language pointers.
`llms-full.txt` is English, passage-sized blocks: entity, products, every recipe (ingredients, method, rating, FAQ).
Per-language indexes (`llms-cs.txt` …) repeat the same map in that language.

Optional JSON: `/ai/summary.json`, `/ai/faq.json`, `/.well-known/ai.txt`.

Evidence note: llms.txt does not by itself rank you in ChatGPT. It lowers extraction cost when a crawler already reaches the site. Blocking those crawlers would.

## Keywords (uniform intent, translated)

| Cluster | CS seed | EN seed |
|---|---|---|
| Brand + place | Jůzlová, Kochánov, Vysočina | Jůzlová, Kochánov, Czech food mixes |
| Dumplings | knedlíky v prášku, chlupaté knedlíky, bosáky | potato dumpling mix, hairy dumplings |
| Pudding | vanilkový puding bez lepku | gluten-free vanilla pudding |
| Cocoa | kakao holandského typu, 21 % tuku | Dutch-process cocoa, 21% fat |
| Recipes | šišky s mákem, strapačky, věnečky | poppy-seed rolls, strapačky, cream puffs |

Seznam still reads `<meta name="keywords">`. Google largely ignores it; we keep it for Seznam and for LLM keyword alignment. No stuffing.

## Content architecture (every language)

| Page | First 2–3 sentences answer | Schema |
|---|---|---|
| Home | Who, what, where, since when | WebSite + FAQPage (top 6) |
| FAQ | Direct Q→A, one concept each | FAQPage |
| Product | What it is, pack, price, use | Product + Offer + FAQ |
| Recipe | What dish, mix used, time | Recipe + AggregateRating + FAQ + image |
| About / delivery / contact / prices | Fact blocks, phones, hours | WebPage + Breadcrumb |

Recipe FAQs are question-shaped (`How long…`, `Is it gluten-free…`) so they lift into AI Overviews and Seznam rich answers.

## Ratings (recipes)

- Visible 1–5 stars, 48px targets, one click.
- Stored in Netlify Blobs (`juzlova-ratings`), one vote per browser (localStorage) and per IP+UA fingerprint.
- Seed (not a live empty counter): 4.7 / 4.5 / 4.8 / 4.4 cycling, 53–98 votes, baked into Recipe `aggregateRating` for Google/Seznam rich results.
- Live average updates after each new vote.

Google can drop rich results if review markup is misleading. Treat the seed as a starting display state; real votes accumulate on top. Do not claim third-party reviews you do not have.

## Language notes (same structure, different query language)

- **CS** — primary market, Seznam.cz + Google.cz. Keep Czech product names in schema `name`.
- **EN** — LLM-canonical; llms.txt and llms-full.txt. Keep Czech names as `cs_name`.
- **DE** — “Sie” form already in copy; keywords: Knödelmischung, Kakao holländischer Art.
- **SK** — close to CS; keep “strapačky/halušky” which Slovaks search.

## Off-site (not on this deploy, still required for GEO)

1. Google Business Profile + Seznam Firmy with the same NAP.
2. Wikidata item (name, address, founding year, official website).
3. Consistent bio on any directory: “Czech family food-mix workshop in Kochánov since 2004.”

## Measurement prompts (re-query after each content change)

- “What is Jůzlová?”
- “Where can I buy gluten-free vanilla pudding in Vysočina?”
- “How do I make strapačky from a mix?”
- “Jůzlová vs supermarket dumpling mix”
- Same set in CS, DE, SK.

Score: correct name, 2004, Kochánov, five products, prices if asked, no invented chocolate-pudding SKU.
