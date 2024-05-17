from operator import add, mul


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


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
    if x == y:
        return [[x]]
    elif 2 * x > y:
        return [[x] + path for path in paths(x+1, y)]
    else:
        a = [[x] + path for path in paths(x+1, y)]
        b = [[x] + path for path in paths(x*2, y)]
        return a + b


# 1.2
def merge(s1, s2):
    """ Merges two sorted lists """
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    elif s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    else:
        return [s2[0]] + merge(s1, s2[1:])


def mergesort(seq):
    """ Merge Sort

    >>> mergesort([])
    []
    >>> mergesort([1])
    [1]
    >>> mergesort([2, 4, 1, 3])
    [1, 2, 3, 4]
    """
    if len(seq) == 0 or len(seq) == 1:
        return seq
    else:
        mid = len(seq) // 2
        return merge(mergesort(seq[:mid]), mergesort(seq[mid:]))


# 2.1
def long_paths(tree: Tree, n: int):
    """Return a list of all paths in tree with length at least n.

    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    <0 1 2>
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 6 9>
    <0 11 12 13 14>
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 11 12 13 14>
    >>> long_paths(whole, 4)
    [Link(0, Link(11, Link(12, Link(13, Link(14)))))]
    """
    if tree.is_leaf():
        if n <= 0:
            return [Link(tree.label)]
        else:
            return []
    else:
        paths = []
        for b in tree.branches:
            b_paths = long_paths(b, n-1)
            paths += (b_paths)
        i = 0
        while i < len(paths):
            paths[i] = Link(tree.label, paths[i])
            i += 1
        return paths


# 2.2
def widest_level(t: Tree):
    """
    >>> sum([[1], [2]], [])
    [1, 2]
    >>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]),
    ...     Tree(4, [Tree(9, [Tree(2)])])])
    >>> widest_level(t)
    [1, 5, 9]
    """
    levels = []
    x = [t]
    while x:
        levels.append([node.label for node in x])
        x = sum([[sub_node for sub_node in node.branches] for node in x], [])
    return max(levels, key=lambda lst: len(lst))


# 3.1
def question_3_1_test():
    """
    >>> cats = [1, 2]
    >>> dogs = [cats, cats.append(23), list(cats)]
    >>> cats
    [1, 2, 23]
    >>> dogs[1] = list(dogs)
    >>> dogs[1]
    [[1, 2, 23], None, [1, 2, 23]]
    >>> dogs[0].append(2)
    >>> cats
    [1, 2, 23, 2]
    >>> cats[1::2]
    [2, 2]
    >>> cats[:3]
    [1, 2, 23]
    >>> dogs[2].extend([list(cats).pop(0), 3])
    >>> dogs[3]
    Traceback (most recent call last):
    ...
    IndexError: list index out of range
    >>> dogs
    [[1, 2, 23, 2], [[1, 2, 23, 2], None, [1, 2, 23, 1, 3]], [1, 2, 23, 1, 3]]
    """


# 3.2
def question_3_2_test(bake):
    s = [1]
    banana, bread = bake(s, [7, 2, s])


def bake(banana, bread):
    # _______________(____________(__________))  # This line is Multiple Choice
    banana.append(bread.append(1))      # A
    banana.extend([bread.extend([1])])  # C
    # Select all correct answers for the blank above
    # A. banana.append(bread.append(1))
    # B. bread.append(banana.append(1))
    # C. banana.extend([bread.extend([1])])
    # D. bread.extend([banana.extend([1])])
    bread += banana[: (len(banana) - 1)]
    banana.append(bread[bread[1]])
    return banana, bread


# 3.3
def question_3_3_test(bake):
    g = [1, 2, 3]
    skeld = amon(g)
    pink = skeld(1)
    purple = skeld(2)


def amon(g):
    n = 0

    def u(s):
        nonlocal n
        def f(x): return x + g.pop() + n
        n += 1
        return f(s)
    return u


# 4.1
def question_4_1_test():
    """
    >>> Emotion.num
    0
    >>> joy = Joy()
    >>> sadness = Sadness()
    >>> Emotion.num # number of Emotion instances created
    2
    >>> joy.power
    5
    >>> joy.catchphrase() # Print Joy's catchphrase
    Think positive thoughts
    >>> sadness.catchphrase() #Print Sad's catchphrase
    I'm positive you will get lost
    >>> sadness.power
    5
    >>> joy.feeling(sadness) # When both Emotions have same power value, print "Together"
    Together
    >>> sadness.feeling(joy)
    Together
    >>> joy.power = 7
    >>> joy.feeling(sadness) # Print the catchphrase of the more powerful feeling before the less powerful feeling
    Think positive thoughts
    I'm positive you will get lost
    >>> sadness.feeling(joy)
    Think positive thoughts
    I'm positive you will get lost
    """


class Emotion(object):
    num = 0

    def __init__(self):
        self.power = 5
        Emotion.num += 1

    def feeling(self, other):
        if self.power == other.power:
            print('Together')
        elif self.power > other.power:
            self.catchphrase()
            other.catchphrase()
        else:
            other.catchphrase()
            self.catchphrase()


class Joy(Emotion):
    def catchphrase(self):
        print('Think positive thoughts')


class Sadness(Emotion):
    def catchphrase(self):
        print("I'm positive you will get lost")


# 5.1
def remove_duplicates(lnk: Link) -> None:
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    """
    if lnk is Link.empty or lnk.rest is Link.empty:
        return
    else:
        if lnk.first == lnk.rest.first:
            lnk.rest = lnk.rest.rest
            remove_duplicates(lnk)
        else:
            remove_duplicates(lnk.rest)


# 6.1
def repeated(f):
    """
    >>> double = lambda x: 2 * x
    >>> funcs = repeated(double)
    >>> identity = next(funcs)
    >>> double = next(funcs)
    >>> quad = next(funcs)
    >>> oct = next(funcs)
    >>> identity(1)
    1
    >>> double(1)
    2
    >>> quad(1)
    4
    >>> oct(1)
    8
    >>> [g(1) for _, g in
    ...     zip(range(5), repeated(lambda x: 2 * x))]
    [1, 2, 4, 8, 16]
    """
    def g(x): return x
    while True:
        yield g
        g = (lambda last_g: lambda x: f(last_g(x)))(g)


# 6.2
# CAN'T WORK! (I also wirte answer like this......)
# The value g changes with each iteration so the bodies
# of the lambdas yielded change as well.


# 6.3
def accumulate(iterable, f):
    """
    >>> list(accumulate([1, 2, 3, 4, 5], add))
    [1, 3, 6, 10, 15]
    >>> list(accumulate([1, 2, 3, 4, 5], mul))
    [1, 2, 6, 24, 120]
    """
    it = iter(iterable)
    new_num = next(it)
    yield new_num
    for item in list(it):
        new_num = f(new_num, item)
        yield new_num
