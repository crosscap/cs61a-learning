# Generalization

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def pi_term(k):
    return 8 / (4 * k - 3) * (4 * k - 1)

def summation(n, term):
    """Sun the first N terms of a sequence.
    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def sum_naturlas(n):
    """Sum the first N natural number.
    >>> sum_naturlas(5)
    15
    """
    return summation(n, identity)

def sum_cubes(n):
    """Sum the first N cubes of batural number.
    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)
