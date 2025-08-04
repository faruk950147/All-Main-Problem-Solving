def decorator1(callback):
    def wrapper():
        return callback().capitalize()
    return wrapper # must return wrapper

def decorator2(callback):
    def wrapper():
        return callback().lower()
    return wrapper # must return wrapper

def decorator3(callback):
    def wrapper():
        return callback().upper()
    return wrapper # must return wrapper

def decorator4(callback):
    def wrapper():
        return callback().swapcase()
    return wrapper # must return wrapper

def decorator5(callback):
    def wrapper():
        return callback().title()
    return wrapper # must return wrapper

def decorator6(callback):
    def wrapper():
        return callback().casefold()
    return wrapper # must return wrapper


def decorator7(callback):
    def wrapper():
        return callback().split()
    return wrapper # must return wrapper

def decorator8(callback):
    def wrapper():
        return callback().strip()
    return wrapper # must return wrapper
# calling
def display():
    return "Hello World"

print(decorator1(display)())
print(decorator2(display)())
print(decorator3(display)())
print(decorator4(display)())
print(decorator5(display)())
print(decorator6(display)())
print(decorator7(display)())
print(decorator8(display)())
