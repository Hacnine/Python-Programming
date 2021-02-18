
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
        print(value)
        print(char_set[value])

        if char_set[value]:
            return False

        char_set[value] = True

    return True


# str = "GB1CDEF2354"
str1 = 'B1CD102354'
print(is_unique_chars(str1))
