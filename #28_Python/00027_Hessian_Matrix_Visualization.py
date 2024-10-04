import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return x**2 + y**2 + np.exp(-x**2 - y**2)

def hessian(x, y):
    f_xx = 2 - 4*x**2*np.exp(-x**2 - y**2)
    f_xy = -4*x*y*np.exp(-x**2 - y**2)
    f_yy = 2 - 4*y**2*np.exp(-x**2 - y**2)
    return np.array([[f_xx, f_xy], [f_xy, f_yy]])

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

hessian_matrices = np.empty(X.shape + (2, 2))
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        hessian_matrices[i, j] = hessian(X[i, j], Y[i, j])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Hessian Matrix Visualization')

# Choose a point to visualize the Hessian matrix
x0, y0 = 1, 1
z0 = f(x0, y0)
hessian_matrix = hessian(x0, y0)

# Plot the eigenvectors of the Hessian as arrows
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        if (i + j) % 20 == 0:
            eigvals, eigvecs = np.linalg.eig(hessian_matrices[i, j])
            for eigval, eigvec in zip(eigvals, eigvecs.T):
                scale = 0.5 / np.sqrt(eigval)
                ax.quiver(X[i, j], Y[i, j], Z[i, j], scale * eigvec[0], scale * eigvec[1], eigval, color='red')

ax.plot([x0], [y0], [z0], color='red', marker='o', markersize=5)
plt.show()
