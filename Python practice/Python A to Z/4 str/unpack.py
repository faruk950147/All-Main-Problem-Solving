full_name = "John Doe"
first_name, last_name = full_name.split(" ")
print(first_name)
print(last_name)

full_name = "John Michael Doe"
first_name, middle_name, last_name = full_name.split(" ")
print(first_name)
print(middle_name)
print(last_name)

def unpack_full_name(full_name):
    first_name, middle_name, last_name = full_name.split(" ")
    return first_name, middle_name, last_name

first_name, middle_name, last_name = unpack_full_name("John Michael Doe")
print(first_name)
print(middle_name)
print(last_name)