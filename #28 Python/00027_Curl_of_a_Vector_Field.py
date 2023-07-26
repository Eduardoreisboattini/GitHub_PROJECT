import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def vector_field(x, y, z):
    return np.cos(y), np.sin(z), np.sin(x)

x = np.linspace(-2*np.pi, 2*np.pi, 20)
y = np.linspace(-2*np.pi, 2*np.pi, 20)
z = np.linspace(-2*np.pi, 2*np.pi, 20)
X, Y, Z = np.meshgrid(x, y, z)

U, V, W = vector_field(X, Y, Z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, U, V, W, length=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Vector Field: Curl')

# Compute the curl of the vector field
curl_x = np.zeros_like(X)
curl_y = np.zeros_like(Y)
curl_z = np.zeros_like(Z)

for i in range(1, X.shape[0]-1):
    for j in range(1, X.shape[1]-1):
        for k in range(1, X.shape[2]-1):
            curl_x[i, j, k] = (W[i, j+1, k] - W[i, j-1, k]) / (Y[0, 1, 0] - Y[0, 0, 0]) - (V[i, j, k+1] - V[i, j, k-1]) / (Z[0, 0, 1] - Z[0, 0, 0])
            curl_y[i, j, k] = (U[i, j, k+1] - U[i, j, k-1]) / (Z[0, 0, 1] - Z[0, 0, 0]) - (W[i+1, j, k] - W[i-1, j, k]) / (X[1, 0, 0] - X[0, 0, 0])
            curl_z[i, j, k] = (V[i+1, j, k] - V[i-1, j, k]) / (X[1, 0, 0] - X[0, 0, 0]) - (U[i, j+1, k] - U[i, j-1, k]) / (Y[0, 1, 0] - Y[0, 0, 0])

# Plot the curl as a separate surface
curl_magnitude = np.sqrt(curl_x**2 + curl_y**2 + curl_z**2)
ax.plot_surface(X, Y, Z, facecolors=plt.cm.plasma(curl_magnitude))
plt.colorbar(mappable=plt.cm.ScalarMappable(cmap=plt.cm.plasma), label='Curl Magnitude')
plt.show()
