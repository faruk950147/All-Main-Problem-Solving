from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         raise NotImplementedError("Subclass must implement 'area' method")
#     @abstractmethod
#     def perimeter(self):
#         raise NotImplementedError("Subclass must implement 'perimeter' method")

# class Shape:
#     def area(self):
#         raise NotImplementedError("Subclass must implement 'area' method")

#     def perimeter(self):
#         raise NotImplementedError("Subclass must implement 'perimeter' method")


# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

#     def perimeter(self):
#         return 2 * 3.14 * self.radius


# r = Rectangle(10, 5)
# print("Rectangle Area:", r.area())
# print("Rectangle Perimeter:", r.perimeter())

# c = Circle(7)
# print("Circle Area:", c.area())
# print("Circle Perimeter:", c.perimeter())

# class BankServer(ABC):
#     def database(self):
#         print("Connecting to database on server...")

#     @abstractmethod
#     def security(self):
#         print("security passed server...")

# class MobileServer(BankServer):
#     def mobile_login(self):
#         print("Mobile login server is running...")

#     def security(self):
#         print("Security passed server...")


# if __name__ == "__main__":
#     server = MobileServer()
#     server.mobile_login()
#     server.security()

# class BankServer(ABC):
#     def __init__(self, server_name):
#         self.server_name = server_name

#     @abstractmethod
#     def database(self, db_name):
#         print("Connecting to database on Bank server...")

#     @abstractmethod
#     def security(self, level):
#         print("Security passed Bank server...")
    
#     def display(self):
#         print("Server name:", self.server_name)

# class MobileServer(BankServer):
#     def __init__(self, server_name):
#         super().__init__(server_name)
    
#     def database(self, db_name):
#         print("Connecting to database on Mobile server...")

#     def security(self, level):
#         print("Security passed Mobile server...")

#     def mobile_login(self):
#         print("Mobile login server is running...")

# if __name__ == "__main__":
#     server = MobileServer("MobileBank")
#     server.database("CustomerDB")
#     server.security("High")
#     server.display()
#     server.mobile_login()


# @display.setter
# def display(self, num):
#     self.__num = num

# এটা কোন setter?
# এটা হলো:

#  Property Setter
#  অর্থাৎ Python এর @property Decorator এর Setter Version
#  ডিটেইল ব্যাখ্যা:

# তোমার উপরের কোডে আগে এইটা ছিল 

# @property
# def display(self):
#     print("Number:", self.__num)

#  এইটা হলো property getter
#  মানে:

# test.display

# লিখলে এটা কল হবে।
#  এখন তুমি এইটা লিখেছ

# @display.setter
# def display(self, num):
#     self.__num = num

#  এইটার মানে হলো  setter for the same property display
#  এই setter এর কাজ:

#  তুমি যখন এইভাবে লিখবে:

# test.display = 500

#  তখন Python Internally এই setter method কল করবে, আর এই লাইন রান হবে:

# self.__num = num@display.setter
# def display(self, num):
#     self.__num = num

# এটা কোন setter?
#  এটা হলো:

#  Property Setter
#  অর্থাৎ Python এর @property Decorator এর Setter Version
#  ডিটেইল ব্যাখ্যা:

# তোমার উপরের কোডে আগে এইটা ছিল 

# @property
# def display(self):
#     print("Number:", self.__num)

#  এইটা হলো property getter
#  মানে:

# test.display

# লিখলে এটা কল হবে।
#  এখন তুমি এইটা লিখেছ 

# @display.setter
# def display(self, num):
#     self.__num = num

#  এইটার মানে হলো  setter for the same property display
#  এই setter এর কাজ:

#  তুমি যখন এইভাবে লিখবে:

# test.display = 500

#  তখন Python Internally এই setter method কল করবে, আর এই লাইন রান হবে:

# self.__num = num
class  Test(object):
    def __init__(self, num = 0):
        self.num = num
        self.__num = 100
    
    def get_num(self):
        return self.__num
    
    def set_num(self, num):
        self.__num = num
        
    @property
    def display(self):
        print("Number:", self.__num)
        
    @display.setter
    def display(self, num):
        self.__num = num
    
    @staticmethod
    def print_hello():
        print("Hello")
    
    def __str__(self):
        return f"Number: {self.__num}"
    
    def __del__(self):
        print("Object is deleted")
        
if __name__ == "__main__":
    test = Test()
    test.set_num(200)
    test.display
    test.print_hello() 
    print(test)
    del test