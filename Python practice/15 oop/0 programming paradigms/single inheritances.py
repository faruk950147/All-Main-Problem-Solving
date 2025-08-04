# Single Inheritance
# level 1
class Vehicle:
    def __init__(self, name):
        self.name = name
        print("I'm from vehicle constructor")
    
    def VehicleName(self):
        print("I'm from vehicle method",self.name)
        
# level 2
class Car(Vehicle):
    def __init__(self, name, wheel, color, driver, cc):
        super().__init__(name)
        self.wheel = wheel
        self.color = color
        self.driver = driver
        self.cc = cc
        print("I'm from car constructor")
    
    def CarName(self):
        print("I'm from car method",self.name)
    
    def CarDetails(self):
        print("I'm from car method",self.name, self.wheel, self.color, self.driver, self.cc)

# Create an object of Car
car = Car("Toyota", 4, "Red", "Driver", 1500)
car.CarName()
car.VehicleName()
car.CarDetails()
