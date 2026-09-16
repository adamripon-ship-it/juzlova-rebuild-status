"""Cocoa origin and cadmium copy (docs/messaging/07-cocoa-origin-and-cadmium.md).

Owner brief 2026-09-16: Theobroma cacao, beans mainly from Ivory Coast, Ghana,
Cameroon and Nigeria; low-cadmium West African soils. Sources: Primoris lab,
"Cocoa and its region"; Regulation (EU) 2023/915, Annex I, 3.2.15.
No supplier names. No invented measured values.
"""

# Replaces the paragraph under the "Odkud je" heading on the cocoa product page.
CAPSULE = {
    "cs": ("Boby jsou z kakaovníku Theobroma cacao ze západní Afriky — hlavně z Pobřeží slonoviny, "
           "Ghany, Kamerunu a Nigérie. Fermentují se v banánových listech a suší na slunci. Půdy v této "
           "oblasti mají přirozeně nízký obsah kadmia, proto ho má nízký i naše kakao; hodnotu k šarži "
           "najdete v laboratorním certifikátu, který pošleme na vyžádání. Alkalizujeme přírodními solemi "
           "na pH 7,8–8,2 — proto je barva sytě červenohnědá a chuť kulatá, bez kyselosti."),
    "en": ("The beans are Theobroma cacao from West Africa, mainly Ivory Coast, Ghana, Cameroon and Nigeria. "
           "They are fermented in banana leaves and dried in the sun. Soils in this region are naturally low "
           "in cadmium, so our cocoa is too; the value for your batch is in the certificate of analysis, sent "
           "on request. We alkalise with natural salts to pH 7.8–8.2, which gives the deep red-brown colour "
           "and a round taste without acidity."),
    "de": ("Die Bohnen stammen vom Kakaobaum Theobroma cacao aus Westafrika, vor allem aus der Elfenbeinküste, "
           "Ghana, Kamerun und Nigeria. Sie werden in Bananenblättern fermentiert und an der Sonne getrocknet. "
           "Die Böden dieser Region enthalten von Natur aus wenig Cadmium, deshalb auch unser Kakao; den Wert "
           "Ihrer Charge finden Sie im Laborzertifikat, das wir auf Anfrage senden. Alkalisiert wird mit "
           "natürlichen Salzen auf pH 7,8–8,2 — daher die tief rotbraune Farbe und der runde Geschmack ohne Säure."),
    "sk": ("Bôby sú z kakaovníka Theobroma cacao zo západnej Afriky — najmä z Pobrežia Slonoviny, Ghany, "
           "Kamerunu a Nigérie. Fermentujú sa v banánových listoch a sušia na slnku. Pôdy v tejto oblasti majú "
           "prirodzene nízky obsah kadmia, preto ho má nízky aj naše kakao; hodnotu k šarži nájdete v "
           "laboratórnom certifikáte, ktorý pošleme na vyžiadanie. Alkalizujeme prírodnými soľami na pH 7,8–8,2 — "
           "preto je farba sýto červenohnedá a chuť okrúhla, bez kyslosti."),
}

# Headings whose following paragraph the capsule replaces.
ORIGIN_H2 = {"cs": "Odkud je", "en": "Where it comes from", "de": "Woher er kommt", "sk": "Odkiaľ je"}

# Three FAQ pairs appended to the cocoa page (FAQPage JSON-LD follows automatically).
FAQ = {
    "cs": [
        ("Odkud pochází kakao Jůzlová?",
         "Ze západní Afriky — hlavně z Pobřeží slonoviny, Ghany, Kamerunu a Nigérie. Je to kakaovník Theobroma cacao. "
         "Boby se fermentují v banánových listech, suší na slunci a u nás se melou a alkalizují na holandský typ."),
        ("Proč má kakao Jůzlová nízký obsah kadmia?",
         "Kadmium se do bobů dostává z půdy. Vysoké hodnoty mívá kakao z vulkanických půd části Latinské Ameriky, "
         "například z Peru a Ekvádoru. Západoafrické půdy kadmia obsahují málo, a tak ho má málo i kakao odtud. "
         "Limit EU pro kakaový prášek je 0,60 mg/kg (nařízení (EU) 2023/915); hodnotu naší šarže máme v laboratorním "
         "certifikátu a pošleme ho na vyžádání."),
        ("A co olovo?",
         "V západní Africe je to hlavní sledovaný kov. Drží se na slupce bobu, ne v jádru, a odchází při loupání před "
         "mletím. I olovo je v certifikátu k šarži."),
    ],
    "en": [
        ("Where does Jůzlová cocoa come from?",
         "West Africa, mainly Ivory Coast, Ghana, Cameroon and Nigeria. The tree is Theobroma cacao. The beans are "
         "fermented in banana leaves, sun-dried, then ground and alkalised to Dutch-process cocoa."),
        ("Why is the cadmium content of Jůzlová cocoa low?",
         "Cadmium enters the beans from the soil. High values are typical of cocoa grown on volcanic soils in parts of "
         "Latin America, for example Peru and Ecuador. West African soils hold little cadmium, so cocoa from there is "
         "low too. The EU limit for cocoa powder is 0.60 mg/kg (Regulation (EU) 2023/915); the value for our batch is "
         "in the certificate of analysis, sent on request."),
        ("What about lead?",
         "In West Africa lead is the metal that is watched. It stays on the bean's husk, not in the nib, and leaves "
         "with the shell before grinding. Lead is in the batch certificate as well."),
    ],
    "de": [
        ("Woher kommt der Kakao von Jůzlová?",
         "Aus Westafrika, vor allem aus der Elfenbeinküste, Ghana, Kamerun und Nigeria. Der Baum ist Theobroma cacao. "
         "Die Bohnen werden in Bananenblättern fermentiert, an der Sonne getrocknet, dann gemahlen und zu Kakao "
         "holländischer Art alkalisiert."),
        ("Warum ist der Cadmiumgehalt im Kakao von Jůzlová niedrig?",
         "Cadmium gelangt aus dem Boden in die Bohne. Hohe Werte sind typisch für Kakao von vulkanischen Böden in Teilen "
         "Lateinamerikas, etwa aus Peru und Ecuador. Westafrikanische Böden enthalten wenig Cadmium, also auch der Kakao "
         "von dort. Der EU-Grenzwert für Kakaopulver liegt bei 0,60 mg/kg (Verordnung (EU) 2023/915); den Wert unserer "
         "Charge finden Sie im Laborzertifikat, das wir auf Anfrage senden."),
        ("Und Blei?",
         "In Westafrika ist Blei das Metall, auf das geachtet wird. Es bleibt auf der Schale der Bohne, nicht im Kern, "
         "und geht beim Schälen vor dem Mahlen ab. Auch Blei steht im Chargenzertifikat."),
    ],
    "sk": [
        ("Odkiaľ pochádza kakao Jůzlová?",
         "Zo západnej Afriky — najmä z Pobrežia Slonoviny, Ghany, Kamerunu a Nigérie. Je to kakaovník Theobroma cacao. "
         "Bôby sa fermentujú v banánových listoch, sušia na slnku a potom sa melú a alkalizujú na holandský typ."),
        ("Prečo má kakao Jůzlová nízky obsah kadmia?",
         "Kadmium sa do bôbov dostáva z pôdy. Vysoké hodnoty máva kakao z vulkanických pôd časti Latinskej Ameriky, "
         "napríklad z Peru a Ekvádoru. Západoafrické pôdy kadmia obsahujú málo, a tak ho má málo aj kakao odtiaľ. "
         "Limit EÚ pre kakaový prášok je 0,60 mg/kg (nariadenie (EÚ) 2023/915); hodnotu našej šarže máme v "
         "laboratórnom certifikáte a pošleme ho na vyžiadanie."),
        ("A čo olovo?",
         "V západnej Afrike je to hlavný sledovaný kov. Drží sa na šupke bôbu, nie v jadre, a odchádza pri lúpaní pred "
         "mletím. Aj olovo je v certifikáte k šarži."),
    ],
}

# Caption for the cacao-flower cut-out on the cocoa page.
FLOWER_CAPTION = {
    "cs": "Kakaovník kvete přímo z kmene; z každého květu, který se ujme, vyroste jeden plod.",
    "en": "The cacao tree flowers straight from its trunk; every flower that sets grows into one pod.",
    "de": "Der Kakaobaum blüht direkt am Stamm; aus jeder Blüte, die ansetzt, wird eine Frucht.",
    "sk": "Kakaovník kvitne priamo z kmeňa; z každého kvetu, ktorý sa ujme, vyrastie jeden plod.",
}
FLOWER_ALT = {
    "cs": "Tři květy kakaovníku na kůře kmene",
    "en": "Three cacao flowers on the bark of the trunk",
    "de": "Drei Kakaoblüten auf der Rinde des Stammes",
    "sk": "Tri kvety kakaovníka na kôre kmeňa",
}

# One-line fact for llms.txt (answer engines).
LLMS_LINE = {
    "cs": "Kakao Jůzlová: Theobroma cacao ze západní Afriky (Pobřeží slonoviny, Ghana, Kamerun, Nigérie), holandský typ, 20–22 % kakaového másla, půdy s nízkým kadmiem; limit EU pro kakaový prášek 0,60 mg/kg; certifikát k šarži na vyžádání.",
    "en": "Jůzlová cocoa: Theobroma cacao from West Africa (Ivory Coast, Ghana, Cameroon, Nigeria), Dutch-process, 20–22 % cocoa butter, low-cadmium soils; EU limit for cocoa powder 0.60 mg/kg; batch certificate on request.",
    "de": "Jůzlová Kakao: Theobroma cacao aus Westafrika (Elfenbeinküste, Ghana, Kamerun, Nigeria), holländische Art, 20–22 % Kakaobutter, cadmiumarme Böden; EU-Grenzwert für Kakaopulver 0,60 mg/kg; Chargenzertifikat auf Anfrage.",
    "sk": "Kakao Jůzlová: Theobroma cacao zo západnej Afriky (Pobrežie Slonoviny, Ghana, Kamerun, Nigéria), holandský typ, 20–22 % kakaového masla, pôdy s nízkym kadmiom; limit EÚ pre kakaový prášok 0,60 mg/kg; certifikát k šarži na vyžiadanie.",
}
