# 01 · Brand identity — Jůzlová

Phase 1 of the juzlova.cz redesign. Builds on `00-reference-analysis.md` (the
DNA checklist and component blueprint) and on the messaging work in
`docs/messaging/` (rules 03, personas 02). Where this document and
`docs/messaging/03-messaging-rules.md` overlap, the messaging rules win.

Rendered samples: `docs/design/samples/01-specimen.html` (serve the repo root
with `python3 -m http.server`) and the desktop and mobile PNG captures beside
it.

**Revision 5 (2026-09-17).** Buttons follow the owner's specification (white
fill with gold text and white outline with white text on gold bands, recorded
as the owner's AA exception in §3.2c); every CTA has a fill-sweep hover, lift
and focus ring; numerals count up on entry; the vine leaf is a generated
cacao leaf (parametric drawing removed); leaves, silhouettes and cut-outs sway
in the wind with independent periods; a four-language switcher fed by the
real content files; root type scale for phones, laptops, monitors and TVs;
version stamp on the page. See `02b-check-responsive-l10n-seo-copy.md`.

**Revision 4 (2026-09-16, night).** Botanicals and product objects are now
AI-generated on-brand (Recraft V4.1 vector, white on gold) instead of
parametric; photo masks are cut from the real outlines; photoreal cut-outs
with a hand-cut white sticker outline take the reference's floating-object
role; leaves attach to the vines along the stroke; a motion layer (reveals,
parallax, stroke-draw, marquee) is specified; a fourth colour is proposed;
white-on-gold text is formally ruled out. See `01b-botanical-assets.md`.

**Revision 3 (2026-09-16, evening).** Botanicals rebuilt as solid white
silhouettes generated parametrically (`samples/botanicals.py`, output
`samples/botanicals-defs.svg`) instead of hand-typed outlines; hero reduced to
tagline + display headline + bridging photo; numerals set heavier (500); vine
strokes thickened to match the reference; footer form enlarged.

**Revision 2 (2026-09-16).** Removed the brown "cocoa" surface and the
brown-grey ink tokens; page surface is white, not cream; photo masks are now
derived from each product; the botanical line-art is specified motif by motif
and drawn into the specimen; footer and contact form follow the reference's
structure. Typography is unchanged.

---

## 1. Brand archetype

### 1.1 Classical archetype: the Caregiver, with the Everyman's manners

Jůzlová exists so that a family lunch lands: dumplings that hold, pudding a
coeliac child can eat, cocoa that bakes dark. The people who make it answer
the phone themselves. That is a **Caregiver** brand (nurturing, reliable,
generous with practical help) that behaves like an **Everyman** (no e-shop, no
call centre, kilo prices, plain talk).

Ruled out: the Sage (no lecturing about nutrition), the Ruler (no "premium",
no "leading"), the Magician (no transformation promises), the Jester (no puns).

Fits because ___: the reference's tone is "confident, organic, editorial";
Caregiver + Everyman keeps the confidence and the organic feel but roots them
in a real family workshop instead of a lifestyle fantasy.

### 1.2 Aesthetic archetype: a declared blend

| Dimension | Archetype | Contributes | Refused |
|---|---|---|---|
| Layout and structure | **Editorial Restrained** | Centred single column, narrow prose measure, one accent, accent only at display size or as decoration | Its navy ink, its cool teal, its B2B register |
| Colour and typography | **Luxe Considered** (sunlit variant, as in the reference) | Deep-value accent (gold), serif display at light weights, generous vertical rhythm | Cream paper (the reference is white), serif body copy, text-only CTAs |
| Imagery and voice | **Documentary Honest** | Real workshop photography with captions as content, journalistic specificity (dates, distances, names) | Its greyness, its refusal of any accent |

The reference itself is Editorial Restrained structure with a sunlit Luxe
accent. We keep that skeleton and swap lifestyle cut-outs for documentary
photographs, because the farmhouse photos are the asset we may not change.

---

## 2. Brand voice

"We are X, not Y". These sit on top of the fifteen binding rules in
`docs/messaging/03-messaging-rules.md`.

| We are | Not | Test |
|---|---|---|
| **Direct** | Salesy | Could Jiřina say it on the phone without blushing? |
| **Warm** | Cute | Would a 60-year-old head cook nod, not smile politely? |
| **Rural** | Folksy | Names a place, a distance, a person; never dialect for effect |
| **Precise** | Clinical | Numbers with units and context, never a spec sheet without a reason |
| **Unhurried** | Slow | Short sentences; the page never nags or counts down |

### 2.1 Tone by context

| Context | Tone | Sample (cs) |
|---|---|---|
| Hero | Fact with the buyer's situation inside it | "Bramborové knedlíky na stole za 20 minut — z mouky z mlýna 12 km od naší dílny." |
| Product facts | Numeral first, label after | "5 kg · 250 Kč" · "21 % tuku" · "1 kg, ne sáček" |
| Price | Plain, ex-works, one disclaimer | "Ceny platí při vyzvednutí v dílně. Dopravu naceníme předem." |
| Form status | What happened, what to do | "E-mail chybí. Doplňte ho a zkuste to znovu." |
| FAQ | Answer first, context after | "Ano, puding je bez lepku. Základ je kukuřičný škrob…" |
| B2B | Labour, portions, paperwork, delivery certainty | "Pět set porcí se třemi lidmi v kuchyni. Papíry k tomu." |
| Legal / cookies | One sentence, one verb | "Analytiku zapneme jen se souhlasem." |

### 2.2 Per-language notes

| Language | Register | Notes |
|---|---|---|
| cs | Source of truth. "Vy". First person plural is the family. | Jiřina appears by name as the person you call. Keep "vanilínový" when it is vanillin. |
| sk | "Vy". Adapt the argument, not the sentence. | Slovak food words (knedle, halušky, puding, kakao). Strapačky are home turf: say so. |
| de | "Sie". Compound nouns yes, adjective chains no. | "Knödel", "Pudding", "Kakao". Czech place names unchanged. No thousands separators in kilogram figures. |
| en | Plain, British-leaning. | "Dumplings" not "gnocchi". Prices stay in Kč, no conversions. Explain "hairy dumplings" once, then use it. |

### 2.3 Voice samples

1. "Voláte tomu, kdo to míchá."
2. "Puding v kile. Cukr v kile. Knedlíky v pětikilovém pytli."
3. "Mouka z mlýna 12 km od dílny. Mlýn vede naše širší rodina."
4. "Nic neodejde, dokud cenu neodsouhlasíte."
5. "Sunday lunch that lands."
6. "Wir mischen seit 2004. Sie rufen an, wir wiegen ab."
7. "Halušky zo Slovenska, cesto z Vysočiny."

Banned words stay banned: poctivý, kvalitní, prémiový, bez kompromisů, jako
domácí, k nerozeznání, luxusní, gurmánský, tradiční hodnoty.

---

## 3. Colour system

Three colours carry the site, exactly as three carry the reference: **gold**,
**white**, **ink**. Greys exist only for placeholders, borders and pick-up
marks. Photo colours never become UI colours. **There is no brown, no beige,
no cream and no dark band anywhere.**

### 3.1 Tokens

| Token | Hex | RGB | Role |
|---|---|---|---|
| `--gold` | `#D4AF37` | 212 175 55 | **Surface A and accent.** Bands, bullets, underlines, arrows, hairlines, wave path fill, the filled CTA (ink text). Never text. |
| `--gold-hover` | `#C7A22E` | 199 162 46 | CTA hover fill only |
| `--white` | `#FFFFFF` | 255 255 255 | **Surface B.** Page, cards, form block |
| `--ink` | `#1A1A1A` | 26 26 26 | All text, numerals, headings on both surfaces, logo on light |
| `--ink-soft` | `#3D3D3D` | 61 61 61 | Lead paragraphs, labels under numerals |
| `--grey` | `#767676` | 118 118 118 | Placeholders, captions, pick-up marks |
| `--line` | `#E4E4E4` | 228 228 228 | Input borders, table rules |
| `--field` | `#F6F6F6` | 246 246 246 | Input fill |
| `--ok` | `#2E6B3A` | 46 107 58 | Form success, "bez lepku" badge text |
| `--error` | `#B3261E` | 179 38 30 | Form error |
| `--shadow` | `rgba(26,26,26,.18)` | — | The one shadow, under bridging photos |

Retired from the current stylesheet: `--paper #faf6ef`, `--cream #f3ecdf`,
`--card #fffdf8`, `--gold #b08d3c`, `--gold-deep #8a6d2c`, `--rust #9c4a21`,
`--ink #241f1a`, `--ink-soft #4a4238`, the brown footer.

### 3.2 Contrast, WCAG 2.1 (computed)

| Pairing | Ratio | Result | Use |
|---|---|---|---|
| ink on gold | 8.28 | AAA | Headings, numerals, body on gold bands |
| ink on gold-hover | 7.16 | AAA | CTA hover |
| ink-soft on gold | 5.17 | AA | Labels under numerals on gold |
| ink on white | 17.40 | AAA | Everything on white |
| ink-soft on white | 10.86 | AAA | Lead text |
| grey on white | 4.54 | AA | Captions, pick-up marks, placeholders |
| grey on field | 4.20 | AA-large | Placeholder text only (exempt, but close) |
| ok on white | 6.40 | AA | Success text |
| error on white | 6.54 | AA | Error text |
| **white on gold** | **2.10** | **FAIL** | **Never text.** Line-art, silhouettes, wave, rules only |
| **gold on white** | **2.10** | **FAIL** | **Never text.** Bullets, underlines, arrows, hairlines, fills only |

The reference sets white headings on its yellow. On gold that fails at every
size, so **headings on gold bands are ink**; every other white-on-gold element
in the reference (vine, leaves, silhouette, wave path, hairlines) is decorative
and stays white. This is the single deviation from the reference and it is
forced by the WCAG AA requirement in the brief.

### 3.2b Proposed fourth colour (awaiting the owner's decision)

The owner asked for one vibrant companion to gold that passes WCAG. Candidate
set tested against white, gold and ink; the winner is a **petrol teal**:

| Token | Hex | On white | White on it | On gold | Gold on it |
|---|---|---|---|---|---|
| `--teal` (proposed) | `#094853` | 10.18 AAA | 10.18 AAA | 4.84 AA | 4.84 AA |

Why petrol and not green, claret or cobalt: it is the only candidate that
passes AA both as text on white *and* as text on gold while staying visibly
vibrant next to the gold; leaf greens and clarets fall to 3.0–4.3 on gold,
navy passes but is not vibrant. Uses, if approved: focus rings (also on gold
bands), link hover, the "bez lepku" badge, form success. Never a surface larger
than a badge or a small button; never in the botanicals.

### 3.2c White text on gold, checked

White `#FFFFFF` on gold `#D4AF37` = **2.10:1**. WCAG 2.0 and 2.1 require 4.5:1
for normal text and 3.0:1 for large text at level AA; 2.10 fails both, and
there is no exemption for headings. Verdict: text on gold bands is ink
(8.28:1, AAA). White stays for silhouettes, sticker outlines, the wave, vines
and hairlines, which are decorative and out of scope for the contrast rule.

### 3.2d Buttons on gold (owner's decision, 2026-09-17)

The owner specified: on gold bands the primary button is white-filled with
gold text, the secondary is a white outline with white text. Both text/fill
pairs measure 2.10:1, below WCAG 2.0/2.1 AA. They are implemented as
instructed and are the only AA exception on the page. Hover and focus invert
to an ink fill with white text (8.28:1), so the active state is compliant.
On white surfaces the primary stays gold with ink text (8.28:1) and hovers
to ink with white text.

### 3.3 Usage hierarchy

White ≈ 55 % of any page, gold ≈ 45 % as bands (the reference is close to
50/50). Ink is text only. Greys never exceed a form's chrome. Semantic
colours appear only as form status and one badge. No gradients.

---

## 4. Typography system

Two families, both SIL OFL 1.1, both variable, both self-hosted. Neither is
Inter, Space Grotesk or Playfair Display.

### 4.1 Faces

**Display and numerals: Fraunces** (Undercase Type). At optical size 144 with
SOFT 0 it is a crisp high-contrast serif, the reference's Didone numeral role;
its terminals carry a hand-made warmth next to the brush-script wordmark.
Verified with fontTools: no missing glyph in
`ÁáČčĎďÉéĚěÍíŇňÓóŘřŠšŤťÚúŮůÝýŽž ÄäĹĺĽľÔôŔŕ ÖöÜüß „“‚‘»«–—…×€`; features
`case`, `kern`, `liga`, `ss01`.

**Structure, body and UI: Geologica** (Monokrom). Geometric-humanist sans with
an ExtraLight that tracks out cleanly in uppercase (the reference's Montserrat
Light role), a Regular that reads at 17 px for long recipes, `tnum` tabular
figures for the price list, `case`, `locl`, full Latin Extended (836 glyphs).

Rejected after testing: Albert Sans (no capital ẞ), Bodoni Moda (pure Didone
felt cold beside the photos), Jost and Sora (too period / too technical),
Instrument Serif (Latin-1 only).

### 4.2 Roles, weights, scale

Root 17 px. Fluid `clamp()`. Unitless line heights.

| Role | Face | Weight | Size | Line | Tracking | Case |
|---|---|---|---|---|---|---|
| Hero tagline | Fraunces | 400 | 1.1rem | 1 | +0.25em | lower |
| H1 | Fraunces, opsz 144 | 400 (numerals 300) | `clamp(2.4rem, 6vw, 5.4rem)` | 1.02 | −0.01em | Sentence |
| Stat numeral | Fraunces, opsz 144 | 500 | `clamp(3rem, 6vw, 5rem)` | 1 | −0.02em | — |
| Journey number | Fraunces, opsz 144 | 500 | `clamp(3.5rem, 7vw, 6.5rem)` | 1 | −0.02em | — |
| H2 | Geologica | 300 | `clamp(1.8rem, 3.6vw, 3rem)` | 1.1 | +0.04em | UPPER |
| H3 / form heading | Geologica | 500 | 1.35rem | 1.3 | 0 | Sentence |
| Lead | Geologica | 400 | 1.15rem | 1.55 | 0 | — |
| Body | Geologica | 400 | 1rem | 1.6 | 0 | — |
| Caption / label | Geologica | 400 | .95rem | 1.4 | 0 | — |
| Nav | Geologica | 400 | 1rem | 1 | 0 | Sentence |
| Button | Geologica | 500 | 1rem | 1 | 0 | Sentence |
| Footer phone | Geologica | 500 | 1.6rem | 1.2 | 0 | — |
| Table figures | Geologica `tnum` | 500 | inherit | — | — | — |

Measure: body ≤ 26 em, lead ≤ 34 em. `text-wrap: balance` on headings.
`font-synthesis: none`. No italics in the system.

### 4.3 Language support proof

fontTools 4.65 on the Google Fonts source files, 2026-09-16. Test set: Czech
`ÁáČčĎďÉéĚěÍíŇňÓóŘřŠšŤťÚúŮůÝýŽž`, Slovak `ÄäĹĺĽľÔôŔŕ`, German `ÄäÖöÜüß`,
punctuation `„“‚‘»«–—…×·€%½¼`, figures.

| Font | Missing | Features kept |
|---|---|---|
| Fraunces (upright) | none | case, kern, liga, ss01 |
| Geologica | none | calt, case, frac, kern, liga, locl, pnum, tnum, ss01 |

Capital ẞ (U+1E9E) present in both. The specimen shows the same block in
cs / sk / de / en side by side.

### 4.4 Licensing and hosting

- SIL OFL 1.1 for both; licence text ships in `assets/fonts/`.
- Self-hosted WOFF2 built with fontTools instancer + pyftsubset:
  `Fraunces-var.woff2` (opsz + wght; SOFT, WONK pinned to 0) **82 KB**;
  `Geologica-var.woff2` (wght; CRSV, SHRP, slnt pinned to 0) **29 KB**.
  Total ≈ 111 KB, both preloaded, `font-display: swap`, `size-adjust` tuned
  against the fallbacks. No italic file.
- Subset: `U+0000-00FF, U+0100-017F, U+0218-021B, U+1E9E, U+2000-206F,
  U+20AC, U+2122, U+2190-2199, U+27F6, U+FB01-FB02`.

### 4.5 Fallback stacks

```css
--serif: "Fraunces", "Iowan Old Style", "Palatino Linotype", "Book Antiqua", Georgia, serif;
--sans:  "Geologica", "Avenir Next", "Segoe UI", system-ui, -apple-system, sans-serif;
```

---

## 5. Imagery rules

The rustic farmhouse product photographs are fixed. Nothing in them changes.

### 5.1 Product objects and the masks cut from them

Each product is represented by the **plant it comes from**, generated as a
white silhouette with gold interior lines (Recraft V4.1 vector, see
`01b-botanical-assets.md`). The photo mask is the outer outline of that
object, so the photo really sits inside the real shape.

| Product | Object | Mask use | Fits because ___ |
|---|---|---|---|
| Bramborové knedlíky v prášku | Two potato tubers with a potato-plant sprig | Knedlíky photo, bag and plate inside the tubers | The raw material; two tubers give the mask a large body |
| Chlupaté knedlíky v prášku | Three wheat ears with leaves | Silhouette and marquee only (too slender for a photo) | Flour from the family mill 12 km away |
| Vanilkový puding bez lepku | Vanilla planifolia flower with leaves and tendril, one object | Pudding photo zoomed to the bowl inside the flower | The ingredient, not the pudding |
| Kakao holandského typu | Cacao pod with two leaves on a branch | Kakao photo inside pod and leaves | The pod is the recognisable form of cocoa |
| Vanilínový cukr | Sugarcane stalk with leaves and flowering plume | Silhouette and marquee only | Sugar's plant, as the owner specified |

Rule for masks: the product must stay readable inside the object's largest
mass; if the object is slender (wheat, sugarcane) it is shown as a silhouette
or cut-out next to the photo instead of masking it.

### 5.2 Rules

1. **Photos stay whole.** No cut-outs, recolouring, AI edits or background
   removal. If the owner later regenerates product photos, that happens only
   after the whole design is finished and approved, and the new photos must
   keep the warm side-light and wooden table.
2. **Photos live on white.** Gold bands host type, numerals and white line-art.
   The one exception is bridging: a masked photo may overhang the edge between
   a gold band and the white band by up to 30 % of its height, with the one
   shadow under it.
3. **One shadow.** `0 24px 48px -24px rgba(26,26,26,.18)` under bridging or
   floated shapes; nothing under inline images.
4. **Captions are content.** Every product or workshop photo carries a
   centred caption in Geologica .95rem ink.
5. **No icons, no stock, no illustrated people.** Information is carried by
   numerals, photos and line-art.

### 5.3 Botanical system: silhouettes, cut-outs, vines

Three layers, all documented with prompts and job ids in `01b-botanical-assets.md`:

1. **White silhouettes with gold interior lines** (ten motifs): banana leaf,
   cacao leaf spray, vanilla vine, vanilla beans, sugarcane leaves, plus the
   five product objects. Gold bands only, behind content, opacity .4–1.
2. **Photoreal cut-outs with a hand-cut white outline** (six objects: split
   cacao pod with beans, vanilla flower with beans, banana leaf, cacao leaf
   spray, sugarcane, wheat). They take the reference's floating-object role:
   hero (over the right end of the headline), journey (bridging up), the
   three-column band (low right). Outline = SVG filter `#sticker`
   (feMorphology dilate 6 px, white flood) plus the one soft shadow.
3. **Vines and the wave**: 6 px white strokes; single leaves are attached by
   `01-specimen.js` along the actual path (base on the stroke, rotated to the
   tangent, alternating sides), so they never float free.

---

## 6. Logo and wordmark treatment

The existing marks are kept: the brush-script **Jůzlová** wordmark and the
calligraphic **J** mark. Nothing new is drawn.

| Surface | Wordmark | Mark |
|---|---|---|
| white | ink | ink |
| gold | ink | white (decorative use only, e.g. watermark) |
| Favicon / touch icon | — | ink J on white; maskable variant white J on gold |

Rules: minimum wordmark height 28 px; clear space equal to the J ascender
height; never stretched, rotated, outlined, shadowed, placed over a photo, or
combined with a tagline in one lockup. The reference's "letter replaced by
product" device is not used; it would be a new logo. The navy of the current
favicon set retires.

---

## 7. Component specifications (from the reference blueprint)

- **Header:** white bar; wordmark left (30 px); right cluster of three text
  links (gap 2.4rem) with a 3 px gold underline on the active item; gold pill
  CTA "Zavolat Jiřině" (ink text, 10–12 px radius, 48 px tall). On ≤ 900 px the
  links collapse behind the existing menu toggle; the CTA stays.
- **Hero:** gold band; tracked serif tagline centred; H1 in ink at up to
  6rem; **no lead paragraph and no buttons** (the header button is the one
  CTA, as in the reference); the potato-shaped knedlíky photo bridging into
  the white band; vanilla flower, banana leaf and two cocoa leaves behind.
- **Stats block:** centred H2; five columns (bullet prose · 3 numerals · 3
  stacked masked photos · 3 numerals · bullet prose); "Kompletní ceník ⟶" link
  bottom right (ink text, gold underline, long gold arrow).
- **Journey band:** gold; left H2; white wave with five Fraunces numbers and
  two-word labels alternating above and below crests; cocoa leaves and vanilla
  beans on the wave; masked product photo bridging up from the right.
- **Recipes:** centred H2; bullet prose + three masked recipe photos with
  captions; link bottom right.
- **Three-column band:** gold; left H2; three bullet paragraphs (white dots,
  ink text); vine and leaves at the bottom; cocoa pod + vanilla bean
  silhouettes bottom centre.
- **Footer:** white; gold hairline across the top broken by the centred
  wordmark; left: nav (active underlined), phone 1.6rem, email, pick-up marks
  in grey; right: form heading beside the name input, full-width phone input,
  note left + gold button right. Inputs: field fill, 1 px line border, 12 px
  radius, 4.25rem tall, grey placeholder, ink 2 px focus ring.
- **Price marquee:** gold strip at the hero's foot, 1 px white hairlines, ink
  product names (Geologica) and prices (Fraunces 500, tabular), white product
  silhouettes as separators; 46 s linear loop, pauses on hover and focus,
  static wrapped list under reduced motion.
- **Wind:** every silhouette sways from its stem (±1.5°, 8–13 s), vine leaves flutter from the petiole (±4°, 5–8 s), cut-outs drift 9 px; each element gets its own period and phase from the script so nothing moves in lockstep; all off under reduced motion.
- **Numerals:** count up on entry over 1.4 s (ease-out quart) from 0, or from a nearby value for years; static under reduced motion and in captures.
- **Motion:** reveals fade-up 800 ms with 90 ms sibling stagger; parallax on
  silhouettes and cut-outs at 15–50 px per viewport (rAF, pointer: fine only);
  stroke-draw on the wave and vines when they enter the viewport; nav underline
  and arrow slides; all off under `prefers-reduced-motion`; content visible
  without JS.
- **Bullet:** .42em gold dot on white, white dot on gold, hanging 1.1rem.
- **Link with arrow:** ink text, 2 px gold underline, "⟶" in gold with
  .3em gap; hover moves the arrow 4 px right.

---

## 8. Ideas added beyond the reference (with fit lines)

| Idea | Fits because ___ |
|---|---|
| Product-derived masks (potato, dumpling, flower, pod, bean) instead of one fruit outline | I1: the reference masks photos to *its* product; five products need five shapes |
| Fact numerals row (5 kg · 15 · 2004 · 12 km · 21 % · 1 kg) around stacked product shapes | T2, direct structural translation of the stats block |
| "Od pole na talíř" five-step wave | Mirrors the numbered journey with a story the brand already tells (I3, M1) |
| Vanilla vine with cocoa and banana leaves as the one line-art system | I3: same job as the avocado vine, drawn from the brief's plants |
| Pick-up marks (Kochánov · Humpolec) where the reference shows card logos | F1: same footer slot, honest to a phone-and-pick-up business |
| Tabular numerals in the price board | T2: numbers as a set |

Rejected: curved band dividers, gradient gold, a green second accent, any
dark or brown band, animated counters, a new logo device.

---

## 9. Definition of done for this phase

- [x] Archetype named and rationalised (§1)
- [x] Voice attributes, tone table, per-language notes, samples (§2)
- [x] Three-colour system with computed WCAG ratios (§3)
- [x] Two typefaces justified, glyph coverage proven, scale, hosting plan, fallbacks (§4)
- [x] Product-shape mask system and botanical background system (§5)
- [x] Logo adaptation without a new logo (§6)
- [x] Component specs from the reference blueprint (§7)
- [x] Rendered samples: `samples/01-specimen.html` + desktop and mobile PNGs
- [ ] Owner's "go" before any change to `assets/`, `scripts/` or generated HTML
- [ ] Higgsfield generation only after the complete design is approved
