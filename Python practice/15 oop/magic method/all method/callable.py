# Callable object is an object that can be called as a function

# work: Check if object is callable (like function)
# callable() # return True or False it's a built-in function in Python

# Example:
def add(a, b):
    return a + b
print(callable(add))
print(add(1, 2))
