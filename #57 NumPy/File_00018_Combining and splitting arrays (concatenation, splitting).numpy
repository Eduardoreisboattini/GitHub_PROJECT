
import numpy as np

# Concatenation
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

print(np.concatenate((x, y), axis=0))

# Splitting
x = np.array([1, 2, 3, 4, 5, 6])

print(np.split(x, 3))
print(np.split(x, [1, 3]))
<<<<<<<  f96c081d-e785-443d-84bf-049463136e0c  >>>>>>>
