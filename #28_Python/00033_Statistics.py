import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate data following a normal distribution
mu, sigma = 0, 1  # mean and standard deviation
data = np.random.normal(mu, sigma, 1000)

# Create a histogram of the data
count, bins, ignored = plt.hist(data, 30, density=True)

# Plot the probability density function (PDF) of the normal distribution
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='r')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Normal Distribution: Modeling Probability of Outcomes')

# Add a legend
plt.legend(['Normal Distribution', 'Data'])

# Display the plot
plt.show()
