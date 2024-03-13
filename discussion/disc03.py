# 1.1
def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if m < n:
        return multiply(n, m)
    elif n == 0:
        return 0
    elif n == 1:
        return m
    else:
        return m + multiply(m, n - 1)

# 1.2
def rec(x, y):
    if y > 0:
        return x * rec(x, y - 1)
    return 1
rec(3, 2)

# 1.3
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2:
        return hailstone(3 * n + 1) + 1
    else:
        return hailstone(n // 2) + 1

# 1.4
def merge(n1, n2):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 <= n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10

# 1.5
def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(time):
        if time == 1:
            return f(x)
        else:
            return f(repeat(time - 1))
    return repeat

# 1.6
def is_prime_iter(n):
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """

    def prime_helper(n, k):
        if k == 0:
            return False
        elif k == 1:
            return True
        elif n % k == 0:
            return False
        else:
            return prime_helper(n, k - 1)
    return prime_helper(n, n - 1)
