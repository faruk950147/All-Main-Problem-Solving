data = input("Enter your data: ")
with open("L:\\Programming\\Python\\Main Problem Solving\\Python practice\\13 filleHandle\\dataFile\\data.txt", "w") as file:
    if data == "":
        print("Data is empty")
    else:
        file.write(data)
        print("Data is written successfully")
    
# with open("L:\\Programming\\Python\\Main Problem Solving\\Python practice\\13 filleHandle\\dataFile\\data.txt", "r") as file:
#     print(file.read())
