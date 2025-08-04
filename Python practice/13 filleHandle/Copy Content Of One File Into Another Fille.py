# f1 = open("L:\\Programming\\Python\\Main Problem Solving\\Python practice\\13 filleHandle\\dataFile\\1.txt", "r", encoding="utf-8")
# f2 = open("L:\\Programming\\Python\\Main Problem Solving\\Python practice\\13 filleHandle\\dataFile\\2.txt", "w+", encoding="utf-8")
# data = f1.readlines()
# for i in data:
#     f2.write(i)
# f2.seek(0)
# print(f2.read())
# f2.close()
# f1.close()

with open("L:\\Programming\\Python\\Main Problem Solving\\Python practice\\13 filleHandle\\dataFile\\1.txt", "r", encoding="utf-8") as f1:
    with open("L:\\Programming\\Python\\Main Problem Solving\\Python practice\\13 filleHandle\\dataFile\\2.txt", "w+", encoding="utf-8") as f2:
        data = f1.readlines()
        for i in data:
            f2.write(i)
        f2.seek(0)
        print(f2.read())