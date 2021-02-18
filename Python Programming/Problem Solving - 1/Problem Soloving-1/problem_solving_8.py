
if __name__ == '__main__':
    n = 20
    if n % 2 != 0:
        print('Weird')
    if n == 4:
        print('Not Weird')
    if n % 2 == 0 and n in range(6, 21):
        print('Weird')
    if n % 2 == 0 and n > 20:
        print('Not Weird')


# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

