import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return x**2 + y**2

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Point at which to find the tangent plane
x0, y0 = 2, 2
z0 = f(x0, y0)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(elev=30, azim=45)
plt.title('Tangent Plane to the Surface')
plt.plot([x0], [y0], [z0], color='red', marker='o')

# Compute the tangent plane
z_tangent = z0 + 4*(X-x0) + 4*(Y-y0)

# Plot the tangent plane
ax.plot_surface(X, Y, z_tangent, alpha=0.6, color='green')
plt.show()
