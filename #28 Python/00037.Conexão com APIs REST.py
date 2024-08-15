import requests
import pandas as pd

# URL da API
url = "https://api.exemplo.com/dados"

# Fazendo a solicitação GET
response = requests.get(url)

# Convertendo a resposta JSON para um DataFrame do Pandas
data = pd.json_normalize(response.json())

# Exibindo as primeiras linhas do DataFrame
print(data.head())