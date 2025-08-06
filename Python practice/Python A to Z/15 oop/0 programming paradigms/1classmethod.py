# A class method is a method that is bound to the class and not the instance.
# A class method receives the class itself as the first argument (usually named 'cls').
# A class method can access and modify class variables that are shared across all instances.

class University:
    university_name = "AUST University Bangladesh"  # class variable

    def __init__(self, department, location):
        self.department = department  # instance variable
        self.location = location      # instance variable

    @classmethod
    def get_university_name(cls):
        # This is a class method because it takes 'cls' as the first parameter.
        # It accesses the class variable using 'cls'.
        return cls.university_name

    def display(self):
        # Instance method to print instance-specific data
        print(self.department, self.location)

    def __str__(self):
        # Instance method to return a string representation of the object
        return f"{self.university_name} {self.department} {self.location}"
