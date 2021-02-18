def greatest_num(numberss):
    init_maximum = numberss[0]
    for number in numberss:
        if init_maximum < number:
            init_maximum = number
    return init_maximum


