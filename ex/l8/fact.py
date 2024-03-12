def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n - 1) * n

def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1

    return total
