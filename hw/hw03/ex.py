from lab05 import *

def min_depth(t):
    if is_leaf(t):
        return 0
    return 1 + min([min_depth(b) 
                    for b in branches(t)])
