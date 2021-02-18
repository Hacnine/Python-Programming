from logging import *
import employee

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g.
# ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.


logger = getLogger(__name__)
logger.setLevel(DEBUG)

formatter = Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = FileHandler('sample.log')
file_handler.setLevel(ERROR)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

stream_handler = StreamHandler()
logger.addHandler(stream_handler)
stream_handler.setFormatter(formatter)

# LOG_FORMAT = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
# basicConfig(filename='test.log', level=DEBUG, format=LOG_FORMAT)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        # logger.error('Tried to divide by zero')
        logger.exception('Tried to divide by zero')
    else:
        return result


num_1 = 20
num_2 = 0

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
