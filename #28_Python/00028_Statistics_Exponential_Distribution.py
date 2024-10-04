import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

scale = 2
data_exponential = np.random.exponential(scale, 1000)

plt.hist(data_exponential, bins=30, density=True, alpha=0.6, color='purple')
x = np.linspace(0, 10, 100)
plt.plot(x, expon.pdf(x, scale=scale), 'r', label='PDF')
plt.title('Exponential Distribution')
plt.legend()
plt.show()
