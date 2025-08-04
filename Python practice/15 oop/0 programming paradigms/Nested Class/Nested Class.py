class Outer:
    def __init__(self):
        self.inner = self.Inner()
    
    def show(self):
        print("Outer class")
    
    class Inner:
        def __init__(self):
            print("Inner class")
        
        def show(self):
            print("Inner class")

if __name__ == "__main__":
    outer = Outer()
    outer.show()
    inner = outer.inner
    inner.show()
