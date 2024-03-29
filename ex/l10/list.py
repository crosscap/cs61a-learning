def count(s, value):
    """Count the number of times that value appears in sequence s.

    >>> count([1, 2, 1, 2, 1], 1)
    3
    """
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

def count_sum(pairs):
    """
    >>> count_same([1, 2], [2, 2], [3, 2], [4, 4]])
    2
    """
    same_count = 0
    for x, y in pairs:
        if x == y:
            same_count += 1
    return same_count

