# # Basic class

# class Vehicle:
#     pass

# if __name__=="__main__":

#     car = Vehicle()
#     car.name = "Premio"
#     car.wheel = 4
#     car.color = "Light Black"
#     car.driver = "Faruk"
#     print("\n The car name is : ",car.name,"\n The car wheel is : ",car.wheel,"\n The car color is : ",car.color,"\n The car driver name is : ",car.driver)




# class Vehicle:
#     def display(self): #what happen here self = car
#         print("\n The car name is : ",car.name,"\n The car wheel is : ",car.wheel,"\n The car color is : ",car.color,"\n The car driver name is : ",car.driver)

# if __name__=="__main__":
     
#     car = Vehicle()
#     car.name = "Premio"
#     car.wheel = 4
#     car.color = "Light Black"
#     car.driver = "Faruk"
#     car.display()


class Vehicle:
    #this is instance method
    def setValue(self, name, wheel, color, driver):
        self.name = name
        self.wheel = wheel
        self.color = color
        self.driver = driver
      
    def display(self): #This here self = car ok
        print("\n",self.name, "\n",self.wheel, "\n",self.color, "\n",self.driver)
        
if __name__ =="__main__":
    
    car = Vehicle()
    car.setValue("BMW", 4, "yellow", "jamal miah")
    car.display()