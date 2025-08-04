class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("I'm from constructor")
    
    def add(self):
        print("I'm from add")
        return self.a + self.b
    
    def sub(self):
        print("I'm from sub")
        return self.a - self.b
    
    def mul(self):
        print("I'm from mul")
        return self.a * self.b
    
    def div(self):
        print("I'm from div")
        return self.a / self.b
    
    def mod(self):
        print("I'm from mod")
        return self.a % self.b
    
    def pow(self):
        print("I'm from pow")
        return self.a ** self.b
    
    def floor_div(self):
        print("I'm from floor_div")
        return self.a // self.b
    
    def __str__(self):
            return f"Math({self.a}, {self.b})"
    
if __name__ == "__main__":
    math = Math(10, 20)
    print(math.add())
    print(math.sub())
    print(math.mul())
    print(math.div())
    print(math.mod())
    print(math.pow())
    print(math.floor_div())
    print(math.__str__())