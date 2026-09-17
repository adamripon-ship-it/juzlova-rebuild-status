# 01b · Botanical assets (Higgsfield MCP)

Generated 2026-09-16 evening on the owner's Higgsfield account (plan: ultra).
Credits before 1875.37, after 1722.37: **153 credits** for the whole set,
including one discarded black-on-white test and the cacao-flower pair added
from the owner's botanical references. On 2026-09-17 two more silhouettes (sheaf, cane; 20 credits) were added because the thin wheat and sugarcane outlines cannot hold a photograph.

## Two asset families

| Family | Model | Why this model | Output | Count | Cost |
|---|---|---|---|---|---|
| **White silhouettes** (the reference's vine, leaves and product silhouette) | `recraft_v4_1`, `model_type=vector`, `resolution=2k`, `colors=["#FFFFFF","#D4AF37"]`, `background_color="#D4AF37"` | Built for SVG-like illustration; accepts a locked palette and a flat background colour; returns **real SVG**, so the silhouettes ship as vectors and the photo masks are cut from their true outlines | `.svg`, white paths + gold interior lines on a gold background | 11 + 2 tests | 10 credits each |
| **Photoreal cut-outs** (the reference's floating fruit and seedling) | `gpt_image_2_5`, then `remove_background` | Default general model; clean isolated objects on white with the warm daylight of the farmhouse photos; background remover gives a usable alpha in one pass | `.png` with alpha → trimmed `.webp` ≤ 1200 px | 7 | 1 credit each + removal |

Owner rules applied: every asset is on-brand at generation time (white on gold
or a real object); the black-on-white test (job `4174e9ca…`) was discarded and
its file deleted.

## Silhouette prompts (Recraft V4.1)

Common tail on every prompt: *"Pure white flat vector silhouette on a plain
solid gold background, one centred object filling about 80 percent of the
frame, botanically accurate proportions, smooth clean curves, only two colours
white and gold, no gradients, no shadow, no outline stroke, no text."*

| id | product / role | aspect | prompt head | job |
|---|---|---|---|---|
| cocoa | Kakao (object + mask) | 4:3 | Ripe Theobroma cacao pod hanging from a short branch beside two large elliptic cacao leaves with drip tips; pod oblong, blunt stem end, tapered tip, five deep furrows as thin gold lines; leaf midribs and pinnate veins as thin gold lines | 2e968be8 |
| potato | Bramborové knedlíky (object + mask) | 4:3 | Two potato tubers side by side with a potato-plant sprig of three compound leaves rising behind; eye dimples as small gold dots | 5463c883 |
| wheat | Chlupaté knedlíky (flour) | 4:3 | Bundle of three wheat ears on curving stems with two narrow leaves, grains as overlapping scales separated by thin gold lines, fine awns | 835da92b |
| vanilla | Vanilkový puding (object + mask) | 4:3 | Vanilla planifolia flower from the front, three sepals, two petals, tubular frilled lip, on a vine section with two thick oval leaves and a coiled tendril | 5ee9275b |
| sugarcane | Vanilínový cukr (object + mask) | 3:4 | Sugarcane stalk section with nodes, fan of four arching leaves, feathery flowering plume | e965392d |
| leaf-banana | motif | 16:9 | Single large banana leaf, oblong, strong midrib, parallel oblique ribs, two natural tears | f0de97aa |
| leaf-cocoa | motif | 3:2 | Spray of three cacao leaves on one twig, drip tips, pinnate veins | fc33aaa9 |
| vine-vanilla | motif | 16:9 | Horizontal vanilla vine with alternating oval leaves on petioles, two small flowers, one tendril | b605228d |
| beans | motif | 3:2 | Fan of four vanilla beans tied with string, hooked tips, gold seam line | 0d337aea |
| sugarcane-leaves | motif | 16:9 | Cluster of arching sugarcane leaves fanning from one point, no stalk | 4a3e3ec8 |
| leaf-single | vine leaf (attached along the wave and vines) | 3:2 | A single cacao leaf, petiole left, tip right, midrib and six vein pairs as gold lines that stay inside the leaf | 3cbbe4b9 |
| sheaf | Chlupaté knedlíky photo mask (solid form of the wheat) | 4:3 | Tied wheat sheaf: about twelve ears bunched into one dense head, stalks bound with a twisted band, fanning below; reads as one filled shape | a09e2b15 |
| cane | Vanilínový cukr photo mask (solid form of the sugarcane) | 4:3 | Bundle of three cut cane stalk sections standing together, nodes as gold lines, small leaf crown | daadc280 |
| flower-cocoa | motif (cocoa page) | 3:2 | Three small cacao flowers hanging on short stalks from a knobbly horizontal branch, five long narrow sepals, tiny cup petals, five fine staminodes as gold lines, one round bud (from the owner's botanical references, 2026-09-16) | 15527d20 (first try f776b620 rejected: read as lilies on a block) |

Result: the ten original motifs accepted on the first pass; the cacao flower needed one re-roll with a tighter prompt (stalks on a branch instead of "a piece of bark").

## Cut-out prompts (gpt_image_2_5)

Common tail: *"Isolated on a pure white background, soft warm natural daylight
from the upper left, high detail, realistic texture, no shadow on the
background, no other objects, no text."*

| id | aspect | subject | job → cut-out job |
|---|---|---|---|
| cocoa-pod | 1:1 | Ripe cacao pod split open, white pulp and dark beans, three roasted beans beside | 68c1c209 → 70569504 |
| vanilla | 2:3 | Vanilla planifolia flower on a vine section with two leaves and two cured beans | 24871f0d → a6d8e5ff |
| leaf-banana | 3:2 | Single fresh banana leaf, one small tear | 1e013bc0 → 64bcdff3 |
| leaf-cocoa | 3:2 | Spray of three glossy cacao leaves on a twig | 0d79ac57 → f2e2c67c |
| sugarcane | 2:3 | Cut sugarcane stalk with nodes, arching leaves, small plume | 11e5a7aa → 698a69e2 |
| wheat | 2:3 | Bundle of three golden wheat ears with two leaves | 0a5ba1c3 → b9e3d29e |
| flower-cocoa | 3:2 | Three cacao flowers on bark, cream star flowers with maroon staminodes, one bud | 1b795c51 → a2797778 |

Result: all seven accepted on the first pass.

## Processing (`docs/design/samples/process_botanicals.py`)

1. Strip the C2PA metadata block and the full-frame gold background path.
2. Snap `rgb()` fills to exactly `#ffffff` (shape) and `#D4AF37` (lines).
3. Write the cleaned silhouette to `assets/botanicals/<id>.svg` and a
   `<symbol id="sil-<id>">` into `docs/design/samples/botanicals-sprite.svg`.
4. For the photo masks: rasterise the cleaned SVG with headless Chrome at
   1600 px, threshold, apply a morphological closing (seals vein slits that
   reach the margin), flood-fill from the corners, trace with `potrace`, and
   normalise the path to 0–1 as `<clipPath id="m-<id>" clipPathUnits="objectBoundingBox">`.
5. Round symbol coordinates to integers and mask coordinates to three
   decimals (sprite ≈ 330 KB; Phase 3 ships it as one cached external file
   and inlines only the five masks per page).
6. Cut-outs: crop to the alpha bounding box, resize to ≤ 1200 px, save WebP
   quality 86 (65–190 KB each) in `assets/botanicals/cutouts/`.

## Where each asset is used (specimen rev. 4)

| Asset | Use |
|---|---|
| cut-out cocoa-pod | Hero object over the right end of the headline, sticker outline, parallax |
| cut-out vanilla | Journey band, bridging up into the white band, sticker outline |
| cut-out leaf-banana | Three-column band, low right, sticker outline |
| sil-cocoa | Large silhouette bottom centre of the three-column band; marquee separator |
| sil-leaf-banana | Large low-opacity backdrop in hero and journey |
| sil-leaf-cocoa, sil-beans | Hero accents; marquee separators |
| sil-vine-vanilla | Journey band, bottom left |
| sil-sugarcane-leaves | Three-column band, bottom left |
| sil-potato, sil-wheat, sil-vanilla, sil-cocoa, sil-sugarcane | Product legend; marquee separators |
| m-potato, m-cocoa, m-vanilla | Photo masks in the stats stack and the recipes row |
| sil-leaf-single (generated) | Single leaves attached along the wave and the vines by `01-specimen.js`; the earlier parametric leaf is retired |
| sil-flower-cocoa, cut-out flower-cocoa | Cocoa product page (Phase 3): flowers grow straight from the trunk, one caption; in the specimen only in the legend |

## Licence

Higgsfield-generated assets belong to the account holder under Higgsfield's
terms; keep the job ids above as provenance. The photoreal cut-outs are
decorative objects, not product photography, so the "photos stay whole" rule
in `01-brand-identity.md` §5 is not affected.

## Moving photos (2026-09-17, Seedance 2.5 image-to-video)

Each product and home-recipe photo has a five-second moving version generated from the exact still (`mode=omni_reference`, start image = the photo, 720p, no audio, locked camera, only the subject moves: cocoa haze, flour dust, steam, a pudding wobble, trickling sugar, drifting icing sugar). Encoded with ffmpeg to H.264, 720 px wide, CRF 28, 80–140 KB each, in `assets/video/`. Shown inside the product outline on hover (desktop) or when the card is centred (phone shelf) or in view (product panel); see `03-implementation.md`.

| clip | photo | job |
|---|---|---|
| kakao | produkt-kakao | 402d59ed |
| puding | produkt-vanilkovy-puding | 2c6e4cef |
| bramborove | produkt-bramborove-knedliky | de4d82ab |
| chlupate | produkt-chlupate-knedliky | d79b09a1 |
| cukr | vanilkovy-cukr-kilo (gpt_image_2_5 job 777e1579) | 3f2ca9b3 |
| sisky | sisky-s-makem | f2115023 |
| strapacky | strapacky | 2cd5cd18 |
| hruskovy-kolac | hruskovy-kolac | 7848fd2d |
