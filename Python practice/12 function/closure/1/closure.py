# Closure in Python (Function Closures)
# num = 10
# def Checker():
#     num2 = 10
#     def CheckNumber(num3):
#         return num + num2 + num3
#     return CheckNumber

# func = Checker()
# print(func(20))
# print(func.__closure__)  
# print([cell.cell_contents for cell in func.__closure__])

num = 10
def Checker(num2):
    num3 = 10
    def CheckNumber(num4):
        return num + num2 + num3 + num4
    return CheckNumber

func = Checker(5)         # num2 = 5
print(func(20))           # num + num2 + num3 + num4 = 10 + 5 + 10 + 20 = 45
print(func.__closure__)  
print([cell.cell_contents for cell in func.__closure__])
