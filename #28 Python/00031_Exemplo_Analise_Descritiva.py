import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para realizar análise descritiva
def realizar_analise_descritiva(arquivo, coluna_alvo):
    try:
        # Carregue seu conjunto de dados
        df = pd.read_csv(arquivo)

        # Examine as primeiras linhas do conjunto de dados para entender sua estrutura
        print("Primeiras linhas do conjunto de dados:")
        print(df.head())

        # Estatísticas descritivas
        estatisticas_resumo = df.describe()
        print("\nEstatísticas descritivas:")
        print(estatisticas_resumo)

        # Visualização da distribuição da coluna alvo
        plt.figure(figsize=(12, 6))

        # Histograma
        plt.subplot(1, 2, 1)
        sns.histplot(df[coluna_alvo], bins=20, kde=True, color='skyblue')
        plt.title(f'Histograma da Coluna {coluna_alvo}')
        plt.xlabel(coluna_alvo)
        plt.ylabel('Frequência')

        # Boxplot
        plt.subplot(1, 2, 2)
        sns.boxplot(x=df[coluna_alvo], color='lightcoral')
        plt.title(f'Boxplot da Coluna {coluna_alvo}')
        plt.xlabel(coluna_alvo)

        plt.tight_layout()
        plt.show()

        # Contagem de valores únicos na coluna alvo
        contagem_valores = df[coluna_alvo].value_counts()
        print(f"\nContagem de valores únicos na coluna {coluna_alvo}:\n{contagem_valores}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado. Verifique o caminho do arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

# Substitua 'seu_arquivo.csv' pelo nome do seu arquivo de dados
arquivo_dados = 'seu_arquivo.csv'

# Permita que o usuário escolha a coluna alvo para a análise descritiva
coluna_alvo = input("Digite o nome da coluna que deseja analisar descritivamente: ")

# Realize a análise descritiva
realizar_analise_descritiva(arquivo_dados, coluna_alvo)
