
# Multiple Inheritance
class Vehicle:
    def __init__(self, name):
        self.name = name
        print("I'm from vehicle constructor")
    
    def VehicleName(self):
        print("I'm from vehicle method",self.name)
        
class Driver:
    def __init__(self, name):
        self.name = name
        print("I'm from driver constructor")
        
    def DriverName(self):
        print("I'm from driver method",self.name)
        

class Car(Vehicle, Driver):
    def __init__(self, name):
        super().__init__(name)
        print("I'm from car constructor")    
    def CarName(self):
        print("I'm from car method",self.name)
        

        
if __name__ =="__main__":
    v1 = Vehicle("Premio")
    v1.VehicleName()
    
    d1 = Driver("Faruk")
    d1.DriverName()
    
    c1 = Car("Audi")
    c1.CarName()
    c1.VehicleName()
    c1.DriverName()
    
# multi level inheritance

class Vehicle:
    def __init__(self, name):
        self.name = name
        print("I'm from Vehicle constructor")
    
    def VehicleName(self):
        print("I'm from Vehicle method", self.name)

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        print("I'm from Car constructor")
    
    def CarName(self):
        print("I'm from Car method", self.name)

class SportsCar(Car):
    def __init__(self, name):
        super().__init__(name)
        print("I'm from SportsCar constructor")
    
    def SportsCarName(self):
        print("I'm from SportsCar method", self.name)


if __name__ == "__main__":
    sc1 = SportsCar("Ferrari")
    sc1.VehicleName()
    sc1.CarName()
    sc1.SportsCarName()

# Multiple Inheritance
class Vehicle:
    def __init__(self, name):
        self.name = name
        print("I'm from vehicle constructor")
    
    def VehicleName(self):
        print("I'm from vehicle method",self.name)
        
class Driver(Vehicle):
    def __init__(self, name):
        self.name = name
        print("I'm from driver constructor")
        
    def DriverName(self):
        print("I'm from driver method",self.name)
        

class Car(Driver):
    def __init__(self, name):
        super().__init__(name)
        print("I'm from car constructor")    
    
    def CarName(self):
        print("I'm from car method",self.name)


# Hierarchical Inheritance

class Vehicle:
    def __init__(self, name):
        self.name = name
        print("I'm from vehicle constructor")
    
    def VehicleName(self):
        print("I'm from vehicle method",self.name)
        
class Driver(Vehicle):
    def __init__(self, name):
        self.name = name
        print("I'm from driver constructor")
        
    def DriverName(self):
        print("I'm from driver method",self.name)
        

class Car(Driver):
    def __init__(self, name):
        super().__init__(name)
        print("I'm from car constructor")    
    
    def CarName(self):
        print("I'm from car method",self.name)
