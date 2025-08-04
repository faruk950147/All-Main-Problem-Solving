# def decorator(callback):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         callback(*args, **kwargs)
#         print("Something is happening after the function is called.")
#     return wrapper


# @decorator
# def say_hello(name):
#     print(f"Hello, {name}!")

# say_hello("Alice")

def decorator(callback):
    def wrapper():
        print("Before the function call")
        callback()
        print("After the function call")
    return wrapper


@decorator
def my_function():
    print("Hello, World!")

my_function()

# Decorator with arguments
def decorator(callback):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        callback(*args, **kwargs)
        print("After the function call")
    return wrapper

@decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
