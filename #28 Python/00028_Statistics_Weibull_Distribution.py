import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

c = 2
data_weibull = np.random.weibull(c, 1000)

plt.hist(data_weibull, bins=30, density=True, alpha=0.6, color='purple')
x = np.linspace(0, 5, 100)
plt.plot(x, weibull_min.pdf(x, c), 'r', label='PDF')
plt.title('Weibull Distribution')
plt.legend()
plt.show()
