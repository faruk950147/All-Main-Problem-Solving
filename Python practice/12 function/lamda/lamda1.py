#============================= this is example in convert lambda to function 1 =============================
# def wrapper():
#     def add(a, b):
#         return a + b
#     return add
# print(wrapper()(10, 20))

# wrapper = wrapper()
# print(wrapper(10, 20))

# def add(a, b):
#     def sub(x, y):
#         return x - y
#     print("Calling inner sub():", sub(a, b))  # inner function called here
#     return a + b


# result = add(10, 20)
# print("Result from add():", result)

# def add(a, b):
#     def sub(a, b):
#         print("Inner result (bad):", a - b)
#     sub(a, b)  # directly calling sub inside
#     return a + b

# add = add(10, 20)
# print("Add:", add)

#============================= this is example in convert lambda to function 2 =============================
def add(a, b):
    return a + b

print((lambda a, b: a + b)(10, 20))

#============================= this is example in convert lambda to function 3 =============================
def outer():
    return lambda a, b: a + b

print(outer()(10, 20))

#============================= this is example in convert lambda to function 4 =============================
print((lambda:lambda a, b: a + b)(10, 20))

#============================= this is example in convert lambda to function 5 =============================