from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd

# Função para realizar análise preditiva
def realizar_analise_preditiva(arquivo, feature_col, target_col):
    try:
        # Carregue e explore seu conjunto de dados
        df = pd.read_csv(arquivo)

        # Examine as primeiras linhas do conjunto de dados para entender sua estrutura
        print("Primeiras linhas do conjunto de dados:")
        print(df.head())

        # Divida o conjunto de dados em features (X) e target (y)
        X = df[[feature_col]]
        y = df[target_col]

        # Divida o conjunto de dados em treinamento e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Crie e treine um modelo preditivo (usando regressão linear como exemplo)
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Faça previsões no conjunto de teste
        predictions = model.predict(X_test)

        # Avalie o desempenho do modelo (usando erro médio quadrático como exemplo)
        mse = mean_squared_error(y_test, predictions)
        print(f"\nErro Médio Quadrático (MSE): {mse}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado. Verifique o caminho do arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

# Substitua 'seu_arquivo.csv', 'feature_column' e 'target_column' pelos valores reais
arquivo_dados_preditivos = 'seu_arquivo.csv'
feature_column = 'feature_column'
target_column = 'target_column'

# Realize a análise preditiva
realizar_analise_preditiva(arquivo_dados_preditivos, feature_column, target_column)
