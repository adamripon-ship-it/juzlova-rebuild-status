# 4. Editorial copy

[← Back to the handbook](README.md)

---

## Read every page

The full text of every page, in every language, is exported to readable files:

| | Language | Pages |
|---|---|---|
| 🇨🇿 | [Czech — all page copy](generated/copy/cs/README.md) | 39 |
| 🇬🇧 | [English — all page copy](generated/copy/en/README.md) | 28 |
| 🇩🇪 | [German — all page copy](generated/copy/de/README.md) | 28 |
| 🇸🇰 | [Slovak — all page copy](generated/copy/sk/README.md) | 28 |

Each file shows the page's title, its search-result description, and all
visible text in reading order: headings, paragraphs, lists, buttons.

> These files are **for reading**. To change the wording, edit the source
> files listed below. The export updates itself on the next rebuild.

## Where the words come from

| To change | Edit this file |
|---|---|
| Page text, product descriptions, buttons, menus | `scripts/content_cs.py` (then `_en`, `_de`, `_sk`) |
| Recipes | `scripts/recipes_cs.py` (then `_en`, `_de`, `_sk`) |
| Team / "about us" details | `scripts/team_data.py` |
| Reviews summary | `scripts/reviews_data.py`, `data/reviews.json` |
| Search titles and descriptions | `scripts/seo_data.py` |

**Czech is the source of truth.** English, German and Slovak are adaptations
of the Czech argument, not word-for-word translations. A change in one
language usually needs the same change in all four.

## House rules for writing

These are the owner's rules. Every page follows them.

### Voice

- Direct, warm, rural, unhurried. Short sentences.
- Formal "you": *Vy* in Czech and Slovak, *Sie* in German.
- "We" is the family. Jiřina is named as the person you will speak to.

### Structure

- **One main heading (H1) per page.**
- **One main action per page:** call Jiřina (or write) with what you want and
  where you are.
- **Each fact appears once per page.** Phone and address go in the call-to-action
  and the footer only. Prices go only in the price card.
- **Each page owns its own FAQ.** No question appears on two pages. The home
  page has no FAQ.

### Proof, not adjectives

- ✅ Allowed proof: the family mill 12 km away, "since 2004", water-only
  preparation, cooking time, the ingredient list, cocoa specification numbers,
  real reviews from live profiles.
- ❌ Banned words: *poctivý, kvalitní, prémiový, bez kompromisů, jako domácí,
  k nerozeznání* (honest, quality, premium, no compromise, like homemade,
  indistinguishable).
- ❌ No taste claims ("nobody will notice it's from a mix").
- ❌ No supermarket comparisons ("4× cheaper") and no invented scores.
- ❌ Never mention Google, AI, or how the website is built in visible copy.

### 🚫 Strict owner ban

- **Never name ingredient suppliers** (cocoa or otherwise).
- **Never write copy that says we won't name them** (no "Do you name the
  cocoa supplier?" questions). Stay silent. Describe the product type and
  specifications only.

## Prices on the site (October 2026)

| Product | Price at workshop pick-up |
|---|---|
| Potato dumpling mix | 5 kg / 250 Kč |
| Raw-potato ("chlupaté") dumpling mix | 5 kg / 260 Kč |
| Gluten-free vanilla pudding powder | 1 kg / 60 Kč · 400 g / 30 Kč |
| Dutch-process cocoa | 500 g / 270 Kč |
| Vanilla sugar | 1 kg / 60 Kč |

## Background reading

The research behind the copy lives in [`docs/messaging/`](../messaging/):
customer personas, the full rule set, the page-by-page Czech rewrite, the
translation notes, and claims that still need the owner to confirm
([`06-needs-verification.md`](../messaging/06-needs-verification.md)).
