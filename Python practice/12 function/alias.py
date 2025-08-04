# alias is used to give a new name to a function
# alias is used to give a new name to a variable
# alias is used to give a new name to a class
# alias is used to give a new name to a module
def display():
    print("Hello")
# alias is used to give a new name to a function
alias_display = display
alias_display()

# alias is used to give a new name to a variable
num = 10
alias_num = num
print(alias_num)
alias_num = 20
print(num)
print(alias_num)

# alias is used to give a new name to a class
class Display:
    def __init__(self):
        self.num = 10
    def display(self):
        print(self.num)
# alias is used to give a new name to a class
alias_display = Display
alias_display().display()

# alias is used to give a new name to a module
import math
alias_math = math
print(alias_math.sqrt(16))