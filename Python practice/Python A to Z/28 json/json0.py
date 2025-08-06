import json

person = {
    "name": "Faruk",
    "age": 22,
    "gender": "Male",
    "married": False,
    "children": None,
    "pets": ["cat", "dog"],
    "cars": [
        {
            "model": "BMW",
            "mpg": 27.5
        }
    ]
}

# json.dumps() Python dictionary to JSON string
data = json.dumps(person, indent = 4, sort_keys = True)
print(data)
print(type(data))



person = ["Faruk", 22, "Male", False, None, ["cat", "dog"], {"model": "BMW", "mpg": 27.5}]

# json.dumps() Python list to JSON string
data = json.dumps(person, indent = 4, sort_keys = True)
print(data)
print(type(data))

person = ("Faruk", 22, "Male", False, None, ["cat", "dog"], {"model": "BMW", "mpg": 27.5})

# json.dumps() Python tuple to JSON string
data = json.dumps(person, indent = 4, sort_keys = True)
print(data)
print(type(data))

name = "Faruk"

# json.dumps() Python string to JSON string
data = json.dumps(name, indent = 4, sort_keys = True)
print(data)
print(type(data))

age = 22

# json.dumps() Python integer to JSON string
data = json.dumps(age, indent = 4, sort_keys = True)
print(data)
print(type(data))

paid = False

# json.dumps() Python boolean to JSON string
data = json.dumps(paid, indent = 4, sort_keys = True)
print(data)
print(type(data))

children = None

# json.dumps() Python None to JSON string
data = json.dumps(children, indent = 4, sort_keys = True)
print(data)
print(type(data))

pets = ["cat", "dog"]

# json.dumps() Python list to JSON string
data = json.dumps(pets, indent = 4, sort_keys = True)
print(data)
print(type(data))

