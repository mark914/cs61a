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



def mysum(list):
    """compute the sum of elements in list

    Args:
        list (list):list
    >>> mysum([1,2,3])
    6   
    >>> mysum([1])
    1
    """
    if list == []:
        return 0
    return list[0]+mysum(list[1:])

def reverse(str):
    """reverse the string

    Args:
        str (str): string

    >>> reverse('abc')
    'cba'
    >>> reverse('a')
    'a'
    """
    if str == "":
        return ""
    else:
        return reverse(str[1:])+str[0]