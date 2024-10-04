import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cauchy

loc = 0
scale = 1
data_cauchy = np.random.standard_cauchy(1000)

plt.hist(data_cauchy, bins=30, density=True, alpha=0.6, color='green')
x = np.linspace(-10, 10, 100)
plt.plot(x, cauchy.pdf(x, loc, scale), 'r', label='PDF')
plt.title('Cauchy Distribution')
plt.legend()
plt.show()
