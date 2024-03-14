# Tree recursion
from ucb import trace

@trace
def fib(n):
    """Compute the nth Fibonacci number.

    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

