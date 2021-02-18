def no_tin(a, b, c):
    return fix_tin(a) + fix_tin(b) + fix_tin(c)


def fix_tin(n):

    if n[13, 14, 17, 18, 19]:
        return 0
    return n


# no_tin(2, 1, 14)


def calculate_num(num1, num2, num3):

    if num1 < 20 and 12 < num1 and num1 != 16:
        if num1 != 15:
            num1 = 0
            print(f'number1 set to {num1}')

    if num2 < 20 and 12 < num2 and num2 != 16:
        if num2 != 15:
            num2 = 0
            print(f'number2 set to {num2}')

    if num3 < 20 and 12 < num3 and num3 != 16:
        if num3 != 15:
            num3 = 0
            print(f'number3 set to {num3}')
            sum(num1, num2, num3)

    else:
        sum(num1, num2, num3)


def sum(num1, num2, num3):
    print(num1 + num2 + num3)


calculate_num(14, 1, 14)



