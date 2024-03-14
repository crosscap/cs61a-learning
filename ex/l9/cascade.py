def cascade(n):
    """Print a cascade of prefixes of n.

    >>> cascade(1234)
    1234
    123
    12
    1
    12
    123
    1234
    """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)


def cascade2(n):
    """Print a cascade of prefixes of n."""
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)


def inverse_cascade(n):
    """Print an inverse cascade of prefixes of n.

    >>> inverse_cascade(1234)
    1
    12
    1234
    123
    12
    1
    """
    grow(n)
    print(n)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


def grow(n): return f_then_g(grow, print, n // 10)
def shrink(n): return f_then_g(print, shrink, n // 10)
