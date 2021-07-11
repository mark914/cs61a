import doctest
def prime_factor(n):
    """Print the prime factor in non-decreasing order.
    
    >>> prime_factor(8)
    2
    2
    2
    >>> prime_factor(9)
    3
    3
    >>> prime_factor(858)
    2
    3
    11
    13
    >>> prime_factor(12)
    2
    2
    3
    >>> prime_factor(11)
    11
    """
    while n > 1:
        k = 2 
        while n % k != 0:
            k = k+1
        n = n // k
        print(k)


def summation(n, term):
	total, k = 0, 1
	while k <= n:
	    total, k = total + term(k), k + 1
	return total
	


def cube(x):
	return x*x*x
	
def sum_cubes(n):
	return summation(n, cube)


def area_shape(r,constant_area):
    assert r>0,'A length must be positive.'
    return r*r*constant_area

