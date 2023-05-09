#Example of using lambda functions to sort a list of tuples by the second value:
data = [("John", 28), ("Jane", 35), ("Bob", 20), ("Alice", 32)]
sorted_data = sorted(data, key=lambda x: x[1])

# Example output
print(sorted_data) # Output: [('Bob', 20), ('John', 28), ('Alice', 32), ('Jane', 35)]