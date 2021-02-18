def find_even(num):
    return num % 2 == 0


def find_odd(num):
    return num % 2 != 0


num_list = [1, 2, 4, 5]
even_num = filter(find_even, num_list)
odd_num = filter(find_odd, num_list)

print(f'Odd number in the list {list(odd_num)}')
print(f'Even number in the list {list(even_num)}')

# Making the find odd function to Lambda expression

odd_num_lambda = filter(lambda num: num % 2 != 0, num_list)
print(f'Odd number in the list using lambda expression: {list(odd_num_lambda)}')

