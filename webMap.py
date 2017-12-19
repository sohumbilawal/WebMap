import folium
import pandas

volData = pandas.read_csv("Volcanoes_USA.txt")

lats = list(volData["LAT"])
lons = list(volData["LON"])

elev = list(volData["ELEV"])

def elevCol(elevation):
    if elevation < 1000.0:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

myMap=folium.Map(location = [34.094156, -118.341796], zoom_start=5, tiles = "Mapbox Bright")

featGrp = folium.FeatureGroup(name = "My Map")

for lat, lon, el in zip(lats, lons, elev):
    featGrp.add_child(folium.Marker(location=[lat, lon], popup = str(el)+" m", icon = folium.Icon(color=elevCol(el))))

myMap.add_child(featGrp)

myMap.save("map1.html")
