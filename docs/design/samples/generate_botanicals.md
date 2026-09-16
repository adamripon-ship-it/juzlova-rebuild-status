# Botanical generation brief · Recraft V4.1 (vector)

Common parameters: `model=recraft_v4_1`, `model_type=vector`, `resolution=2k`,
`colors=["#000000"]`, `background_color="#FFFFFF"`. One object per image.
Cost preflight: 10 credits per image.

Common prompt tail (verbatim on every prompt):
"Solid black flat vector silhouette on a pure white background, one centred
object filling about 80 percent of the frame, botanically accurate proportions,
smooth clean curves, no gradients, no shadow, no outline stroke, no text."

| id | product / role | aspect | prompt head |
|---|---|---|---|
| potato | Bramborové knedlíky (object + mask) | 4:3 | Two potato tubers side by side with a short potato-plant sprig of three compound leaves rising from behind them; tubers slightly irregular ovals with a few eye dimples as small white dots |
| wheat | Chlupaté knedlíky (flour from the family mill) | 4:3 | A bundle of three wheat ears on curving stems with two long narrow leaves, grains clearly articulated as overlapping scales, fine awns; the ears lean to one side |
| vanilla | Vanilkový puding (object + mask) | 4:3 | A Vanilla planifolia orchid flower seen from the front, three slender pointed sepals and two narrower petals, a tubular frilled lip in the centre, on a short vine section with two thick oval leaves and a coiled tendril; thin white lines mark the petal midlines and leaf midribs |
| cocoa | Kakao holandského typu (object + mask) | 4:3 | A ripe Theobroma cacao pod hanging from a short branch beside two large elliptic cacao leaves with drip tips; the pod is oblong, blunt at the stem end, tapered at the tip, with five deep longitudinal furrows drawn as thin white lines; leaf midribs and pinnate veins as thin white lines |
| sugarcane | Vanilínový cukr (object + mask) | 3:4 | A section of sugarcane stalk with visible nodes, a fan of four long arching sugarcane leaves and a feathery flowering plume at the top; thin white lines mark the leaf midribs |
| leaf-banana | background motif | 16:9 | A single large banana leaf seen flat, oblong with a rounded base and blunt tip, strong midrib and closely spaced parallel oblique ribs drawn as thin white lines, two natural tears along the ribs |
| leaf-cocoa | background motif | 3:2 | A spray of three cacao leaves on one twig, elliptic with drip tips, midribs and pinnate veins as thin white lines |
| vine-vanilla | background motif (wave ornaments) | 16:9 | A horizontal Vanilla planifolia vine with alternating thick oval leaves, two small orchid flowers and one coiled tendril, leaves attached to the vine by short petioles |
| beans | background motif | 3:2 | A fan of four long slender vanilla beans tied at the base with a twist of string, tips gently hooked |
| sugarcane-leaves | background motif | 16:9 | A cluster of long arching sugarcane leaves with midribs as thin white lines, no stalk |

Anchor: `cocoa` first (job 4174e9ca-0cf8-4bb0-b082-560ff7785153). Batch the rest only after the anchor passes its four checks.
