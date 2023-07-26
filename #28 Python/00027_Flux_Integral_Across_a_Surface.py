import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def vector_field(x, y, z):
    return x**2, y**2, z**2

# Function representing a surface in 3D
def surface(x, y):
    return 2*x + y - 4

x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)
Z_surface = surface(X, Y)

# Compute the vector field on the surface
U_surface, V_surface, W_surface = vector_field(X, Y, Z_surface)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z_surface, alpha=0.5)
ax.quiver(X, Y, Z_surface, U_surface, V_surface, W_surface, length=0.1, normalize=True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Flux Integral Across a Surface')

# Compute the normal vector to the surface
n_x = 2
n_y = 1
n_z = -1

# Compute the flux integral across the surface
flux_integral = np.sum(U_surface * n_x + V_surface * n_y + W_surface * n_z)

plt.text(0.8, 0.8, 0.8, f'Flux Integral = {flux_integral:.2f}', fontsize=12)
plt.show()
