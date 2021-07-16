def mutiply(n,m):
    """使用递归的方法计算两个整数的积

    Args:
        n (int): 整数
        m (int): 整数

    Returns:
        int: n*m
    """
    if m == 1:
        return n
    else:
        return mutiply(n,m-1) + n
    
def rec(x, y):
    if y <= 0:
        return 1
    else:
        return x * rec(x, y-1)


def hailstone(n):
    print(n)
    if n == 1:
        return
    elif is_even(n):
        return hailstone(n // 2)
    else:
        return hailstone(n*3+1)    

    

def is_even(n):
    return n % 2 == 0



####
# 1) we'll start off with something familiar. without looking at sum digits, 
#    implement the following function so that md(number) returns the PRODUCT of the 
#    digits of number.
#    
#    md(4023) -> 4 * 0 * 2 * 3 = 0
#    md(423) -> 4 * 2 * 3 = 24
####

def md(number):
    if number < 10 :
        return number
    else:
        return md(number//10)*(number%10)



####
# 2) Exponents are basically repeated multiplication! For example,
#    2^3 (2 to the power of 3) = 2 * 2 * 2 = 8
#    Basically, it's three 2's multiplied together.
#    We can write a function for this recursively! 
#    2 is the base, and 3 is the exponent in this case.
#    So, for base ^ exponent, write the following function that returns that value!
#    
#    HINT: remember when we did factorial, we thought about how we have to 
#    make the problem smaller, and tried to relate the smaller problem
#    to our original problem. That may help here!
#
#    rec_power(2, 3) = 2 * 2 * 2 = 8
#    rec_power(4, 2) = 4 * 4 = 16
#
####

def rec_power(base, exponent):
    if exponent == 0:
        return 1

    exponent = exponent - 1
    return base*rec_power(base, exponent)




####
# 3) Implement the following function so that count8(number)
#    counts the number of times the number "8" appears in number.
#    
#    I've given you parts of the base cases; if the number left is 8, we've
#    found an 8, so what should we return?
#    If the number left isn't 8, but can't be made any smaller, what should
#    we return then?
#
#    count8(3283) -> 1
#    count8(32883) -> 2
#    count8(8388) -> 3
####

def count8(number):
    if number == 8:
        return 1
    elif number < 10:
        return 0

    rightmost_digit = number % 10
    rest_of_number = number // 10

    if rightmost_digit == 8:
        return count8(rest_of_number)+1
    else:
        return count8(rest_of_number)



#  In game theory, a subtraction game is a simple game with two players, player 0 and player 1. At the beginning, there is a pile of n cookies. The players alternate turns; each turn, a player can take anywhere from 1 to 3 cookies. The player who takes the last cookie wins. Fill in the function can_win, which returns True if it is possible to win starting at the given number of cookies. It uses the following ideas:

# if the number of cookies is negative, it is impossible to win.
# otherwise, the current player can choose to take either 1, 2, or 3 cookies.
# evaluate each action: if that action forces the opponent to lose, then return True (since we can win)
# if none of the actions can force a win, then we can't guarantee a win.       

def can_win(number):
    """Returns True if the current player is guaranteed a win
    starting from the given state. It is impossible to win a game
    from an invalid game state.

    >>> can_win (-1) # invalid game state
    False
    >>> can_win (3) # take all three !
    True
    >>> can_win (4)
    False
    """
    "*** YOUR CODE HERE ***"

    if number == 0:
        return False
    else:
        action = 1
        while action <= 3:
            new_nubmer = number - action
            action += 1
            if not can_win(new_nubmer):
                return True
            return False
