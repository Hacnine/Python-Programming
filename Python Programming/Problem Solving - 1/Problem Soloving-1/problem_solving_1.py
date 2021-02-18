word = 'django'
# one type solution:

print('one type solution:')
empty_str = ''
empty_str2 = ''
empty_str3 = ''
for letter in word:
    if letter == 'd':
        print('d')
    if letter == 'o':
        print('o')

    if letter != 'g' and letter != 'o':
        empty_str += letter

    if letter != 'd' and letter != 'g' and letter != 'o':
        empty_str2 += letter

    if letter != 'd' and letter != 'j' and letter != 'a' and letter != 'n':
        empty_str3 += letter

print(empty_str)
print(empty_str2)
print(empty_str3 + '\n')

# another solution is:

word = 'django'
print('another solution is:')
print(word[0])
print(word[5])
print(word[:4])
print(word[1:4])
print(word[4:])