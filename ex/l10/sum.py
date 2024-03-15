def my_sum_iter(L):
    sum_num = 0
    for num in L:
        sum_num += num
    return sum_num

def my_sum_recu_helper(L):
    def halper(n):
        if n == len(L):
            return 0
        else:
            return halper(n + 1) + L[n]
    return halper(0)

def my_sum_iter(L):
    if (L == []):
        return 0
    else:
        return L[0] + my_sum_iter(L[1:])

