def fib(n):
    """用来计算斐波那契数列"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-2)+fib(n-1)


def count(f):
    """相当于一个修饰器，用来数总共调用了多少次函数f"""
    def counted(*arg):
        counted.call_count += 1
        return f(*arg)
    counted.call_count = 0
    return counted


def memo(f):
    """相当于一个修饰器，用来减少函数的重复"""
    cache = {}
    def memoization(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoization


def space_count(f):
    def counted(n):
        counted.open_envir += 1
        if counted.open_envir > counted.max_envir:
            count.max_envir = count.open_envir
        result = f(n)
        counted.open_envir -= 1
        return result
    counted.open_envir = 0
    counted.max_envir = 0
    return counted