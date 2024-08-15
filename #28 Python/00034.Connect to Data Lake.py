# Importando as bibliotecas necessárias
from azure.storage.blob import BlobServiceClient
import pandas as pd
import io

# Configurações de conexão ao Data Lake
# Substitua os valores abaixo pelas suas próprias credenciais e informações
connection_string = "SUA_STRING_DE_CONEXAO"  # String de conexão ao Data Lake
container_name = "NOME_DO_CONTAINER"  # Nome do container no Data Lake
blob_name = "CAMINHO/DO/ARQUIVO.csv"  # Caminho do arquivo dentro do container

# Criando um cliente de serviço de Blob
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Criando um cliente de blob para acessar o arquivo específico
blob_client = blob_service_client.get_blob_client(container_name, blob_name)

# Baixando o conteúdo do blob (arquivo)
blob_data = blob_client.download_blob().readall()

# Convertendo os dados para um DataFrame do Pandas
# Aqui, estamos assumindo que o arquivo é um CSV; ajuste conforme necessário para outros formatos
data = pd.read_csv(io.BytesIO(blob_data))

# Exibindo as primeiras linhas do DataFrame para verificar os dados
print(data.head())

# Salvando o DataFrame em um arquivo CSV local (ou em outro formato que o Power BI suporte)
output_path = "dados_exportados.csv"
data.to_csv(output_path, index=False)

print(f"Dados salvos em: {output_path}")
