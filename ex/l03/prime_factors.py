def my_prime_factors(n):
    """Print the prime factores of n in non-decreasing order.
    >>> my_prime_factors(8)
    2
    2
    2
    >>> my_prime_factors(9)
    3
    3
    >>> my_prime_factors(10)
    2
    5
    >>> my_prime_factors(11)
    11
    >>> my_prime_factors(12)
    2
    2
    3
    >>> my_prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_prime_factor(n)
        n = n // k
        print(k)

def smallest_prime_factor(n):
    """Return the smallest k > 1 that evenly devides by n."""
    k = 2
    while n % k != 0:
        k = k + 1
    return k
