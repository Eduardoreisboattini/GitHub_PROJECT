import matplotlib.pyplot as plt
import numpy as np

temperatura = [25, 28, 30, 32, 35, 38]
vendas_sorvetes = [200, 220, 250, 280, 300, 320]

# Calcula a correlação de Pearson
correlacao = np.corrcoef(temperatura, vendas_sorvetes)[0, 1]

# Cria o gráfico de dispersão
plt.scatter(temperatura, vendas_sorvetes, color='blue')
plt.title(f'Correlação de Pearson: {correlacao:.2f}')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Vendas de Sorvetes (unidades)')
plt.show()