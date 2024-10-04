import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Criação dos dados paramétricos
t = np.linspace(0, 20 * np.pi, 1000)  # Vetor de tempo
x = np.cos(t)  # Coordenada x
y = np.sin(t)  # Coordenada y
z = t  # Coordenada z

# Criação da figura
fig = plt.figure()

# Adição do gráfico 3D
ax = fig.add_subplot(111, projection='3d')

# Plotagem da hélice 3D
ax.plot(x, y, z)

# Configurações dos rótulos dos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Título do gráfico
plt.title('3D Parametric Plot: Helix')

# Exibição do gráfico
plt.show()