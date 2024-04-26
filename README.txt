
Le développement du projet comprend 6 fichiers dont 4 fichier python, 1 fichier javaScript et un fichier HTML pis le fichier actuel

Fichiers Pythons
 
1- Fichier testen
    Ce fichier comporte 4 fonctions dont :

    Fonction pour recuperation de la liste des contrat list_contracts(api_key): prend en parametre la cle api jcdecaux
    Fonction pour recuperation de la liste des stations list_stations(api_key): prend en parametre la cle api jcdecaux
    Fonction pour recuperation de la liste des stations d'un contract list_stations_contract(contract_name, api_key) : prend en parametre la cle api jcdecaux et un nom de contrat
    Fonction pour Fonction pour recuperer les datas d'un contrat get_datas(api_key, contract_name): prend en parametre la cle api jcdecaux et un nom de contrat

2- Fichier testen2
    Ce fichier compoerte la fonction addToMap(stations_data) qui prent en parametre la liste des station afin d'afficher 
    les informations de chaques stations sur une map 
    La map est génerer grace a la bibliotheque folium puis est ouvert dans le navigateur grace a la bibliotheque webbrowser

3- Fichier testenUpdate.js 
    Ce fichier permet d'acceder a l'API de jcdecaux et d'actualiser les informations en popup au click sur une station toutes 
    les 60 secondes grace à sa fonction updateStations()
    Le script est ajjouter a l'entete de la page stations_map.html ne fois generer 

4-Fichier testenMain.py
    Ce fichier est le fichier principal et fait appel aux fontions des fichier testen et testen2

5- Fichier testenStatic.py
    Ce fichier utilise les documents js du dossier Station_info_Json afin d'afficher toutes les stations 
    grace a la bibliotheque folium

6- Fichier stations_map.html qui est generer site a l'execution du programme

