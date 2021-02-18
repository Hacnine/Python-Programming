import numpy as np

arr1 = np.ones((5, 5))
# print(arr1)
arr2 = np.zeros((3, 3))
arr2[1, 1] = 9
# print(arr2)
arr1[1:4, 1:4] = arr2
print(arr1)