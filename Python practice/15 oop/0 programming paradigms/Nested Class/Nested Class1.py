class Student:
    def __init__(self, name, roll, age, day, month, year):
        self.name = name
        self.roll = roll
        self.age = age
        self.dob = self.DOB(day, month, year)
    
    class DOB:
        def __init__(self, day, month, year):
            self.day = day
            self.month = month
            self.year = year
            
        def display(self):
            print(f"DOB: {self.day}/{self.month}/{self.year}")
            
s1 = Student("Omar", 101, 22, 1, 1, 2000)
s1.dob.display()
        
        