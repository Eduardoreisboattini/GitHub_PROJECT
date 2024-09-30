# Criação de um mapa básico no folium
m = folium.Map(location=[15,75],  
               zoom_start=5.5, tiles='Stamen Toner')
m.save('map.html')
m
