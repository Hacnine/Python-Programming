input_num = 15
if input_num % 3 == 0:
    if input_num % 5 == 0:
        print('FizzBuzz')
    else:
        print('Fizz')
elif input_num % 5 == 0:
    if input_num % 3 == 0:
        print('FizzBuzz')
    else:
        print('Buzz')

else:
    print(input_num)