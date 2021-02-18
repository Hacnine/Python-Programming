import logging


logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print('1')
        print(func(*args))
    return log_func


def add(x, y):
    print('2')
    return x+y


def sub(x, y):
    return x-y


add_logger = logger(add)
sub_logger = logger(sub)
# print(add_logger.__name__)

add_logger(4, 5)

sub_logger(10, 5)
