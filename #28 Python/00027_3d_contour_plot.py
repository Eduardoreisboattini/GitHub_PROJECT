import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function for the surface
def surface_func(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# Define the gradient function
def gradient_func(x, y):
    grad_x = 2 * x * np.cos(np.sqrt(x**2 + y**2)) / np.sqrt(x**2 + y**2)
    grad_y = 2 * y * np.cos(np.sqrt(x**2 + y**2)) / np.sqrt(x**2 + y**2)
    grad_z = np.ones_like(x)  # Constant gradient in the z-direction
    return grad_x, grad_y, grad_z

# Generate sample data
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = surface_func(X, Y)

# Calculate the gradient vectors
U, V, W = gradient_func(X, Y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Plot the gradient vectors
ax.quiver(X, Y, Z, U, V, W, length=0.3, color='red')

# Set labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Gradient Vectors 3D Graphic')

# Show the plot
plt.show()
