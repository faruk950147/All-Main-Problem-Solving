# A constructor is a special method that is called when an object is created.
# constructor is used to initialize the object
# without constructor object will not be created
# constructor is called automatically when object is created
class BankAccount:
    # default constructor working here
    def account(self):
        print("Account created")

    def deposit(self):
        print("Deposit made")

class University:
    # parameterized constructor working here
    def __init__(self, department, location):
        self.department = department
        self.location = location
        print("Constructor called")

uni = University("CSE", "Dhaka")

class Car:
    # non parameterized constructor working here
    def __init__(self):
        self.brand = "Toyota"
        self.model = "Camry"
        print("Car created")

    def display(self):
        print(self.brand, self.model)

# object creation
car = Car()
car.display()
