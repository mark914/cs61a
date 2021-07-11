def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    temp = 1
    while k >= 1:
        temp = temp*n
        n -= 1
        k -= 1
    return temp



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"

    sum_num = 0 
    while (y>0):
        remainder = y%10
        y = y//10
        sum_num = sum_num + remainder
    
    return sum_num

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    n = str(n)
    if '88' in n:
        return True
    else:
        return False


def prime_factors(n):
    """Print the prime factor in non-decreasing order.
    
    >>>prime_factors(8)
    2
    2
    2
    >>>prime_factor(9)
    3
    3
    3
    >>>prime_factor(858)
    2
    3
    11
    13
    >>>prime_factor(12)
    2
    3
    4
    >>>prime_factor(11)
    11    
    """
    while n > 1:
        k = 2 
        while n % k != 0:
            k = k+1
        n = n // k
        print(k)