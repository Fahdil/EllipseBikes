// Fonction pour mettre à jour les informations des stations sur la carte
function updateStations() {
    // Effectuer une requête à l'API JCDecaux pour obtenir les informations sur les stations
    fetch('https://api.jcdecaux.com/vls/v3/stations?apiKey=e0a1bf2c844edb9084efc764c089dd748676cc14')
    .then(response => response.json())
    .then(data => {
        // Parcourir les données des stations
        data.forEach(station => {
            console.log(station.name);
            // Mettre à jour les marqueurs sur la carte avec les nouvelles informations
            var marker = markers.find(m => m.stationNumber === station.number);
            if (marker) {
                marker.setPopupContent(`<b>${station.name}</b><br>Nombre de vélos disponibles: ${station.totalStands.availabilities.bikes}<br>Nombre d'emplacements disponibles: ${station.totalStands.availabilities.stands}`);
            }
        });
    });
} 

// Appeler la fonction de mise à jour des stations toutes les 60 secondes
setInterval(updateStations, 60000);
