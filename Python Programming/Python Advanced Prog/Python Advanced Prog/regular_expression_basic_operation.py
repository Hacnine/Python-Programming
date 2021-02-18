import re


def multi_re_find(patterns, phrase):
    for pattern in patterns:
        print(f'Searching for patterns {pattern}')
        print(re.findall(pattern, phrase))
        print('\n')


test_phrase = 'sdsd..sssddd..sdddsddd...sdd..dsds...dssss...sddddd'
# test_patterns = ['sd*']
# test_patterns = ['sd+']
# test_patterns = ['sd?']
# test_patterns = ['sd{2,3}']
# test_patterns = ['s[sd]+ ']

test_phrase2 = 'How amazing exp 12345!But I have some question #hash.Can ask that?'
# test_patterns2 = ['[^!.?]'+'']
# test_patterns2 = ['[^!.?]+']
# test_patterns2 = ['[A-Z]+']
# to search digit
# test_patterns2 = [r'\d+']
# to search non digit
# test_patterns2 = [r'\D+']
# to white space
# test_patterns2 = [r'\s+']
# to non white space
# test_patterns2 = [r'\S+']
# to alpha numeric
# test_patterns2 = [r'\w+']
# to # tag
test_patterns2 = [r'\W+']
multi_re_find(test_patterns2, test_phrase2)