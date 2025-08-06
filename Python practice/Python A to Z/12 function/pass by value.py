# When a variable is passed to a function, a copy of it is sent.
# The original variable remains unaffected. 

# যখন কোনো ভ্যারিয়েবল function-এ পাঠানো হয় তার কপি (copy) পাঠানো হয়।
# মূল ভ্যারিয়েবল এর উপর কোনো প্রভাব পড়ে না।

def pass_by_value(x):
    print(f"{x} Before memory location inside function:", x, id(x))
    x = x + 1 # pass by value
    print(f"{x} Inside function x:", x)
    print(f"{x} After memory location inside function x:", x, id(x))
    return x    


a = 10
print(f"{a} Before modification a:", a, id(a))
pass_by_value(a)
print(f"{a} After modification a:", a, id(a))

# def change_value(x):
#     print(f"{x} before memory location inside function:", x, id(x))
#     x += 10
#     print(f"{x} Inside function x:", x)
#     print(f"{x} after memory location inside function x:", x, id(x))
#     return x

# a = 5
# print(f"{a} Before modification a:", a, id(a))
# change_value(a)
# print(f"{a} After modification a:", a, id(a))


