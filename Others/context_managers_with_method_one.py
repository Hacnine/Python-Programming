from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()


with open_file('demo.txt', 'w') as f:
    f.write("Is written")

print(f.closed)
