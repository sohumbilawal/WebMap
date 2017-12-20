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
    featGrp.add_child(folium.CircleMarker(location=[lat, lon], radius = 5,  fill_color=elevCol(el), color = 'black', fill = True, fill_opacity = 0.8, popup = str(el)+" m"))

featGrp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding = 'utf-8-sig').read(), style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

myMap.add_child(featGrp)

myMap.save("map1.html")
