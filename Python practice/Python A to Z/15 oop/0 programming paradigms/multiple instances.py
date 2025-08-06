
# Multiple Inheritance
# level 1
class Vehicle:
    def __init__(self, name):
        self.name = name
        print("I'm from vehicle constructor")
    
    def VehicleName(self):
        print("I'm from vehicle method",self.name)
        
# level 2
class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("I'm from driver constructor")
        
    def DriverName(self):
        print("I'm from driver method",self.name, self.age)
        
# level 3
class Car(Vehicle, Driver):
    def __init__(self, name, age, cc):
        super().__init__(name)
        Driver.__init__(self, name, age)
        self.cc = cc
        print("I'm from car constructor")    
    def CarName(self):
        print("I'm from car method",self.name, self.cc)
        

        
if __name__ =="__main__":
    v1 = Vehicle("Premio")
    v1.VehicleName()
    
    d1 = Driver("Faruk", 22)
    d1.DriverName()
    
    c1 = Car("Audi", 22, 500)
    c1.CarName()
    c1.VehicleName()
    c1.DriverName()