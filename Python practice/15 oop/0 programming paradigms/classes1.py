class Companies:
    """Companies class"""
    # constructor
    def __init__(self, name, details, location):
        self.name = name
        self.details = details
        self.location = location
    
    # instance method
    def display(self):
        print(self.name, self.details, self.location)
    
class Employee:
    """Employee class"""
    # constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    # instance method
    def display(self):
        print(self.name, self.age, self.salary)
if __name__ == "__main__":
    comp = Companies("Google", "Tech", "USA")
    emp = Employee("Faruk", 21, 1000)
    print(getattr(emp, "name"))       # "Faruk" print
    print(hasattr(emp, "age"))        # True return
    print(setattr(emp, "salary", 2000))  # Nothing return, but salary update
    # print(delattr(emp, "salary"))    # salary delete
    print(emp.__dict__)              # All attribute dictionary show
    print(emp.__doc__)               # class docstring show → "Employee class"
    print(emp.__module__)            # __main__ show because it is a script
    print(emp.__class__)             # Employee class show
    print(Employee.__name__)              # __name__ show because it is a script
    print(Employee.__module__)            # __main__ show because it is a script
    print(Employee.__class__)             # Employee class show
    print(Employee.__str__(emp))             # Employee class show
    print(isinstance(emp, Employee))             # True show
    print(issubclass(Employee, object))             # True show
    print(issubclass(Employee, Employee))             # True show
    comp.display()                    
    emp.display()

