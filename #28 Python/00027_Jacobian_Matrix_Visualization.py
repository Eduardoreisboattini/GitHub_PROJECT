import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(u, v):
    return u**2 + 2*v**2

def jacobian(u, v):
    df_du = 2*u
    df_dv = 4*v
    return np.array([df_du, df_dv])

u = np.linspace(-5, 5, 100)
v = np.linspace(-5, 5, 100)
U, V = np.meshgrid(u, v)
Z = f(U, V)

jacobians = np.empty(U.shape + (2,))
for i in range(U.shape[0]):
    for j in range(U.shape[1]):
        jacobians[i, j] = jacobian(U[i, j], V[i, j])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(U, V, Z, cmap='viridis', alpha=0.8)
ax.set_xlabel('U')
ax.set_ylabel('V')
ax.set_zlabel('Z')
plt.title('Jacobian Matrix Visualization')

# Choose a point to visualize the Jacobian matrix
u0, v0 = 2, 2
z0 = f(u0, v0)
jacobian_matrix = jacobian(u0, v0)

# Plot the vectors of the Jacobian matrix as arrows
for i in range(U.shape[0]):
    for j in range(U.shape[1]):
        if (i + j) % 10 == 0:
            ax.quiver(U[i, j], V[i, j], Z[i, j], jacobians[i, j, 0], jacobians[i, j, 1], 0, color='red')

ax.plot([u0], [v0], [z0], color='red', marker='o', markersize=5)
plt.show()
