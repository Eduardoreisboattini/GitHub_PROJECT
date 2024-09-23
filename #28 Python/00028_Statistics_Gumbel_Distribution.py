import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gumbel_r

loc = 0
scale = 1
data_gumbel = np.random.gumbel(loc, scale, 1000)

plt.hist(data_gumbel, bins=30, density=True, alpha=0.6, color='brown')
x = np.linspace(-5, 5, 100)
plt.plot(x, gumbel_r.pdf(x, loc, scale), 'r', label='PDF')
plt.title('Gumbel Distribution')
plt.legend()
plt.show()