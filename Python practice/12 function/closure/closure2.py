# Closure in Python (Function Closures)
# Closure means:
# A inner function, which can hold outer function's variable or state, even after outer function execution has finished.
# this is most common use of closure
# Example:
num1 = 10
num2 = 20

# def sum(): # outer function not a closure
#     return num1 + num2 # inner function
# # this is most common use of closure
# func = sum()
# print(func)

#it is a closure because num1 and num2 are in the scope of add3
# def add3() :
#     num3 = 50
#     return  lambda : num1 + num2 + num3
# # this is most common use of closure
# sum3 = add3()
# print(dir(sum3))
# print(sum3())

# def Checker():
#     num = 10
#     def CheckNumber(num2):
#         return num + num2
#     return CheckNumber

# func = Checker()
# print(func(20))
# print(dir(func))

# def Counter():
#     count = 0
#     def Increment():
#         nonlocal count
#         count += 1
#         return count
#     return Increment

# func = Counter()
# print(func())
# print(func())
# print(func())





def Checker():
    num = 10
    def CheckNumber(num2):
        return num + num2
    return CheckNumber

func = Checker()
print(func(20))
print(dir(func))

