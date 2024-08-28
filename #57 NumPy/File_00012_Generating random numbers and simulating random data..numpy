+import random
+
+def generate_random_numbers(num_of_numbers, lower_bound, upper_bound):
+    random_numbers = [random.randint(lower_bound, upper_bound) for _ in range(num_of_numbers)]
+    return random_numbers
+
+def simulate_random_data(num_of_data_points, num_of_random_numbers, lower_bound, upper_bound):
+    random_data = [generate_random_numbers(num_of_random_numbers, lower_bound, upper_bound) for _ in range(num_of_data_points)]
+    return random_data
+
+num_of_data_points = 10
+num_of_random_numbers = 5
+lower_bound = 1
+upper_bound = 10
+
+random_data = simulate_random_data(num_of_data_points, num_of_random_numbers, lower_bound, upper_bound)
+
+for data_point in random_data:
+    print(data_point)