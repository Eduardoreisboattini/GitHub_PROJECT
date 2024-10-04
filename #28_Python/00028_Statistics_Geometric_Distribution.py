import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom

p = 0.3
data_geometric = np.random.geometric(p, 1000)

plt.hist(data_geometric, bins=15, density=True, alpha=0.6, color='brown')
x = np.arange(1, 15)
plt.vlines(x, 0, geom.pmf(x, p), colors='r', lw=5, alpha=0.5)
plt.title('Geometric Distribution')
plt.show()
