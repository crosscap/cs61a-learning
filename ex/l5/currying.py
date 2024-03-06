# Currying

from operator import add, mul

def curry2(f):
    """Curry a two-argument function.

    >>> m = curry2(add)
    >>> add_three = m(3)
    >>> add_three(4)
    7
    >>> m(2)(1)
    3
    """
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
