# Convert the following 1-D array with 12 elements into a 3-D array.
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr = arr.reshape(2, 3, 2)
print(arr)


# Consider the following code:
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr.shape)
# What will be the printed result?

# The printed result will be:(2, 3)



# Consider the following code:
# import numpy as np
# original_array = np.array([1, 2, 3])
# x = original_array.copy()
# x[0] = 5
# print(original_array)
# What will be the printed result?

# The printed result will be: [1 2 3] 




