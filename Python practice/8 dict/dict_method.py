dict1 = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "country": "USA",
    "gender": "Female"
}


print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1.get('name'))
print(dict1.pop('name'))
print(dict1.popitem())
print(dict1.setdefault('name', 'Alice'))
print(dict1.update({'name': 'Bob'}))
print(dict1.clear())
print(dict1.copy())
print(dict1.fromkeys(['name', 'age', 'city'], 'Unknown'))