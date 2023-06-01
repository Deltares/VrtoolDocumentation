# Aan de slag

## Structuur



## Installatie-instructies

### Miniconda of Anaconda
Om de preprocessing en de VRTOOL te gebruiken is het nodig om [miniconda](https://docs.conda.io/en/latest/miniconda.html) of installed [Anaconda](https://www.anaconda.com/download) te installeren. 
### Preprocessor
De preprocessor bestaat uit een python code die te installeren is via [LINK NAAR PREPROCESSING](link)

### VRTOOL
De VRTOOL bestaat uit een python code die te installeren is via [LINK NAAR VRTOOL](link)



### Dashboard

Het Dashboard bestaat uit een python code die te installeren is via [LINK NAAR Dashboard](link)


## Python environment bouwen

Om miniconda of anaconda te gebruiken om de preprocessing of de VRTOOL te draaien is het belangrijk om een nieuwe python enviroment aan te maken. 

Dit kan door eerst een `environment.yml` file aan te maken met daarin:
```
name: vrtool_env
channels:
  - conda-forge
  - defaults
dependencies:
  - conda-forge::python=3.10
  - conda-forge::openturns=1.19
  - pip
```

En daarna de command window van anaconda of miniconda te openen en de volgende twee commandline te draaien.

1. `conda env create -f environment.yml -p vrtool_env`
2. `conda activate vrtool_env`


**==> Hier ook poetry installatie uitleggen?**