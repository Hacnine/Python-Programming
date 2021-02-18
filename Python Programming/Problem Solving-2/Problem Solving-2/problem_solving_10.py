my_string = 'aabbbccde'
class_list = {}


def countA(text):
    new_string = list(text)
    uniques = []

    for letter in new_string:
        if letter not in uniques:
# print(uniques.append(letter))

            uniques.append(letter)
    length = len(uniques)
    # print(length)
    i = 0
    for c in uniques:
        i += 1
        count_letters(text, c, i, length)


def count_letters(word, char, i, length):
    # print(char, word.count(char))
    name = char
    score = word.count(char)
    class_list[name] = score

    # print(i)
    if i == length:
        print(class_list)

        listofTuples = sorted(class_list.items(), reverse=True, key=lambda x: x[1])

        class_list2 = {}
        for elem in listofTuples:
            # print(elem[0], elem[1])
            name = elem[0]
            score = elem[1]
            class_list2[name] = score

        print(class_list2)
        # for x, y in class_list2.items():
        #     print(x, y)

        value_list = list(class_list2.values())
        key_list = list(class_list2.keys())

        a0 = str(key_list[0])
        b0 = int(value_list[0])
        a1 = str(key_list[1])
        b1 = int(value_list[1])
        a2 = str(key_list[2])
        b2 = int(value_list[2])

        print(a0+" "+str(b0))
        print(a1+" "+str(b1))
        print(a2+" "+str(b2))


countA("aacccddde")


