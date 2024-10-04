import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

shape = 2
scale = 2
data_gamma = np.random.gamma(shape, scale, 1000)

plt.hist(data_gamma, bins=30, density=True, alpha=0.6, color='cyan')
x = np.linspace(0, 15, 100)
plt.plot(x, gamma.pdf(x, shape, scale=scale), 'r', label='PDF')
plt.title('Gamma Distribution')
plt.legend()
plt.show()
