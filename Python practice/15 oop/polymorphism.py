
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print(f"{self.name} says Woof!")

# class Cat(Animal):
#     def sound(self):
#         print(f"{self.name} says Meow!")

# class Cow(Animal):
#     def sound(self):
#         print(f"{self.name} says Moo!")

# def animal_sound(animal):
#     animal.sound()

# if __name__ == "__main__":
#     dog = Dog("Tommy")
#     cat = Cat("Kitty")
#     cow = Cow("Bessie")

#     animals = [dog, cat, cow]

#     for animal in animals:
#         animal_sound(animal)

class animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("Animal makes a sound")
class Hen(animal):
    def sound(self):
        print(f"{self.name} says Cluck!")
class Duck(animal):
    def sound(self):
        print(f"{self.name} says Quack!")
class Cow(animal):
    def sound(self):
        print(f"{self.name} says Moo!")

#define a function that takes an animal object and calls its sound method
# if you want manualy call the sound method so remove this function

# def animal_sound(animal):
#     animal.sound()

# if __name__ == "__main__":
#     hen = Hen("Hen")
#     duck = Duck("Duck")
#     cow = Cow("Cow")
#     # hen.sound()
#     # duck.sound()
#     # cow.sound()

#     animals = [hen, duck, cow]

#     for animal in animals:
#         animal_sound(animal)

# class Shape:
#     def __init__(self, name):
#         self.name = name

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius
    
#     def area(self):
#         return 3.14 * self.radius * self.radius

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__("Rectangle")
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width

# def shape_area(shape):
#     return shape.area()

# if __name__ == "__main__":
#     circle = Circle(5)
#     rectangle = Rectangle(4, 6)

#     shapes = [circle, rectangle]

#     for shape in shapes:
#         print(f"Area of {shape.name}:", shape_area(shape))


class Vehicle:
    def __init__(self, name,color, price):
        self.name = name
        self.color = color
        self.price = price
    
    def get_details(self):
        return f"Name: {self.name}, Color: {self.color}, Price: {self.price}"
    
    def max_speed(self):
        return "Max speed: 120 km/h"
    
    def gear(self):
        return "Gear change: 5"

class Car(Vehicle):
    def __init__(self, name, color, price, cc):
        super().__init__(name, color, price)
        self.cc = cc
    def get_details(self):
        return f"{super().get_details()}, CC: {self.cc}"
    def max_speed(self):
        return "Max speed: 220 km/h"
    def gear(self):
        return "Gear change: 6"
