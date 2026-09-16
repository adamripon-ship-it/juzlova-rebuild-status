# 00 · Reference analysis — "Avocado (food and benefits)"

Phase 0 of the juzlova.cz redesign. Source: seven screenshot crops of the
Behance module (see `reference/behance/README.md`). This document extracts the
reference's DNA as a checklist and a component blueprint. Every later idea
must pass the checklist. Nothing from the reference is copied literally:
no avocado, no yellow, no Russian, no fruit-shaped mask.

**Revision 3 (2026-09-16, evening).** The owner rated revision 2 at 3/10 for
match and quality. Re-reading the crops showed the decisive misread: the
reference's botanicals are **solid white silhouettes with thick, smooth
strokes**, not thin outline drawings, and its hero is a typographic statement
with no body copy and no buttons. Section 5 and the blueprint below are
corrected accordingly.

**Revision 2 (2026-09-16, same day).** Version 1 drifted from the reference
in four ways the owner rejected: a cream page surface instead of white, a
brown "cocoa" band and brown-grey text tokens, an egg-shaped photo mask that
read as an avocado, and a form that ignored the reference's layout. It also
described the botanical line-art without drawing it. This revision measures
the reference component by component and maps each component to a juzlova.cz
equivalent so those drifts cannot recur.

Terms: **band** = full-bleed horizontal section; **cut-out** = photo with the
background removed, floating with a soft shadow; **line-art** = white
single-stroke vector drawing; **silhouette** = solid white shape at low weight.

---

## 1. Page anatomy (crop 1, whole page ≈ 530 × 1520 at thumbnail scale)

Nine stacked zones, hard-edged, no dividers, no curves between bands:

| # | Zone | Surface | Heading alignment | Height share |
|---|---|---|---|---|
| 0 | Header bar | white | — | 4 % |
| 1 | Hero | **yellow** | centred, display serif | 13 % |
| 2 | About + six stats | **white** | centred, light sans uppercase | 17 % |
| 3 | Journey (5 numbered steps on a wave) | **yellow** | left, light sans uppercase | 18 % |
| 4 | Recipes (3 masked photos) | **white** | centred | 17 % |
| 5 | Three-column text + vine + silhouette | **yellow** | left | 20 % |
| 6 | Footer: nav, phone, mail, logo, help form | **white** | — | 8 % |
| 7 | "Thank you" sign-off | white | centred | 3 % |

Rule: **surfaces alternate strictly.** Yellow never touches yellow. The two
surfaces are the only backgrounds on the page. There is no third surface, no
tint, no dark band, no brown.

## 2. Grid and measurements (from the 2000 px-wide crops)

| Property | Value |
|---|---|
| Outer gutter | 140 px → **7 %** of the canvas |
| Content width | ≈ 1720 px → 86 % |
| Text column | 360–480 px (≈ 45–55 characters at 22 px) |
| Band vertical padding | 120–160 px top, 100–140 px bottom |
| Heading → content gap | ≈ 120 px |
| Body line height | ≈ 1.5 |
| Three-column row | 3 × 480 px columns, 140 px gaps |
| Stats block | Two stat columns (≈ 300 px) flanking a 300 px image column; outer prose columns 360 px |
| Footer | 2 halves; left column starts at the gutter, right form block ≈ 660 px wide |

Whitespace: at least **55 % of every band is bare surface or line-art**.
Objects never touch each other; nothing touches a band edge except objects
that intentionally **bridge** two bands.

## 3. Colour logic

| Role | Reference | Where |
|---|---|---|
| Surface A | Saturated yellow ≈ #F7C531 | Bands 1, 3, 5 |
| Surface B | **Pure white #FFFFFF** | Bands 0, 2, 4, 6, 7 |
| Ink | Near-black ≈ #1A1A1A | All body copy, numerals, small copy on yellow |
| Light type | White | Section headings on yellow, hero wordmark |
| Accent on white | The same yellow | Bullet dots, nav underline, "more →" link and arrow, footer hairlines, CTA fill |
| Decoration on yellow | White | Vine, leaves, product silhouette, wave path |
| Greys | ≈ #8A8A8A | Payment marks, input placeholders, input borders only |
| Photo colours | Greens, browns, cream | **Inside photographs only.** Never a UI colour. |

There is no gradient, no shadow except under cut-outs, no brown, no beige,
no tinted panel. Three colours carry the whole page: yellow, white, ink.

## 4. Typography hierarchy

Two families only.

| Level | Face | Size on crop | Treatment |
|---|---|---|---|
| Hero wordmark | High-contrast Didone serif, white | ≈ 480 px cap height, 2 lines | One letter replaced by the cut-out |
| Hero tagline | Same serif, white, tracked +25 % | ≈ 40 px | Centred above the wordmark |
| H2 | Geometric sans **Light**, uppercase | ≈ 80 px | Tracking +4 %, line height 1.1, max 3 lines |
| Stat numeral | Didone serif Regular, ink | ≈ 80 px | Unit inside the numeral ("6 mg"); label in sans 20 px below |
| Journey number | Didone serif, ink | ≈ 110 px | Two-word sans label to its right/below |
| Body | Geometric sans Regular | 22–24 px | Narrow measure, yellow bullet dot |
| Nav | Sans Regular | 22 px | Active item: 3 px yellow underline |
| Footer phone | Sans Medium | ≈ 36 px | Email below in 24 px |
| Form heading | Sans Medium, 2 lines | ≈ 32 px | Left of the first input |
| Input placeholder | Sans Regular, grey | ≈ 24 px | Inputs ≈ 72 px tall |
| CTA | Sans Regular, sentence case | 22–26 px | Yellow fill, ink text, 10–12 px radius |

Principle: **sans carries structure, serif carries emotion and numbers.**

## 5. Imagery treatment

1. **Cut-outs with soft offset shadow** (hero fruit, seed, halves, whole
   fruit, seedling). Three sizes: hero, section anchor, stat marker. Cut-outs
   bridge band edges: the hero fruit casts its shadow onto the white band; the
   whole fruit hangs from band 2 into band 3.
2. **Masked lifestyle photos** (band 4): three photos, each cut to the
   product's own silhouette, caption centred beneath in sans 22 px. The mask is
   derived from *the product*, which is the reusable idea; the pear outline is
   not.
3. **White silhouette system on yellow** (bands 3 and 5): one continuous vine
   drawn as a **thick smooth stroke (≈ 8 px at 2000 wide, round caps)**; leaves
   are **solid white fills** with at most one vein cut in; a numbered wave path
   in the same thick stroke; a large **solid white silhouette** of the product
   at the band's bottom centre (band 5), cut by the band edge. No thin outline
   drawing anywhere. Always behind content, never crossing body text,
   opacity 0.9–1.
4. Photos are top-lit and low-clutter; no icons anywhere.

## 6. Component blueprint (the parts to rebuild, exactly)

**Header (band 0).** White bar. Logo left (≈ 70 px tall). Right cluster: three
text links with 40 px gaps, the active one underlined 3 px in yellow, then a
yellow pill CTA (ink text, ≈ 48 px tall, 12 px radius). Nothing else.

**Hero (band 1).** Yellow. Tagline centred in tracked serif. Display serif
wordmark on two lines, white, centred, with the cut-out replacing a letter and
overhanging the band's bottom edge by ≈ 30 % of its height; its shadow falls
on the white band below. **No body copy, no buttons**: the only call to action
is the header button.

**About + stats (band 2).** White. Centred H2. Below: five columns. Column 1 =
bullet paragraph (yellow dot, 360 px). Columns 2 and 4 = three stat numerals
each, stacked, serif 80 px with sans label. Column 3 = three cut-outs stacked
(small, medium, large). Column 5 = bullet paragraph. Bottom right: "more ⟶"
in yellow with a long thin arrow.

**Journey (band 3).** Yellow. Left-aligned white H2 on three lines. A white
wave path (stroke ≈ 4 px) runs edge to edge with five serif numbers placed
alternately above and below the crests, each with a two-word label. Small
white leaves sit on the wave. A large cut-out (seedling + fruit) anchors the
right third and bridges up into band 2.

**Recipes (band 4).** White. Centred H2. Row: bullet paragraph (360 px) + three
masked photos (≈ 340 × 420 px) with captions centred beneath. Bottom right:
"more ⟶".

**Three-column text (band 5).** Yellow. Left white H2 (two lines). Three
bullet paragraphs (white dots, ink text) in 480 px columns. Below, the vine
with leaves runs edge to edge and a large white silhouette of the product sits
bottom centre, touching the band's lower edge.

**Footer (band 6).** White. A thin yellow hairline runs across the top with a
gap for the centred logo. Left half: nav (three links, active underlined),
phone in 36 px, email in 24 px, then three grey payment marks. Right half:
form heading on two lines beside a "Your name" input; a full-width "Your phone
number" input below; then a note ("Leave a call-back request") left and a
yellow "Contact us" button right. Inputs: light grey fill, 1 px grey border,
12 px radius, 72 px tall, 24 px grey placeholder.

**Sign-off (band 7).** Centred light sans uppercase line with the product
outline replacing one letter.

## 7. Motion (inferred from the static composition)

Parallax on floating objects (slower than scroll), stroke-draw on the vine
and wave paths, staggered fade-up on numerals and headings, ≥ 600 ms,
ease-out, nothing bouncy, hard band edges stay hard.

## 8. Emotional tone

**Sunlit · airy · editorial · organic · confident.** A food-magazine spread
turned into one long page. Premium without being cold, playful without being
childish.

---

## 9. The DNA checklist

Every layout, section, component or animation for juzlova.cz must pass all
twelve. Write "fits because ___" for each idea.

| # | Check | Pass condition |
|---|---|---|
| G1 | Grid | Centred single column, 7 % gutters, prose ≤ 480 px, never full width |
| G2 | Rhythm | Bands alternate gold / white strictly; headings centred on white, left-aligned on gold; hard edges |
| W1 | Whitespace | ≥ 55 % of each band is bare surface or line-art |
| C1 | Three colours | Gold `#D4AF37`, white `#FFFFFF`, ink. Nothing else as a surface or text colour. Greys only for placeholders, borders, disabled marks |
| C2 | Accent use | Gold only as band, bullet, underline, arrow, hairline, or the filled CTA. **No brown, no beige, no dark band** |
| T1 | Two families | A high-contrast serif for numerals and emotion, a geometric sans for structure |
| T2 | Numerals | Facts shown as large serif numerals with a small sans label |
| I1 | Product shapes | Photos are masked to a silhouette derived from *that product*; the product stays fully visible and centred inside the shape |
| I2 | Bridging | One object per band pair may overhang the band edge with a soft shadow |
| I3 | Silhouettes | White **solid** botanical silhouettes and thick smooth strokes on gold bands only, behind content, never across body text; no thin outline drawing |
| F1 | Form | Reference footer structure: heading beside the first input, full-width second input, note left + gold button right; tall rounded grey inputs |
| M1 | Motion | Slow parallax, stroke-draw, staggered fade-up; ≥ 600 ms; nothing bouncy |

## 10. Translation map for juzlova.cz

| Reference element | juzlova.cz equivalent | Consequence |
|---|---|---|
| Yellow #F7C531 | **Gold #D4AF37** | White text on gold measures 2.10:1 and fails WCAG AA at every size. Section headings on gold bands are therefore **ink**; white stays for line-art, silhouettes, wave path and rules, which are decorative and exempt. This is the single forced deviation. |
| White surface | White `#FFFFFF` | Not cream. The current site's cream `#FAF6EF` is retired. |
| Avocado cut-outs | The **five product photos**, untouched, masked to product-derived shapes (potato, dumpling, vanilla flower, cocoa pod, vanilla bean) and used as the bridging objects | Photos are not cut-outs, so the shape does the "floating object" work; a soft shadow under the shape gives the lift |
| Floating seed / halves / whole fruit in the stats column | Three masked product photos stacked (small → large) | Same silhouette rhythm, no cut-outs |
| Vine + leaves + fruit silhouette | **Vanilla vine** with cocoa leaves and banana leaves; vanilla flower and cocoa pod as silhouettes; vanilla bean as the wave's leaf ornaments | Drawn as white SVG line-art now; Higgsfield renders only after the design is complete |
| "AVOCA/DO" wordmark with fruit as O | Serif H1 headline in ink on the gold hero, with the potato-shaped knedlíky photo bridging into the white band | The existing brush wordmark stays the logo; no letter-replacement device |
| "6 mg vitamin C" stats | 5 kg · 250 Kč, 15 minut, 2004, 12 km, 21 %, 1 kg | All facts already on the site |
| Numbered wave journey | Pole → mlýn (12 km) → dílna Kochánov → vyzvednutí / rozvoz → talíř | Five steps that exist in the brand story |
| Payment marks | Pick-up places (Kochánov · Humpolec) in grey sans | The workshop sells by phone and pick-up |
| Russian copy | cs / en / de / sk | Unchanged |

## 11. What we deliberately do not take

- The avocado (or any single-fruit) silhouette as a mask or ornament.
- The exact yellow, a cream tint, or any brown.
- The "letter replaced by product" logo device.
- Card-payment logos.
- A mask that hides part of the product: if a product shape would crop the
  bag or the bowl, the photo is scaled inside the shape until the whole product
  is visible, even if that leaves table and cloth in the corners.
