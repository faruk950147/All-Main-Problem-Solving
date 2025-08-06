class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def display(self):
        print(self.name, self.age, self.salary)
        
class Changes:
    @staticmethod
    def increment_salary(obj, amount):
        obj.salary += amount
        obj.display()

if __name__ == "__main__":
    emp = Employee("Faruk", 21, 1000)
    Changes.increment_salary(emp, 1000)
