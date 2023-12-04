import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Gerando dados aleatórios para a demonstração
np.random.seed(42)
X = 2 * np.random.rand(20, 1)
Y = 3 * X + 1 + np.random.randn(20, 1)

# Criando um modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X, Y)

# Realizando previsões
Y_pred = modelo.predict(X)

# Calculando o R^2
r2 = r2_score(Y, Y_pred)

# Plotando os pontos de dados e a linha de regressão
plt.scatter(X, Y, label='Pontos de Dados')
plt.plot(X, Y_pred, color='red', label=f'Linha de Regressão\nR^2 = {r2:.2f}')
plt.xlabel('X (Variável Independente)')
plt.ylabel('Y (Variável Dependente)')
plt.title('Regressão Linear com Linha de Tendência')
plt.legend()

# Exibindo o gráfico
plt.show()
