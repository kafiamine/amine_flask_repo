
build:


#une cible "prepare" qui fasse l'instalation des dependances du projet 

prepare:
	pipenv install


#TODO: ajouter une cible "test" qui teste la qualité du projet (et plante sinon)

test:
	pipenv run pylint *.py
