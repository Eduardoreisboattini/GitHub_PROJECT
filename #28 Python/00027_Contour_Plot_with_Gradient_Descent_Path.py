import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return x**2 + y**2

def df(x, y):
    return 2*x, 2*y

def gradient_descent(eta, iterations):
    path = []
    x, y = 4, 4  # Initial point
    for _ in range(iterations):
        path.append((x, y, f(x, y)))
        dx, dy = df(x, y)
        x -= eta * dx
        y -= eta * dy
    return path

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

path = gradient_descent(0.3, 30)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')
ax.view_init(elev=20, azim=30)
plt.title('Contour Plot with Gradient Descent Path')
ax.plot([p[0] for p in path], [p[1] for p in path], [p[2] for p in path], color='red', marker='o')
plt.show()
