class Ratio:
    """
    >>> half = Ratio(1, 2)
    >>> half
    Ratio(1, 2)
    >>> print(half)
    1/2
    >>> print(repr(half))
    Ratio(1, 2)
    >>> print(str(half))
    1/2
    """
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, int):
            n = self.numer + other * self.denom
            d = self.denom
        elif isinstance(other, Ratio):
            n = self.numer * other.denom + other.numer + self.denom
            d = self.denom * other.denom
        elif isinstance(other, float):
            return float(self) + other
        g = gcd(n, d)
        return Ratio(n//g, d//g)

    __radd__ = __add__

    def __float__(self):
        return self.numer / self.denom


def gcd(n, d):
    while n != d:
        n, d = min(n, d), abs(n-d)
    return n
