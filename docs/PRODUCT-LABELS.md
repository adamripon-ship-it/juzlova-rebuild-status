# Printed label text, 5 kg sacks

Transcribed from photographs of the actual sacks, 2026-09-03. This is the
authoritative record of what is printed on the packaging.

It exists for two reasons. First, the product pages carry no composition,
allergen, nutrition or preparation data at all, and every word of it is here.
Second, when a product photograph is regenerated the label text has to be
handed to the image model verbatim — left to itself it invents plausible
Czech and the result looks right until somebody reads it.

Both labels end with the same producer block:

    Vyrobila: Jiřina Jůzlová, Kochánov 40, 582 53 Štoky
    tel.: 728 466 141, e-mail: juzlj@seznam.cz
    www.juzlova.cz

Note the address includes **Štoky**, which the site's footer omits.

## Chlupaté knedlíky / Halušky

    Hmotnost: 5 kg
    Uschovejte v suchu a chladu. Minimální trvanlivost do: [handwritten]

    100 g výrobku průměrně obsahuje:
      sacharidy: 76,49 g
      bílkoviny: 8,83 g
      tuky: 1,43 g
      sůl: 2 g
      energetická hodnota: 1459,4 kJ/100 g

    Složení:
    pšeničná mouka, sušená bramborová kaše, sušené brambory,
    bramborový škrob, sůl, sušená vejce

    Alergenní složky: lepek

    Návod k použití:
    1kg směsi nasypeme do misky, přelijeme 1,2 litru vody, řádně
    promícháme a těsto necháme 10 minut bobtnat. Lžící vytvarujeme
    knedlíky, které vložíme do vroucí vody a vaříme, až vyplavou
    (asi 5 - 8 minut dle velikosti).

## Bramborové knedlíky

    Hmotnost: 5 kg
    Uschovejte v suchu a chladu. Minimální trvanlivost do: [handwritten]

    100 g výrobku průměrně obsahuje:
      sacharidy: 71,53 g
      bílkoviny: 9,55 g
      tuky: 1,42 g
      sůl: 2 g
      energetická hodnota: 1432,7 kJ/100 g

    Složení:
    pšeničná mouka, sušená bramborová kaše (přírodní barvivo E 100,
    antioxidant E 304, E 223, emulgátor E 471), sůl, sušená vejce,
    kypřidlo, škrob

    Alergenní složky: lepek, sušená vejce

    Návod k použití:
    1kg směsi nasypeme do misky, přelijeme 1 litrem vody, řádně
    prohněteme a těsto necháme 2 až 3 minuty odležet. Z těsta
    vypracujeme válečky o průměru cca 6cm, které vložíme do vroucí
    vody a vaříme 15 - 20 minut (dle velikosti knedlíků).

## Where the label and the site disagree

Three things fell out of cross-referencing the labels against
`scripts/content_cs.py`. None is changed here; they are the owner's to
settle.

1. The bramborové knedlíky page says *"v těstě není nic navíc — jen to, co
   do bramborového knedlíku patří."* The label declares E 100, E 304, E 223,
   E 471 and a raising agent. The additives are carried in the bought-in
   dried potato rather than added by the workshop, but the sentence reads as
   a claim about the finished mix and a customer holding the sack can check
   it.

2. E 223 is sodium metabisulphite, a sulphite and one of the 14 EU
   allergens. `Alergenní složky` lists only lepek and sušená vejce.
   Declaration is required above 10 mg/kg as SO2; below that it is not. Worth
   confirming the figure with the dried-potato supplier.

3. The page says potato dumplings are ready *"do 20 minut"*. The label is
   2–3 minutes resting plus 15–20 minutes boiling, so 20 is the floor rather
   than the ceiling.
