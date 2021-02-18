items = [
    ('product', 10),
    ('product1', 9),
    ('product2', 12)
]
filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)


def filter_num(numbers):
    if numbers > 4:
        return numbers


num_list = [3, 6, 4, 20, 8, 1]
filter_numbers = list(filter(filter_num, num_list))
print(filter_numbers)

print('Same result we can using lambda expression')
# (filter(key=lambda parameters:expression, num_list))
modified_nums = list(filter(lambda numbers: numbers > 4, num_list))
print(modified_nums)
