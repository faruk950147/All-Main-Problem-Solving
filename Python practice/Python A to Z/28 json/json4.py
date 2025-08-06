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
# print(data)
print(type(data))

# json.loads() JSON string to Python dictionary
person = json.loads(data)
print(person)
print(type(person))