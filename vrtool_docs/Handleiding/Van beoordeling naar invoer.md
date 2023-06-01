# Van beoordeling naar invoer

## Overzicht van de workflows

De eerste stap in het voorbereiden van gegevens voor berekeningen met de VRTOOL is het genereren van een vakindeling. Deze vakindeling is de basis van de analyses, en moet aan de volgende voorwaarden voldoen:
* De vakindeling voor alle faalmechanismen is gelijk.
* Voor elk faalmechanisme is 1 mechanismeberekening beschikbaar, voor minimaal 1 relevant faalmechanisme.


## Basisinvoerbestanden

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

### Vullen van een invoerbestand voor Hydra-Ring

## Workflows 

### Genereren van een vakindeling voor de VRTOOL

Op basis van de vakindeling invoerbestand (excel) bestand kan vervolgens met de volgende code een shapefile worden gegenereerd waarin de shapefile van het betreffende traject wordt gedownload van de webserver van het Nationaal Basisbestand Primaire Waterkeringen, en vervolgens conform de m-waarden wordt opgeknipt. 

Dit kan door middel van [`generate_vakindeling_workflow.py`](https://github.com/Deltares/VRSuiteUtils/blob/main/preprocessing/workflows/generate_vakindeling.py) uit de `VRUtils` GitHub.

Deze workflow kan worden aangeroepen vanuit de terminal (bijv. via Anaconda Prompt) door middel van het commando:

    python /pad/naar/generate_vakindeling_workflow.py 'traject-1' '/pad/naar/vakindeling.csv'

Waarbij het eerste argument een officiële trajectnaam moet zijn, en het tweede pad moet verwijzen naar de vakindeling.csv.
Let op dat de paden relatief zijn tot de locatie in de console.

De uitvoer bestaat uit 2 bestanden die in dezelfde map als `vakindeling.csv` worden weggeschreven:
* `Vakindeling_traject.geojson` waarin de opgeknipte vakindeling is opgeslagen.
* `Vakindeling_traject.png` waarin een figuur met de vakindeling is opgeslagen.

Een voorbeeld van een vakindeling volgend uit de workflow is onderstaand weergegeven:
![Vakindeling voor dijktraject 38-1](vakindeling.png)


## Workflow Hydra-Ring



