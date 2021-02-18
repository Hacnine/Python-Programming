import numpy as np

file_data = np.genfromtxt('data.txt', delimiter=',')
file_data2 = file_data.astype('int32')
# print(file_data)
# print(file_data2)
boolen = file_data2 > 50
# print(boolen)

get_value_greater_than_50 = file_data[file_data > 50]
# print(get_value_greater_than_50)
# print(np.all(file_data2 > 50, axis=1))

print((file_data2 > 50) and (file_data2 < 100))