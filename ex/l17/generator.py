def plus_minus(x):
    """
    >>> t = plus_minus(3)
    >>> next(t)
    3
    >>> next(t)
    -3
    """
    yield x
    yield -x


def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2


def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)
    else:
        yield 'Blast off'


def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s


def prefixes_for(s):
    """Same to prefixes(s)"""
    if s:
        for x in prefixes_for(s[:-1]):
            yield x
        yield s


def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])
