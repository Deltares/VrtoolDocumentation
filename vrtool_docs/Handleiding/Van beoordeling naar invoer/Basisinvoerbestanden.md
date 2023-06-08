# Basisinvoerbestanden

Er zijn XX basisinvoerbestanden die hieronder worden toegelicht.

## Vullen van een invoerbestand voor vakindeling
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


## Vullen van een invoerbestand voor Hydra-Ring

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


### Automatisch genereren van invoer voor Hydra-Ring berekeningen


## Vullen van een invoerbestand voor Piping

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


