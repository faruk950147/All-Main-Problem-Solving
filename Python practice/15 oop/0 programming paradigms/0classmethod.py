# class method is a method that is bound to the class and not the instance of the class
# class method can modify class state that applies across all instances of the class

# class method হলো একটি মেথড যেটি class এর উপর কাজ করে, object বা instance-এর উপর না।
# class method এ প্রথম প্যারামিটার হিসেবে self না দিয়ে cls ব্যবহার করা হয়, কারণ এটি পুরো class কে represent করে, যেমন: University class।
# cls.university_name হচ্ছে class variable university_name কে access করা।
# মানে 👉 class variable read বা modify করতে

class University:
    university_name = "AUST University Bangladesh"

    def __init__(self, department, location):
        self.department = department
        self.location = location

    @classmethod
    def get_university_name(cls):
        return cls.university_name  # class method is used to modify class state that applies across all instances of the class
    
    @classmethod
    def set_university_name(cls, university_name):
        cls.university_name = university_name

    def display(self):
        print(self.department, self.location)  # instance method

    def __str__(self):
        return f"{self.university_name} {self.department} {self.location}"  # instance method

university1 = University("CSE", "Dhaka")
university2 = University("EEE", "Chittagong")

print("Before University name: ", university1.get_university_name())
university1.set_university_name("DIU")
print("After University name: ", university1.get_university_name())