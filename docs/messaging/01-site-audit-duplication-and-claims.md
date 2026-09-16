# 01 — Live-site messaging audit (before any new copy)

Scope: every indexable page on www.juzlova.cz, all four languages (EN/DE/SK are straight translations of CS, so every finding below applies ×4).

## A. Same message repeated on the same page

Rule applied: a fact may appear **once** per page in the body plus once in FAQ *only if* the FAQ is the canonical FAQ page. Everything else below is cut in the rewrite.

| Page | Duplicated message | Times on one page | Where |
|---|---|---|---|
| Every page | Language banner *"Německé stránky jsou hotové. Odpovědi z dílny bývají česky; němčinu si majitelé občas pomáhají překladačem."* | 1 × 45 pages | Header. This is a **developer status note**, not customer copy. Remove. Replace with a plain language switcher. |
| Every page | Phone numbers `+420 728 466 141 / +420 607 629 931` | 3–5 | Hero, body paragraph, FAQ answer, CTA block, footer. Keep: CTA + footer. |
| Every page | Address `Kochánov 40, 582 53` | 3–6 | Same. Keep: footer + one contextual mention. |
| Every product page | *"Uvedená cena je jen za zboží. Sledovaná doprava, balení a pojištění se účtují zvlášť."* | 2 (hero + FAQ) | Keep once, under the price. |
| Every product page | Price + pack size | 4 (title, hero, body paragraph, FAQ) | Keep: price card + meta title. |
| Every product page | *"Starší ceny z roku 2017 neplatí"* | 1–2 | Internal anti-Google-cache note. Cut from body; belongs in the price-list page only, once. |
| Home | Free-delivery thresholds (5000 / 1000 / 3000 Kč) | 2 (Why-cheap block + FAQ) | Keep once, in a "Doprava" line. |
| Home | Full price list | 2 (product cards + FAQ answer) | Keep on cards. |
| Home | FAQ block | Verbatim copy of `/faq/` | Cut from home; link to FAQ. |
| Home, Kdo jsme | *"Hvězdičky bereme z živých profilů… Čísla se obnovují při sestavení webu. Google Maps a Firmy.cz zůstávají zdrojem pravdy."* | 2 pages | Build-process explanation. Users don't care how stars are refreshed. Keep one sentence: "Reviews come from our live Google and Firmy.cz profiles." |
| Chlupaté knedlíky | "Hotové za 15 minut" | 4 | Hero, body ×2, FAQ. |
| Chlupaté knedlíky | Serving suggestions (zelí, uzené, škvarky, mák) | 2 | Body + FAQ. |
| Vanilkový puding | "Kakaový puding jako hotovou směs nevedeme / smícháte s kakaem" | 4 | Body, FAQ ×3. Keep once as a tip, once in FAQ. |
| Vanilínový cukr | "ne lusk vanilky" | 3 | Body, FAQ ×2. |
| Kakao | Every H2 section is repeated as an FAQ answer (origin, fat %, no sugar, allergens, heavy metals) | 2 each | Keep sections; FAQ keeps only questions *not* answered in sections. |
| Velkoobchod | *"Značky zákazníků nejmenujeme"* | 3 | Body, card, FAQ. Keep once. |
| Velkoobchod | Brno free from 5000 Kč | 3 | Card, body, FAQ. |
| Velkoobchod | List of customer types | 3 (subhead, "Pro kuchyně" card, "Komu dodáváme" list) | Keep the list. |
| Do EU / Objednávka / Návštěvníkům | "Cena platí při vyzvednutí; doprava, krabice, pojištění, bublinková fólie zvlášť" | 3–4 | Keep once. |
| Do EU | Country list DE/AT/SK/PL | 2 | Body + FAQ. |
| Ceník | Full price table | 3 (intro paragraph, cards, FAQ) | Keep cards. The 60-word intro paragraph re-listing every price is written for a crawler, not a person. |
| Kontakt / Objednávka / Návštěvníkům / Do EU | "Objednávka podle místa" link list (8 links) | Same block on 4 pages | Fine as nav; but it is styled as content. Move to a sidebar/footer nav. |

**Cross-page duplication** (not in brief but blocks GEO): `/faq/` ≡ home FAQ ≡ `/kdo_jsme/` FAQ ≡ product FAQs. Search engines and LLMs see five pages answering "kde sídlíte a jak objednat" identically and pick one at random. The rewrite gives each page *its own* three questions.

## B. Text written for machines, leaking to humans

Cut from the reader-facing copy (keep the facts in schema / llms.txt):

- *"Odpovědi, které lidé i vyhledávače hledají nejdřív"* (home FAQ intro)
- *"Krátké, přímé odpovědi — pro lidi, Google, Seznam.cz i jazykové modely."* (FAQ H1 subhead)
- *"Fotografie doplníme. Teď jsou na místě neutrální zástupné portréty."* (Kdo jsme) — dev note
- *"Čísla se obnovují při sestavení webu."* (reviews block)
- *"Do e-mailu majitelů jde české označení tématu."* (wholesale form)
- *"PSČ je 582 53. Nikoli 582 91."* as an FAQ on three pages — keep only in Contact/Where-to-find-us.
- Meta descriptions that are price lists: *"Knedlíky v prášku 5 kg/250 Kč, chlupaté 260 Kč, puding 60 Kč, kakao 270 Kč."* Prices in the SERP are fine; a bare list with no benefit is not.

## C. Claims on the live site that read as unsubstantiated

Marked **Keep** (verifiable from the site's own facts), **Soften** (true but over-stated), **Cut** (no evidence, or attacks competitors without proof), **Verify** (probably true, needs owner confirmation — listed again in `06-needs-verification.md`).

| Claim (live copy) | Page(s) | Verdict | Why |
|---|---|---|---|
| "Knedlíky jako od babičky" | Home H1 | Soften | Emotional, fine as a metaphor; not a taste test. |
| "chutí k nerozeznání od domácích" / "nerozeznáte od knedlíků připravovaných celé odpoledne" | Home, Chlupaté | **Cut** | Blind-test claim with no test. Forum users explicitly say mixes *are* distinguishable ("z prášku" is a pejorative). Replace with what is provable: ingredients, time, no additives list. |
| "Hotové za 15 minut" (chlupaté) vs "na stole do 20 minut" (bramborové) | Home, products | Keep, but **one number per product** | Currently 15 vs 20 are used interchangeably on the home page. |
| "bez kompromisů v kvalitě" | Hero subhead ×4 | Cut | Empty superlative. |
| "Poctivé potravinářské směsi" | Hero | Soften | "Poctivé" is a Czech food cliché (every brand says it). Replace with the specific: flour source, water-only prep. |
| "Přímý prodej je zhruba o 40 % levnější než přes překupníky" | Home, Ceník | **Verify** | No basis shown. If the owners can show a reseller shelf price, keep as "at [reseller] the same 5 kg costs X Kč". Otherwise cut. |
| "V běžných obchodech bývají srovnatelné výrobky často asi čtyřikrát dražší … necháte si zhruba 750 Kč / 780 / 180 / 810 Kč" | Ceník comparison block | **Cut** | Own disclaimer admits "obecný průměrný odhad, ne o cenu konkrétního řetězce". A 4× multiplier with a made-up savings figure is exactly what a sceptical Czech buyer distrusts. Replace with unit price per kg / per portion, which is arithmetic, not a claim. |
| "Náš nejvyhledávanější výrobek" | Bramborové | Keep | Internal sales fact; phrase as "our best seller". |
| "oblíbené v jídelnách i restauracích" / "Už zásobujeme řadu restaurací, pekáren, kaváren a škol" | Chlupaté, Velkoobchod | Soften | True per owner, unnamed. Phrase as "we supply canteens and restaurants; we don't publish their names". Count would help — **Verify**. |
| "mouka oceněná značkou KLASA z mlýna … který vlastní a vede naše širší rodina" | Everywhere | **Verify** | KLASA is awarded to a specific product. Confirm the exact flour product holds a current KLASA certificate and the mill name. This is the strongest trust claim on the site; it must be airtight. |
| "Kakao třídy 21 % tuku", "20–22 % kakaového másla", pH, fineness, shell max, heavy-metal limits | Kakao | Keep + **Verify** spec sheet | Site says lab certificate per batch is available. Ask for the supplier spec sheet and keep the numbers exactly as on it. |
| "hubených supermarketových kakaí (často 10–12 %)" | Kakao | Keep (external support) | Vitalia.cz (7 Dec 2020) cites 10 % for cheap baking cocoa and the 20 % legal threshold. Cite it. |
| "Některé značky melou kakaové lusky, slupky a dužinu a přimíchávají je … aby přidaly na váze" | Kakao FAQ | **Cut** | Unnamed competitor accusation. Say what *yours* is made of instead. |
| "Kakao z Jižní Ameriky jich [těžkých kovů] mívá víc… naše ze středozápadní Afriky" | Kakao FAQ | Soften + Verify | Origin claim needs the supplier's certificate of origin. Keep "tested within EU 2023/915 limits, certificate per batch on request". |
| Flavour profile scores "Intenzita 92, Krémovost 88, Pražení 78, Barva 94, Jemnost 86" | Kakao | **Cut** | Invented numbers with no method. |
| Nutrition "hořčík 490 mg, draslík 4 400 mg, železo 31 mg na 100 g" | Kakao | Verify | Must match the label. |
| "Bereme prémiovou jakost" | Kakao | Cut | Undefined. |
| "Přirozená chuť bez chemických odstínů" | Puding | Soften | Every pudding powder is a chemical. Say: corn starch, vanilla flavour, no gluten. |
| "Až 7 nových receptů týdně" | Newsletter ×many | **Verify** | 13 recipes exist on the site after 20 years. Promise what you will keep: "new recipes when we have them, seasonal tips before Christmas and Easter". |
| "Rod Jůzlových kořeny asi 400 let" / "stovky let" | Kdo jsme | Verify | Two numbers on one page. Pick one or cut. |
| "Z pětikilogramového balení … 60–70 porcí" | Bramborové | Keep | Arithmetic from pack instructions; confirm portion size on pack. |
| "Recenze na Google a Seznamu" block | Home, Kdo jsme | Keep | Correctly refuses fake stars. Firmy.cz shows 3 reviews (12 Apr 2025, 3 Jun 2022, 18 Jul 2017), no visible star average; Google profile is not yet claimed per the audit report. Do not show a number until the profiles have ≥ 5 reviews. |
| "Rozvoz po Vysočině zdarma od 5000 Kč" etc. | Many | Keep | Policy, owner-controlled. |
| "Ochutnávku / vzorky nenabízíme" | Kontakt, Návštěvníkům | Keep | Honest; keep once. |

## D. Structural findings that affect messaging

1. **No single primary CTA.** Home offers "Naše produkty", "Zavolejte nebo napište", "Kompletní ceník", "Velkoobchodní nabídka", "Jak posíláme do EU", "Přihlásit se", "Chcete objednat?". Seven exits. The rewrite gives every page one primary action (call/write with what you want) and at most one secondary.
2. **The buyer's first question is unanswered above the fold**: "Can I actually get this where I live?" 90 % of orders are local; the hero should say Vysočina pickup / CZ delivery / EU parcel in one line.
3. **Home page hides the strongest proof** (family mill 12 km away, since 2004, you phone the maker) below a product grid.
4. **Product pages open with a price disclaimer** before saying what the product is for.
5. **Wholesale and household copy blur**: the home page speaks to families, then a 5 kg pack (a canteen size) is the only pack size for dumplings. The rewrite states plainly that 5 kg is a family stock-up size and what it yields.
6. **EN/DE/SK are word-for-word CS**, including Czech-only references (Bernard brewery pickup, Seznam Firmy.cz, "Češi i Moravané"). DE/SK need cultural adaptation, not translation (see `05-rewrite-en-de-sk.md`).
