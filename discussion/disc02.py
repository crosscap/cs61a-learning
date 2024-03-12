# 1.1
def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """

    i = 1
    while i <= n:
        if cond(i):
            print(i)
        i += 1

# 1.2


def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """

    def h(f):
        return keep_ints(f, n)
    return h

# 1.3


def curry2(h):
    def f(x):
        def g(y):
            return h(x, y)
        return g
    return f


make_adder = curry2(lambda x, y: x + y)
add_three = make_adder(3)
add_four = make_adder(4)
five = add_three(2)

# 1.4


def curry2_lambda(h):
    return lambda x: lambda y: h(x, y)


# 1.5
n = 7


def f(x):
    n = 8
    return x + 1


def g(x):
    n = 9

    def h():
        return x + 1
    return h


def f(f, x):
    return f(x+n)


f = f(g, n)
g = (lambda y: y())(f)

# 1.6
y = "y"
h = y


def y(y):
    h = "h"
    if y == h:
        return y + "i"

    def y(y):
        return y(h)
    return lambda h: y(h)


y = y(y)(y)

# 1.7
def print_delayed(x):
    """Return a new function. This new function, when called,
    will print out x and return another function with the same behavior.
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    >>> f("hi")
    5
    <function print_delayed> # a function is returned
    """
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print
