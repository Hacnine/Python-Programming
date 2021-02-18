
items = [
    ('product3', 10),
    ('product1', 9),
    ('product2', 12)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# smart way
# items.sort(key=lambda parameters:expression)

items.sort(key=lambda item: item[1])
list_item = sorted(items, key=lambda item: item[1])
# print(list_item)

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

print(sorted(student_tuples, key=lambda student_list: student_list[2]))
