import pandas as pd
import folium

# Load your data
data = pd.read_csv(
    'C:/Users/Eduardo Boattini/Documents/09.SET/23 09 2024 - Inteligencia de Dados/MAPA/dados.csv'
)

# Print column names to verify
print(data.columns)

# Strip any leading/trailing spaces from column names
data.columns = data.columns.str.strip()

# Plot the data
m = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=10)
for index, row in data.iterrows():
    folium.CircleMarker(location=[row['Latitude'], row['Longitude']], radius=1, color='blue').add_to(m)

m