names = ["John", "Doe"]
first_name, last_name = names
print(first_name)
print(last_name)

names = ["John", "Doe", "Smith"]
first_name, last_name = names[:2]
print(first_name)
print(last_name)

names = ["John", "Doe", "Smith"]
first_name, middle_name, last_name = names[:3]
print(first_name)
print(middle_name)
print(last_name)

def unpack_names(names):
    first_name, middle_name, last_name = names[:3]
    return first_name, middle_name, last_name

first_name, middle_name, last_name = unpack_names(["John", "Doe", "Smith"])
print(first_name)
print(middle_name)
print(last_name)