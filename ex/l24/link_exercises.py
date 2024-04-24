# Linked lists
def ordered(s):
    """Is Link s ordered?

    >>> ordered(Link(1, Link(3, Link(4))))
    True
    >>> ordered(Link(1, Link(4, Link(3))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))))
    False
    >>> ordered(Link(-4, Link(-1, Link(3))))
    True
    """
    if s is Link.empty or s.rest is Link.empty:
        return True
    elif s.first > s.rest.first:
        return False
    else:
        return ordered(s.rest)


def ordered_key(s, key=lambda x: x):
    """Is Link s ordered?

    >>> ordered_key(Link(1, Link(3, Link(4))))
    True
    >>> ordered_key(Link(1, Link(4, Link(3))))
    False
    >>> ordered_key(Link(1, Link(-3, Link(4))))
    False
    >>> ordered_key(Link(1, Link(-3, Link(4))), key=abs)
    True
    >>> ordered_key(Link(-4, Link(-1, Link(3))))
    True
    >>> ordered_key(Link(-4, Link(-1, Link(3))), key=abs)
    False
    """
    if s.rest is Link.empty:
        return True
    elif key(s.first) > key(s.rest.first):
        return False
    else:
        return ordered_key(s.rest, key)


def merge(s, t):
    """Return a sorted Link containing the elements of sorted s & t.

    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(5))
    >>> b
    Link(1, Link(4))
    """
    # if s is Link.empty:
    #     return t
    # elif t is Link.empty:
    #     return s
    # elif s.first == t.first:
    #     return Link(s.first, Link(t.first, merge(s.rest, t.rest)))
    # elif s.first < t.first:
    #     return Link(s.first, merge(s.rest, t))
    # else:
    #     return Link(t.first, merge(s, t.rest))

    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, merge(s, t.rest))


def merge_in_place(s, t):
    """Return a sorted Link containing the elements of sorted s & t.

    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge_in_place(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(1, Link(4, Link(5))))
    >>> b
    Link(1, Link(4, Link(5)))
    """
    # def helper(last_s, last_t, merged):
    #     if merged is Link.empty:
    #         if last_s.first < last_t.first:
    #             merged = last_s
    #             last_s = last_s.rest
    #         else:
    #             merged = last_t
    #             last_t = last_t.rest
    #         merged.rest = Link.empty
    #     elif last_s is Link.empty:
    #         merged.rest = t
    #     elif last_t is Link.empty:
    #         merged.rest = s
    #     elif last_s.first < last_t.first:
    #         merged.rest = last_s
    #         last_s = last_s.rest
    #         merged = merged.rest
    #     elif last_s.first > last_t.first:
    #         merged.rest = last_t
    #         last_t = last_t.rest
    #         merged = merged.rest
    #     else:
    #         merged.rest = last_s
    #         last_s = last_s.rest
    #         merged.rest.rest = last_t
    #         last_t = last_t.rest
    #         merged = merged.rest.rest
    #     helper(last_s, last_t, merged)
    # helper(s, t, Link.empty)
    # return s
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge_in_place(s.rest, t)
        return s
    else:
        t.rest = merge_in_place(s, t.rest)
        return t


class Link:
    """A linked list.

    >>> Link(1, Link(2, Link(3)))
    Link(1, Link(2, Link(3)))
    >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> s
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(s)
    <1 <2 3> 4>
    """

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
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
