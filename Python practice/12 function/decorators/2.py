def decorator(callback):
    def wrapper(*args):
        print("Something is happening before the function is called.")
        result = callback(*args)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@decorator
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5))

    