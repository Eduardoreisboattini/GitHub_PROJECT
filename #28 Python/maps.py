import pandas as pd
import matplotlib.pyplot as plt

# Load your data
data = pd.read_csv(#+
    'C:/Users/Eduardo Boattini/Documents/09.SET/23 09 2024 - Inteligencia de Dados/MAPA/dados.csv'#+
)#+
# Print column names to verify
print(data.columns)

# Strip any leading/trailing spaces from column names
data.columns = data.columns.str.strip()

# Plot the data
plt.scatter(data['Longitude'], data['Latitude'], s=1)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Aliados no Mapa')
plt.show()