import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def vector_field(x, y, z):
    return -y, x, z

x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
z = np.linspace(-2, 2, 10)
X, Y, Z = np.meshgrid(x, y, z)

U, V, W = vector_field(X, Y, Z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, U, V, W, length=0.2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Vector Field: Divergence')

# Compute the divergence of the vector field
divergence = U + V + W

# Plot the divergence as a separate surface
ax.plot_surface(X, Y, Z, facecolors=plt.cm.plasma(divergence))
plt.colorbar(mappable=plt.cm.ScalarMappable(cmap=plt.cm.plasma), label='Divergence')
plt.show()
