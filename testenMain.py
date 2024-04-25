from testen import get_datas
from testen import list_stations


   
def main():
    #api_key
    api_key = 'e0a1bf2c844edb9084efc764c089dd748676cc14'
    contract_name = 'nantes'
    
    #On test la conexion à l'api de jcdecaux
 
    try:
        data= get_datas(api_key, contract_name)
        
        if data: #si la connexion fonctionne  alors
        
                # on Récupére la liste des stations
                stations = list_stations(api_key)
                
                from testen2 import addToMap        
                addToMap(stations)
        else:
            #Affichage de message d'erreur
            print("Impossible de se connecter à l'API")
            return None
    except Exception as e:
        # Gestion des exceptions liées à la requête
        print(f"Erreur de requête: {e}")
        return None

            
if __name__ == "__main__":
    main() 