    """迭代法求某数的平方根
    """
# def square_root(a):
#     x = 1
#     while x*x != a:
#         x = square_root_update(x,a)
#     return a

def square_root_update(x,a):
    return (x + a/x)/2
    

# def cube_root(a):
#     x = 1
#     while x*x*x != a:
#         x = cube_root_update(x,a)
#     return x

def cube_root_update(x,a):
    return (2*x + a/(x*x))/3


def improve(close,update,guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance = 1e-15):
    return abs(x-y) < tolerance


def square_root(a):
    def close(x):
        return approx_eq(x*x, a)
    def update(x):
        return square_root_update(x,a)
    return improve(close,update)


def cube_root(a):
    def close(x):
        return approx_eq(x*x*x, a)
    def update(x):
        return cube_root_update(x, a)
    return improve(close, update)

        """只要得到的函数是最终想要的就可以了，在函数内定义函数，这样就能够
        在函数环境内使用变量，从而可以少定义几个变量。
        """