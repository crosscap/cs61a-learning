# def search(f):
#     x = 0
#     while True:
#         if f(x):
#             return x
#         x += 1
def search(f):
    x = 0
    while not f(x):
        x += 1
    return x


def is_three(x):
    return x == 3


def square(x):
    return x * x


def positive(x):
    return max(0, square(x) - 100)


def inverse(f):
    """Return g(y) such that g(f(x)) -> x
    >>> sqrt = inverse(square)
    >>> sqrt(256)
    16
    """
    return lambda y: search(lambda x: f(x) == y)
