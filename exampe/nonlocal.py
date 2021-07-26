def make_withdraw(balance):
    def withdraw(amount):
        if amount > balance:
            return 'Insufficient funds'
        balance1 = balance - amount
        return balance1
    return withdraw

wd = make_withdraw(20)
wd(5)
wd(3)
