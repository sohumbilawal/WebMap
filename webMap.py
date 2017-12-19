import folium
import pandas

volData = pandas.read_csv("Volcanoes_USA.txt")

lats = list(volData["LAT"])
lons = list(volData["LON"])

myMap=folium.Map(location = [34.094156, -118.341796], zoom_start=11, tiles = "Mapbox Bright")

featGrp = folium.FeatureGroup(name = "My Map")

for lat, lon in zip(lats, lons):
    featGrp.add_child(folium.Marker(location=[lat, lon], popup = "Hi! I am a Marker", icon = folium.Icon(color='green')))

myMap.add_child(featGrp)

myMap.save("map1.html")
