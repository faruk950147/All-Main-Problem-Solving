# An instance method is a method that is bound to the instance of the class.
# Instance methods can access and modify instance variables using 'self'.
# Instance methods can also access and modify class variables using 'self.__class__' or by referencing the class name directly.
# Instance methods do not take 'cls' as the first argument — they take 'self'.
# bound means method of object/class automatically connected (associated) to the object/class

class University:
    university_name = "AUST University Bangladesh"  # class variable

    def __init__(self, department, location):
        self.department = department  # instance variable
        self.location = location      # instance variable

    def display(self):
        # Instance method to print instance-specific data
        print(self.department, self.location)

    def __str__(self):
        # Instance method to return a string representation of the object
        return f"{self.university_name} {self.department} {self.location}"

# Instance methods can be called using an object of the class
uni = University("CSE", "Dhaka")
uni.display()  # Output: CSE Dhaka
print(uni)      # Output: AUST University Bangladesh CSE Dhaka
