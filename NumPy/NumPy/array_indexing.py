import numpy

if __name__ == '__main__':
    arr = numpy.array([[2, 3, 4, 7], [5, 6, 9, 10]])
    # print(arr.shape)
    # print(arr.dtype)
    # print(arr.nbytes)

    b = numpy.array([[9, 5, 10], [30, 20, 11]], dtype='int16')
    # print(arr[0, 0] + arr[0, 1]) # 2 + 3

    arr2 = numpy.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print(arr2[0, 1, 2])



