def take_input():

    lst = []
    n = int(input('How many test case you want to enter: '))
    for i in range(0, n):
        ele = input()

        lst.append(ele)  # adding the element
    print('Output:')

    for item in range(len(lst)):
        print(lst[item])


take_input()


