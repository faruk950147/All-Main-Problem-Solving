def decorator1(callback):
    def wrapper(*args):
        for i in args:
            if not isinstance(i, int):
                raise ValueError("All arguments must be integers")
        return callback(*args)
    return wrapper

def decorator2(callback):
    def wrapper(*args):
        for i in args[1:]:
            if i == 0:
                raise ValueError("All arguments must be non-zero")
        return callback(*args)
    return wrapper

def decorator3(callback):
    def wrapper(*args):
        for i in args[1:]:
            if i < 0:
                raise ValueError("All arguments must be non-negative")
        return callback(*args)
    return wrapper

# @decorator1
# def add(*args):
#     return sum(args)

# @decorator2
# def sub(*args):
#     return args[0] - sum(args[1:])

# @decorator3
# def div(*args):
#     return args[0] / sum(args[1:])
# print(add(1, 2, 3, 4, 5))
# print(sub(1, 2, 3, 4, 5))
# print(div(1, 2, 3, 4, 5))

@decorator1
def add(a, b):
    return a + b

@decorator2
def sub(a, b):
    return a - b

@decorator3
def div(a, b):
    return a / b

print(add(1, 2))
print(sub(1, 2))
print(div(1, 2))