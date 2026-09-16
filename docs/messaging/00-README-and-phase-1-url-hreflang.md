# Jůzlová.cz — URL architecture, hreflang, and full messaging rewrite

Date: 2026-09-15 · Live host audited: https://www.juzlova.cz (local mirror `juzlova-rebuild-status/` matches live byte-for-byte except the Cloudflare beacon)

This folder holds the whole deliverable:

| File | Contents |
|---|---|
| `00-README-and-phase-1-url-hreflang.md` | This file. Scope note, Phase 1 URL architecture + hreflang |
| `01-site-audit-duplication-and-claims.md` | Page-by-page duplication audit, unsubstantiated claims, dev notes leaking to users |
| `02-icp-and-personas.md` | ICP + 2 personas per pillar, with sourced customer language |
| `03-messaging-rules.md` | Non-negotiable messaging rules derived from product-marketing / customer-research / copywriting skills |
| `04-rewrite-cs.md` | Czech master copy, page by page, section by section |
| `05-rewrite-en-de-sk.md` | English, German, Slovak copy for the priority pages |
| `06-needs-verification.md` | Claims left out of the copy until the owners confirm them |

---

## ⚠️ Scope correction you must read first

Your brief says: *"Keep the Swiss-engineered, no-camera, no-microphone, jammer-resilient points — they are the trust differentiators."*

Those points do not exist on juzlova.cz. The live site is a **family food-mix workshop in Kochánov, Vysočina** (potato dumpling mix, hairy-dumpling mix, gluten-free vanilla pudding, Dutch-process cocoa, vanillin sugar). No page, schema entry, `llms.txt` line or source file mentions Switzerland, cameras, microphones or jammers. That sentence looks like residue from a different product's prompt template.

Per your own constraint ("Use only claims that appear on the live site or that I supply"), I have **not** inserted those claims. I mapped the *role* they were meant to play (hard, verifiable trust differentiators) onto what Jůzlová actually has:

| Placeholder in brief | Real Jůzlová trust differentiator (on the live site) |
|---|---|
| "Swiss-engineered" | Flour from the family-run mill in Havlíčkův Brod, 12 km away, KLASA-marked; family workshop since 2004 |
| "No camera / no microphone" (nothing hidden) | No middleman, no e-shop markup, no fake stars: reviews come only from live Google / Firmy.cz profiles; lab certificate per cocoa batch on request |
| "Jammer-resilient" (works when things fail) | You phone the person who mixes the product, daily 8–19, 365 days; dumplings ready in 15–20 min from water only |

If the Swiss / camera / jammer product is a *second* site you meant to include, tell me and I will run the same process on it.

---

# PHASE 1 — URL architecture & hreflang (Technical SEO + GEO)

## 1.1 What the live site does today

Verified from `https://www.juzlova.cz/` `<head>`, the four sitemaps and `robots.txt`:

| Check | Live state | Verdict |
|---|---|---|
| Architecture | Subdirectories `/`, `/en/`, `/de/`, `/sk/` on one host | ✅ correct |
| Canonical | Self-referencing, `https://www.` form, trailing slash | ✅ |
| hreflang set | `cs`, `en`, `de`, `sk`, `x-default → /` on every page, full mesh, sitemap + HTML | ✅ bidirectional, self-ref present |
| Region codes | None (language only) | ⚠️ brief requires language+region |
| Slugs in EN/DE/SK | **Czech slugs reused**: `/en/kdo_jsme/`, `/de/bramborove_knedliky/`, `/sk/vanilkovy_pudink/` | ❌ fails "exact translations of primary keywords" |
| Separators | Underscores in `kdo_jsme`, `bramborove_knedliky`, `vanilkovy_pudink` | ❌ fails hyphen rule (Google treats `_` as a joiner, not a separator) |
| Brand in slug | `domaci-pernik-recept-podle-jirina-juzlova` contains the owner's name; `podle-lucie-kuzelovebebe-rezy-...` contains a staff name and a typo (missing hyphen) | ❌ |
| `<html lang>` | `cs` / `en` / `de` / `sk` | ✅ |
| llms.txt / llms-*.txt | Present per language | ✅ (Google ignores; other AI crawlers read) |
| Duplicate content risk | 44 Czech-only local/wholesale pages mirrored into EN/DE/SK (e.g. `/de/velkoobchod-brno/`) with near-identical thin copy | ⚠️ |

**Net:** the hreflang *mechanics* are already right. The *URL surface* is wrong for the brief and for AI search: a German user asking "Kartoffelknödel Mischung Tschechien" gets a URL that says `bramborove_knedliky`, which no German model or user can read as the topic.

## 1.2 Recommended locale codes

Czech Republic is the core market, so the Czech root stays the x-default. Every alternate URL gets a **region-qualified** tag; German additionally gets `de-AT` on the same URL because the site ships to Austria and Austrian search is a distinct market. English is the only alternate that stays language-only: its audience is "anyone in the EU who doesn't read Czech/German/Slovak", not one country.

| hreflang | Target market | URL prefix |
|---|---|---|
| `cs-CZ` | Czech Republic (core) | `/` |
| `sk-SK` | Slovakia | `/sk/` |
| `de-DE` | Germany | `/de/` |
| `de-AT` | Austria (same page) | `/de/` |
| `en` | EU-wide English fallback | `/en/` |
| `x-default` | Everyone else → Czech home | `/` |

All codes are ISO 639-1 + ISO 3166-1 alpha-2, lowercase-UPPERCASE form.

## 1.3 Recommended URL map (translated slugs, hyphens only, no brand)

Primary keyword per page is the term the persona actually searches (see `02-icp-and-personas.md`). Slugs are exact translations of that keyword, not of the Czech page title.

### Core pages

| Page | cs-CZ (`/`) | en (`/en/`) | de-DE / de-AT (`/de/`) | sk-SK (`/sk/`) |
|---|---|---|---|---|
| Home | `/` | `/en/` | `/de/` | `/sk/` |
| Potato dumpling mix | `/bramborove-knedliky-v-prasku/` | `/en/potato-dumpling-mix/` | `/de/kartoffelknoedel-mischung/` | `/sk/zemiakove-knedle-v-prasku/` |
| Hairy dumpling mix | `/chlupate-knedliky-v-prasku/` | `/en/hairy-potato-dumpling-mix/` | `/de/rohe-kartoffelknoedel-mischung/` | `/sk/chlpate-knedle-v-prasku/` |
| GF vanilla pudding | `/vanilkovy-puding-bez-lepku/` | `/en/gluten-free-vanilla-pudding-powder/` | `/de/glutenfreies-vanillepuddingpulver/` | `/sk/vanilkovy-puding-bez-lepku/` |
| Dutch-process cocoa | `/kakao-holandskeho-typu/` | `/en/dutch-process-cocoa-powder/` | `/de/kakaopulver-hollaendischer-art/` | `/sk/kakao-holandskeho-typu/` |
| Vanillin sugar | `/vanilinovy-cukr/` | `/en/vanilla-sugar/` | `/de/vanillinzucker/` | `/sk/vanilinovy-cukor/` |
| Price list | `/cenik/` | `/en/prices/` | `/de/preisliste/` | `/sk/cennik/` |
| Recipes index | `/recepty/` | `/en/recipes/` | `/de/rezepte/` | `/sk/recepty/` |
| About | `/kdo-jsme/` | `/en/about-us/` | `/de/ueber-uns/` | `/sk/kto-sme/` |
| Wholesale | `/velkoobchod/` | `/en/wholesale/` | `/de/grosshandel/` | `/sk/velkoobchod/` |
| Czechs in the EU / shipping abroad | `/zasilky-do-eu/` | `/en/shipping-to-eu/` | `/de/versand-in-die-eu/` | `/sk/zasielky-do-eu/` |
| Order (CZ-wide) | `/objednavka/` | `/en/order/` | `/de/bestellen/` | `/sk/objednavka/` |
| Contact | `/kontakt/` | `/en/contact/` | `/de/kontakt/` | `/sk/kontakt/` |
| FAQ | `/caste-dotazy/` | `/en/faq/` | `/de/haeufige-fragen/` | `/sk/caste-otazky/` |
| Where to find us | `/kde-nas-najdete/` | `/en/where-to-find-us/` | `/de/anfahrt/` | `/sk/kde-nas-najdete/` |
| Visitors to Vysočina | `/pro-navstevniky/` | `/en/for-visitors/` | `/de/fuer-besucher/` | `/sk/pre-navstevnikov/` |

Notes on the German choices: `ä/ö/ü` are transliterated `ae/oe/ue` (standard for German slugs, avoids percent-encoding). "Chlupaté knedlíky" have no German name; *rohe Kartoffelknödel* ("raw-potato dumplings") is the closest German culinary term and is what Austrians and Bavarians search. In English "hairy dumplings" is a literal calque nobody searches; the slug carries "potato dumpling mix" and the H1 explains the bosáky term.

### Recipe pages (rename in Czech too, remove personal names)

| Current cs slug | New cs | en | de | sk |
|---|---|---|---|---|
| `sisky-s-makem-recept` | keep | `poppy-seed-potato-rolls` | `mohnnudeln-aus-kartoffelteig` | `sulance-s-makom` |
| `hruskovy-kolac-s-vanilkovym-pudinkem-recept` | keep | `pear-cake-with-vanilla-pudding` | `birnenkuchen-mit-vanillepudding` | `hruskovy-kolac-s-vanilkovym-pudingom` |
| `strapacky-se-zelim-a-slaninou-recept` | keep | `strapacky-cabbage-and-bacon` | `strapacky-mit-kraut-und-speck` | `strapacky-s-kapustou-a-slaninou` |
| `podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem` | `bebe-rezy-s-cokoladovym-pudinkem-recept` | `no-bake-biscuit-pudding-slices` | `keksschnitten-mit-schokopudding` | `bebe-rezy-s-cokoladovym-pudingom` |
| `domaci-pernik-recept-podle-jirina-juzlova` | `hrnickovy-pernik-recept` | `cup-measure-gingerbread` | `tassen-lebkuchen` | `hrncekovy-pernik` |
| `slehackova-rolada-recept` | keep | `whipped-cream-roulade` | `sahnerolle` | `slahackova-rolada` |
| `bramborovo-tvarohove-knedliky-s-jahodami` | `tvarohove-knedliky-s-jahodami-recept` | `strawberry-curd-dumplings` | `topfenknoedel-mit-erdbeeren` | `tvarohove-knedle-s-jahodami` |
| `rychle-venecky-ci-vetrnicky-recept` | keep | `quick-choux-rings-and-puffs` | `schnelle-brandteigkraenze` | `rychle-venceky-a-veterniky` |
| `venecky-s-vanilkovym-kremem-recept` | keep | `choux-rings-with-vanilla-cream` | `brandteigkraenze-mit-vanillecreme` | `venceky-s-vanilkovym-kremom` |
| `kremrole-recept` | keep | `cream-horns` | `schaumrollen` | `kremrole` |
| `minivetrnicky-recept` | keep | `mini-cream-puffs` | `mini-windbeutel` | `mini-veterniky` |
| `karamelove-vetrniky-recept` | keep | `caramel-cream-puffs` | `karamell-windbeutel` | `karamelove-veterniky` |
| `irsky-sticky-toffee-pudding-recept` | keep | `sticky-toffee-pudding` | `sticky-toffee-pudding` | `sticky-toffee-pudding` |

### Local landing pages (`vysocina`, `havlickuv-brod`, `humpolec`, `kochanov`, `velkoobchod-*`)

These exist for Czech local search only. Do **not** translate them. Keep them Czech-only, remove them from `sitemap-en/de/sk.xml`, and give them **no hreflang set at all** (a page with no alternates simply has none). Serving `/de/velkoobchod-brno/` to Germans is thin duplicate content and dilutes the German crawl budget. Rename with hyphens: `velkoobchod-vysocina` etc. are already fine.

## 1.4 Migration rules (so canonical = hreflang = sitemap, always)

1. **301 every old URL to its new one**, including the underscore forms and the legacy aliases already in the repo (`kdo-jsme`, `kakaovy_puding`, `vanilkovy_puding`, `recepty-index`, `jirina-juzlova-praha`, `potravinarske-smesi-kontact-praha-ceske-republiky`). One hop only.
2. The `rel=canonical` on each page is its own new URL. The `hreflang` href for that language is the identical string. Sitemap `<loc>` is the identical string. Trailing slash on all three.
3. Old URLs must not appear in any hreflang set or sitemap after cutover.
4. Keep hreflang in **both** HTML and sitemap during the migration month, then drop the HTML version if head bloat matters (it does not at 6 tags).
5. Update `llms.txt`, `llms-*.txt`, `ai/about.md`, schema `url`/`sameAs`, and the language switcher links.
6. Re-submit the four sitemaps in Search Console after deploy.

## 1.5 Exact `<head>` for a core page — Potato dumpling mix

Czech page `https://www.juzlova.cz/bramborove-knedliky-v-prasku/`:

```html
<!-- /bramborove-knedliky-v-prasku/  (lang="cs") -->
<link rel="canonical" href="https://www.juzlova.cz/bramborove-knedliky-v-prasku/">
<link rel="alternate" hreflang="cs-CZ"     href="https://www.juzlova.cz/bramborove-knedliky-v-prasku/">
<link rel="alternate" hreflang="sk-SK"     href="https://www.juzlova.cz/sk/zemiakove-knedle-v-prasku/">
<link rel="alternate" hreflang="de-DE"     href="https://www.juzlova.cz/de/kartoffelknoedel-mischung/">
<link rel="alternate" hreflang="de-AT"     href="https://www.juzlova.cz/de/kartoffelknoedel-mischung/">
<link rel="alternate" hreflang="en"        href="https://www.juzlova.cz/en/potato-dumpling-mix/">
<link rel="alternate" hreflang="x-default" href="https://www.juzlova.cz/bramborove-knedliky-v-prasku/">
```

German page `https://www.juzlova.cz/de/kartoffelknoedel-mischung/` — the return set is the **same six lines**, only the canonical changes:

```html
<!-- /de/kartoffelknoedel-mischung/  (lang="de") -->
<link rel="canonical" href="https://www.juzlova.cz/de/kartoffelknoedel-mischung/">
<link rel="alternate" hreflang="cs-CZ"     href="https://www.juzlova.cz/bramborove-knedliky-v-prasku/">
<link rel="alternate" hreflang="sk-SK"     href="https://www.juzlova.cz/sk/zemiakove-knedle-v-prasku/">
<link rel="alternate" hreflang="de-DE"     href="https://www.juzlova.cz/de/kartoffelknoedel-mischung/">
<link rel="alternate" hreflang="de-AT"     href="https://www.juzlova.cz/de/kartoffelknoedel-mischung/">
<link rel="alternate" hreflang="en"        href="https://www.juzlova.cz/en/potato-dumpling-mix/">
<link rel="alternate" hreflang="x-default" href="https://www.juzlova.cz/bramborove-knedliky-v-prasku/">
```

Same block, canonical swapped, on `/en/potato-dumpling-mix/` and `/sk/zemiakove-knedle-v-prasku/`. That satisfies self-reference, full-mesh return tags, one x-default, and canonical-equals-hreflang on every member.

Sitemap entry (per language sitemap, every `<url>` carries the full set):

```xml
<url>
  <loc>https://www.juzlova.cz/de/kartoffelknoedel-mischung/</loc>
  <xhtml:link rel="alternate" hreflang="cs-CZ"     href="https://www.juzlova.cz/bramborove-knedliky-v-prasku/"/>
  <xhtml:link rel="alternate" hreflang="sk-SK"     href="https://www.juzlova.cz/sk/zemiakove-knedle-v-prasku/"/>
  <xhtml:link rel="alternate" hreflang="de-DE"     href="https://www.juzlova.cz/de/kartoffelknoedel-mischung/"/>
  <xhtml:link rel="alternate" hreflang="de-AT"     href="https://www.juzlova.cz/de/kartoffelknoedel-mischung/"/>
  <xhtml:link rel="alternate" hreflang="en"        href="https://www.juzlova.cz/en/potato-dumpling-mix/"/>
  <xhtml:link rel="alternate" hreflang="x-default" href="https://www.juzlova.cz/bramborove-knedliky-v-prasku/"/>
</url>
```

## 1.6 GEO (AI-search) notes tied to the URL change

- The slug is the first thing an LLM reads when it cites a URL. `/de/kartoffelknoedel-mischung/` is self-describing; `/de/bramborove_knedliky/` is not.
- Keep one H1 per page that repeats the slug's keyword in natural language (done in the rewrite).
- The first paragraph of every product page must answer *what, how much, where* in ≤ 40 words — the passage AI answers quote (kept, but de-duplicated; see audit).
- `llms-de.txt` etc. should list the new URLs; the current ones list Czech slugs.
- Do not add per-language `FAQPage` schema on the home page *and* the FAQ page with identical Q/A (currently the case). One canonical FAQ per language.
