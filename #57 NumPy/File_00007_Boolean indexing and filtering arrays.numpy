# Boolean indexing and filtering arrays
+import numpy as np
+
+# Create a sample array
+arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
+
+# Boolean indexing and filtering arrays
+# Filter out even numbers
+even_numbers = arr % 2 == 0
+
+# Filter out odd numbers
+odd_numbers = arr % 2 != 0
+
+# Print the filtered arrays
+print("Even numbers:", arr[even_numbers])
+print("Odd numbers:", arr[odd_numbers])