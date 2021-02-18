import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)
x = np.where(arr%2 == 0)
x = np.where(arr%2 == 1)

# Find the indexes where the value 4 should be inserted:

x = np.searchsorted(arr, 4)

print(x)