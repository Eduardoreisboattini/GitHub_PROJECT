#Example of using the zip function to iterate over two lists in parallel:
list1 = ["apple", "banana", "orange"]
list2 = [1.0, 2.0, 3.0]

for fruit, price in zip(list1, list2):
    print(fruit, price)

# Example output
# apple 1.0
# banana 2.0
# orange 3.0