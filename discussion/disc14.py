# 1.1
def paths(x, y):
    """Return a list of ways to reach y from x by repeated
    incrementing or doubling.

    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3) # No calls is a valid path
    [[3]]
    """
    # if _________________________:
    #     return _________________________
    # elif _________________________:
    #     return _________________________
    # else:
    #     a = _________________________
    #     b = _________________________
    #     return _________________________


# 1.2
# def merge(s1, s2):
#     """ Merges two sorted lists """
#     if len(s1) == 0:
#         return s2
#     elif len(s2) == 0:
#         return s1
#     elif s1[0] < s2[0]:
#         return [s1[0]] + merge(s1[1:], s2)
#     else:
#         return [s2[0]] + merge(s1, s2[1:])

# def mergesort(seq):


# 2.1
# def long_paths(tree, n):
#     """Return a list of all paths in tree with length at least n.

#     >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
#     >>> left = Tree(1, [Tree(2), t])
#     >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
#     >>> right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
#     >>> whole = Tree(0, [left, Tree(13), mid, right])
#     >>> for path in long_paths(whole, 2):
#     ...     print(path)
#     ...
#     <0 1 2>
#     <0 1 3 4>
#     <0 1 3 4>
#     <0 1 3 5>
#     <0 6 7 8>
#     <0 6 9>
#     <0 11 12 13 14>
#     >>> for path in long_paths(whole, 3):
#     ...     print(path)
#     ...
#     <0 1 3 4>
#     <0 1 3 4>
#     <0 1 3 5>
#     <0 6 7 8>
#     <0 11 12 13 14>
#     >>> long_paths(whole, 4)
#     [Link(0, Link(11, Link(12, Link(13, Link(14)))))]
#     """


# 2.2
# def widest_level(t):
#     """
#     >>> sum([[1], [2]], [])
#     [1, 2]
#     >>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]),
#     ...     Tree(4, [Tree(9, [Tree(2)])])])
#     >>> widest_level(t)
#     [1, 5, 9]
#     """
    # levels = []
    # x = [t]
    # while __________________________________________________:
    #     _____________________________________________________
    #     __________ = sum(_______________________________, [])
    # return max(levels, key=_________________________________)


# 3.2
# def bake(banana, bread):
#     _______________(____________(__________)) # This line is Multiple Choice
#     # Select all correct answers for the blank above
#     # A. banana.append(bread.append(1))
#     # B. bread.append(banana.append(1))
#     # C. banana.extend([bread.extend([1])])
#     # D. bread.extend([banana.extend([1])])
#     bread += banana[: (len(______________) - ______________)]
#     banana._______________(bread[___________[______________]])
#     return ___________, ______________


# 3.3
# def amon(g):
#     _____________________
#     def u(s):
#         ______________________
#         f = lambda x: x + g._________ + n
#         _________________

#         return f(s)
#     return u


# 4.1
# class Emotion(_______):
#     def __init__(self):
#     def feeling(self, other):

# class Joy(_______):
#     def catchphrase(self):

# class Sadness(_______):
#     def catchphrase(self):


# 5.1
# def remove_duplicates(lnk):
#     """
#     >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
#     >>> remove_duplicates(lnk)
#     >>> lnk
#     Link(1, Link(5))
#     """


# 6.1
# def repeated(f):
#     """
#     >>> double = lambda x: 2 * x
#     >>> funcs = repeated(double)
#     >>> identity = next(funcs)
#     >>> double = next(funcs)
#     >>> quad = next(funcs)
#     >>> oct = next(funcs)
#     >>> quad(1)
#     4
#     >>> oct(1)
#     8
#     >>> [g(1) for _, g in
#     ...     zip(range(5), repeated(lambda x: 2 * x))]
#     [1, 2, 4, 8, 16]
#     """
    # g = ________________________________________________________________________
    # while True:
    #     ________________________________________________________________________
    #     ________________________________________________________________________


# 6.3
# from operator import add, mul
# def accumulate(iterable, f):
#     """
#     >>> list(accumulate([1, 2, 3, 4, 5], add))
#     [1, 3, 6, 10, 15]
#     >>> list(accumulate([1, 2, 3, 4, 5], mul))
#     [1, 2, 6, 24, 120]
#     """
    # it = iter(iterable)
    # ______________________________________________________________________________
    # ______________________________________________________________________________
    # for __________________________________________________________________________:
    #     __________________________________________________________________________
    #     __________________________________________________________________________
