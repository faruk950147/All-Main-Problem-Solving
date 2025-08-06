# Decorators in Python
# decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
# def decorator(callback):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         callback() # exiting functionality
#         # adding new functionality
#         print("Something is happening after the function is called.")
#     return wrapper # must return wrapper

# @decorator # first way for decorator calling
# def display():
#     print("Display function.")

# display()

# display = decorator(display) # second way for decorator calling
# display()


def decorator(callback):
    def wrapper(num):
        sum = callback(10, 20)  # existing functionality
        print("Sum is:", sum + num)   # new functionality
    return wrapper

@decorator
def add(a, b):
    return a + b

add(60)

