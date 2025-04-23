import streamlit as st
import folium
from streamlit_folium import st_folium
geojson_data = {
"type": "FeatureCollection",
"features": [
{
"type": "Feature",
"properties": {"lot": "lot1", "name": "Lot 1", "bati": True},
"geometry": {
"type": "Polygon",
"coordinates": [[
[-7.603869, 33.589886],
[-7.603869, 33.599886],
[-7.593869, 33.599886],
[-7.593869, 33.589886],
[-7.603869, 33.589886]
]]
}
},
{
"type": "Feature",
"properties": {"lot": "lot2", "name": "Lot 2", "bati": False},
"geometry": {
"type": "Polygon",
"coordinates": [[
[-7.613869, 33.579886],
[-7.613869, 33.589886],
[-7.603869, 33.589886],
[-7.603869, 33.579886],
[-7.613869, 33.579886]
]]
}
},
{
"type": "Feature",
"properties": {"lot": "lot3", "name": "Lot 3", "bati": True},
"geometry": {
"type": "Polygon",
"coordinates": [[
[-7.623869, 33.569886],
[-7.623869, 33.579886],
[-7.613869, 33.579886],
[-7.613869, 33.569886],
[-7.623869, 33.569886]
]]
}
}
]
}
def style_function(feature):
if feature["properties"]["bati"]:
return {"fillColor": "green", "color": "green", "fillOpacity": 0.5, "weight": 1}
else:
return {"fillColor": "orange", "color": "orange", "fillOpacity": 0.5, "weight": 1}
m = folium.Map(location=[33.589886, -7.603869], zoom_start=12, tiles="CartoDB positron")
folium.GeoJson(
geojson_data,
style_function=style_function,
tooltip=folium.features.GeoJsonTooltip(fields=["name", "lot", "bati"], aliases=["Nom", "Lot", "Bâti"])
).add_to(m)
st.title("Cartographie des lots de Casablanca")
st.write("Lots bâtis en vert, lots non bâtis en orange.")
st_folium(m, width=800, height=600)
