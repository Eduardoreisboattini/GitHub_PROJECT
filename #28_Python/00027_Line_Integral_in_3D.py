import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y, z):
    return x**2 + y**2 + z**2

def line_integral(t_values):
    x = np.cos(t_values)
    y = np.sin(t_values)
    z = np.sin(2*t_values)
    return np.sqrt(x**2 + y**2 + z**2)

t = np.linspace(0, 2*np.pi, 100)
X, Y, Z = np.cos(t), np.sin(t), np.sin(2*t)
T_values = np.linspace(0, 2*np.pi, 100)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(X, Y, Z, label='Curve in 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Line Integral in 3D')

line_integral_values = line_integral(T_values)
integral_point = np.array([X[-1], Y[-1], Z[-1]])

ax.plot([X[0]], [Y[0]], [Z[0]], color='red', marker='o', markersize=5)
ax.plot(X, Y, Z, color='blue')
ax.plot([integral_point[0]], [integral_point[1]], [integral_point[2]], color='red', marker='o', markersize=5)
ax.plot(X, Y, line_integral_values, color='green')

# Create a ribbon connecting the curve to the surface
verts = [(X[i], Y[i], Z[i]) for i in range(len(X))] + [(X[i], Y[i], line_integral_values[i]) for i in range(len(X))]
ax.plot([X[0], X[-1]], [Y[0], Y[-1]], [Z[0], Z[-1]], color='blue')
ax.plot([X[0], X[-1]], [Y[0], Y[-1]], [line_integral_values[0], line_integral_values[-1]], color='green')

ribbon_collection = Poly3DCollection([verts], color='gray', alpha=0.3)
ax.add_collection3d(ribbon_collection)

plt.legend()
plt.show()
