# add function
def add(a, b):
    return a + b
#store function in variable
addition = add
print(addition(10, 20))
print(type(addition))

# sub function
def sub(a, b):
    return a - b
subtraction = sub
print(subtraction(10, 20))
print(type(subtraction))

# mul function
def mul(a, b):
    return a * b
multiplication = mul
print(multiplication(10, 20))
print(type(multiplication))

# div function
def div(a, b):
    return a / b
division = div
print(division(10, 20))
print(type(division))
