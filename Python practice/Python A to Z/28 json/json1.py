import json
# what is json is a data format 
# json is a data format that is used to store and exchange data
# json is language independent and platform independent
# json is a text format that is written in key-value pairs
# absolutely double quote is used in json


# dumps is used to write json data to a file
# loads is used to read json data from a file
person = {
    "name": "Faruk",
    "age": 22,
    "gender": "Male"
}
# data = json.dumps(person, indent = 4) # json.dumps(obj , indent = 4) Python dictionary to JSON string
# print(data)
# print(type(data))

# parse json from file
with open('L:/Python/Python Problem Solving/Python practice/json/file/person.json', 'w') as file:# json.dump() Python dictionary to JSON string
    json.dump(person, file, indent = 4)

with open('L:/Python/Python Problem Solving/Python practice/json/file/person.json', 'r') as file:# json.loads() JSON string to Python dictionary 
    data = json.loads(file.read())  
    print(data)