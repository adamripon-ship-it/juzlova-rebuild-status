# 02b · Check-up: responsive, localisation, SEO/GEO visibility, editorial copy

Run 2026-09-17 against specimen rev. 5 (`docs/design/samples/01-specimen.html`)
and, for SEO/GEO, against the live site. Companion to
`02a-seo-technical-audit.md` (written by the technical-SEO agent). Everything
here is a finding with a fix; site code stays untouched until the owner's "go".

## 1. Responsive matrix (headless Chrome, static mode)

| Width | Device class | Result | What changed to make it pass |
|---|---|---|---|
| 390 | phone | pass | Header CTA shortened to one word ("Zavolat" / "Call us" / "Anrufen" / "Zavolať"); nav links hidden; product-shape stack given an explicit width (a grid item with `max-width` + `margin:auto` and %-width children collapses to 0) |
| 768 | tablet portrait | pass | Stats grid drops to 3 columns with prose full width; cut-out sits below the CTAs |
| 1024 | tablet landscape | pass | Same 3-column stats; short CTA (the long one wrapped "Pro kuchyně" onto two lines); cut-out static below the buttons instead of overlapping the headline |
| 1440 | laptop | pass | Reference layout; pod cut-out moved right so the German headline clears it; bean silhouette moved to the corner (it ran over the outline button text) |
| 1920 | monitor | pass | Root size 19 px scales type, spacing and the 74 rem content column together |
| 2560 | TV / large monitor | pass | Root 22 px; content column 1 628 px; bands and art scale with `vw` clamps |
| 3840 | 4K TV | not captured | Root 30 px rule exists; verify on a real 4K panel in Phase 4 |

Motion checks in the live pane: reveals with stagger, count-up numerals on
entry, wave and vines draw in, leaves and silhouettes sway with independent
periods, cut-outs drift, CTA fill sweeps on hover, marquee pauses on hover.
`prefers-reduced-motion` and `?static=1` (headless captures) switch all of it
off and show final values.

## 2. Localisation (cs / en / de / sk)

Source of truth: the real strings from `scripts/content_{cs,en,de,sk}.py` and
`recipes_*.py`, pulled into `samples/i18n.json`; only the specimen-specific
labels (stat captions, journey steps, form) were written new, in all four
languages.

| Finding | Evidence | Fix |
|---|---|---|
| German is the longest language and fits | "Kartoffelknödel auf dem Tisch in 20 Minuten" runs two lines at 1440; marquee item "Rohe Kartoffelknödel-Mischung (chlupaté knedlíky) 5 kg · 260 Kč" fits; journey H2 runs four lines at 14ch | none; keep `text-wrap: balance` and the 16ch H1 measure |
| The real en/de H1s are 122–124 characters | `hero_h1` in `content_en.py` / `content_de.py` | At display size they would run five lines. Split each into a main clause (≤ 45 characters, the benefit) and a proof sub-line, as the specimen does with `.h1-sub`; the H1 element keeps both, so messaging rule 3 (situation + benefit + proof in the H1) still holds. Proposed: en "Czech potato dumplings on the table in 20 minutes" + "from flour milled 12 km from our workshop"; de "Kartoffelknödel auf dem Tisch in 20 Minuten" + "aus Mehl, gemahlen 12 km von unserer Werkstatt"; sk "Zemiakové knedle na stole za 20 minút" + "z múky z mlyna 12 km od našej dielne" |
| Currency label differs by language | en content uses "CZK", cs/de/sk use "Kč" (also flagged in 02a) | One convention: "Kč" everywhere, with "Kč (CZK)" on first mention on the en price list |
| Two cooking times next to each other | H1 says 20 minutes (bramborové), the stat said "15 minut od vody k talíři" (chlupaté) | Stat label now names the product: "minut na chlupaté knedlíky" (and en/de/sk equivalents). Messaging rule 6: one number per product |
| Diacritics | č ř ě ů ľ ĺ ô ä ß render in Fraunces and Geologica at every size captured | none |
| Lowercased tagline | `text-transform: lowercase` turns "Czechia" / "Tschechien" lowercase | acceptable as a typographic device; if the owner prefers, drop the transform for en/de |

## 3. SEO and answer-engine (GEO) visibility of the live site

Two independent checks were run on `https://www.juzlova.cz`.

**GEO audit tool: 86/100 (excellent).** robots.txt names and allows every
major AI crawler; `llms.txt`, `llms-full.txt` and the four language files
exist and validate; JSON-LD types found: Organization, LocalBusiness,
FoodManufacturer, WebSite, WebPage, ItemList, FAQPage. Its suggestions, with
a verdict:

| Suggestion | Verdict |
|---|---|
| Add `sameAs` to Wikipedia / Wikidata | Only when a Wikidata item exists for the workshop; do not create one for SEO |
| Visible "about" link | Exists ("Kdo jsme"); nothing to do |
| Keyword density "knedlã 3.4 %" | Tool artefact: it mis-decoded UTF-8 ("KnedlÃ­ky"); the live page declares `<meta charset="utf-8">` in the first bytes. No action beyond fix 9 in 02a (charset in the HTTP header) |
| RSS/Atom feed linked in `<head>` | Reasonable for the recipes index in Phase 3 |
| `SearchAction` on WebSite | No site search exists; skip |
| Form labels | The redesign's form has `aria-label` and placeholders; Phase 3 adds visible labels |

**Technical-SEO agent report** (`02a-seo-technical-audit.md`, 74/100 on its
rubric). The single critical finding is a deployment gap, not a design bug:
the live site still serves the old underscore slugs and generic hreflang,
while the repository's last commit already has translated slugs, region
hreflang (`cs-CZ`, `sk-SK`, `de-DE`, `de-AT`, `en`, `x-default`) and the
redirect stubs. **Deploying the current build resolves findings 1, 2 and 7.**
The rest becomes Phase 3/4 work:

| Finding | Where it lands |
|---|---|
| Product thumbnails without `width`/`height` (CLS) | Phase 3, product cards in `build_site.py` |
| No security headers | Phase 3, `nginx.conf` (HSTS, nosniff, baseline CSP) |
| Two-hop http→https with a 302 | Phase 3, `nginx.conf` |
| Render-blocking single stylesheet | Phase 3: inline critical CSS, preload the rest, self-hosted fonts preloaded |
| `Content-Type` without charset | Phase 3, `nginx.conf` |
| Product schema: `sku` = slug, no `priceValidUntil` | Phase 3, JSON-LD in `build_site.py` |
| Currency label inconsistency | Copy fix above |

What already works and must not regress in Phase 3: robots allow list, five
valid sitemaps with 38 pages per language, self-referential canonicals, rich
JSON-LD, citable one-question-one-answer FAQ blocks, llms.txt family, no
mixed content, hero image preload, titles 43–54 and descriptions 142–159
characters, no Czech leaking into en/de/sk.

## 4. Editorial copy (website-copy-intelligence pass)

Method: 5-second test on the hero, scanning check on headings, specificity,
marketese scan, EU trust check, CTA formula, readability by eye (short
sentences, one idea per paragraph).

| Check | Result |
|---|---|
| 5-second test, cs hero | Who: "rodinná dílna · kochánov · od roku 2004". What: "Bramborové knedlíky na stole za 20 minut". Why: "z mouky z mlýna 12 km od naší dílny". Next: "Zavolat Jiřině a objednat". Pass in all four languages |
| Headings read alone (layer-cake) | "Pět směsí. Jedno místo výroby.", "Jak se směs dostane na váš stůl", "Co z toho uvaříte", "Víte, odkud je mouka. A komu voláte." each carry their section without the body. Pass |
| Specificity | Every claim carries a number or a place: 20 min, 12 km, 5 kg, 250 Kč, 2004, 21 %, 1 kg, Havlíčkův Brod, KLASA. Pass |
| Marketese | None in the specimen. **The live site still shows the old hero: "Knedlíky jako od babičky. Hotové za 15 minut." and "Poctivé potravinářské směsi … bez kompromisů v kvalitě"**, two phrases the messaging rules ban ("poctivé", "bez kompromisů", "jako od babičky"). The rewritten copy exists in the repository; deploy it |
| EU trust | No pressure tactics, honesty items visible (no e-shop, call the maker, prices ex-works, callback hours). Pass |
| CTA formula | Verb + what you get: "Zavolat Jiřině a objednat", "Podívat se na ceník", "Zavolat mi zpět". Pass. Header and hero share one action, so the page still has a single primary CTA |
| Readability | Sentences ≤ 20 words, paragraphs ≤ 4 sentences throughout the specimen |
| A/B hypothesis for Phase 4 | Control: benefit H1 + proof sub-line. Variant: proof-first H1 "Mouka z mlýna 12 km od dílny. Knedlíky za 20 minut." Prediction: control wins on the phone-call rate because the time benefit is the persona's trigger (docs/messaging/02, persona 1A). Metric: tel: link taps per 100 sessions |

## 5. Buttons and contrast (owner's decision, recorded)

On gold bands the owner specified a white-filled button with gold text and an
outline button with white border and white text. Both pairs measure 2.10:1,
below WCAG 2.0/2.1 AA (4.5 normal, 3.0 large). Implemented as instructed and
marked as the owner's exception in `01-brand-identity.md` §3.2; every other
text on the page stays AA or better. Hover states invert to ink fill with
white text (8.28:1 on gold), so the hovered state is compliant.

## 6. Open items

- Deploy the current build (translated slugs, region hreflang, rewritten copy) before any SEO re-measure.
- 4K verification on a real panel.
- Lighthouse runs belong to Phase 4 (the brief's ≥ 90 / ≥ 95 / 100 targets) once the design is in `assets/site.css` and `build_site.py`.
