def f(x):
    return x + 1

def g(x):
    return x*x

def compose1(f,g):
    """返回一个复合函数

    Args:
        f (int): 加一
        g (int): 平方
    
    >>> compose1(f,g)(1)
    >>> 2

    """
    def h(x):
        return f(g(x))
    return h




def compose11(f,g):
    return lambda x: f(g(x))

h = compose11(lambda x: x+1, lambda x: x*x)

