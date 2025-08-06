# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print(self.name, self.age)

# p1 = Person("Faruk", 22)
# p1.display()
# # Add a new attribute
# p1.gender = "Male"
# print(p1.gender)

# class Person:
#     def __init__(self, name, age, country):
#         self.name = name
#         self.age = age
#         self.country = country
    
#     def display(self):
#         if self.country == "Bangladesh":
#             print("Assalamualaikum Walaikum Mr", self.name, "You are", self.age, "years old and you are from", self.country)
#         else:
#             print("Hello Mr", self.name, "You are", self.age, "years old and you are from", self.country)

# p1 = Person("Faruk", 22, "Bangladesh")
# p1.display()

# p2 = Person("Alex", 22, "USA")
# p2.display()



class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
    
def display(person):
    print(f"My name is {person.name}, I am {person.age} years old and I am from {person.country}")
    #if we want to change the value of the object
    p = Person("Miller", 22, "South Africa")
    return p

p1 = Person("Faruk", 22, "Bangladesh")
dis = display(p1)
print(dis.name)


