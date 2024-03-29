def combo(a, b):
    """Return the smallest integer with all of the digits of a and b (in order).

    >>> combo (531, 432)
    45312 # contains both _531_ and 4_3_2.
    >>> combo (531, 4321)
    45321 contains both _53_1 and 4_321.
    >>> combo (1234, 9123)
    91234 contains both_1234 and 9123_.
    >>> combo (0, 321) # The number o has no digits, so 0 is not in the result.
    321
    """
    if a == 0 or b == 0:
        return a + b
    elif a % 10 == b % 10:
        return combo(a // 10, b // 10) * 10 + (a % 10)
    return min(combo(a // 10, b) * 10 + (a % 10),
               combo(a, b // 10) * 10 + (b % 10))
