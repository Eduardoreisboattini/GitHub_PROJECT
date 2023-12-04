import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import powerlaw

a = 2
data_power = np.random.power(a, 1000)

plt.hist(data_power, bins=30, density=True, alpha=0.6, color='magenta')
x = np.linspace(0, 1, 100)
plt.plot(x, powerlaw.pdf(x, a), 'r', label='PDF')
plt.title('c)
plt.legend()
plt.show()
