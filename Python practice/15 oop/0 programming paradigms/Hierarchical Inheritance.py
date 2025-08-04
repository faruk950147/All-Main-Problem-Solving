class Vehicle:
    def __init__(self, name):
        self.name = name
        print("I'm from vehicle constructor")
    
    def VehicleName(self):
        print("I'm from vehicle method", self.name)


class Driver(Vehicle):  # child class 1
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print("I'm from driver constructor")
    
    def DriverName(self):
        print("I'm from driver method", self.name, self.age)


class Car(Vehicle):  # child class 2
    def __init__(self, name, cc):
        super().__init__(name)
        self.cc = cc
        print("I'm from car constructor")
    
    def CarName(self):
        print("I'm from car method", self.name, self.cc)
        


if __name__ == "__main__":
    v1 = Vehicle("Premio")
    v1.VehicleName()
    
    print()

    d1 = Driver("Faruk", 22)
    d1.DriverName()
    
    print()

    c1 = Car("Audi", 500)
    c1.CarName()
    c1.VehicleName()
    c1.DriverName()


