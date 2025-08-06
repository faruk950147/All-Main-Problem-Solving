# Closure in Python (Function Closures)
# Closure means:
# A inner function, which can hold outer function's variable or state, even after outer function execution has finished.
# Example:


# jodi outer function er variable k inner function er moddhe hold kore rakhe mane inner function return korbe function er variable k hold kore rakhe
a = 10
b = 20
def sum(): # outer function not a closure
    return a + b # inner function
# this is most common use of closure
func = sum()
print(func)

# def outer():
#     x = 10
#     def inner():
#         print(x)
#     return inner
# this is most common use of closure
# func = outer()


# def outer(x):
#     def inner(y):
#         return x + y
#     return inner



# this is most common use of closure
# closure_func = outer(10) # eivabe outer function er variable k inner function er moddhe hold kore rakhe mane inner function return korbe  function er variable k hold kore rakhe
# print(dir(closure_func))   # Output: ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']



def Checker():
    num = 10
    def CheckNumber(num2):
        return num + num2
    return CheckNumber

func = Checker()
print(func(20))
print(dir(func))