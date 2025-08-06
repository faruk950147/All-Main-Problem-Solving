# LEGB Rules
# L: Local
# E: Enclosing
# G: Global
# B: Built-in

# LEGB Rules is used to find the variable
# LEGB Rules is used to find the function
# all are scopes in python are variables

# num1 = 90 # global scope
# def display():
#     global num1 # global keyword and built-in scope
#     num1 += 10 # global scope
#     print("num in function global",num1)
#     num1 = 20 # local scope
#     print("Hello",num1)

# display()
# print("num in outside",num1)

def wrapper():
    num = 10 # Nonlocal scope
    def display():
        nonlocal num
        num+=30
        print("num in function nonlocal",num)
        num = 20 # local scope
        print("num in function local",num)
    display()
wrapper()
