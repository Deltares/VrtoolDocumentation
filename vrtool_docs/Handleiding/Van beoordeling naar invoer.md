# Van beoordeling naar invoer

## Overzicht van de workflows

De eerste stap in het voorbereiden van gegevens voor berekeningen met de VRTOOL is het genereren van een vakindeling. Deze vakindeling is de basis van de analyses, en moet aan de volgende voorwaarden voldoen:
* De vakindeling voor alle faalmechanismen is gelijk.
* Voor elk faalmechanisme is 1 mechanismeberekening beschikbaar, voor minimaal 1 relevant faalmechanisme.

De tweede stap is dan het genereren van de waterstanden en wanneer relevant van de GEKB som met Hydra Ring. Belangrijk is om een correcte installatie van een recente versie van Hydra-Ring te hebben, bijvoorbeeld door de laatste versie van Riskeer te installeren.
De berekeningen worden uitgevoerd via de `VRSuiteUtils`. [Installatieinstructies](link) zijn hier te vinden.

## Basisinvoerbestanden

Er zijn XX basisinvoerbestanden die hieronder worden toegelicht.

### Vullen van een invoerbestand voor vakindeling
De basis voor het genereren van de vakindeling is het invoerbestand `Vakindeling.csv`. Dit bestand heeft de volgende kolommen die moeten worden gevuld:

| Kolom       	|           	| Beschrijving                                                                                                                                                                                 	      |
|-------------	|-----------	|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| objectid    	| Verplicht 	| Unieke identifier (moeten verschillende getallen zijn)                                                                                                                                       	      |
| vaknaam     	| Verplicht 	| Nummer/naam van het dijkvak (moet uniek zijn, kan identiek zijn aan OBJECTID)                                                                                                                     	 |
| m_start     	| Verplicht 	| startpunt op lijn van traject                                                                                                                                                         	             |
| m_eind      	| Verplicht 	| eindpunt op lijn van traject                                                                                                                                                          	             |
| in_analyse  	| Verplicht 	| Vak meenemen in analyse of niet (TRUE/FALSE)                                                                                                                                                 	      |
| van_dp      	| Optioneel 	| Begrenzing dijkpaalnummers                                                                                                                                                                   	      |
| tot_dp      	| Optioneel 	| Begrenzing dijkpaalnummers                                                                                                                                                                   	      |
| {}          	| Optioneel 	| Doorsnede voor een mechanisme. Wanneer dit niet wordt ingevuld moet dit later worden afgeleid uit bijv een shapefile met uittredepunten. Daarvoor zijn specifieke workflows beschikbaar. 	          |
| opmerkingen 	| Optioneel 	| extra opmerkingen, moet altijd de laatste kolom zijn                                                                                                                                         	      |

Belangrijk bij het genereren van de vakindeling zijn met name de `m_start` en `m_eind` parameters. 

**Let op:** 
- De separator in de csv files moet een komma zijn, en het teken voor decimalen een punt.
- De m_eind en m_start van alle vakken moeten overeen aan elkaar aansluiten


### Vullen van een invoerbestand voor Hydra-Ring

De basis voor het genereren van de waterstanden en overslag berekeningen is het invoerbestand `HR_default.csv`. Dit bestand heeft de volgende kolommen die moeten worden gevuld:

| Kolom       	                  | 	         | Beschrijving                                                                                                                                                                                 	                                                                                          |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| doorsnede    	                 | Optioneel 	 | Wanneer berekeningen gekoppeld moeten worden aan naamgeving in Vakindeling.csv is dit veld verplicht en moet het overeenkomen met veld overslag                                                                                                                                       	 |
| bovengrens     	               | Verplicht 	 | Bovengrens voor waterstandsberekeningen (bijv bij kans 1/30 van de signaleringswaarde)	                                                                                                                                                                                                                                                                                       |
| ondergrens     	               | Verplicht 	 | Ondergrens voor waterstandsberekeningen (bijv bij kans 1/10)                                                                                                                                                                                                                                                                          |
| prfl_bestand      	            | Verplicht 	 | Naam van het prfl bestand te gebruiken voor overslag	                                                                                                                                                                                                                                                                                       |
| orientatie  	                  | Optioneel 	 | Orientatie van het profiel voor overslagberekeningen. Wordt in principe uit het prfl bestand gelezen. Ter controle	                                                                                                                                                                                                                                                                                       |
| dijkhoogte      	              | Verplicht 	 | Hoogte van de dijk                                                                                                                                                              	                                                                                                                         |
| zodeklasse      	              | Verplicht 	 | Beschrijving van de graszodekwaliteit. Waarden moeten overeenkomen met de waarden in de standaardtabel.                                                                                                                                                           	                                                                                          |
| bovengrens_golfhoogteklasse 	  | Verplicht 	 | Bovengrens van de golfhoogteklasse. Bij 0-1 meter dus "1 meter", 1-2 meter wordt "2 meter" etc. 	                                                                                              |
| faalkans 	                     |  Optioneel 	 | Faalkans uit beoordeling, ter controle                                                                                                                                        	                                                                                          |
| kruindaling      	             | Verplicht 	 | Jaarlijkse kruindaling in m                                                                                                                                                                 	                                                                                          |
| m_value          	             | Optioneel 	 | Verplicht wanneer berekeningen geografisch moeten worden gekoppeld. Kan worden gevuld met aparte workflow                                                                                              |
| hrlocation/hr_koppel	          | Verplicht | Verwijzing naar de bijbehorende locatie in de hydraulische database. Hrlocation kan worden afgeleid o.b.v. hr_koppel                                                                                                                                       	                                                                                          |


### Vullen van een invoerbestand voor Piping

De basis voor het genereren van de piping berekeningen is het invoerbestand `Piping_default.csv`. Dit bestand heeft de volgende kolommen die moeten worden gevuld:

| Kolom       	 | 	         | Beschrijving                                                                                                                                                                                 	                                       |
|----------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| doorsnede | Verplicht 	 | Naam van het dwarsprofiel. In het geval van de uittredepuntenmethode is dit het ID van het punt                                                                                                                                     	 |
| scenario | Verplicht 	 | Indien er meerdere ondergrondscenario's zijn, dient hier het scenario ID te worden ingevoerd. Bij voorkeur een nummer, maar kan ook een string zijn                                                                                  |
| scenariokans | Verplicht | Conditionele kans op het ondergrondscenario [-]                                                                                                                                                                                      |
| mhw      | Verplicht 	 | Maatgevend hoogwater [m+NAP]                                                                                                                                                                                                         |
| polderpeil | Verplicht 	 | Polderpeil [m+NAP]                                                                                                                                                                                                                   |
| d_wvp    | Verplicht 	 | Dikte van het watervoerend pakket [m]	                                                                                                                                                                                               |
| d70      | Verplicht 	 | Zeefmaat die 70% (massa) van de zandkorrels van de zandfractie laat passeren [m]	                                                                                                                                                    |
| d_cover 	 | Verplicht 	 | Dike van de deklaag [m]                                                                                                                                                                                                              |
| h_exit 	 |  Verplicht 	 | Bodemhoogte bij uittredepunt [m+NAP]	                                                                                                                                                                                                |
| r_exit   | Verplicht 	 | Dempingsfactor bij uittredepunt [-] (afname van stijghoogte in watervoerend pakket ten gevolge van lek door slappelagenpakket)	                                                                                                      |
| l_voor  	 | Verplicht 	 | Leklengte intredepunt tot binnenteen dijk [m]                                                                                                                                                                                        |
| l_achter | Verplicht | Leklengte binnenteen tot uittredepunt [m]	                                                                                                                                                                                           |
| k  	     | Verplicht 	 | Doorlatendheid van het watervoerend pakket [m/s]	                                                                                                                                                                                    |
| gamma_sat | Verplicht 	 | Verzadigd gewicht van de deklaag [kN/m3]	                                                                                                                                                                                            |
| kwelscherm | Verplicht 	 | Aanwezigheid kwelscherm. 0 = kwelscherm afwezig, 1 = kwelscherm aanwezig	                                                                                                                                                            |
| dh_exit 	 | Verplicht 	 | Jaarlijkse bodemdaling van het achterland [m/jaar]	                                                                                                                                                                                  |
| pf_s 	   |  Optioneel | Jaarlijkse faalkans, gegeven het ondergrondscenario [-]. Optioneel, vooral handig als check	                                                                                                                                         |
| m_value  | Verplicht 	 | De M-waarde van het uittredepunt of de doorsnede [m]. Bij uittredepunten kan de m-waarde ook worden berekend, indien x-,y-coordinaten zijn gegeven. 	                                                                                |
| x_coord  	 | Verplicht | In het geval dat de uittredepuntenmethode is gebruikt, moet hier de x-coordinaat van het punt worden ingevuld (rijksdriehoekscoördinaten)                                                                                            |
| y_coord  | Verplicht | In het geval dat de uittredepuntenmethode is gebruikt, moet hier de y-coordinaat van het punt worden ingevuld (rijksdriehoekscoördinaten)	                                                                                           |




## Workflows 

### Workflow Genereren van een vakindeling voor de VRTOOL

Op basis van de vakindeling invoerbestand (`Vakindeling.csv`) bestand kan vervolgens met de volgende python code een shapefile worden gegenereerd: [`generate_vakindeling_workflow.py`](https://github.com/Deltares/VRSuiteUtils/blob/main/preprocessing/workflows/generate_vakindeling.py) uit de `VRUtils` GitHub.

De shapefile van het betreffende traject wordt gedownload van de webserver van het Nationaal Basisbestand Primaire Waterkeringen (NBPW), en vervolgens conform de m-waarden wordt opgeknipt. Een aandachtspunt hier is dat de richting van het opgeknipte traject volgens `Vakindeling.csv` anders kan zijn dan de richting van het traject volgens (NBPW). 

**Let op:** De trajectlengte moet gelijk zijn aan de som van alle vaklengtes.

Het is ook mogelijk om het betreffende traject zelf in te voeren door 'XXXXXX'

#### Draaien van de berekeningen voor vakindeling

Deze workflow kan worden aangeroepen vanuit de terminal (bijv. via Anaconda Prompt) door middel van het commando:

    python '/pad/naar/generate_vakindeling_workflow.py' 'traject-1' '/pad/naar/vakindeling.csv'

Waarbij:
- ``'/pad/naar/generate_vakindeling_workflow.py'`` vervangen moet worden met de pad naar de python code
- ``'traject-1'`` vervagen moet worden door de officiële trajectnaam 
- ``'/pad/naar/vakindeling.csv'`` vervangen moet worden met de pad moet verwijzen naar de vakindeling.csv.

**Let op** dat de paden relatief zijn tot de locatie in de console.

#### Uitvoer van de code voor vakindeling
De uitvoer bestaat uit 2 bestanden die in dezelfde map als `vakindeling.csv` worden weggeschreven:
* `Vakindeling_traject.geojson` waarin de opgeknipte vakindeling is opgeslagen.
* `Vakindeling_traject.png` waarin een figuur met de vakindeling is opgeslagen.

Wanneer beide bestaande zijn aangemaakt en de vakindeling van de figuur klopt met de verwachting is de code succesvol uitgevoerd.

Een voorbeeld van een vakindeling volgend uit de workflow is onderstaand weergegeven:
![Vakindeling voor dijktraject 38-1](vakindeling.png)


### Workflow Hydra-Ring

Als voorbereiding op analyses met de `VRTOOL` moet een aantal berekeningen gemaakt worden met `Hydra-Ring`. Als eerste moet de benodigde invoer worden klaargezet in het bestand `HR_default.csv`. Dit bevat alle informatie voor de berekeningen voor overslag en waterstand. 
Het is ook mogelijk dit bestand automatisch te vullen op basis van een shapefile met beoordelingsgegevens, en de shapefile van de vakindeling. 
Zie daarvoor de workflow [automatisch genereren van invoer voor Hydra-Ring berekeningen](link).

#### Berekeningen voor waterstand

#### Voorbereiden van de berekeningen voor waterstand
Als input voor de `VRTOOL` moeten voor 2023 en 2100 frequentielijnen van de waterstand worden afgeleid. De locaties zijn opgenomen in het bestand HR_default.csv.
Daarnaast moet een map worden gemaakt met daarin de submappen 2023 en 2100, volgens de volgende structuur:
```
Waterstandsberekening
├── 2023/
└── 2100/
```
In de mappen moeten de juiste hydraulische database bestanden worden geplaatst. In 2023 voor WBI2017, in 2100 voor het gewenste klimaatscenario.
Dit betreft zowel een HRD database, een config database, en de HLCD database met de juiste statistiek.

#### Draaien van de berekeningen voor waterstand
Het draaien van de berekeningen wordt gedaan via `preprocessing/workflows/hydraring_waterlevel_workflow.py`.
Voor het draaien van de code moeten in de python code drie paden worden gespecificeerd:
* `work_dir`: deze verwijst naar de hoofdfolder (`Waterstandsberekening`)
* `HydraRing_path`: deze verwijst naar de installatiefolder van Hydra-Ring (meestal een submap van de installatiefolder van Riskeer)
* `database_paths`: een `list` met daarin de subfolders waarin de hydraulische databases staan.

Alle opgegeven paden moeten als pathlib.Path object worden opgegeven. Dus `Path(r'mijnpad')`. **Let daarbij op** dat niet afgesloten moet worden met een `\`.
Vervolgens kunnen door het runnen van `hydraring_waterlevel_workflow.py` alle waterstandsberekeningen worden uitgevoerd. 

Deze workflow voor waterstandsberekeningen kan worden aangeroepen vanuit de terminal (bijv. via Anaconda Prompt) door middel van het commando:

    python '/pad/naar/hydraring_waterlevel_workflow'

Waarbij `/pad/naar/hydraring_waterlevel_workflow` moet vervangen worden door de pad naar `hydraring_waterlevel_workflow.py` relatief aan de locatie in de console. 

#### Uitvoer van de code berekeningen voor waterstand
Resultaten worden weggeschreven in subfolders met de naam van de doorsnede.

#### Interpreteren en verder verwerken van de uitvoer
Resultaat van de berekeningen zijn frequentielijnen voor 2023 en 2100.
Verdere instructies volgen.

### Berekeningen voor overslag

#### Voorbereiden van de berekeningen voor overslag
Voor overslag zijn iets meer gegevens nodig. De structuur is identiek aan die van waterstandsberekeningen, maar nu moeten de gegevens in de volgende structuur worden opgegeven:
```
Waterstandsberekening
├── 2023/
├── 2100/
└── prfl/
```

In de folder `prfl` moeten profielbestanden worden opgenomen voor alle door te rekenen doorsnedes. De naam van het bestand moet daarbij overeenkomen met de doorsnede uit het *.csv invoer bestand.

Verder werkt deze workflow identiek aan die van waterstand, via het bestand `hydraring_overflow_workflow.py`.

