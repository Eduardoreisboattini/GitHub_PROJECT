# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np

def criar_dataframe():
    """
    Cria um DataFrame fictício com informações de idade e salário.

    Returns:
    pd.DataFrame: O DataFrame criado.
    """
    dados = {'Idade': [25, 30, 35, 40, 45],
             'Salario': [50000, 60000, 75000, 90000, 80000]}
    df = pd.DataFrame(dados)
    return df

def exibir_dataframe(df):
    """
    Exibe o DataFrame para visualização.

    Parameters:
    df (pd.DataFrame): O DataFrame a ser exibido.
    """
    print("DataFrame Original:")
    print(df)

def calcular_estatisticas_descritivas(df):
    """
    Calcula e exibe estatísticas descritivas básicas usando Pandas.

    Parameters:
    df (pd.DataFrame): O DataFrame para o qual as estatísticas serão calculadas.
    """
    # Obtendo estatísticas descritivas básicas usando Pandas
    estatisticas_descritivas = df.describe()
    
    # Imprimindo as estatísticas descritivas
    print("\nEstatísticas Descritivas:")
    print(estatisticas_descritivas)

def calcular_medias(df):
    """
    Calcula e exibe a média de cada coluna usando NumPy.

    Parameters:
    df (pd.DataFrame): O DataFrame para o qual as médias serão calculadas.
    """
    # Calculando a média de cada coluna usando NumPy
    media_idade = np.mean(df['Idade'])
    media_salario = np.mean(df['Salario'])
    
    # Imprimindo as médias
    print(f"\nMédia de Idade: {media_idade}")
    print(f"Média de Salário: {media_salario}")

# Função principal
def main():
    # Criar o DataFrame
    df = criar_dataframe()
    
    # Exibir o DataFrame
    exibir_dataframe(df)
    
    # Calcular e exibir estatísticas descritivas
    calcular_estatisticas_descritivas(df)
    
    # Calcular e exibir médias
    calcular_medias(df)

# Executar a função principal se este script for executado diretamente
if __name__ == "__main__":
    main()
