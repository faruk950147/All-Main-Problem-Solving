# Property Decorator


class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # this is not a proper way to create an email because if we change the first_name or last_name, the mail will not change
        # self.mail = f"{first_name.lower()}.{last_name.lower()}@email.com"
        
    @property
    def mail(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@email.com"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @full_name.setter
    def full_name(self, name): # Ensure that function name is same as the property name
        first_name, last_name = name.split(" ") # split the name into first_name and last_name respectively
        self.first_name = first_name
        self.last_name = last_name
        
    @full_name.deleter
    def full_name(self): # Ensure that function name is same as the property name
        self.first_name = None
        self.last_name = None
    
emp1 = Employee("Jane", "Dawson")
emp2 = Employee("Bob", "Smith")
emp3 = Employee("Charlie", "Brown")

emp1.first_name = "John"
print(emp1.first_name)
print(emp1.mail)
print(emp1.full_name)
emp1.full_name = "Alice Johnson"
print("after setting full name")
print(emp1.full_name)
print(emp1.mail)
print('-' * 50)


