thislist = [2, 3, 4, 4,  6, 7, 8]

uniques = []
for number in thislist:
    if number not in uniques:
        uniques.append(number)
print(uniques)