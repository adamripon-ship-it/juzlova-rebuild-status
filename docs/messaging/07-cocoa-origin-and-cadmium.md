# 07 — Cocoa origin and cadmium: FAQ and answer-engine copy

Written 2026-09-16 from the owner's brief (origin countries, low-cadmium soils)
and two sources. Ready to drop into `scripts/cocoa_faq.py` and the cocoa
product page body in Phase 3. Nothing here is live yet.

## Sources and what they actually say

| Source | Fact used |
|---|---|
| Owner (chat, 2026-09-16) | The cocoa is Theobroma cacao, beans mainly from **Ivory Coast, Ghana, Cameroon and Nigeria**; soils there are low in cadmium. |
| Primoris lab, "Cocoa and its region" (primoris-lab.com/en-BE/news/cocoa-and-its-region) | Cadmium is "a particular concern in Latin America, especially Peru and Ecuador", because of "naturally high cadmium levels found in volcanic soils"; it is taken up by the roots and accumulates in the nib. In West Africa the heavy-metal concern is **lead**, which "tends to remain on the husk", removed during processing. Origin directly affects compliance. |
| Regulation (EU) 2023/915, Annex I, 3.2.15 | Maximum cadmium in **cocoa powder sold to the final consumer**: **0.60 mg/kg**. Chocolate ≥ 50 % cocoa solids: 0.80; chocolate < 50 % and milk chocolate ≥ 30 %: 0.30; milk chocolate < 30 %: 0.10. |
| Existing site copy (`content_cs.py`, cocoa page) | "Boby ze středozápadní Afriky, fermentované v banánových listech a sušené na slunci." Certificate of analysis per batch available on request (wholesale FAQ). |

Rules kept: no supplier or cooperative names; no invented measured values (the
measured cadmium figure lives in the certificate of analysis and is quoted on
request); each fact once per page; the cocoa page owns these FAQs, the wholesale
page keeps the certificate FAQ.

Needs verification before publishing (add to `06-needs-verification.md`):
the exact country list per current batch, and whether the owner wants the
measured cadmium value printed (if yes, take it from the latest certificate).

---

## A. Answer capsule for the cocoa page (replaces the "Odkud je" paragraph)

**cs**
> **Odkud je.** Boby jsou z kakaovníku *Theobroma cacao* ze západní Afriky — hlavně z Pobřeží slonoviny, Ghany, Kamerunu a Nigérie. Fermentují se v banánových listech a suší na slunci. Půdy v této oblasti mají přirozeně nízký obsah kadmia, proto ho má nízký i naše kakao; hodnotu k šarži najdete v laboratorním certifikátu, který pošleme na vyžádání.

**en**
> **Where it comes from.** The beans are *Theobroma cacao* from West Africa, mainly Ivory Coast, Ghana, Cameroon and Nigeria. They are fermented in banana leaves and dried in the sun. Soils in this region are naturally low in cadmium, so our cocoa is too; the value for your batch is in the certificate of analysis, sent on request.

**de**
> **Woher er kommt.** Die Bohnen stammen vom Kakaobaum *Theobroma cacao* aus Westafrika, vor allem aus der Elfenbeinküste, Ghana, Kamerun und Nigeria. Sie werden in Bananenblättern fermentiert und an der Sonne getrocknet. Die Böden dieser Region enthalten von Natur aus wenig Cadmium, deshalb auch unser Kakao; den Wert Ihrer Charge finden Sie im Laborzertifikat, das wir auf Anfrage senden.

**sk**
> **Odkiaľ je.** Bôby sú z kakaovníka *Theobroma cacao* zo západnej Afriky — najmä z Pobrežia Slonoviny, Ghany, Kamerunu a Nigérie. Fermentujú sa v banánových listoch a sušia na slnku. Pôdy v tejto oblasti majú prirodzene nízky obsah kadmia, preto ho má nízky aj naše kakao; hodnotu k šarži nájdete v laboratórnom certifikáte, ktorý pošleme na vyžiadanie.

---

## B. FAQ for the cocoa product page (three new pairs for `PRODUCT_COCOA_FAQ`)

### cs

1. **Odkud pochází kakao Jůzlová?**
   Ze západní Afriky — hlavně z Pobřeží slonoviny, Ghany, Kamerunu a Nigérie. Je to kakaovník *Theobroma cacao*. Boby se fermentují v banánových listech, suší na slunci a u nás se melou a alkalizují na holandský typ.

2. **Proč má kakao Jůzlová nízký obsah kadmia?**
   Kadmium se do bobů dostává z půdy. Vysoké hodnoty mívá kakao z vulkanických půd části Latinské Ameriky, například z Peru a Ekvádoru. Západoafrické půdy kadmia obsahují málo, a tak ho má málo i kakao odtud. Limit EU pro kakaový prášek je 0,60 mg/kg (nařízení (EU) 2023/915); hodnotu naší šarže máme v laboratorním certifikátu a pošleme ho na vyžádání.

3. **A co olovo?**
   V západní Africe je to hlavní sledovaný kov. Drží se na slupce bobu, ne v jádru, a odchází při loupání před mletím. I olovo je v certifikátu k šarži.

### en

1. **Where does Jůzlová cocoa come from?**
   West Africa, mainly Ivory Coast, Ghana, Cameroon and Nigeria. The tree is *Theobroma cacao*. The beans are fermented in banana leaves, sun-dried, then ground and alkalised to Dutch-process cocoa.

2. **Why is the cadmium content of Jůzlová cocoa low?**
   Cadmium enters the beans from the soil. High values are typical of cocoa grown on volcanic soils in parts of Latin America, for example Peru and Ecuador. West African soils hold little cadmium, so cocoa from there is low too. The EU limit for cocoa powder is 0.60 mg/kg (Regulation (EU) 2023/915); the value for our batch is in the certificate of analysis, sent on request.

3. **What about lead?**
   In West Africa lead is the metal that is watched. It stays on the bean's husk, not in the nib, and leaves with the shell before grinding. Lead is in the batch certificate as well.

### de

1. **Woher kommt der Kakao von Jůzlová?**
   Aus Westafrika, vor allem aus der Elfenbeinküste, Ghana, Kamerun und Nigeria. Der Baum ist *Theobroma cacao*. Die Bohnen werden in Bananenblättern fermentiert, an der Sonne getrocknet, dann gemahlen und zu Kakao holländischer Art alkalisiert.

2. **Warum ist der Cadmiumgehalt im Kakao von Jůzlová niedrig?**
   Cadmium gelangt aus dem Boden in die Bohne. Hohe Werte sind typisch für Kakao von vulkanischen Böden in Teilen Lateinamerikas, etwa aus Peru und Ecuador. Westafrikanische Böden enthalten wenig Cadmium, also auch der Kakao von dort. Der EU-Grenzwert für Kakaopulver liegt bei 0,60 mg/kg (Verordnung (EU) 2023/915); den Wert unserer Charge finden Sie im Laborzertifikat, das wir auf Anfrage senden.

3. **Und Blei?**
   In Westafrika ist Blei das Metall, auf das geachtet wird. Es bleibt auf der Schale der Bohne, nicht im Kern, und geht beim Schälen vor dem Mahlen ab. Auch Blei steht im Chargenzertifikat.

### sk

1. **Odkiaľ pochádza kakao Jůzlová?**
   Zo západnej Afriky — najmä z Pobrežia Slonoviny, Ghany, Kamerunu a Nigérie. Je to kakaovník *Theobroma cacao*. Bôby sa fermentujú v banánových listoch, sušia na slnku a potom sa melú a alkalizujú na holandský typ.

2. **Prečo má kakao Jůzlová nízky obsah kadmia?**
   Kadmium sa do bôbov dostáva z pôdy. Vysoké hodnoty máva kakao z vulkanických pôd časti Latinskej Ameriky, napríklad z Peru a Ekvádoru. Západoafrické pôdy kadmia obsahujú málo, a tak ho má málo aj kakao odtiaľ. Limit EÚ pre kakaový prášok je 0,60 mg/kg (nariadenie (EÚ) 2023/915); hodnotu našej šarže máme v laboratórnom certifikáte a pošleme ho na vyžiadanie.

3. **A čo olovo?**
   V západnej Afrike je to hlavný sledovaný kov. Drží sa na šupke bôbu, nie v jadre, a odchádza pri lúpaní pred mletím. Aj olovo je v certifikáte k šarži.

---

## C. Answer-engine notes (for `llms.txt` and the FAQ JSON-LD in Phase 3)

- One-line fact for `llms-*.txt`, cs: "Kakao Jůzlová: *Theobroma cacao* ze západní Afriky (Pobřeží slonoviny, Ghana, Kamerun, Nigérie), holandský typ, 20–22 % kakaového másla, půdy s nízkým kadmiem; limit EU pro kakaový prášek 0,60 mg/kg; certifikát k šarži na vyžádání."
- FAQ JSON-LD: the three pairs above go into the cocoa page's `FAQPage` block only (the home page has no FAQ; the household FAQ page must not repeat them).
- Keep the existing "Proč se cena kakaa mění?" answer; it already mentions EU heavy-metal limits, so link the two mentally but do not repeat the limit value there.
- Do not add a "lower than competitors" claim. The comparison is regional (West Africa vs. volcanic Latin America), sourced, and worded as such.

## D. Where it shows in the redesign

- Cocoa product page: answer capsule under "Odkud je", FAQ block, the cacao
  pod silhouette and the cacao-flower cut-out (the flowers grow straight from
  the trunk, which is worth one caption on the page: "Kakaovník kvete přímo
  z kmene; z každého květu, který se ujme, vyroste jeden plod.").
- Wholesale page: unchanged, keeps the certificate FAQ.
