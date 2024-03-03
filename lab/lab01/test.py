def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    flag = False
    while n != 0:
        if flag == True:
            if n % 10 == 8:
                return True
            else:
                flag = False
        else:
            if n % 10 == 8:
                flag = True
        n //= 10
    return False
