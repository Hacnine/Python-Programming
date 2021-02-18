
def alphanumeric(s):
    letter_flag = False
    number_flag = False
    for i in s:
        if i.isalpha():
            letter_flag = True
        if i.isdigit():
            number_flag = True
    # print('Number:'+ number_flag)
    # print("Letter:"+ letter_flag)
    return letter_flag and number_flag


def is_uid_valid(uid, uppers, digits, repeats):
    if len(uid) == 10 and uppers > 1 and digits > 2 and repeats == True and alphanumeric(uid) == True:
        print('Valid')

    else:
        print('Invalid')


def is_unique_chars(string1):
    # String length cannot be more than
    if len(string1) > 256:
        return False
    # Initialize occurrences of all characters
    char_set = [False] * 256
    for i in range(0, len(string1)):
        # Find ASCII value and check if it
        # exists in set.
        value = ord(string1[i])
        # print(value)
        # print(char_set[value])

        if char_set[value]:
            return False

        char_set[value] = True

    return True


def take_input():

    lst = []
    n = int(input('How many test case you want to enter: '))
    for i in range(0, n):
        ele = input().strip()

        lst.append(ele)  # adding the element

    for uid in lst:

        upper = 0
        digit = 0
        for i in uid:
            if i.isupper():
                upper = upper + 1
            elif i.isdigit():
                digit = digit + 1

        repeat = is_unique_chars(uid)
        # print(upper, digit)

        # print(repeat)
        is_uid_valid(uid, upper, digit, repeat)


take_input()
# test case
''' 
B1CD102354
B1CDEF2354
e74D412L2I 
'''

