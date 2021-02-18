def find_letters(str1, str2):
    print((len(string2)))
    return string1[-(len(string2)):] == string2[-(len(string1)):]

    # also has another way, it will also return same value
    # if str1 in str2 or str2 in str1:
    #     return True
    # else:
    #     return False


letter1 = 'abc'
letter2 = "abXabc"
string1 = letter1.lower()
string2 = letter2.lower()

print(find_letters(string1, string2))

# another way
value = string1.endswith(string2) or string2.endswith(string1)
print(value)






