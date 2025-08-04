# Decorators are used to modify the behavior of a function or method
# Decorators are used to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it
# Decorators are usually called before the definition of a function you want to decorate

class Decorator(object):
    def __init__(self, func):
        self.function = func

    def __call__(self, *args):
        try:
            # If any argument is string, raise TypeError
            if any([isinstance(i, str) for i in args]):
                raise TypeError("Cannot pass string as arguments")
            else:
                return self.function(*args)
        except Exception as obj:
            print(obj)

# Function decorated with Decorator
@Decorator
def add(*args):
    sum1 = 0
    for num in args:
        sum1 = sum1 + num
    return sum1

# Valid call (no string, only integers)
print(add(10, 20, 30))  # Output: 60

# Invalid call (contains a string)
print(add(10, '20', 30))  # Output: Cannot pass string as arguments
