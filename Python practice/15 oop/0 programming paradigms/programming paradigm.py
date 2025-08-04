# Programming Paradigm
# Programming Paradigm is a way of solving a problem
# Programming Paradigm is a way of thinking
# Programming Paradigm is a way of writing code
# Programming Paradigm is a way of structuring code
# Programming Paradigm is a way of organizing code
# Programming Paradigm is a way of designing code
# Programming Paradigm is a way of implementing code
# Programming Paradigm is a way of testing code
# Programming Paradigm is a way of maintaining code
# Programming Paradigm is a way of debugging code
# Programming Paradigm is a way of profiling code
# Programming Paradigm is a way of optimizing code
# Programming Paradigm is a way of scaling code
# Programming Paradigm is a way of deploying code
# Programming Paradigm is a way of monitoring code
# Programming Paradigm is a way of securing code
# Programming Paradigm is a way of documenting code
# Programming Paradigm is a way of versioning code
# Programming Paradigm is a way of collaborating code
# Programming Paradigm is a way of sharing code
# Programming Paradigm is a way of reusing code

# Python programming paradigm
    # python supports multiple programming paradigms
    # python supports procedural programming
        # procedural programming is a programming paradigm that uses procedures or routines to implement a program
    # python supports functional programming
        # functional programming is a programming paradigm that uses functions to implement a program
    # python supports object-oriented programming
        # object-oriented programming is a programming paradigm that uses objects to implement a program

# an object in OOP represents real life objects
    # example: a car is an object in OOP
    # attributes  of a car: color, brand, model, price
    # methods of a car: start(), stop(), accelerate(), brake()
    
# Why OOP?
    # 1.inheritance reusability
    # 2.encapsulation data security
    # 3.polymorphism poly means many morph means form
    # 4.abstraction data hiding


# what is class?
    # python everything is object
    # class is a blueprint of an object or class is a template for creating objects
    
#What is constructor?
    # constructor is a special method that is called when an object is created
    # constructor is used to initialize the object
    # Types of constructors:
    # 1. Default constructor
    # 2. Parameterized constructor
    # 3. Non-Parameterized constructor
    # 4. self is a reference variable that points to the current object and memory location allocated to the object called instance
        # s = Student("Omar", 21, "Male") memory location allocated to the object called instance
class Car: # default constructor
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")
    def accelerate(self):
        print("Car accelerated")
    def brake(self):
        print("Car braked")

c=Car()
    
class Student:
    # def __init__(self): # non parameterized constructor
    #     self.name = "Omar"
    #     self.age = 21
    #     self.gender = "Male"

    def __init__(self, name, age, gender): # parameterized constructor
        self.name = name
        self.age = age
        self.gender = gender
        

s = Student("Omar", 21, "Male")
s1 = Student("Alex", 22, "Female")
print(s.__dict__)
print(s1.__dict__)
        