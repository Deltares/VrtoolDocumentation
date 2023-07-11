# Vakindeling

Bij de veiligheidsrendement methode moet één vakindeling gemaakt worden die voor alle faalmechanismen gebruikt wordt. Hiervoor zijn drie stappen nodig. 

## Stap 1: Excel invoerbestand invullen

De basis voor het genereren van de vakindeling is het invoerbestand `Vakindeling.csv`. Dit bestand is terug te vinden in: ```.\VRSuiteUtils-main\preprocessing\default_files``` in de ZIP bestand die bij de installatie van de [preprocessing script](..\Installaties\VRUtils.md) is gedownload.

Dit bestand heeft de volgende kolommen die ingevul dmoeten worden:

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
- De m_eind en m_start van alle vakken moeten op elkaar aansluiten

## Stap 2: Command-Line Interface voorbereiden 

Deze stap kan je overslaan als Anaconda Prompt al open staat en de juiste enviroment al geactiveerd is. Dit is het geval als bijvoorbeeld zojuist de [installatie van de preprocssing is gemaakt](..\Installaties\VRUtiles.md).


1. Open Anaconda Prompt

![Opening_Anaconda_promt.PNG](Opening_Anaconda_promt.PNG)

2. Ga naar de juiste directory waar je [preprocessing script staat](..\Installaties\VRUtils.md) met behulp van de volgende commandline. Vervang "C:/link_naar_ZIP_file_map" met de locatie van de map waar de ZIP file is uitgepakt.
```
cd C:/link_naar_ZIP_file_map
```


3. Activeer het environment van de preprocessor: 
```
conda activate .env
```
**Let op:** als je het environment een andere naam hebt gegeven, vervang ".env" dan door de naam die je aan het environment gegeven hebt.

## Stap 3: Script voor vakindeling runnen

Via de **Command Line Interface (CLI)** kan de Preprocessing tool worden aangeroepen, zonder dat de gebruiker in de Python code hoeft te werken. Dit werkt als volgt:


```
python -m preprocessing vakindeling {input arguments}
```


Vervang nog "{input arguments}" met behorend inputs van een vakindeling: ```--input_naam1 "input_1" --input_naam2 "input_2" etc.```


De inputs van een vakindeling zijn: 

| Input naam       	      | 	           | Beschrijving                                                                                                                                                                                 	                                                                                                                                                                                                                                                                                                                                               |
|-------------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --traject_id    	       | Verplicht 	 | Hier geef je aan om welk traject het gaat. Dit is een string, bijvoorbeeld ‘38-1’.                                                                           	                                                                                                                                                                                                                                                                                                                                                                               |
| --vakindeling_csv     	 | Verplicht 	 | Link naar de CSV met de vakindeling.                                                                                                               	                                                                                                                                                                                                                                                                                                                                                                                         |
| --output_folder     	   | Verplicht 	 | Link naar de map waar de trajectshapefile (inclusief een afbeelding in PNG) terecht moet komen.                                                                                                                                                       	                                                                                                                                                                                                                                                                                      |
| --traject_shape    | Optioneel 	 | Link naar de trajectshapefile. Let op: voer deze alleen in als de gebruikte shapefile afwijkt van de shapefile in het Nationaal Bestand Primaire Waterkeringen (NBPW). Als je deze optie niet gebruikt, wordt de shapefile uit het NBPW gebruikt. Deze invoer is optioneel, en dient enkel gebruikt te worden wanneer de gebruikte trajectshape afwijkt van de trajectshape in NBPW.                                                                                                                                                       	 |
| --flip  	           | Optioneel 	 | Soms staat de shapefile in het NBPW in de tegenovergestelde richting van je vakindeling. Met andere woorden: de vakindeling begint aan de 'verkeerde' kant van de shapefile. Als dit het geval is, kan de shapefile worden omgedraaid door deze optie op True te zetten.                                                                                                                                              	                                                                                                                      |




**Let op:** deze regel is vanuit elke directory te runnen, je hoeft dus niet eerst naar een bepaalde folder te gaan.

Om meer informatie over de code te krijgen, gebruik je: 
``` python -m preprocessing vakindeling --help. ```

### Voorbeeld van code om de vakindeling te runnen 

```
python -m preprocessing vakindeling --traject_id “38-1” --vakindeling_csv “c:\VRM\test_vakindeling_workflow\Vakindeling 38-1.csv” --output_folder “c:\VRM\test_vakindeling_workflow\result\”
```


