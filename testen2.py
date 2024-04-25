import folium

import webbrowser

def addToMap(stations_data):
    # Créer une carte centrée sur une position initiale
    mymap = folium.Map(location=[45.774204, 4.867512], zoom_start=14)
    

    # Ajouter les stations à la carte en utilisant des marqueurs
    for station in stations_data:
        latitude = station['position']['latitude']
        longitude = station['position']['longitude']
        bikes_available = station['totalStands']['availabilities']['bikes']
        stands_available = station['totalStands']['availabilities']['stands']
        velo_eletrique = station['totalStands']['availabilities']['electricalBikes']
        velo_mecanique = station['totalStands']['availabilities']['mechanicalBikes']


        # Déterminer la couleur de l'icône en fonction du statut de la station
        icon_color = 'blue' if station['status'] == 'OPEN' else 'red'

        # Ajouter un marqueur pour chaque station
        folium.Marker(
            location=[latitude, longitude],
            popup=f"<b>{station['name']}</b><br>Nombre de vélos disponibles: {bikes_available}<br>Nombre d'emplacements disponibles: {stands_available} <br>Nombre de velo eletrique: {velo_eletrique} <br>Nombre de velo eletrique: {velo_mecanique}",
            icon=folium.Icon(color=icon_color)
        ).add_to(mymap)

    
    # Sauvegarder la carte dans un fichier HTML
    mymap.save("stations_map.html")
    #ouverture du fichier dans le navigateur
    webbrowser.open_new_tab("stations_map.html")
