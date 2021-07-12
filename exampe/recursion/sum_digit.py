def split(n):
    return n // 10, n % 10

def sum_digit(n):
    if n<10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digit(all_but_last) + last

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return lugh_sum_double(all_but_last) + last

def lugh_sum_double(n):
    all_but_last, last = split(n)
    lugh_digit = sum_digit(2*last)
    if n < 10:
        return  lugh_digit 
    else:
        return luhn_sum(all_but_last) + lugh_digit