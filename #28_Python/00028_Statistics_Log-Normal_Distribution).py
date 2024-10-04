import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

sigma = 0.8
data_lognormal = np.random.lognormal(0, sigma, 1000)

plt.hist(data_lognormal, bins=30, density=True, alpha=0.6, color='orange')
x = np.linspace(0, 10, 100)
plt.plot(x, lognorm.pdf(x, sigma), 'r', label='PDF')
plt.title('Log-Normal Distribution')
plt.legend()
plt.show()
