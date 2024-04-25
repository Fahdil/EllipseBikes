import requests as req


#recuperation de la liste des contrat
def list_contracts(api_key):
    # Requête pour accéder à la liste des contrats
    url = f"https://api.jcdecaux.com/vls/v3/contracts?apiKey={api_key}"
    
    try:
        # Récupération de la réponse
        response = req.get(url, timeout=10)
         
        if response.status_code == 200:
            # Affichage du contenu de la réponse sous forme de liste avec JSON
            contenu_reponse = response.json()
            return contenu_reponse
        else:
            # Affichage de message d'erreur
            print(f"Erreur: {response.status_code}")
            return None
    except req.RequestException as e:
        # Gestion des exceptions liées à la requête
        print(f"Erreur de requête: {e}")
        return None
    
#recuperation de la liste des stations
def list_stations(api_key):
    
    #requete pour acceder a la liste des contrats
    url = f"https://api.jcdecaux.com/vls/v3/stations?apiKey={api_key}"
    
    #recuperation de la reponse
    reponse = req.get(url, timeout=10)
    
    try:
        if reponse.status_code == 200:
            #affichage du contenu de la reponse sous forme de list avec Json
            contenu_reponse = reponse.json()
            return contenu_reponse
        else:
            #Affichage de message d'erreur
            print(reponse.status_code)
            return None
    except req.RequestException as e:
        # Gestion des exceptions liées à la requête
        print(f"Erreur de requête: {e}")
        return None
    
    
#recuperation de la liste des stations d'un contract
def list_stations_cntract(contract_name, api_key):
    
    #requete pour acceder a la liste des contrats
    url = f"https://api.jcdecaux.com/vls/v3/stations?contract={contract_name}&apiKey={api_key}"
    
    #recuperation de la reponse
    reponse = req.get(url)
    try:
        if reponse.status_code == 200:
            #affichage du contenu de la reponse sous forme de list avec Json
            contenu_reponse = reponse.json()
            return contenu_reponse
        else:
            #Affichage de message d'erreur
            print( reponse.status_code)
            return None
    except req.RequestException as e:
        # Gestion des exceptions liées à la requête
        print(f"Erreur de requête: {e}")
        return None


#Fonction pour recuperer les datas 

def get_datas(api_key, contract_name):

    #variable url permettand d'implementer la requete HTTP
    url = f"https://api.jcdecaux.com/vls/v1/stations?contract={contract_name}&apiKey={api_key}"

    # recuperation de la reponse 
    reponse = req.get(url)

    if reponse.status_code == 200:
        #affichage du contenu de la reponse sous forme de list avec Json
        contenu_reponse = reponse.json()
        return contenu_reponse
    else:
        #Affichage de message d'erreur
        print(reponse.status_code)
        return None

    