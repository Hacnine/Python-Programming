# let's say we are interested in just product price, so we wanna sort the price
items = [
    ('product', 10),
    ('product1', 9),
    ('product2', 12)
]

# in older way we can do this.
prices = []
for item in items:
    prices.append(item[1])
# print(prices)

# and also smart way we can do this
x = map(lambda item: item[1], items)
for item in x:
    print(item)
# or we can convert it in list
y = list(map(lambda item: item[1], items))
# print(y)

list2 = [1, 2, 4]
multiple = list(map(lambda number: number*3, list2))
print(multiple)