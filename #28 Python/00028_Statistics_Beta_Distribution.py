import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

alpha = 2
beta = 5
data_beta = np.random.beta(alpha, beta, 1000)

plt.hist(data_beta, bins=30, density=True, alpha=0.6, color='blue')
x = np.linspace(0, 1, 100)
plt.plot(x, beta.pdf(x, alpha, beta), 'r', label='PDF')
plt.title('Beta Distribution')
plt.legend()
plt.show()