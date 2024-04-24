def min_abs_indices(s):
    """Indices of all elements in list s that have the smallest absolute value.

    >>> min_abs_indices([-4, -3, -2, 3, 2, 4])
    [2, 4]
    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    """
    # My solution
    # abs_s = [abs(i) for i in s]
    # return [index for index in range(len(s)) if abs_s[index] == min(abs_s)]

    min_abs = min(map(abs, s))
    return [i for i in range(len(s)) if abs(s[i]) == min_abs]

    # Other solution
    # min_abs = min(map(s, min))
    # return list(filter(lambda i: abs(s[i]) == min_abs), range(len(s)))


def largest_adj_sum(s):
    """Largest sum of two adjacent elements in a list s.

    >>> largest_adj_sum([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_adj_sum([-4, 3, -2, -3, 2, -4])
    1
    """
    return max([s[i] + s[i+1] for i in range(len(s)-1)])

    # Other solution
    # return max([a + b for a, b in zip(s[:-1], s[1:])])


def digit_dict(s):
    """Map each digit d to the lists of elements in s that end with d.

    >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    # My solution
    # dig_dict = {}
    # for item in s:
    #     if item % 10 not in dig_dict.keys():
    #         dig_dict[item%10] = [item]
    #     else:
    #         dig_dict[item%10].append(item)
    # return dig_dict

    # return {d: [x for x in s if x % 10 == d] for d in range(10)
    #         if any([x % 10 == d for x in s])}

    last_digits = [x % 10 for x in s]
    return {d: [x for x in s if x % 10 == d] for d in range(10) if d in last_digits}


def all_have_an_equal(s):
    """Does every element equal some other element in s?

    >>> all_have_an_equal([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal([4, 3, 2, 3, 2, 4])
    True
    """
    # return all([True if s.count(item) > 1 else False for item in s])
    # return all([s[i] in s[:i] + s[i+1:] for i in range(len(s))])
    return min([s.count(x) for x in s]) >  1
