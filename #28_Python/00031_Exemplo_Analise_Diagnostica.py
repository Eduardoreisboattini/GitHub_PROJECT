# Importe as bibliotecas necessárias
import pandas as pd

def realizar_analise_diagnostica(arquivo, evento_especifico):
    try:
        # Carregue e explore seu conjunto de dados
        df = pd.read_csv(arquivo)

        # Examine as primeiras linhas do conjunto de dados para entender sua estrutura
        print("Primeiras linhas do conjunto de dados:")
        print(df.head())

        # Identifique as causas de um evento específico
        dados_evento_especifico = df[df['Evento'] == evento_especifico]

        # Exiba informações sobre o evento específico
        print(f"\nInformações sobre o evento '{evento_especifico}':")
        print(dados_evento_especifico)

        # Estatísticas descritivas para o evento específico
        estatisticas_evento = dados_evento_especifico.describe()
        print(f"\nEstatísticas descritivas para o evento '{evento_especifico}':")
        print(estatisticas_evento)

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado. Verifique o caminho do arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

# Substitua 'seu_arquivo.csv' pelo nome do seu arquivo de dados
arquivo_dados = 'seu_arquivo.csv'

# Permita que o usuário forneça dinamicamente o evento específico
evento_especifico = input("Digite o nome do evento específico que deseja analisar: ")

# Realize a análise diagnóstica
realizar_analise_diagnostica(arquivo_dados, evento_especifico)
