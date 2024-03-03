"""Our first Python source file."""

from operator import floordiv, mod

def devide_exact(n, d):
    """Return the quotient and remainder of deviding N by D.
    >>> q, r = devide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n, d), mod(n, d)

# print("Quotient:", q)
# print("Remainder:", r)

def absolute_value(x):
    """Reture the absolute value of x."""
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x
