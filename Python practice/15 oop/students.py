# class Students:
#   name="Kiran"
# s1 = Students()
# print(s1)
# print(s1.name)
# s2 = Students()
# print(s2)
# print(s2.name)



# class Students:
#   """docstring for Students"""
#   def __init__(self, name, marks):
#     self.name = name
#     self.marks = marks
    
# s1 = Students("Kiran", 99)

# print(s1.name, s1.marks)


# class Students:
#   def __init__(self, name, marks):
#     self.name = name
#     self.marks = marks

#   def wellcome(self):
#     print(f"Wellcome to our collage {self.name}")

#   def get_marks(self):
#     return self.marks

# s1 = Students("Faruk", 80)
# s1.wellcome()
# print(s1.get_marks())



class Students:
    coll = "TMSS TECHNICAL INSTITUTE (TTI)"#this is class veriable
    def __init__(self, id, name, department, marks):
        self.id = id
        self.name = name
        self.department = department
        self.marks = marks

    def get_sum_marks(self):
        sum = 0
        for i in self.marks:
            sum += i
        return sum
    
    def get_average_marks(self):
        return self.get_sum_marks() / len(self.marks)

    def display(self): #This here self = car ok
        print("\n", self.coll, "\n", self.id, self.name, "\n", self.department, "\n", self.get_sum_marks(), "\n", self.get_average_marks())
        
if __name__ =="__main__":
    s1 = Students(1, "Ritu", "CSE", [80, 80, 80])
    s1.display()
    
    s2 = Students(2, "Faruk", "SWE", [80, 80, 80])
    s2.display()