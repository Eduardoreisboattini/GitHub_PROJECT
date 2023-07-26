import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import exponnorm

K = 2
data_emg = np.random.exponnorm(K, size=1000)

plt.hist(data_emg, bins=30, density=True, alpha=0.6, color='magenta')
x = np.linspace(0, 10, 100)
plt.plot(x, exponnorm.pdf(x, K), 'r', label='PDF')
plt.title('Exponentially Modified Gaussian Distribution')
plt.legend()
plt.show()
