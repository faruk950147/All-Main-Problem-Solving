# Aggregation in no access to private data and possible  getter and setter method
class Customer:
    def __init__(self, name, gender, age, address):
        self.name = name
        self.gender = gender
        self.age = age
        self.address = address
    # Aggregation in no access to private data and possible  getter and setter method
    def display(self):
        print(f"Name: {self.name}\nGender: {self.gender}\nAge: {self.age}\nAddress: {self.address.get_city()}, {self.address.state}, {self.address.zip_code}")
        
class Address:
    def __init__(self, city, state, zip_code):
        self.__city = city
        self.state = state
        self.zip_code = zip_code
    
    def get_city(self):
        return self.__city
    
    def set_city(self, city):
        self.__city = city

address = Address("Dhaka", "Dhaka", "1200")
customer = Customer("Faruk", "Male", 22, address)
customer.display()

address1 = Address("Chittagong", "Dhaka", "1200")
customer1 = Customer("Faruk", "Male", 22, address1)
customer1.display()

address.set_city("Chittagong")
customer.display()