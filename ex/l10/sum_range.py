def sum_iter(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

def sum_recu(n):
    if n == 0:
        return 1
    else:
        return sum_recu(n - 1) + n

