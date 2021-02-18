# we assign parameter value
def increment(number, by=1):

    # returning tuple
    return number, number + by


print(increment(2))


# time hinting or time annotation
def increment_value(number: int, by: int = 1) -> tuple:

    # returning tuple
    return number, number + by


print(increment_value(2))
