import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rayleigh

scale = 1
data_rayleigh = np.random.rayleigh(scale, 1000)

plt.hist(data_rayleigh, bins=30, density=True, alpha=0.6, color='teal')
x = np.linspace(0, 5, 100)
plt.plot(x, rayleigh.pdf(x, scale), 'r', label='PDF')
plt.title('Rayleigh Distribution')
plt.legend()
plt.show()
