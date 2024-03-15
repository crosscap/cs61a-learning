# my version
# def remove(n, digit):
#     """Return all digits of non-negative N
#     that are not DIGIT, for some
#     non-negative DIGIT less than 10.
#     >>> remove(231, 3)
#     21
#     >>> remove(243132, 2)
#     4313
#     """
#     kept, digits = 0, 0
#     while n > 0:
#         n, last = n // 10, n % 10
#         if last != digit:
#             kept = 1 if kept == 0 else kept * 10
#             digits = digits + last * kept
#     return kept

def remove(n, digit):
    """Return all digits of non-negative N
    that are not DIGIT, for some
    non-negative DIGIT less than 10.
    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept + last * 10 ** digits
            digits = digits + 1
    return kept
