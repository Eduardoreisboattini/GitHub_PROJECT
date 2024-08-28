+import numpy as np
+
+def numpy_operation(arr):
+    # Calculate the mean of the array
+    mean = np.mean(arr)
+
+    # Calculate the standard deviation of the array
+    std_dev = np.std(arr)
+
+    # Calculate the variance of the array
+    variance = np.var(arr)
+
+    return mean, std_dev, variance
+
+# Example usage:
+arr = np.array([1, 2, 3, 4, 5])
+mean, std_dev, variance = numpy_operation(arr)
+print("Mean:", mean)
+print("Standard Deviation:", std_dev)
+print("Variance:", variance)

