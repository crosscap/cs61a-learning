from math import gcd

# Constructer and selections

def rational(n, d):
    """Construct a rational number that represents N/D."""
    g = gcd(n ,d)
    return [n//g, d//g]

def numer(x):
    """Return the numerator of rational number X."""
    return x[0]

def denom(x):
    """Return the denominator of rational number X."""
    return x[1]

# Rational arithmetic

def mul_rational(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def add_rational(x, y):

    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def equal_rational(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    print(numer(x), "/", denom(x))

