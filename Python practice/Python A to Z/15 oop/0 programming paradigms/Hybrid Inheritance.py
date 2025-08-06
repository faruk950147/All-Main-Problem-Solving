# Hybrid Inheritance is a combination of multiple inheritances

class Vehicle:
    def __init__(self, name):
        self.name = name
        print("I'm from vehicle constructor")
    
    def VehicleName(self):
        print("I'm from vehicle method", self.name)


class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        print("I'm from car constructor")
    
    def CarName(self):
        print("I'm from car method", self.name)


class Truck(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        print("I'm from truck constructor")
    
    def TruckName(self):
        print("I'm from truck method", self.name)


class ElectricCar(Car, Truck):  # Hybrid: inherits from both Car and Truck (multiple + multilevel)
    def __init__(self, name, cc):
        Car.__init__(self, name)
        Truck.__init__(self, name)
        self.cc = cc
        print("I'm from electric car constructor")
    
    def ElectricCarName(self):
        print("I'm from electric car method", self.name, self.cc)


if __name__ == "__main__":
    v1 = Vehicle("Premio")
    v1.VehicleName()
    
    print()

    c1 = Car("Audi")
    c1.CarName()
    c1.VehicleName()
    
    print()

    t1 = Truck("Tata")
    t1.TruckName()
    t1.VehicleName()
    
    print()

    ec1 = ElectricCar("Tesla", 500)
    ec1.ElectricCarName()
    ec1.CarName()
    ec1.TruckName()
    ec1.VehicleName()
