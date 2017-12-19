import folium
myMap=folium.Map(location = [34.094156, -118.341796], zoom_start=11, tiles = "Mapbox Bright")

featGrp = folium.FeatureGroup(name = "My Map")

for coordinates in [[34.1, -118.3],[36.1, -110.3]]:
    featGrp.add_child(folium.Marker(location=coordinates, popup = "Hi! I am a Marker", icon = folium.Icon(color='green')))

myMap.add_child(featGrp)

myMap.save("map1.html")
