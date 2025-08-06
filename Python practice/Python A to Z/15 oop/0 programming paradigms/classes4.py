class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def display(self):
        print(self.name, self.age, self.salary)

    def change_salary(self, salary):
        self.salary = salary    
    def __str__(self):
        return f"{self.name} {self.age} {self.salary}"

emp1 = Employee("John", 30, 5000)
emp1.display()
emp1.change_salary(6000)
emp1.display()
print(emp1)