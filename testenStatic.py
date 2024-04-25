import folium
import os
import json
import webbrowser

# Chemin vers le dossier contenant les fichiers JSON
dossier = 'Station_info_Json'

def addToMap(dossier):
    # Créer une carte centrée sur une position initiale
    mymap = folium.Map(location=[45.774204, 4.867512], zoom_start=14)
    
    # Ajouter les stations à la carte en utilisant des marqueurs
    for station_file in os.listdir(dossier):
        if station_file.endswith('.json'):  # Vérifier s'il s'agit d'un fichier JSON
            chemin_fichier = os.path.join(dossier, station_file)
            
            try:
                with open(chemin_fichier, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    for station in data:
                        latitude = station.get('latitude')
                        longitude = station.get('longitude')
                        numero = station.get('number')
                    
                        # Vérifier si toutes les propriétés nécessaires existent
                        if latitude is not None and longitude is not None and numero is not None:
                            # Déterminer la couleur de l'icône en fonction du statut de la station
                            icon_color = 'orange'

                            # Ajouter un marqueur pour chaque station
                            folium.Marker(
                                location=[latitude, longitude],
                                popup=f"<b>{station['name']}</b><br>Numero de station: {numero}",
                                icon=folium.Icon(color=icon_color)
                            ).add_to(mymap)
                            
                            
                            
                        else:
                            print(f"Les données de la station dans le fichier {station_file} sont incomplètes.")
            except Exception as e:
                print(f"Une erreur s'est produite lors de la lecture du fichier {station_file}: {e}")
                
    # Sauvegarder la carte dans un fichier HTML
    mymap.save("stations_map_Static.html")
    #ouverture du fichier dans le navigateur
    webbrowser.open_new_tab("stations_map_Static.html")


addToMap(dossier)