# Boolean indexing and filtering arrays
arr = np.array([1, 2, 3, 4, 5])

# Boolean indexing
print(arr[arr % 2 == 0])
# Output: [2, 4]

# Boolean indexing with multiple conditions
print(arr[(arr % 2 == 0) & (arr > 3)])
# Output: [4]

# Boolean indexing with the ~ operator
print(arr[~(arr % 2 == 0)])
# Output: [1, 3, 5]
<<<<<<<  50515052-5ed9-4694-ab4d-58c4c418054f  >>>>>>>
