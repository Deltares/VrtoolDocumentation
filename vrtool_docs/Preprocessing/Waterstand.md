# Waterstand


## Stap 1: Excel invoerbestand invullen

De basis voor het genereren van berekeningen voor waterstand en overslag is het invoerbestand `HR_default.csv`. Dit bestand is terug te vinden in: ```.\VRSuiteUtils-main\preprocessing\default_files``` in de folder met de uitgepakte installatie voor de [preprocessing](..\Installaties\VRUtils.md).

Dit bestand heeft de volgende kolommen die ingevuld moeten worden:

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

 
## Stap 2: Command-Line Interface voorbereiden
Stap 2 is identiek als de preprocessing van de [vakindeling](Vakindeling.md)

## Stap 3: Script voor waterstanden runnen 

Via de **Command Line Interface (CLI)** kan de VR Preprocessing tool worden aangeroepen, zonder dat de gebruiker in de Python code hoeft te werken. Dit werkt als volgt:

```
python -m preprocessing waterlevel {input arguments}”
```

Vervang nog "{input arguments}" met behorend inputs van overslag: ```--input_naam1 "input_1" --input_naam2 "input_2" etc.```

De inputs van overslag zijn: 

| Input naam       	      | 	           | Beschrijving                                                                                                                                                                                 	                                                                                                                                                                               |
|-------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --work_dir  	       | Verplicht 	 | 	Dit is de werkmap, waarin je de resultaten van de waterstandsommen wilt uitvoeren. Belangrijk is dat deze map leeg is.                                                                                                                                                                                                                                                                                                        |
| --database_paths     	 | Verplicht 	 | Link naar de map met de Hydraulische database. Omdat er zowel een map voor de situatie huidig, als voor 2100 is, moet deze optie twee keer worden opgegeven. Dus: "--database_paths <pad naar de database voor huidige situatie> --database_paths <pad naar database voor de 2100 situatie>.                                                                                 |
| --hydraring_path    	   | Verplicht 	 | Link naar de map met de Hydraring executable ‘MechanismComputation.exe’. Deze executable is meestal te vinden in: ‘c:\Program Files (x86)\BOI\Riskeer 21.1.1.2\Application\Standalone\Deltares\HydraRing-20.1.3.10236’.                                                                                                                                                     	 |
| --file_name    | Verplicht 	 | Link naar de HR_default.csv.                                                                                                                                                     	                                                                                                                                                                                           |


**Let op:** deze regel is vanuit elke directory te runnen, je hoeft dus niet eerst naar een bepaalde folder te gaan.

Om meer informatie over de code te krijgen, gebruik je: 
``` python -m preprocessing waterlevel --help. ```

#### Voorbeeld invoer: 
```
python -m preprocessing waterlevel --work_dir c:\VRM\test_hydraring_workflow_wdod\waterlevel --database_paths "c:\VRM\test_hydraring_workflow_wdod\HR\2023" --database_paths "c:\VRM\test_hydraring_workflow_wdod\HR\2100" --hydraring_path "c:\Program Files (x86)\BOI\Riskeer 21.1.1.2\Application\Standalone\Deltares\HydraRing-20.1.3.10236" --file_name “c:\VRM\test_hydraring_workflow_wdod\HR_default.csv”
```
