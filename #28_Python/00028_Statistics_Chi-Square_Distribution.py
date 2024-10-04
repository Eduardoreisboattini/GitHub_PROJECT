import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

df = 5
data_chi2 = np.random.chisquare(df, 1000)

plt.hist(data_chi2, bins=30, density=True, alpha=0.6, color='gray')
x = np.linspace(0, 30, 100)
plt.plot(x, chi2.pdf(x, df), 'r', label='PDF')
plt.title('Chi-Square Distribution')
plt.legend()
plt.show()