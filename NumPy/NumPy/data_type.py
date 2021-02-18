import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

# print(arr)
# print(arr.dtype)

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

# print(arr)
# print(newarr)
# print(newarr.dtype)

arr = np.array([1, 0, 5])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)