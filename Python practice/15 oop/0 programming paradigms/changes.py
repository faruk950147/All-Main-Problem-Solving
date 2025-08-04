class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def display(self):
        print(self.name, self.age, self.salary)
        
if __name__ == "__main__":
    emp = Employee("Faruk", 21, 1000)
    emp.display()
    # Add a new attribute
    emp.gender = "Male"
    emp.display()
    # Update an attribute
    emp.name = "Omar"
    emp.age = 22
    emp.salary = 2000
    emp.display()
    # Delete an attribute
    del emp.gender
    emp.display()