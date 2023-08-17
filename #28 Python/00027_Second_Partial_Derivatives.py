import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return x**2 + y**3 - 3*x*y

def d2f_dx2(x, y):
    return 2 - 3*y

def d2f_dy2(x, y):
    return -6*x

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
plt.title('Function: f(x, y) = x^2 + y^3 - 3xy')

d2f_dx2_values = d2f_dx2(X, Y)
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, d2f_dx2_values, cmap='viridis')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('d^2f/dx^2')
plt.title('Second Partial Derivative d^2f/dx^2')
plt.show()