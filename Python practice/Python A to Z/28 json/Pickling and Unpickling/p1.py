import pickle


# what is pickling and unpickling
# pickling is a process of converting a python object into a byte stream
# unpickling is a process of converting a byte stream into a python object


# pickling
person = {
    "name": "Faruk",
    "age": 22,
    "gender": "Male"
}
byte_stream = pickle.dumps(person)
print(byte_stream)
print(type(byte_stream))

# unpickling
unpickled_data = pickle.loads(byte_stream)
print(unpickled_data)
print(type(unpickled_data))
