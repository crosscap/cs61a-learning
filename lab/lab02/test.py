def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def cycle_funcs(n):
        assert n >= 0, "Input number should be a positive number or 0."
        def do_cycles(x):
            def do_funcs(x, n):
                if n == 0:
                    return x
                elif n % 3 == 1:
                    return do_cycles(f1(x), n - 1)
                elif n % 3 == 2:
                    return do_cycles(f2(x), n - 1)
                else:
                    return do_cycles(f3(x), n - 1)
            return do_funcs(x, n)
        return do_cycles
    return cycle_funcs

def add1(x):
    return x + 1

def times2(x):
    return x * 2

def add3(x):
    return x + 3

my_cycle = cycle(add1, times2, add3)

identity = my_cycle(0)
identity(5)

add_one_then_double = my_cycle(2)
add_one_then_double(1)

do_all_functions = my_cycle(3)
do_all_functions(2)

do_more_than_a_cycle = my_cycle(4)
do_more_than_a_cycle(2)
