import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
lst = []
for number in np.nditer(arr):
    lst.append(number * 2)
# print(lst)

lst = []
for x in arr:
    for y in x:
        for z in y:
            lst.append(z*2)
            # print(z)

# print(lst)
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    pass
# print(x)

# to skip 1 array element

for x in np.nditer(arr[:, ::4]):
    # print(x)
    pass

# to know array index

for x in np.ndenumerate(arr):
    print(x)

