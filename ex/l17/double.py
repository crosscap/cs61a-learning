def double(x):
    """
    >>> m = map(double, [3, 5, 7])
    >>> next(m)
    *** 3 => 6 ***
    6
    >>> next(m)
    *** 5 => 10 ***
    10
    >>> next(m)
    *** 7 => 14 ***
    14
    """
    print('***', x, '=>', 2*x, '***')
    return 2 * x

def built_in_demo():
    """Using built-in sequence functions.

    >>> bcd = ['b', 'c', 'd']
    >>> [x.upper() for x in bcd]
    ['B', 'C', 'D']
    >>> caps = map(lambda x: x.upper(), bcd)
    >>> next(caps)
    'B'
    >>> next(caps)
    'C'
    >>> s = range(3, 7)
    >>> doubled = map(double, s)
    >>> next(doubled)
    *** 3 => 6 ***
    6
    >>> next(doubled)
    *** 4 => 8 ***
    8
    >>> list(doubled)
    *** 5 => 10 ***
    *** 6 => 12 ***
    [10, 12]
    >>> f = lambda x: x < 10
    >>> a = filter(f, map(double, reversed(s)))
    >>> list(a)
    *** 6 => 12 ***
    *** 5 => 10 ***
    *** 4 => 8 ***
    *** 3 => 6 ***
    [8, 6]
    >>> t = [1, 2, 3, 2, 1]
    >>> reversed(t) == t
    False
    >>> list(reversed(t)) == t
    True
    >>> d = {'a': 1, 'b': 2, 'c': 3}
    >>> items = iter(zip(d.keys(), d.values())) # Call next(items)

