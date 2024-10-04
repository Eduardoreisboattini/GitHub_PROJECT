from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Carregar dados
data = pd.read_csv('dados.csv')

# Preparação dos dados
X = data.drop('target', axis=1)
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Treinamento de modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Previsão e adição ao DataFrame
data['previsao'] = model.predict(X)

# Exibindo as primeiras linhas com as previsões
print(data.head())