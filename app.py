
import streamlit as st
import folium
from streamlit_folium import st_folium
import json

# Charger les données GeoJSON depuis le fichier
with open("geojson_terrains_casablanca.json", "r") as f:
    geojson_data = json.load(f)

# Fonction pour attribuer une couleur à chaque type de terrain
def style_function(feature):
    terrain_type = feature["properties"]["type"]
    color_map = {
        "bâti": "red",
        "non bâti": "green",
        "industriel": "blue",
        "sportif": "purple",
        "agricole devenu urbain": "brown"
    }
    return {
        "fillColor": color_map.get(terrain_type, "gray"),
        "color": color_map.get(terrain_type, "gray"),
        "fillOpacity": 0.6,
        "weight": 1
    }

# Création de la carte
m = folium.Map(location=[33.589886, -7.603869], zoom_start=12, tiles="CartoDB positron")

# Ajout des terrains à la carte
folium.GeoJson(
    geojson_data,
    style_function=style_function,
    tooltip=folium.features.GeoJsonTooltip(
        fields=["lot", "type", "prix_marche", "prix_fiscal", "note", "batiment_existant", "plan_amenagement"],
        aliases=["Lot", "Type", "Prix du marché", "Prix fiscal", "Note", "Bâtiment existant", "Plan d'aménagement"],
        localize=True
    )
).add_to(m)

# Interface utilisateur
st.title("Carte interactive des terrains à Casablanca")
st.write("Chaque terrain est coloré selon sa catégorie. Cliquez dessus pour voir les détails.")
st_folium(m, width=800, height=600)
