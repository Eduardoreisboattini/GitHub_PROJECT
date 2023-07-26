import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return x**3 - 3*x + y**3 - 3*y

def df_dx(x, y):
    return 3*x**2 - 3

def df_dy(x, y):
    return 3*y**2 - 3

def d2f_dx2(x, y):
    return 6*x

def d2f_dy2(x, y):
    return 6*y

def d2f_dxdy(x, y):
    return 0

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
plt.title('Function: f(x, y) = x^3 - 3x + y^3 - 3y')

d2f_dx2_values = d2f_dx2(X, Y)
d2f_dy2_values = d2f_dy2(X, Y)
d2f_dxdy_values = d2f_dxdy(X, Y)

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, d2f_dx2_values, cmap='plasma', alpha=0.8)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('d^2f/dx^2')
plt.title('Second Partial Derivative d^2f/dx^2')

plt.show()

fig3 = plt.figure(figsize=(12, 5))
ax3 = fig3.add_subplot(121, projection='3d')
ax3.plot_surface(X, Y, d2f_dy2_values, cmap='plasma', alpha=0.8)
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('d^2f/dy^2')
plt.title('Second Partial Derivative d^2f/dy^2')

ax4 = fig3.add_subplot(122, projection='3d')
ax4.plot_surface(X, Y, d2f_dxdy_values, cmap='plasma', alpha=0.8)
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('d^2f/dxdy')
plt.title('Second Mixed Partial Derivative d^2f/dxdy')

plt.show()
