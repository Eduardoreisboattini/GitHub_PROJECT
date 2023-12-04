import random
import numpy as np
from scipy.stats import mode

# Generate a list of 20 random numbers
data = [random.randint(1, 100) for _ in range(20)]

# 1. Mean:
data_mean = np.mean(data)

# 2. Median:
data_median = np.median(data)

# 3. Mode:
data_mode = mode(data).mode[0]

# 4. Standard Deviation:
data_std = np.std(data)

# 5. Variance:
data_var = np.var(data)

# 6. Range:
data_range = np.ptp(data)

# 7. Quartiles:
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

# 8. Interquartile Range (IQR):
iqr = q3 - q1

# Display the statistical summary
print("List of Random Numbers:", data)
print("Mean:", data_mean)
print("Median:", data_median)
print("Mode:", data_mode)
print("Standard Deviation:", data_std)
print("Variance:", data_var)
print("Range:", data_range)
print("Quartiles - Q1:", q1, "Q3:", q3)
print("Interquartile Range (IQR):", iqr)
