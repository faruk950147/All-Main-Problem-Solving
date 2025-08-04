class Vehicle:
    def __init__(self, name, wheel, color, driver, cc):
        self.name = name
        self.wheel = wheel
        self.color = color
        self.driver = driver
        self.cc = cc
        self.acc = False
        self.brk = False
        self.clutch = False        

    def start(self):
        self.acc = True
        self.clutch = True
        self.brk = False
        print("\nStarting the vehicle")
    
    def stop(self):
        self.brk = True
        print("\nStopping the vehicle")
    
    def turn(self, direction):
        if direction == "left":
            print("\nTurning the vehicle left")
        elif direction == "right":
            print("\nTurning the vehicle right")
    
    def display(self):
        print("\n", self.name, "\n", self.wheel, "\n", self.color, "\n", self.driver, "\n", self.cc)
        
if __name__ == "__main__":
    car1 = Vehicle("Marcedes", 4, "Light Black", "Faruk", 1500)
    car1.display()
    car1.start()
    car1.turn("left")
    car1.stop()
    
    car2 = Vehicle("Premio", 4, "Light Black", "Faruk", 1500)
    car2.display()
    car2.start()
    car2.turn("right")
    car2.stop()

