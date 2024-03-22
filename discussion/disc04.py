# 1.1
def count_stair_ways(n):
    """Count how many way you can go up to a N steps stairs.
    N means a positive number which means how many step do stairs have.

    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(3)
    3
    """
    if n == 0 or n == 1:
        return 1
    else:
        begin_with_1 = count_stair_ways(n-1)
        begin_with_2 = count_stair_ways(n-2)
        return begin_with_1 + begin_with_2


# 1.2
def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        num_sum = 1
    else:
        num_sum, i = 0, 1
        while i < k + 1 and n - i >= 0:
            num_sum += count_k(n-i, k)
            i += 1
    return num_sum

# 2.1
# 1 3
# 5
# False
# True
# 2


# 2.2
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i * s[i] for i in range(len(s)) if s[i] % 2 == 1]


# 2.3
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.

    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        without_this = max_product(s[1:])
        with_this = s[0] * max_product(s[2:])
        return max(without_this, with_this)
