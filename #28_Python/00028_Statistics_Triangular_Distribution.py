import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import triang

left = 0
mode = 2
right = 5
data_triangular = np.random.triangular(left, mode, right, 1000)


plt.hist(data_triangular, bins=30, density=True, alpha=0.6, color='teal')
x = np.linspace(0, 5, 100)
plt.plot(x, triang.pdf(x, left, mode, right-left), 'r', label='PDF')
plt.title('Triangular Distribution')
plt.legend()
plt.show()
