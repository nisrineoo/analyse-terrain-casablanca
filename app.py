import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Analyse Terrains Casablanca", layout="wide")

st.title("Application IA - Analyse de Terrains à Casablanca")

st.markdown("Cette application vous aide à visualiser et évaluer le potentiel foncier à Casablanca pour des investissements immobiliers.")

@st.cache_data
def load_data():
    data = pd.read_csv("data/terrains_casablanca.csv")
    return data

data = load_data()

st.subheader("Liste des terrains disponibles")
st.dataframe(data)

st.subheader("Carte interactive des terrains")
map_casa = folium.Map(location=[33.5898, -7.6039], zoom_start=12)

for _, row in data.iterrows():
    popup_text = f"""
    <b>{row['Nom Terrain']}</b><br>
    Superficie: {row['Superficie (m²)']} m²<br>
    Prix: {row['Prix demandé (MAD)']:,} MAD
    """
    folium.Marker(
        [row['Latitude'], row['Longitude']],
        popup=popup_text,
        icon=folium.Icon(color="blue")
    ).add_to(map_casa)

st_folium(map_casa, width=1000)
