# Voorbereidende berekeningen met Hydra-Ring
Als voorbereiding op analyses met de `VRTOOL` moet een aantal berekeningen gemaakt worden met `Hydra-Ring`. Belangrijk is om een correcte installatie van een recente versie van Hydra-Ring te hebben, bijvoorbeeld door de laatste versie van Riskeer te installeren.
De berekeningen worden uitgevoerd via de `VRSuiteUtils`. [Installatieinstructies](link) zijn hier te vinden.

Als eerste moet de benodigde invoer worden klaargezet in het bestand `HR_default.csv`. Dit bevat alle informatie voor de berekeningen voor overslag en waterstand. 
Het is ook mogelijk dit bestand automatisch te vullen op basis van een shapefile met beoordelingsgegevens, en de shapefile van de vakindeling. 
Zie daarvoor de workflow [automatisch genereren van invoer voor Hydra-Ring berekeningen](link).

## Berekeningen voor waterstand

### Voorbereiden van de berekeningen
Als input voor de `VRTOOL` moeten voor 2023 en 2100 frequentielijnen van de waterstand worden afgeleid. De locaties zijn opgenomen in het bestand HR_default.csv.
Daarnaast moet een map worden gemaakt met daarin de submappen 2023 en 2100, volgens de volgende structuur:
```
Waterstandsberekening
├── 2023/
└── 2100/
```
In de mappen moeten de juiste hydraulische database bestanden worden geplaatst. In 2023 voor WBI2017, in 2100 voor het gewenste klimaatscenario.
Dit betreft zowel een HRD database, een config database, en de HLCD database met de juiste statistiek.

### Draaien van de berekeningen
Het draaien van de berekeningen wordt gedaan via `preprocessing/workflows/hydraring_waterlevel_workflow.py`.
Hierin moeten 3 paden worden gespecificeerd:
* `work_dir`: deze verwijst naar de hoofdfolder (`Waterstandsberekening`)
* `HydraRing_path`: deze verwijst naar de installatiefolder van Hydra-Ring (meestal een submap van de installatiefolder van Riskeer)
* `database_paths`: een `list` met daarin de subfolders waarin de hydraulische databases staan.

Alle opgegeven paden moeten als pathlib.Path object worden opgegeven. Dus `Path(r'mijnpad')`. Let daarbij op dat niet afgesloten moet worden met een `\`.
Vervolgens kunnen door het runnen van `hydraring_waterlevel_workflow.py` alle waterstandsberekeningen worden uitgevoerd. Resultaten worden weggeschreven in subfolders met de naam van de doorsnede.

### Interpreteren en verder verwerken van de uitvoer
Resultaat van de berekeningen zijn frequentielijnen voor 2023 en 2100.
Verdere instructies volgen.

## Berekeningen voor overslag
Voor overslag zijn iets meer gegevens nodig. De structuur is identiek aan die van waterstandsberekeningen, maar nu moeten de gegevens in de volgende structuur worden opgegeven:
```
Waterstandsberekening
├── 2023/
├── 2100/
└── prfl/
```

In de folder `prfl` moeten profielbestanden worden opgenomen voor alle door te rekenen doorsnedes. De naam van het bestand moet daarbij overeenkomen met de doorsnede uit het *.csv invoer bestand.

Verder werkt deze workflow identiek aan die van waterstand, via het bestand `hydraring_overflow_workflow.py`.

