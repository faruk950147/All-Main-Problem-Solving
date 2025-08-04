class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def register(self):
        print(f"{self.name} is registered")
        return True
    
    def login(self):
        print(f"{self.name} is logged in")
        return True

class Student(User):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll
    
    def enroll(self):
        print(f"{self.name} is enrolled")
        return True 
s = Student("Faruk", 22, 123456)
s.register()
s.login()
s.enroll()