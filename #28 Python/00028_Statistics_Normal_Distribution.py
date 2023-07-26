import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, uniform, expon, poisson

# Example 1: Normal Distribution (Gaussian Distribution)
mean = 0
std_dev = 1
data_normal = np.random.normal(mean, std_dev, 1000)

plt.hist(data_normal, bins=30, density=True, alpha=0.6, color='g')
x = np.linspace(-5, 5, 100)
plt.plot(x, norm.pdf(x, mean, std_dev), 'r', label='PDF')
plt.title('Normal Distribution')
plt.legend()
plt.show()

# Example 2: Uniform Distribution
low = 0
high = 10
data_uniform = np.random.uniform(low, high, 1000)

plt.hist(data_uniform, bins=30, density=True, alpha=0.6, color='b')
x = np.linspace(low, high, 100)
plt.plot(x, uniform.pdf(x, low, high-low), 'r', label='PDF')
plt.title('Uniform Distribution')
plt.legend()
plt.show()

# Example 3: Exponential Distribution
scale = 2
data_exponential = np.random.exponential(scale, 1000)

plt.hist(data_exponential, bins=30, density=True, alpha=0.6, color='purple')
x = np.linspace(0, 10, 100)
plt.plot(x, expon.pdf(x, scale=scale), 'r', label='PDF')
plt.title('Exponential Distribution')
plt.legend()
plt.show()

# Example 4: Poisson Distribution
lambda_ = 3
data_poisson = np.random.poisson(lambda_, 1000)

plt.hist(data_poisson, bins=15, density=True, alpha=0.6, color='orange')
x = np.arange(0, 15)
plt.vlines(x, 0, poisson.pmf(x, lambda_), colors='r', lw=5, alpha=0.5)
plt.title('Poisson Distribution')
plt.show()
