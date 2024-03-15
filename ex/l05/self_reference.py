# Self Reference

def print_all(k):
    """Print all arguments of repeated calls.

    >>> f = print_all(1)(2)(3)(4)(5)
    1
    2
    3
    4
    5
    """
    print(k)
    return print_all


def print_sums(n):
    """Print all sums of arguments of repeated calls.

    >>> f = print_sums(1)(2)(3)(4)(5)
    1
    3
    6
    10
    15
    """
    print(n)

    def next_sum(k):
        return print_sums(n+k)
    return next_sum
