from trees import *


# 1.1
def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        return max([height(b) for b in branches(t)]) + 1


# 1.2
def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    else:
        return label(t) + max([max_path_sum(b) for b in branches(t)])


# 1.3
def square_tree(t):
    """Return a tree with the square of every element in t

    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    if is_leaf(t):
        return tree(label(t) ** 2)
    else:
        return tree(label(t) ** 2, [square_tree(b) for b in branches(t)])


# 1.4
def find_path(tree, x):
    """
    >>> t = tree(6, [tree(7, [tree(5)])])
    >>> find_path(t, 5)
    [6, 7, 5]
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    # Version1
    # if label(tree) == x:
    #     return [x]
    # elif not is_leaf(tree):
    #     path = [find_path(b, x) for b in branches(tree) if find_path(b, x)]
    #     if path != []:
    #         return [label(tree)] + path[0]

    if label(tree) == x:
        return [x]
    elif not is_leaf(tree):
        path = []
        for b in branches(tree):
            new_path = find_path(b, x)
            path += new_path if new_path != None else []
        return [label(tree)] + path if path != [] else None


# 2.2
# wrong
def prune_binary(t, nums):
    """
    >>> t = tree("1", [tree("0", [tree("0"), tree("1")]), tree("1", [tree("0")])])
    >>> print_tree(prune_binary(t, ["01", "110", "100"]))
    1
      0
        0
      1
        0
    """
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        # next_valid_nums = [num[1:] for num in nums]
        next_valid_nums = [num[1:] for num in nums if num[0] == label(t)]
        new_branches = []
        for b in branches(t):
            pruned_branch = prune_binary(b, next_valid_nums)
            if pruned_branch is not None:
                new_branches = new_branches + [pruned_branch]
        if not new_branches:
            return None
        # return new_branches
        return tree(label(t), new_branches)
