import pandas as pd
import pyodbc

# Configurações de conexão
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=servidor_nome;'
                      'DATABASE=nome_banco_dados;'
                      'UID=usuario;'
                      'PWD=senha')

# Consulta SQL
query = "SELECT * FROM tabela_exemplo"

# Carregar os dados no DataFrame do Pandas
data = pd.read_sql(query, conn)

# Exibir as primeiras linhas dos dados
print(data.head())
