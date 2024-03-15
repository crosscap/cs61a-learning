odds = [1, 3, 5, 7, 9]
[x+1 for x in odds]
[x for x in odds if 25 % x == 0]

def divisors(n):
    return [1] + [x for x in range(2, n) if n%x==0]

