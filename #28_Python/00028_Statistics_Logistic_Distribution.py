import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import logistic

loc = 0
scale = 1
data_logistic = np.random.logistic(loc, scale, 1000)

plt.hist(data_logistic, bins=30, density=True, alpha=0.6, color='purple')
x = np.linspace(-5, 5, 100)
plt.plot(x, logistic.pdf(x, loc, scale), 'r', label='PDF')
plt.title('Logistic Distribution')
plt.legend()
plt.show()