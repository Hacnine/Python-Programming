# def how_many_digit(uid):
#     upper = 0
#     digit = 0
#     for i in uid:
#         if i.isupper():
#             upper = upper + 1
#             return upper
#         elif i.isdigit():
#             digit = digit + 1
#             return digit
#
#
# uid = 'B1CD102354'
# print(how_many_digit(uid))

import string


def is_char_repeating(chars, check_strings, nums):
    print(check_strings)
    for char in chars:
        counter = check_strings.count(char)
        if counter > 1:
            return 'True'

    for char in nums:
        counter = check_strings.count(char)
        if counter > 1:
            return 'True'
    return 'False'


def take_input():
    charsA_Z = string.ascii_uppercase
    nums0_9 = '0123456789'

    lst = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = input()

        lst.append(ele)  # adding the element

    for uid in lst:
        repeat = is_char_repeating(charsA_Z, uid, nums0_9)
    # return repeat


take_input()
# B1CD102354
# B1CDEF2354