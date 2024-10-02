import folium
# Create a map centered around a specific location
my_map = folium.Map(location=[-23.2237, -45.9009], zoom_start=12)
# Save the map to an HTML file
my_map.save("my_map.html")