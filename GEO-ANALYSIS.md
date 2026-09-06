# GEO-ANALYSIS — Jůzlová (juzlova.cz)

Date: 2026-09-03  
Live audit: `geo audit --url https://www.juzlova.cz` (geo-optimizer CLI)  
Baseline score before this rebuild: **77 / 100** (band: good)

Google’s position (Search Central, 2026): optimizing for AI search is still SEO. `llms.txt` is ignored by Google Search — it will not help or harm Google rankings or AI Overviews. We keep it for ChatGPT, Perplexity, Claude, and other non-Google crawlers. Schema and `llms.txt` do **not** guarantee citations.

---

## 1. GEO Readiness Score: 77/100 (live baseline)

| Category | Score | Max | Notes |
|---|---:|---:|---|
| robots | 15 | 18 | Citation bots allowed; not all named until this rebuild |
| llms | 14 | 18 | Present; missing Optional + companion `.md` until this rebuild |
| schema | 13 | 16 | Org + WebSite + FAQ + Product + Recipe already live |
| meta | 14 | 14 | Title, description, canonical, Open Graph complete |
| content | 11 | 12 | Front-loaded; no external source links |
| signals | 4 | 6 | `lang` + dateModified; no RSS |
| AI discovery | 3 | 6 | Files existed; summary/FAQ shape failed the checker |
| brand entity | 6 | 10 | Strong NAP; no Wikipedia / Wikidata / LinkedIn |
| Negative | −3 | — | Homepage “knedlíky” density flagged |

**Target after this deploy:** mid-80s if discovery JSON, explicit citation bots, and `llms.txt` Optional/companion pass. Off-site mentions (Wikidata, Seznam Firmy, Google Business) are the remaining ceiling — those are not a website file.

---

## 2. Platform breakdown

| Platform | Audit score | How it cites | What we do |
|---|---:|---|---|
| Google AI Overviews | 80 | Pages that already rank + extractable passages | Classic SEO: titles, hreflang, FAQ, Product/Recipe, static HTML |
| Google AI Mode | (same crawl) | Broader pool; freshness + entity | Keep `dateModified` current; one entity name everywhere |
| ChatGPT Search | 80 | GPTBot / OAI-SearchBot + clear pages | Allow those bots; English `llms.txt` as a cheap index |
| Perplexity | 75 | PerplexityBot + citable facts | Numbers, prices, “we do not sell cocoa pudding” |
| Claude | (allowed) | ClaudeBot / Claude-SearchBot | Same as ChatGPT: crawlable static HTML |

Only about 11% of domains are cited by both ChatGPT and Google AI Overviews for the same query. Treat them as separate surfaces.

---

## 3. AI crawler access status

Live check (2026-09-02): GPTBot, ClaudeBot, and PerplexityBot all received HTTP 200 with the same HTML as a browser. No CDN challenge.

| Crawler | Owner | Status |
|---|---|---|
| OAI-SearchBot | OpenAI citations | Allowed (now named in robots.txt) |
| GPTBot | OpenAI | Allowed |
| ChatGPT-User | OpenAI (user-triggered) | Allowed; ignores robots by design |
| ClaudeBot / Claude-SearchBot | Anthropic citations | Allowed (SearchBot named in this rebuild) |
| PerplexityBot | Perplexity | Allowed |
| Googlebot | Google Search + AI Overviews | Allowed |
| Google-Extended | Gemini / Vertex *training* opt-out | Allowed (does not control AI Overviews) |
| Bingbot | Bing / Copilot | Allowed in this rebuild |

We do **not** block citation bots. Training-only blocks would be a later owner decision; they are not required for this plan.

---

## 4. llms.txt status

| File | Role | Google Search |
|---|---|---|
| `/llms.txt` | English index (H1, blockquote, H2 + links) | Ignored |
| `/llms-full.txt` | Full extract: NAP, products, recipes | Ignored |
| `/llms-{cs,en,de,sk}.txt` | Same map in each language | Ignored |
| `/ai/about.md` | Companion entity notes | Ignored |

Present before this work. This rebuild adds: “Facts AIs get wrong”, Optional section, companion `.md`, today’s date, no invented star ratings. Linked from `robots.txt`, every page `<head>`, and the footer.

**Honest limit:** this lowers extraction cost when a crawler already reaches the site. It does not buy ChatGPT citations by itself.

---

## 5. Brand mention analysis

| Surface | Status | Action |
|---|---|---|
| Own site (CS/EN/DE/SK) | Strong, consistent “Jůzlová” | Keep one name |
| Google Business Profile | Exists as Juzlova - Potravinářské směsi, Kochánov 40, 582 53 | Already listed — do not claim or create |
| Seznam Mapy / Firmy | Exists — search Juzlova → firm id 12906730 | https://mapy.cz/?source=firm&id=12906730 |
| Wikidata | Missing | Create item (name, address, 2004, official website) |
| Wikipedia | Missing | Do not write your own article |
| LinkedIn / YouTube / Reddit | Missing | Optional later; strongest off-site lever |
| sameAs in schema | Empty (honest) | Add only after those profiles exist |

Brand mentions off-site correlate more with AI visibility than backlinks. The website cannot fake that.

---

## 6. Passage-level citability

Optimal cited passage length in the research: **134–167 words**, answer in the first 40–60 words.

**Already extractable (keep):**
- FAQ “What is Jůzlová?” / “Co je Jůzlová?” — name, year, address, five products, IČO
- Cocoa page: 20–22% fat, no added sugar, not a pudding
- Vanilla pudding FAQ: chocolate taste = cocoa stirred in; no cocoa-pudding SKU
- Price list: five packs and Kč amounts

**Gaps:**
- Homepage H1 is emotional (“Knedlíky jako od babičky”) — the lead paragraph does the citing work; keep the lead factual
- Average section is ~41 words (audit RAG score 46) — good for snippets, short of the 134–167 “full answer” band
- No external source links (KLASA, Vysočina) — add 2–3 official links later, not supplier brands

Do not invent review stars in schema. On-page ratings may collect real votes; JSON-LD must not claim an AggregateRating we did not earn.

---

## 7. Server-side rendering check

**Pass.** The site is static HTML from `python3 scripts/build_site.py`. Audit: 1,073 words and 30 headings in raw HTML; not JavaScript-dependent. AI crawlers that do not run JS can still read products, prices, recipes, and FAQ.

---

## 8. Top 5 highest-impact changes

1. **One entity everywhere** — Jůzlová / Jůzlová s.r.o. / IČO 45900124 / Kochánov 40. Source: `docs/entity-source-of-truth.yaml`.
2. **Stop the cocoa-pudding hallucination** — say it on pudding + cocoa pages, FAQ, `llms.txt`, and `llms-full.txt`.
3. **Let citation bots in by name** — OAI-SearchBot, ClaudeBot, Claude-SearchBot, PerplexityBot, GPTBot, Google-Extended, Bingbot.
4. **Off-site NAP** — Google Maps and Seznam Mapy already exist as Juzlova. Optional later: Wikidata.
5. **Refresh dates and answer-first FAQ** — recency helps AI Mode; question headings help extraction.

---

## 9. Schema recommendations

| Type | Where | Notes |
|---|---|---|
| Organization + LocalBusiness + FoodEstablishment | All pages, `@id` `https://juzlova.cz/#org` | IČO, founders, ContactPoint, OfferCatalog |
| Person | Contact + org.founder | Jiřina Jůzlová, Jiří Jůzl |
| WebSite | All pages, `@id` `#website` | No SearchAction — there is no site search |
| WebPage + speakable | All pages | h1, lead, FAQ |
| Product + Offer | Five product pages | Shared product `@id`; InStock; no fake reviews |
| ItemList | Home (products), recipes index | |
| Recipe + HowToStep | 13 recipes | Times, yield, ingredients; **no** invented AggregateRating |
| FAQPage | Home, FAQ, products, recipes | Real questions only |
| BreadcrumbList | Inner pages | |

Do not add Review/AggregateRating. Do not name cocoa suppliers.

---

## 10. Content reformatting suggestions

- Keep the first two sentences as the answer (already true on product and FAQ pages).
- Prefer question H2s where people actually ask (“Je vanilkový puding bez lepku?”).
- One 134–167 word block on **About** and **Cocoa** stating who / where / five products / cocoa ≠ pudding.
- Diversify homepage copy slightly so “knedlíky” is not the only repeated noun (audit stuffing flag).
- Add `dateModified` visibility in a human line on About or FAQ when you next edit copy.
- Never claim samples, a live Google Form, or a sixth SKU.

### Keyword clusters (same intent, four languages)

| Cluster | CS | EN | DE | SK |
|---|---|---|---|---|
| Dumpling mixes | knedlíky v prášku, bosáky | potato dumpling mix, hairy dumplings | Knödelmischung, Bosáky | knedle v prášku, bosáky |
| GF pudding | vanilkový puding bez lepku | gluten-free vanilla pudding | glutenfreier Vanillepudding | vanilkový puding bez lepku |
| Dutch cocoa | kakao holandského typu | Dutch-process cocoa | Kakao holländischer Art | kakao holandského typu |
| Vanilla sugar | vanilínový cukr | vanilla sugar | Vanillinzucker | vanilínový cukor |
| Recipes | věnečky, strapačky, šišky | cream puffs, strapačky | Brandteig, Strapačky | venčeky, strapačky |
| Pick-up | odběr Kochánov, Humpolec | pick-up Kochánov, Humpolec | Abholung Kochánov, Humpolec | odber Kochánov, Humpolec |

---

## 90-day actions (owner + site)

**Days 1–30:** This deploy (schema, llms, robots, entity file). Check ChatGPT/Perplexity with “What is Jůzlová?” and “Do they sell cocoa pudding?”.

**Days 31–60:** Google Maps and Seznam Mapy already exist. Optional Wikidata later. Forms already go to juzlj@seznam.cz.

**Days 61–90:** Re-run `geo audit`. Add two official external links (KLASA, Vysočina). Re-query the prompt set in CS/EN/DE/SK. Do not buy Wikipedia or fake reviews.
