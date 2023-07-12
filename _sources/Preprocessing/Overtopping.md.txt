# Overslag

Stappen 1 en 2 zijn identiek als de preprocessing van de [waterstanden](Waterstand.md)

## Stap 3: Script voor overslag runnen  

Via de **Command Line Interface (CLI)** kan de VR Preprocessing tool worden aangeroepen, zonder dat de gebruiker in de Python code hoeft te werken. Dit werkt als volgt:

```
python -m preprocessing overflow {input arguments}”
```

Vervang nog "{input arguments}" met behorend inputs van overslag: ```--input_naam1 "input_1" --input_naam2 "input_2" etc.```

De inputs van overslag zijn: 

| Input naam       	      | 	           | Beschrijving                                                                                                                                                                                 	                                                                                                                                                                               |
|-------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --work_dir  	       | Verplicht 	 | 	Dit is de werkmap, waarin je de resultaten van de overslagsommen wilt uitvoeren. Belangrijk is dat deze map voorafgaand aan het runnen van het script al een map met de profielen bevat. Deze map met profielen moet de naam 'prfl' hebben. Naast de profielenmap, moet de map leeg zijn.                                                                                                                                                                                                                                                                                                      |
| --database_paths     	 | Verplicht 	 | Link naar de map met de Hydraulische database. Omdat er zowel een map voor de situatie huidig, als voor 2100 is, moet deze optie twee keer worden opgegeven. Dus: "--database_paths <pad naar de database voor huidige situatie> --database_paths <pad naar database voor de 2100 situatie>.                                                                                 |
| --hydraring_path    	   | Verplicht 	 | Link naar de map met de Hydraring executable ‘MechanismComputation.exe’. Deze executable is meestal te vinden in: ‘c:\Program Files (x86)\BOI\Riskeer 21.1.1.2\Application\Standalone\Deltares\HydraRing-20.1.3.10236’.                                                                                                                                                     	 |
| --file_name    | Verplicht 	 | Link naar de HR_default.csv.                                                                                                                                                     	                                                                                                                                                                                           |


**Let op:** deze regel is vanuit elke directory te runnen, je hoeft dus niet eerst naar een bepaalde folder te gaan.


Om meer informatie over de code te krijgen, gebruik je: 
``` python -m preprocessing overflow --help. ```

### Voorbeeld invoer: 
```
python -m preprocessing overflow --work_dir c:\VRM\test_hydraring_workflow_wdod\overslag --database_paths "c:\VRM\test_hydraring_workflow_wdod\HR\2023" --database_paths "c:\VRM\test_hydraring_workflow_wdod\HR\2100" --hydraring_path "c:\Program Files (x86)\BOI\Riskeer 21.1.1.2\Application\Standalone\Deltares\HydraRing-20.1.3.10236" --file_name “c:\VRM\test_hydraring_workflow_wdod\HR_default.csv”
```