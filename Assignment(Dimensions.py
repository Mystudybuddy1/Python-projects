# # Create a 2D array like:
# # 1 2 3 
# # 4 5 6
# # and print its shape.
# import numpy as np
# arr = np.array([[123],
#                 [456]])
# print(arr)
# # Create a 3D array with 2 blocks, each containing 2 rows × 2 columns, and print the array
# arrr = np.array([
#     [[1, 2], [3, 4]],   
#     [[5, 6], [7, 8]]    
# ])

# print(arrr)

# print(arrr[1,0,1])
# import numpy as np

# arr = np.array([1, 2, 3, 4])

# print(arr[1])
# print(arr[2]+arr[3])
# import numpy as np

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('2nd element on 1st row: ', arr[1,4])

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0,1,2])

