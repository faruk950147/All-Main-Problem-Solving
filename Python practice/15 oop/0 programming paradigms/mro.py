# Method Resolution Order (MRO)
class A:
    def show(self):
        print("I'm from class A")

class B(A):
    def show(self):
        print("I'm from class B")

class C(A):
    def show(self):
        print("I'm from class C")

class D(B, C):  # Multiple Inheritance
    pass

obj = D()
obj.show()