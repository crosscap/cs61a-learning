def prime_factors_my(n):
    """Print the prime factores of n in non-decreasing order.
    >>> prime_factors_my(8)
    2
    2
    2
    >>> prime_factors_my(9)
    3
    3
    >>> prime_factors_my(10)
    2
    5
    >>> prime_factors_my(11)
    11
    >>> prime_factors_my(12)
    2
    2
    3
    >>> prime_factors_my(858)
    2
    3
    11
    13
    """
    while n != 1:
        i = 2
        while n % i != 0:
            i = i + 1
        n = n // i
        print(i)
