# prototype is a design pattern

import copy
def add(a: int, b: int) -> int: # function prototype
    return a + b

class Prototype: # class prototype
    def __init__(self):
        self.objects = {}

    def register_object(self, name, obj):
        self.objects[name] = obj

    def unregister_object(self, name):
        del self.objects[name]

    def clone(self, name, **attributes):
        obj = copy.deepcopy(self.objects.get(name))
        obj.__dict__.update(attributes)
        return obj

# Example Class
class Car: # class prototype
    def __init__(self):
        self.make = "Ford"
        self.model = "Mustang"
        self.color = "Red"

    def __str__(self):
        return f'{self.make} {self.model} {self.color}'

if __name__ == "__main__":
    # Using the Prototype
    prototype = Prototype()
    car = Car()
    prototype.register_object('mustang', car)
    car_clone = prototype.clone('mustang', color='Blue')
    print(car)        # Output: Ford Mustang Red
    print(car_clone)  # Output: Ford Mustang Blue