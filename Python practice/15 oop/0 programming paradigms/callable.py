# Callable is an object that can be called as a function
# x = 5
# print(callable(x))
# def add(a, b):
#     return a + b
# print(callable(add))
# print(add(1, 2))

class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self, *args, **kwargs):
        return self.a + self.b + args[0] + kwargs["c"] + kwargs["d"]

add = Add(1, 2)
print(callable(add))
print(add(1, c=2, d=3))

# class Add:
#     def __call__(self, a, b):
#         return a + b

# add = Add()
# print(callable(add))
# print(add(1, 2))