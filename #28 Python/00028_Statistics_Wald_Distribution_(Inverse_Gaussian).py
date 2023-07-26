import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import invgauss

mean = 2
scale = 1
data_invgauss = np.random.invgauss(mean, scale, 1000)

plt.hist(data_invgauss, bins=30, density=True, alpha=0.6, color='orange')
x = np.linspace(0, 10, 100)
plt.plot(x, invgauss.pdf(x, mean, scale), 'r', label='PDF')
plt.title('Inverse Gaussian (Wald) Distribution')
plt.legend()
plt.show()
