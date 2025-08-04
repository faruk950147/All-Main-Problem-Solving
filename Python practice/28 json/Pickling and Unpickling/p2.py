import pickle

data = ["Faruk", 22, "Male"]
with open("L:\\Programming\\Python\\Main Problem Solving\\Python practice\\28 json\\Pickling and Unpickling\\file\\data.pkl", "wb") as file:
    pickle.dump(data, file)

with open("L:\\Programming\\Python\\Main Problem Solving\\Python practice\\28 json\\Pickling and Unpickling\\file\\data.pkl", "rb") as file:
    data = pickle.load(file)
    print(data)
    print(type(data))
