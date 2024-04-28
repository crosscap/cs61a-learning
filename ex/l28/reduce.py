from operator import add, mul, truediv

def reduce(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.

    E.g., reduce(mul, [2, 4, 8], 1) is equivalent to mul(mul(mul(1, 2), 4), 8).

    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    """
    # Iterator
    # for x in s:
    #     initial = f(initial, x)
    # return initial

    # Recursion
    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce(f, rest, f(initial, first))

def divide_all(n, ds):
    try:
        reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')
