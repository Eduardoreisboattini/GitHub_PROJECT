/*************  ✨ Codeium Command ⭐  *************/
import geopandas as gpd
import folium

# Create a base map
m = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)  # Centered around São Paulo

# Add a marker for Morumbi Stadium
folium.Marker(
    location=[-23.600781655693297, -46.72005013426793],
    popup="Morumbi - Estádio do Tetra Campeão Da Libertadores 2024 - SPFC - Tri-Campeão Mundial - 92-93-05"
).add_to(m)

# Add a marker for Allianz Parque
folium.Marker(
    location=[-23.527374755405372, -46.67835891788951],
    popup="Allianz Parque - O Estádio alugado do time que ainda busca o mundial"
).add_to(m)

# Display the map
m