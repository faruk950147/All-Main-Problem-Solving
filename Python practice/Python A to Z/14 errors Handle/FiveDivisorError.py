# user defined exceptions

class FiveDivisorError(Exception):
    """Five Divisor Error"""
    pass

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    if num2 == 5:
        raise FiveDivisorError("Five Divisor Error")
    print(num1 / num2)
except (FiveDivisorError, ZeroDivisionError) as e:
    print(e)


def divide(num1, num2):
    if num2 == 5:
        raise FiveDivisorError("Five Divisor Error")
    return num1 / num2

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    print(divide(num1, num2))
except (FiveDivisorError, ZeroDivisionError) as e:
    print(e)