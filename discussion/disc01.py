def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining:
        return True
    else:
        return False


def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    test = 2
    while test * test <= n:
        if n % test == 0:
            return False
        test += 1
    return True

# 2.4


def f(x):
    return x


def g(x, y):
    if x(y):
        return not y
    return y


x = 3
x = g(f, x)
f = g(f, 0)
