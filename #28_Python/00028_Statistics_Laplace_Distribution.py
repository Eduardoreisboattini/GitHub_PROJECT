import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import laplace

loc = 0
scale = 1
data_laplace = np.random.laplace(loc, scale, 1000)

plt.hist(data_laplace, bins=30, density=True, alpha=0.6, color='green')
x = np.linspace(-5, 5, 100)
plt.plot(x, laplace.pdf(x, loc, scale), 'r', label='PDF')
plt.title('Laplace Distribution')
plt.legend()
plt.show()
