def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y

# def display(callback):
#     print(callback(10, 20))

# display(add)
# display(sub)
# display(mul)
# display(div)

def display(callback,x,y):
    print(callback(x,y))

display(add,10,20)
display(sub,10,20)
display(mul,10,20)
display(div,10,20)