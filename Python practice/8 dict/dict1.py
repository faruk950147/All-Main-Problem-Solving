# dict1 = {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA', 'gender': 'Female'}
# print(dict1['name'])     # Output: Alice   



# person = {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA', 'gender': 'Female'}
# print(person['name'])     # Output: Alice

# person['age'] = 26        # change value
# print(person)             # Output: {'name': 'Alice', 'age': 26}

# person['city'] = 'Dhaka'  # add new key-value pair
# print(person)             # Output: {'name': 'Alice', 'age': 26, 'city': 'Dhaka'}

# person['country'] = 'Bangladesh'  # add new key-value pair
# print(person)             # Output: {'name': 'Alice', 'age': 26, 'city': 'Dhaka', 'country': 'Bangladesh'}

# person['gender'] = 'Male'  # add new key-value pair
# print(person)             # Output: {'name': 'Alice', 'age': 26, 'city': 'Dhaka', 'country': 'Bangladesh', 'gender': 'Male'}

# person['age'] = 27        # change value
# print(person)             # Output: {'name': 'Alice', 'age': 27, 'city': 'Dhaka', 'country': 'Bangladesh', 'gender': 'Male'}

# person['city'] = 'Dhaka'  # add new key-value pair
# print(person)             # Output: {'name': 'Alice', 'age': 27, 'city': 'Dhaka', 'country': 'Bangladesh', 'gender': 'Male'}

# person['country'] = 'Bangladesh'  # add new key-value pair
# print(person)             # Output: {'name': 'Alice', 'age': 27, 'city': 'Dhaka', 'country': 'Bangladesh', 'gender': 'Male'}

# person['gender'] = 'Male'  # add new key-value pair
# print(person)             # Output: {'name': 'Alice', 'age': 27, 'city': 'Dhaka', 'country': 'Bangladesh', 'gender': 'Male'}

# person['age'] = 28        # change value
# print(person)             # Output: {'name': 'Alice', 'age': 28, 'city': 'Dhaka', 'country': 'Bangladesh', 'gender': 'Male'}

# person['city'] = 'Dhaka'  # add new key-value pair
# print(person)             # Output: {'name': 'Alice', 'age': 28, 'city': 'Dhaka', 'country': 'Bangladesh', 'gender': 'Male'}

# person['country'] = 'Bangladesh'  # add new key-value pair
# print(person)             # Output: {'name': 'Alice', 'age': 28, 'city': 'Dhaka', 'country': 'Bangladesh', 'gender': 'Male'}

# person['gender'] = 'Male'  # add new key-value pair
# print(person)             # Output: {'name': 'Alice', 'age': 28, 'city': 'Dhaka', 'country': 'Bangladesh', 'gender': 'Male'}

# person['age'] = 29        # change value
# print(person)             # Output: {'name': 'Alice', 'age': 29, 'city': 'Dhaka', 'country': 'Bangladesh', 'gender': 'Male'}

# person['city'] = 'Dhaka'  # add new key-value pair
# print(person)             # Output: {'name': 'Alice', 'age': 29, 'city': 'Dhaka', 'country': 'Bangladesh', 'gender': 'Male'}

# person['country'] = 'Bangladesh'  # add new key-value pair
# print(person)             # Output: {'name': 'Alice', 'age': 29, 'city': 'Dhaka', 'country': 'Bangladesh', 'gender': 'Male'}

# person['gender'] = 'Male'  # add new key-value pair
# print(person)             # Output: {'name': 'Alice', 'age': 29, 'city': 'Dhaka', 'country': 'Bangladesh', 'gender': 'Male'}

person = {
    "Name": ["Braund, Mr. Owen Harris", "Allen, Mr. William Henry", "Bonnell, Miss. Elizabeth"],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"]
}
print(person)
man = {
    [
        {
            "Name": "Braund, Mr. Owen Harris",
            "Age": 22,
            "Sex": "male"
        },
        {
            "Name": "Allen, Mr. William Henry",
            "Age": 35,
            "Sex": "male"
        },
        {
            "Name": "Bonnell, Miss. Elizabeth",
            "Age": 58,
            "Sex": "female"
        }
    ]
}
print(man)
# # print(person['Name'])
# # print(person['Age'])
# # print(person['Sex'])
# print(person['Name'][0])
# for item in range(len(person['Name'])):
#     print(person['Name'][item])
#     print(person['Age'][item])
#     print(person['Sex'][item])
    
# keys = ['a', 'b', 'c']
# values = [1,2,3]
# d = dict.fromkeys(keys, values)
# print(d)

# keys = ['a', 'b', 'c']
# d = dict.fromkeys(keys, 1)
# d['a'] = 2
# d['b'] = 3
# d['c'] = 4
# d['d'] = 5
# print(d)

