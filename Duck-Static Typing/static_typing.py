def fabricate(a: int, b: int):
    return a + b


calculate = fabricate(5, 'u')
print(fabricate.__annotations__)


def f():
    lst = ['py']


def g():
    return f() + 45
