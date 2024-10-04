+# This program demonstrates how to create and manipulate 1D and 2D arrays
+
+# Function to create a 1D array
+def create_1d_array(size):
+    return [0] * size
+
+# Function to create a 2D array
+def create_2d_array(rows, cols):
+    return [[0] * cols for _ in range(rows)]
+
+# Function to print a 1D array
+def print_1d_array(arr):
+    print("1D Array:", arr)
+
+# Function to print a 2D array
+def print_2d_array(arr):
+    print("2D Array:")
+    for row in arr:
+        print(row)
+
+# Main program
+if __name__ == "__main__":
+    # Create a 1D array of size 5
+    one_d_array = create_1d_array(5)
+
+    # Print the 1D array
+    print_1d_array(one_d_array)
+
+    # Create a 2D array with 3 rows and 4 columns
+    two_d_array = create_2d_array(3, 4)
+
+    # Print the 2D array
+    print_2d_array(two_d_array)


import numpy as np

# Creating a 1D array
arr1 = np.array([1,2,3,4,5])
print(arr1)

# Creating a 2D array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

# Manipulating the array
arr1 = arr1 * 2
print(arr1)
<<<<<<<  ea1082b6-188e-4b83-9738-fd972e13e55c  >>>>>>>
