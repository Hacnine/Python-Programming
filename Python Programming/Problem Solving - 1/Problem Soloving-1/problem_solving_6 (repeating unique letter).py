''' problem: The = TThhee and TTThhheee = TThhee(repeated two times and also remove duplicates
  and again add duplicates'''

thislist = list('Thheee')
# print(thislist)  # output: ['T', 'h', 'e', 'e', 'e']

uniques = []
for number in thislist:
    if number not in uniques:
        uniques.append(number)


def double_char(string_list):
    holder_string = ''
    for letter in string_list:
        holder_string += letter * 2
    print(holder_string)


double_char(uniques)



# s = "Word to Split"
# wordlist = list(s)               # option 1,
# wordlist = [ch for ch in s]
# print(wordlist)