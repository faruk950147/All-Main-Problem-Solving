# Destructor is a special method that is called when an object is destroyed
# Destructor is used to perform cleanup activities
# Destructor is called automatically when object is destroyed

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def display(self):
        print(self.name, self.age, self.salary)
    
    # Destructor
    def __del__(self):
        print("Object Destroyed")

if __name__ == "__main__":
    emp = Employee("Faruk", 21, 1000)
    emp.display()
    del emp