import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate sample data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Calculate contour lines
cset = ax.contour(X, Y, Z, zdir='z', offset=-2, cmap='coolwarm')
cset = ax.contour(X, Y, Z, zdir='x', offset=-5, cmap='coolwarm')
cset = ax.contour(X, Y, Z, zdir='y', offset=5, cmap='coolwarm')

# Set labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Contour Lines Area Graphic')

# Show the plot
plt.show()