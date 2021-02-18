
my_string = 'Meeololeo'
word = ''
for i in range(len(my_string)):
    if i % 2 == 0:
        word += my_string[i]
        print(i)
        # print(my_string[i])
print(word)
