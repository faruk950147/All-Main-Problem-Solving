studentsData = {
    "Faruk": { "details":
        {
            "age": 22,
            "gender": "Male",
            "course": "BSC in CSE"
        }
    },
    "Naima": {
        "details":
        {
            "age": 21,
            "gender": "Female",
            "course": "BSC in CSE"
        }
    },
    "Bruno": {
        "details":
        {
            "age": 20,
            "gender": "Male",
            "course": "BSC in CSE"
        }
    }
}

for student in studentsData:
    print(student)
    print(studentsData[student])
    print(studentsData[student]['details'])
    print(studentsData[student]['details']['age'])
    print(studentsData[student]['details']['gender'])
    print(studentsData[student]['details']['course'])
    print("\n")