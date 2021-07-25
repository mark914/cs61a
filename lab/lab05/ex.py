import builtins
from lab05 import *

def add_tree(t1,t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    def build_branches(bs1, bs2):
        if min(len(bs1), len(bs2)) == 0:
            return []
        f = add_tree(bs1[0], bs2[0])
        return [f] + build_branches(bs1[1:], bs2[1:])

    
    result_label = label(t1)+label(t2)
    result_branch = build_branches(branches(t1), branches(t2))
    i = len(branches(result_branch))
    result_branch = result_branch+[branches(t1)[i:]]
    result_branch = result_branch+[branches(t2)[i:]]

    return tree(result_label, result_branch)