# multi level inheritance
# level 1
class Vehicle:
    def __init__(self, name):
        self.name = name
        print("I'm from Vehicle constructor")
    
    def VehicleName(self):
        print("I'm from Vehicle method", self.name)
# level 2
class Car(Vehicle):
    def __init__(self, name, cc):
        super().__init__(name)
        self.cc = cc
        print("I'm from Car constructor")
    
    def CarName(self):
        print("I'm from Car method", self.name, self.cc)
# level 3
class SportsCar(Car):
    def __init__(self, name, cc):
        super().__init__(name, cc)
        print("I'm from SportsCar constructor")
    
    def SportsCarName(self):
        print("I'm from SportsCar method", self.name, self.cc)


if __name__ == "__main__":
    sc1 = SportsCar("Ferrari", 500)
    sc1.VehicleName()
    sc1.CarName()
    sc1.SportsCarName()