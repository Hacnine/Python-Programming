
def arrayCheck(numbers):

    # if i dont want to iterate last two items of the list then range(len(numbers)-2)
    for i in range(len(numbers)):
        if numbers[i] == 1 and numbers[i+1] == 2 and numbers[i+2] == 3:
            return True
    return False


print(arrayCheck([1, 1, 2, 1, 2, 3]))


# problem: if 1 2 3 in the list print True otherwise False
# another solution is
def array_check(nums):
    for number in nums:
        if number == 1:
            pass
        elif number == 2:
            pass
        elif number == 3:
            return True
        else:
            return False


print(array_check([1, 1, 2, 3, 1, 1]))


