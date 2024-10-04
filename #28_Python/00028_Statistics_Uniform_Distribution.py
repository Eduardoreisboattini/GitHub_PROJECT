import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

lambda_ = 3
data_poisson = np.random.poisson(lambda_, 1000)

plt.hist(data_poisson, bins=15, density=True, alpha=0.6, color='orange')
x = np.arange(0, 15)
plt.vlines(x, 0, poisson.pmf(x, lambda_), colors='r', lw=5, alpha=0.5)
plt.title('Poisson Distribution')
plt.show()
