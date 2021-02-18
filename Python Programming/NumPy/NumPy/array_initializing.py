import numpy as np
n = np.zeros((2, 3))
# print(n)

m = np.ones((3,), dtype=[('x', 'float'), ('y', 'int')])
# print(m)
# any other number not zero

any_num = np.full((3, 3), 56, dtype=[('x', 'float'), ('y', 'int')])
# print(any_num)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(np.full_like(arr2, 4))

# random decimal number
# print(np.random.rand(4, 3))

# print(np.random.random_sample(arr2.shape))

# random inter value
# print(np.random.randint(6, size=(3, 3)))
# print(np.random.randint(-5, 12, size=(4, 5)))

# identity matrix
# print(np.identity(3))

# repeat an ary
arr = np.array([[1, 2, 3]])
arr2 = np.repeat(arr, 3, axis=0)
print(arr2)