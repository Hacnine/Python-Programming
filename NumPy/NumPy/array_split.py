import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
# print(newarr[2], newarr[1], newarr[0])

# Split the 2-D array into three 2-D arrays.

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

new_arr2 = np.array_split(arr2, 3)
# print(new_arr2)


# new_arr3 = np.array_split(arr2, 3, axis=1)
new_arr3 = np.hsplit(arr2, 3)
print(new_arr3)

