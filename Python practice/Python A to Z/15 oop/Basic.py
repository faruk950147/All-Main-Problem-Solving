class Student:
    def __init__(self, name, age, gender, roll, cgpa,department):
        self.name = name
        self.age = age
        self.gender = gender
        self.roll = roll
        self.cgpa = cgpa
        self.department = department
        
    def display(self):
        print("\n",self.name, "\n", self.age, "\n", self.gender, "\n", self.roll, "\n", self.cgpa, "\n", self.department)
            
if __name__ == "__main__":
    student1 = Student(input("Enter name: "), input("Enter age: "), input("Enter gender: "), input("Enter roll: "), input("Enter cgpa: "), input("Enter department: "))
    student1.display()
    print(student1.__dict__)

    