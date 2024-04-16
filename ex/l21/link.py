class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += (str(self.first) + ' ')
            self = self.rest
        return string + str(self.first) + '>'


def empty(s):
    return s is Link.empty


def range_link(start, end):
    """Return a Link containing consecutive integers from start to end.

    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start+1, end))


def map_link(f, s):
    """Return a Link that contains f(x) for each x in Link s.

    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))


def filter_link(f, s):
    """Return a Link that contains only the elements x of Link s for which f(x)
    is a true value.

    >>> filter_link(odd, range_link(3, 6))
    Link(3, Link(5))
    """
    if s is Link.empty:
        return Link.empty
    filtered_rest = filter_link(f, s.rest)
    if f(s.first) == True:
        return Link(s.first, filtered_rest)
    else:
        return filtered_rest


square, odd = lambda x: x * x, lambda x: x % 2 == 1


def add(s, v):
    """Add v to an ordered list s with no repeats, returning modifieds.

    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 3)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(4, Link(5)))))
    >>> add(s, 6)
    Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))))))
    """

    # my solution (have unsolvable that s is a local variable.)
    # print(repr(s))
    # iterator = s
    # if s.first > v:
    #     s = Link(v, s)
    # else:
    #     while iterator.rest != Link.empty and iterator.rest.first < v:
    #         print(iterator.rest.first)
    #         iterator = s.rest
    #     if iterator.rest.first != v:
    #         new_rest = Link(v, iterator.rest)
    #         iterator.rest = new_rest
    # print(repr(s))
    # return s

    assert s is not Link.empty
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and empty(s.rest):
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s
