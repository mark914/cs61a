def count_stair_ways(n):
    """count the number of ways to get stair with n steps.

    Args:
        n (int): positive

    Returns:
        int: the number of ways to get n steps.
    >>>count_stair_ways(1)
    1
    >>>count_stair_ways(2)
    2
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)

#1.2
def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return sum([count_k(n-x, k) for x in range(1,k+1)])
    #思路确实不太好建立，只能运用推理的方法，一步一步来


#list slicing
lst = [1, 2, 3, 4, 5]
lst[:]
lst[1::2]
lst[0::2]
lst[::-1]
#lst[start:end:step]

#2.2
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    
    return  [i*s[i] for i in range(len(s)) if i%2==0]
    #说实话，这个是看着答案写的。有两个变量，一个是index，一个是x对应数值，


def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    elif len(s) <= 2:
        return max(s)
    else:
        a = s[0]*max_product(s[2:]) #要保证s[2]存在，因此len(s)>=3
        b = max_product(s[1:])
        return max(a,b)