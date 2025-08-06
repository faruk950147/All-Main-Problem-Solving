class Collage:
    collage_name = "TMSS TECHNICAL INSTITUTE BOGURA"  # এটা হলো class variable

    def __init__(self, department, location):
        self.department = department
        self.location = location
          
    def get_collage_name(self):
        return self.collage_name  # class variable access 

    def display(self):
        print(self.department, self.location)

    def __str__(self):
        return f"{self.collage_name} {self.department} {self.location}"

collage1 = Collage("CSE", "Bogura")
collage1.display()  # Output: CSE Bogura

Collage.collage_name = "GCU"  # class variable change
print(collage1.collage_name)  # Output: GCU

collage1.display()  # department and location will be same
