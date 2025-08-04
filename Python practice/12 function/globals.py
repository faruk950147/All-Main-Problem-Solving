num = 10
def display():
    # it is not allowed to modify global variable num += 10
    # it is allowed to modify global keyword num that is global num
    global num
    num += 10
    print("num in function global",num)
    num = 20
    print("num in function local",num)
display()
print("num in outside global",num)