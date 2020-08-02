import folium
import pandas

data=pandas.read_csv("volcanoes.txt")


lat=list(data["LAT"])
lon=list(data["LON"])
elv=list(data["ELEV"])

def colour_elevation(elevation):
    if elevation <1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


html = """<h4>Volcano information:</h4>
Height: %s m
"""

map=folium.Map(location=[38.88, -99.99], zoom_start=6, titles="Stamen Terrain")

fg= folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in  zip(lat, lon, elv):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius =6, popup=folium.Popup(iframe),
    fill_color=colour_elevation(el),color="grey", fill=True, fill_opacity=0.7))


fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map.html")
