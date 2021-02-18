import re

patterns = ['term1', 'term2']

text = 'This is a string with term1'

# for pattern in patterns:
#     print("I'm searching for: " + pattern)
#
#     if re.search(pattern, text):
#         print('MATCH!')
#     else:
#         print('NO MATCH')

# match = re.search('term1', text)
#
# print(match.start())

# split_term = '@'
# email = 'user@gmail.com'
# print(re.split(split_term, email))

print(re.findall('match', 'test phrase match in match middle'))
print(re.search('match', 'test phrase match in match middle'))