def fact(n):
    """Return n * n-1 * ... * 1.

    >>> fact(4)
    24
    """
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def fact_times(n, k):
    """Return k * n * n-1 * ... * 1.

    >>> fact_times(4, 3)
    72
    """
    if n == 0:
        return k
    else:
        return fact_times(n - 1, k * n)

def fact_tail(n):
    return fact_times(n, 1)

