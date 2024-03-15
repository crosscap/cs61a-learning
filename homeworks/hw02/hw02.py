from operator import sub, mul
HW_SOURCE_FILE = __file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    if x == 0:
        return 0
    else:
        if x % 10 == 8:
            return num_eights(x // 10) + 1
        else:
            return num_eights(x // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def halper(i, ping_pong_num, incOrDec):
        if i == n:
            return ping_pong_num
        else:
            if num_eights(i) != 0 or i % 8 == 0:
                return halper(i + 1, ping_pong_num - incOrDec, -incOrDec)
            else:
                return halper(i + 1, ping_pong_num + incOrDec, incOrDec)

    return halper(1, 1, 1)


def pingpong_iter(n):
    i = 1
    ping_pong = 0
    incOrDec = 1  # 1 means increase and -1 means decrease
    while i <= n:
        ping_pong += incOrDec
        if num_eights(i) != 0 or i % 8 == 0:
            incOrDec = -incOrDec
    return ping_pong


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    def halper(num, last_num):
        end_num = num % 10
        if num == 0:
            return 0
        elif end_num != last_num:
            return halper(num // 10, end_num) + (last_num - end_num - 1)
        else:
            return halper(num // 10, end_num)

    return halper(n // 10, n % 10)


def next_largest_coin(coin):
    """Return the next coin.
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    def coins_min_divide(total, min_coin):
        if total == 0:
            return 1
        elif min_coin == None:
            return 0
        elif total < min_coin:
            return 0
        else:
            with_min = coins_min_divide(total-min_coin, min_coin)
            without_min = coins_min_divide(total, next_largest_coin(min_coin))
            return with_min + without_min

    return coins_min_divide(total, 1)


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda n: 1 if n == 1 else f(f, n))(lambda function, x: 1 if x == 1 else x * function(function, x - 1))
# So Diffcult! I get help from Networks! It coms from a problem meet by two
# computer scientist. They finally gave the solution called Y-combinator.
# But this solution use the thinking of curry, also very beautiful if you like lambda expression.
