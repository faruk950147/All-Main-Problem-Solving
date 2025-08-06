import pickle
with open("data.dat", "rb") as file:
    data = pickle.load(file)
    while True:
        try:
            print(data.display())
            break
        except Exception as e:
            print(e)
            break
