# Inheritance method override
# method override means 👉 same name same parameters multiple methods
# 👉 Method Overriding হলো Parent Class-এর method কে Child Class-এ same name, same parameters দিয়ে আবার নতুনভাবে define করা।
# মানে 👉 Parent method টার behavior change করা বা customize করা।
class Phone:
    def __init__(self, name, brand, price, camera):
        self.name = name
        self.brand = brand
        self.price = price
        self.camera = camera
    
    def buy(self):
        print(f"{self.name} is bought")
    
    def sell(self):
        print(f"{self.name} is sold")
        
class SmartPhone(Phone):
    def __init__(self, name, brand, price, camera, battery):
        super().__init__(name, brand, price, camera)
        self.battery = battery
    
    def buy(self):
        print(f"{self.name} is bought with battery {self.battery}")
    
    def sell(self):
        print(f"{self.name} is sold with battery {self.battery}")

s1 = SmartPhone("iPhone", "Apple", 100000, "12 MP", "10000 mAh")
s1.buy()    
s1.sell()

