# Pickling and Unpicklingfrom imghdr import what


# what is pickling and unpickling
# pickling is a process of converting a python object into a byte stream
# unpickling is a process of converting a byte stream into a python object

import pickle

data = ["Faruk", 22, "Male"]
byte_stream = pickle.dumps(data)
print(byte_stream)
print(type(byte_stream))

# unpickling
unpickled_data = pickle.loads(byte_stream)
print(unpickled_data)
print(type(unpickled_data))