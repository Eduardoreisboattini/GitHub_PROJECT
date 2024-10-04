import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2
import geopandas as gpd
from shapely.geometry import LineString
import matplotlib.pyplot as plt

# Função vetorizada para calcular distâncias usando Haversine
def haversine_vectorized(lon1, lat1, lon2, lat2):
    R = 6371  # Raio da Terra em km
    dlon = np.radians(lon2 - lon1)
    dlat = np.radians(lat2 - lat1)
    a = np.sin(dlat / 2) ** 2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return R * c

# O dataset é automaticamente criado pelo Power BI
dataset = dataset.drop_duplicates()

# Exemplo de associação de coordenadas (latitude e longitude) para cada região
coord_map = {
    'Metropolitana': {'Latitude': -23.5505, 'Longitude': -46.6333},
    'Interior': {'Latitude': -20.3155, 'Longitude': -40.3128}
}

# Adicionar colunas de latitude e longitude ao dataframe
dataset['Latitude'] = dataset['Tipo Regiao'].map(lambda x: coord_map.get(x, {'Latitude': np.nan})['Latitude'])
dataset['Longitude'] = dataset['Tipo Regiao'].map(lambda x: coord_map.get(x, {'Longitude': np.nan})['Longitude'])

# Criar o GeoDataFrame
gdf = gpd.GeoDataFrame(dataset, geometry=gpd.points_from_xy(dataset.Longitude, dataset.Latitude))

# Vetorize o cálculo de distâncias
longitudes = gdf['Longitude'].values
latitudes = gdf['Latitude'].values
dist_matrix = np.zeros((len(gdf), len(gdf)))

for i in range(len(gdf)):
    dist_matrix[i, :] = haversine_vectorized(longitudes[i], latitudes[i], longitudes, latitudes)

# Encontrar os pares mais próximos
np.fill_diagonal(dist_matrix, np.inf)  # Ignorar distâncias para o mesmo ponto
min_distance = np.min(dist_matrix)
closest_points = np.where(dist_matrix == min_distance)

# Criar linhas entre os aliados mais próximos
lines = []
for i, j in zip(*closest_points):
    point1 = gdf.iloc[i].geometry
    point2 = gdf.iloc[j].geometry
    line = LineString([point1, point2])
    lines.append(line)

gdf_lines = gpd.GeoDataFrame(geometry=lines)

# Plotar o mapa com as linhas
fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax, color='blue', markersize=50, label='Aliados')
gdf_lines.plot(ax=ax, color='red', linewidth=2, label='Distâncias Mais Próximas')

# Adicionar legendas e título
ax.legend()
ax.set_title('Mapa de Aliados e Distâncias Mais Próximas')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# Salvar o gráfico como uma imagem
output_image = 'output_map.png'
plt.savefig(output_image)

# Fechar a figura
plt.close()

print(f"Imagem do gráfico salva como {output_image}.")
