class Laptop:
    def __init__(self, name, brand, screen_size, ram, rom, price):
        self.name = name
        self.brand = brand
        self.screen_size = screen_size
        self.ram = ram
        self.rom = rom
        self.price = price
        
    def display(self):
        print(self.name, self.brand, self.screen_size, self.ram, self.rom, self.price)
        
class Computer(Laptop):
    def __init__(self, name, brand, cpu, screen_size, ram, rom, price):
        super().__init__(name, brand, screen_size, ram, rom, price)
        self.cpu = cpu
        
    def display(self):
        print(self.name, self.brand, self.cpu, self.screen_size, self.ram, self.rom, self.price)
        
computer = Computer("Dell", "Apple", "i7", "15-inch", 16, 512, 1000)
computer.display()
