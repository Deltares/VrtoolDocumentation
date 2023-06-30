# Binnenwaartse macrostabiliteit

Voor binnenwaarste macrostabiliteit kan de betrouwbaarheid bepaald worden op basis van directe invoer of op basis van D-Stability. 

## Directe invoer 
Bij de directe invoer voor binnenwaartse macrostabiliteit moet de betrouwbaarheid β op 1 tijdstip aangegeven worden. Het meenemen van tijdsafhankelijkheid is op dit moment niet ondersteund.

In sommige gevallen zijn verschillende scenario’s mogelijk. In dat geval is het mogelijk zowel de geaggregeerde β over alle scenario’s, als de β per scenario (incl. scenariokans) in te voeren.

## D-stability
Wanneer een *.stix file beschikbaar is kan deze worden gebruikt om de stabiliteitsberekening opnieuw te maken/aan te passen. 
Dit moet dan voor elk scenario (indien van toepassing) worden gedaan. 
Eventuele aanpassingen kunnen zijn:
- De geometrie:
    - N.a.v. versterking (bermverbreding/kruinverhoging)
    - N.a.v. tijdsafhankelijke verandering van de geometrie (daling kruin en/of teen)
- Toevoegen van constructies in de vorm van forbidden lines (aannames is dat constructie dan stijf is en voldoende sterk).

Mogelijk wordt in de toekomst de mogelijkheid toegevoegd om de buitenwaterstand en bijbehorend freatisch vlak aan te passen.
