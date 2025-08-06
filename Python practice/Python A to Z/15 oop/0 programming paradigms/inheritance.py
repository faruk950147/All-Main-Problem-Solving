# Inheritance is a way of creating a new class from an existing class
# Inheritance is a way of reusing the code

class University:
    def __init__(self, department, location):
        self.department = department
        self.location = location
        print("Constructor called")
    
    def get_department(self):
        return self.department
    
    def get_location(self):
        return self.location
        
class Teacher(University):
    def __init__(self, department, name):
        self.department = department
        self.name = name
        print("Teacher constructor called")
    
    def display(self):
        print(self.name, self.department)

# Create an object of Teacher
teacher = Teacher("CSE", "John")
teacher.display()
