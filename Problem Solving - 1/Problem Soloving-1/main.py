
from collections import Counter, OrderedDict


# class OrderedCounter(Counter, OrderedDict):
#     pass
#
#
# [print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]/\

# cnt = Counter()
# for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
#     cnt[word] += 1
# for x, y in cnt.items():
#     print(x, y)
# print(cnt)
#
# new_list = Counter('B1CD102354').most_common(10)
# for item in new_list:
#     print(item )

import string


def is_char_repeating(chars, check_strings, nums):
    for char in chars:
        counter = check_strings.count(char)
        if counter > 1:
            return 'True'

    for char in nums:
        counter = check_strings.count(char)
        if counter > 1:
            return 'True'
    return 'False'


def alphanumeric(s):
    letter_flag = False
    number_flag = False
    for i in s:
        if i.isalpha():
            letter_flag = 'True'
        if i.isdigit():
            number_flag = 'True'
    return letter_flag and number_flag


def is_uid_valid(uid, uppers, digits, repeats):
    if len(uid) == 10 and uppers > 1 and digits > 2 and repeats == 'False' and alphanumeric(uid) == 'True':
        print('Valid')

    else:
        print('Invalid')


def take_input():
    chars = string.ascii_uppercase
    nums0_9 = '0123456789'

    lst = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = input()

        lst.append(ele)  # adding the element

    for uid in lst:
        repeat = is_char_repeating(chars, uid, nums0_9)
    return repeat



# uid = []
# uid = take_input()


# print(alphanumeric(uid))
# print(alphanumeric('some string'))


upper = 0
digit = 0
for i in uid:
    if i.isupper():
        upper = upper + 1
    elif i.isdigit():
        digit = digit + 1
# print(digit)


# repeat1 = is_char_repeating(chars, uid, nums0_9)
# print(f'Is char repeating: {repeat}')

is_uid_valid(uid, upper, digit, repeat)

