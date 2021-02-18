def alphanumeric(strings):
    letter_flag = False
    number_flag = False
    for i in strings:
        if i.isalpha():
            letter_flag = True
        if i.isdigit():
            number_flag = True
    # print('Number:'+ number_flag)
    # print("Letter:"+ letter_flag)
    return letter_flag and number_flag


print(alphanumeric('B1CD102354'))

# test case
''' 
B1CD102354
B1CDEF2354
e74D412L2I 
'''