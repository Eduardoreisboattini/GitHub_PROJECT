import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return np.exp(-x**2 - y**2)

def directional_derivative(x, y, dx, dy):
    df_dx = -2*x*np.exp(-x**2 - y**2)
    df_dy = -2*y*np.exp(-x**2 - y**2)
    return df_dx*dx + df_dy*dy

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Directional Derivative')
plt.show()

# Compute and plot the directional derivative at a point
x0, y0 = 1, 1
dx, dy = 0.5, 0.5
z0 = f(x0, y0)
directional_deriv = directional_derivative(x0, y0, dx, dy)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Directional Derivative')
ax.plot([x0], [y0], [z0], color='red', marker='o')
ax.quiver(x0, y0, z0, dx, dy, directional_deriv, color='green')
plt.show()
