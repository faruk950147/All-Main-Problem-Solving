# normal function example
def greet(name):
    print(f"Hello, {name}!")   
s = "Bangladesh"
greet(s)

def two():
    print("I'm from two")

def one():
    print("I'm from one")
two()
one()

# Higher Order Function Example
def two():
    print("I'm from two")

def one(func):
    print("I'm from one")
    func()

one(two)
print("I'm from memory location", two)


# Decorator Example
def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper
@decorator
def my_function():
    print("Hello, World!")

my_function()

def my_decorator(func):
    def wrapper(name):
        print("Before function")
        func(name)
        print("After function")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Tuhin")

def get_int_as_str(number):
    return str(number)
print(get_int_as_str(22))

def print_int(my_func,number):
    print(my_func(number))
    return
print_int(get_int_as_str,99)