import numpy as np
arr = np.ones((6, 5)).astype('int')
lst = []
for number in np.nditer(arr):
    lst.append(number *arr)
print(lst)


