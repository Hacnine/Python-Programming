import numpy as np

# we want to copy array so,
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = arr1
print(f'look copy made but {arr2}')
''' now we want to what happen arr1 if we change value of arr2?'''
arr2[0] = 87
print(f'now see value of arr also chagned!but it should not{arr1}')
'''so we need copy() method to do this'''
arr = np.array([1, 2, 3, 4, 5])
copy_arr = arr.copy()
# now we want to the change of copy_array affects original array or not
copy_arr[0] = 90
print(arr)
print(f'After changing copy_arr value {copy_arr}')

view_arr = arr.view()
# now we want to the change of view_array affects original array or not

view_arr[0] = 80
print(f'view method affects the main array {arr}')

# Check if Array Owns it's Data

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)