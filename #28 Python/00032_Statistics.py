import matplotlib.pyplot as plt
import numpy as np

# Generate a random dataset
np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=1000)

# Plot histogram for the dataset
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of Random Dataset')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

# Calculate and display mean, median, and mode
mean_value = np.mean(data)
median_value = np.median(data)
mode_value = float(stats.mode(data)[0])

print(f"Mean: {mean_value:.2f}")
print(f"Median: {median_value:.2f}")
print(f"Mode: {mode_value:.2f}")

# Plot boxplot for the dataset
plt.boxplot(data, vert=False)
plt.title('Boxplot of Random Dataset')
plt.xlabel('Values')
plt.show()

# Calculate and display standard deviation
std_dev = np.std(data)
print(f"Standard Deviation: {std_dev:.2f}")
