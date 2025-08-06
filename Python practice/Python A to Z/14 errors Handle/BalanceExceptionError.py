# user defined exceptions


class BalanceExceptionError(Exception):
    """Balance Exception Error"""
    pass

try:
    balance = 100
    withdraw_amount = int(input("Enter a number: "))
    if withdraw_amount > balance:
        raise BalanceExceptionError("Balance Exception Error")
    print("Withdrawal successful")
except BalanceExceptionError as e:
    print(e)


def withdraw(balance, withdraw_amount):
    if withdraw_amount > balance:
        raise BalanceExceptionError("Balance Exception Error")
    return balance - withdraw_amount

try:
    balance = 100
    withdraw_amount = int(input("Enter a number: "))
    print(withdraw(balance, withdraw_amount))
except BalanceExceptionError as e:
    print(e)
