# and logical and
# or logical or
# not logical not

a = 10
b = 20
print(a and b)
print(a or b)
print(not a)
print(not b)


if a and b:
    print("Both are true")
else:
    print("At least one is false")

if a or b:
    print("At least one is true")
else:
    print("Both are false")

if not a:
    print("a is false")
else:
    print("a is true")  