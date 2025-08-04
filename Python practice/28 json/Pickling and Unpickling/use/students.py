class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        
    def display(self):
        return (f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}")
    