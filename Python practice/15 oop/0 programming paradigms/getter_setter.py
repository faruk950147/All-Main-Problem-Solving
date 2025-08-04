# getter and setter

class University:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def set_name(self, name):
        self.name = name

    def set_location(self, location):
        self.location = location

    def display(self):
        print(self.name, self.location)

    def __str__(self):
        return f"{self.name} {self.location}"
    
if __name__ == "__main__":
    university1 = University(input("Enter University name: "), input("Enter University location: "))
    university2 = University(input("Enter University name: "), input("Enter University location: "))
    print(university1.get_name())
    print(university2.get_location())
    university1.set_name(input("Enter University name: "))
    university1.set_location(input("Enter University location: "))
    print(university1.get_name())
    print(university1.get_location())
