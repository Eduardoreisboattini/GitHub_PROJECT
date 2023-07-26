import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(u, v):
    return u, v, u**2 + v**2

u = np.linspace(-5, 5, 100)
v = np.linspace(-5, 5, 100)
U, V = np.meshgrid(u, v)
X, Y, Z = f(U, V)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Parametric Surface Plot: z = x^2 + y^2')
plt.show()
