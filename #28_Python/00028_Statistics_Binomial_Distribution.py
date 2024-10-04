import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 10
p = 0.3
data_binomial = np.random.binomial(n, p, 1000)

plt.hist(data_binomial, bins=11, density=True, alpha=0.6, color='magenta')
x = np.arange(0, 11)
plt.vlines(x, 0, binom.pmf(x, n, p), colors='r', lw=5, alpha=0.5)
plt.title('Binomial Distribution')
plt.show()