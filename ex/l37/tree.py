def tree(label, branches=[]):
    return [label] + list(branches)


def label(t):
    return t[0]


def branches(t):
    return t[1:]


def is_leaf(t):
    return not branches(t)


class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches


def bigs(t: Tree):
    """Return the number of nodes in t that are larger than all their ancestors.
    >>> a = Tree(1, [Tree(4, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(2)])])])
    >>> bigs(a)
    4
    """
    def f(a, x):
        """
        a: node in t
        x: max ancestor
        """
        if a.label > x:
            return 1 + sum([f(b, a.label) for b in a.branches])
        else:
            return sum([f(b, x) for b in a.branches])
    return f(t, t.label-1)


def bigs_nonlocal(t: Tree):
    """Return the number of nodes in t that are larger than all their ancestors.

    >>> p = Tree(1, [Tree(4, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(6)])])])
    >>> bigs_nonlocal(p)
    5
    >>> q = Tree(1, [Tree(4, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(2)])])])
    >>> bigs_nonlocal(q)
    4
    """
    n = 0
    def f(a, x):
        nonlocal n
        if a.label > x:
            n += 1
        for b in a.branches:
            f(b, x if x > a.label else a.label)
    f(t, t.label-1)
    return n


def smalls(t: Tree):
    """Return the non-leaf nodes in t that are smaller than all their descendants.
    >>> a = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(6)])])])
    >>> sorted([t.label for t in smalls(a)])
    [0, 2]
    """
    result = []
    def process(t: Tree):
        """Find smallest label in t and maybe add t to result."""
        # My Solution
        # if not t.is_leaf():
        #     smallest = min([process(b) for b in t.branches])
        #     if t.label < smallest:
        #         result.append(t)
        #         return t.label
        #     else:
        #         return smallest
        # else:
        #

        # Use gived template
        if t.is_leaf():
            return t.label
        else:
            smallest = min([process(b) for b in t.branches])
            if t.label < smallest:
                result.append(t)
            return min(t.label, smallest)
    process(t)
    return result
