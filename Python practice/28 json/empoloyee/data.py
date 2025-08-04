import json

def salary_credit():
    with open("L:\\Programming\\Python\\All-Main Problem Solving\\Python practice\\28 json\\empoloyee\\emp.json", "r") as file:
        data = json.load(file)
        employees = data["employees"]

        for emp_id, emp_info in employees.items():
            if emp_info["salary"] > 20000:
                print(f"{emp_info['name']} gets salary: {emp_info['salary']}")
            else:
                print(f"{emp_info['name']} gets salary: {emp_info['salary']}")

salary_credit()
