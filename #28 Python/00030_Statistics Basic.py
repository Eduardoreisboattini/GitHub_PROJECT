# Importing necessary libraries
import numpy as np
from scipy import stats

# Sample data
data = np.array([4390, 	1097, 	1959, 	2729, 	3988, 	2468, 	1214, 	4366, 	4450, 	4162, 	3485, 	3571, 	1172, 	2181, 	1930, 	1282, 	616, 	3171, 	619, 	2037, 	2141, 	3147, 	4571, 	1262, 	4624, 	1436, 	1348, 	1075, 	2040, 	1738, 	2219, 	4838, 	1799, 	3360, 	3069, 	4621, 	4748, 	4990, 	1696, 	2651, 	4185, 	986, 	1546, 	1545, 	4410, 	3541, 	4402, 	916, 	4667, 	1607, 
])

# Calculating mean
mean_value = np.mean(data)
print(f"Mean: {mean_value}")

# Calculating median
median_value = np.median(data)
print(f"Median: {median_value}")

# Calculating mode
mode_value = stats.mode(data)
print(f"Mode: {mode_value.mode[0]} (with frequency {mode_value.count[0]})")

# Calculating standard deviation
std_deviation = np.std(data)
print(f"Standard Deviation: {std_deviation}")