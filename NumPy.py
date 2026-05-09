# # import numpy
import numpy as np
# # arr = np.array([1,2,3,4,5])
# # print(arr)
# # print(type(arr))
# # print(np.__version__)
# # nd array
# arrr = np.array((1,2,3,4,5))
# print(type(arrr))

### 0D array ###
# arr = np.array(42)
# print(arr)

#### 1D Array ####
# arr = np.array([1,2,3,4,5])
# print(arr)

### 2D ###.............
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)

### 3D ###........
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr)

### Checking dimensions of arrays ###.........
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

### Higher ###..........
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)