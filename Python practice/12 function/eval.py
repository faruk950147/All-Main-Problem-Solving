# eval is a built-in function in Python that takes a string as input and evaluates it as a Python expression.
# syntax: eval(expression, globals=None, locals=None)
    # expression: a string containing a Python expression to evaluate
    # globals: an optional dictionary containing global variables to be used in the expression
    # locals: an optional dictionary containing local variables to be used in the expression
    # example: eval('2 + 2')
    # return: the result of evaluating the expression

# Example:
# x = 5
# print(type(eval('x + x')))
# print(eval('x + x'))
# output:
# <class 'int'>
# 10

# # Example:
# x = 1
# y = 2
# print(type(eval('x + y', {'x': x, 'y': y})))
# print(eval('x + y', {'x': x, 'y': y}))
# output:
# <class 'int'>
# 3

# # Example:
# x = 1
# y = 2
# print(type(eval('x + y', {'x': x, 'y': y}, {'x': x, 'y': y})))
# print(eval('x + y', {'x': x, 'y': y}, {'x': x, 'y': y}))
# output:
# <class 'int'>
# 3

# string = 'Hello World'
# str1 = eval('string')
# print(type(str1))
# print(str1)
# # output:
# # <class 'str'>
# # Hello World

# list1 = eval('[1, 2, 3, 4, 5]+[6, 7, 8, 9, 10]')
# print(type(list1))
# print(list1)
# output:
# <class 'list'>
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def password():
    print("Secret Password  1234")

def solved():
    eq = input("Enter the equation in the form of x: ")
    value = int(input("Enter the value of x: "))
    answer = eval(eq, {'x': value})
    print(f"Answer: {answer}")

solved()



    