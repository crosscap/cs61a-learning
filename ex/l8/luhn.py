from fact import split, sum_digits


def luhn_sum(n):
    """Return the digit sum of n computed by the Luhn algorithm.

    >>> luhn_sum(2)
    2
    >>> luhn_sum(12)
    4
    >>> luhn_sum(42)
    10
    >>> luhn_sum(138743)
    30
    >>> luhn_sum(5105105105105100) # example Mastercard
    20
    >>> luhn_sum(4012888888881881) # example Visa
    90
    >>> luhn_sum(79927398713) # from Wikipedia
    70
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last


def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(last * 2)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit
