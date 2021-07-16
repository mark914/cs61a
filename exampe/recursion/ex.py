def sum_list(x):
    """compute the sum of a list

    Args:
        x (list): 列表

    Returns:
        int: integer
    """
    if x == []:
        return 0
    else:
        return x[0] + sum_list[1:]

def sum_range(n):
    """compute the sum of range(n)

    Args:
        n (int): non-negative integer

    Returns:
        int: sum of range(n)
    """
    return sum_list(list(range(n+1)))

