lists = [3, 7, [1, 4, 'world']]
# resign world to end
lists[2][2] = 'end'
print(lists)


# remove duplicate
def numbers_filter(nums):
    x = set(nums)
    print(x)


numbers = [1, 2, 2, 5, 5, 6]
numbers_filter(numbers)

dic = {'k1': [{'nest_key': ['this is deep', ['world']]}]}
print(dic['k1'][0]['nest_key'][1][0])