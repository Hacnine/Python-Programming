import numpy as np
# Convert the following 1-D array with 12 elements into a 2-D array.
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3)

# print(newarr)

# Reshape From 1-D to 3-D
# newarr = arr.reshape(2, 3, 2)
# newarr = arr.reshape(3, 3)


# newarr = arr.reshape(2, 2, -1)

# print(newarr)


# Flattening array means converting a multidimensional array into a 1D array.

arr = np.array([[1, 2, 3], [3, 4, 5]])

newarr = arr.reshape(-1)
print(newarr)


