# Partial Function is a function that is used to fix the number of arguments of a function
from functools import partial

def add(x, y):
    return x + y
display = partial(add, 10)
print(display(20))
