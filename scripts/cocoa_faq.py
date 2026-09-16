"""Cocoa product FAQs (D2C) and wholesale extras (B2B).

Household answers live on the cocoa product page. Ice-cream makers and
certificates of analysis live only on wholesale pages. Never name suppliers.
"""

# D2C — cocoa product page. Unique extras (sugar, allergens, storage) stay here.
PRODUCT_COCOA_FAQ = {
    "cs": [
        ("Proč se cena kakaa mění?",
         "Kakao je burzovní komodita: cenu hýbe počasí, poptávka a nové limity EU na těžké kovy. Ceník upravujeme, když se změní náš nákup."),
        ("Je to raw kakao?",
         "Ne. Je alkalizované (holandské) a pražené. Raw kakao je nepražené a chutná hořce a travnatě; to naše je jemné a kulaté, s praženými tóny."),
        ("Hodí se do zmrzliny?",
         "Ano. Vyšší podíl kakaového másla dává zmrzlině hladkou texturu a tmavou barvu, která v mrazu nevybledne."),
    ],
    "en": [
        ("Why does the cocoa price change?",
         "Cocoa is a traded commodity: weather, demand and new EU heavy-metal limits move the price. We adjust the list when our purchase price changes."),
        ("Is it raw cocoa?",
         "No. It is alkalised (Dutch-process) and roasted. Raw cocoa is unroasted and tastes bitter and grassy; ours is smooth and rounded with roasted notes."),
        ("Does it work in ice cream?",
         "Yes. The higher cocoa-butter content gives ice cream a smooth texture and a dark colour that does not fade in the freezer."),
    ],
    "de": [
        ("Warum ändert sich der Kakaopreis?",
         "Kakao ist eine Börsenware: Wetter, Nachfrage und neue EU-Grenzwerte für Schwermetalle bewegen den Preis. Die Liste passen wir an, wenn sich unser Einkauf ändert."),
        ("Ist das Rohkakao?",
         "Nein. Er ist alkalisiert (holländisch) und geröstet. Rohkakao ist ungeröstet und schmeckt bitter und grasig; unserer ist mild und rund mit Röstnoten."),
        ("Eignet er sich für Speiseeis?",
         "Ja. Der höhere Kakaobutteranteil gibt Eis eine glatte Textur und eine dunkle Farbe, die im Gefrierfach nicht verblasst."),
    ],
    "sk": [
        ("Prečo sa cena kakaa mení?",
         "Kakao je burzová komodita: cenou hýbe počasie, dopyt a nové limity EÚ na ťažké kovy. Cenník upravujeme, keď sa zmení náš nákup."),
        ("Je to raw kakao?",
         "Nie. Je alkalizované (holandské) a pražené. Raw kakao je nepražené a chutí horko a trávnato; to naše je jemné a okrúhle, s praženými tónmi."),
        ("Hodí sa do zmrzliny?",
         "Áno. Vyšší podiel kakaového masla dáva zmrzline hladkú textúru a tmavú farbu, ktorá v mraze nevybledne."),
    ],
}

# B2B only — not on the cocoa product page or the household FAQ page.
B2B_COCOA_FAQ = {
    "cs": [
        ("Hodí se kakao výrobcům zmrzliny?",
         "Ano. Vysoký obsah kakaového másla zmrzlině svědčí: silná kakaová chuť, hladká textura a sytá barva, která nevybledne. Cenu podle množství domluvíme. Ozvěte se a napište, co potřebujete."),
        ("Poskytujete certifikát analýzy (CoA)?",
         "Ano. Napište si o něj a pošleme laboratorní certifikát k vaší šarži."),
    ],
    "en": [
        ("Is the cocoa suitable for ice-cream makers?",
         "Yes. The high cocoa butter content is what suits ice cream: a strong cocoa flavour, a smooth texture and a deep colour that does not fade. Quantity prices are agreed case by case. Get in touch and tell us what you need."),
        ("Do you provide a Certificate of Analysis?",
         "Yes. Ask us and we will send the lab certificate for your batch."),
    ],
    "de": [
        ("Eignet sich der Kakao für Eishersteller?",
         "Ja. Der hohe Kakaobutteranteil ist genau das, was Eis braucht: kräftiger Kakaogeschmack, glatte Textur und eine tiefe Farbe, die nicht verblasst. Mengenpreise vereinbaren wir. Melden Sie sich und sagen Sie uns, was Sie brauchen."),
        ("Stellen Sie ein Analysenzertifikat (CoA) zur Verfügung?",
         "Ja. Fragen Sie danach, und wir senden das Laborzertifikat zu Ihrer Charge."),
    ],
    "sk": [
        ("Hodí sa kakao výrobcom zmrzliny?",
         "Áno. Vysoký obsah kakaového masla zmrzline svedčí: silná kakaová chuť, hladká textúra a sýta farba, ktorá nevybledne. Cenu podľa množstva dohodneme. Ozvite sa a napíšte, čo potrebujete."),
        ("Poskytujete certifikát analýzy (CoA)?",
         "Áno. Napíšte si oň a pošleme laboratórny certifikát k vašej šarži."),
    ],
}


def product_cocoa_faq(lang):
    return list(PRODUCT_COCOA_FAQ.get(lang) or PRODUCT_COCOA_FAQ["cs"])


def b2b_cocoa_faq(lang):
    return list(B2B_COCOA_FAQ.get(lang) or B2B_COCOA_FAQ["cs"])
