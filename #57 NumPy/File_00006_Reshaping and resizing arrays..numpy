# Reshaping and resizing arrays.

# Reshaping arrays
import numpy as np
arr = np.array([1,2,3,4,5,6])
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)

# Resizing arrays
import numpy as np
arr = np.array([1,2,3,4])
resized_arr = np.resize(arr, (2,2))
print(resized_arr)
>
