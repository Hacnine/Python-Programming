def multiply(*list):
    num = 1
    for number in list:
        num *= number
    return num


print(multiply(4, 5, 7, 9))


def save_users(**user):
    return user["id"]

save_users( id = 0, name = 'Tusar')

