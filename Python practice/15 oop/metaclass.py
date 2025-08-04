# class A(object):
#     pass
# python 3 automatically inherit from object
class A:
    def __init__(self):
        pass

class B:
    def __call__(self, *args, **kwargs):
        return super(B, self).__call__(self, *args, **kwargs)

a = A()
b = B()

print(a)
print(b)