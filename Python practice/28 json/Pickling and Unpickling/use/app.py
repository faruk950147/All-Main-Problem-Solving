import students
import pickle
with open("data.dat", "wb") as file:
    get_data = int(input("Enter the employee: "))
    for i in range(get_data):
        data = students.Student(input("Enter the name: "), int(input("Enter the roll: ")), input("Enter the marks: "))
    pickle.dump(data, file)
    print("Data written to file successfully")

