# Binnenwaartse macrostabiliteit

Voor binnenwaarste macrostabiliteit kan de betrouwbaarheid bepaald worden op basis van de invoer of op basis van D-Stability. 

## Invoer 
In de invoer voor binnenwaarste macrostabiliteit moet de betrouwbaarheid op minimaal 1 tijdstip aangegeven worden. Wanneer 1 tijdstip wordt gegeven wordt aangenomen dat β constant is in de tijd. Bij meerdere tijdstippen wordt lineair geinterpoleerd.


In sommige gevallen zullen verschillende scenario’s mogelijk zijn. In dat geval moet het mogelijk zijn zowel de geaggregeerde β over alle scenario’s, als de β per scenario (incl. scenariokans) in te voeren (analoog aan piping).

## D-stability
Wanneer een *.stix file beschikbaar is kan deze worden gebruikt om de stabiliteitsberekening opnieuw te maken/aan te passen. Dit moet dan voor elk scenario (indien van toepassing) worden gedaan. Eventuele aanpassingen kunnen zijn:
- De geometrie:
    - N.a.v. versterking (bermverbreding/kruinverhoging)
    - N.a.v. tijdsafhankelijke verandering van de geometrie (daling kruin en/of teen)
- Toevoegen van constructies in de vorm van forbidden lines (aannames is dat constructie dan stijf is en voldoende sterk).
- Mogelijk in de toekomst algemene aanpassingen van parameters t.b.v. gevoeligheidsanalyse (bijv. extra sterkte in onverzadigde zone).
