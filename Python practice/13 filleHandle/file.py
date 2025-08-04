# mode
# r - read
# w - write
# a - append
# b - binary
# r+ - read and write
# w+ - write and read
# a+ - append and read

# readline()
# readlines()
# seek()
# tell()
# write()
# writelines()

# why gap between cursor and data because we are hit enter after typing data where python get \n new line character

# open file and read
# file = open(r"L:\\Programming\\Python\\Main Problem Solving\\Python practice\\13 filleHandle\\dataFile\\file1.txt", "r")
# print(file.read())
# file.close()

# # open file and read with context manager
# with open(r"L:\\Programming\\Python\\Main Problem Solving\\Python practice\\13 filleHandle\\dataFile\\file1.txt", "r") as file:
#     print(file.read())

# open file and write
# file = open(r"L:\\Programming\\Python\\Main Problem Solving\\Python practice\\13 filleHandle\\dataFile\\file1.txt", "w")
# file.write("Hello, World! and Hello, Python!")
# file.close()

# # open file and with context manager
# with open(r"L:\\Programming\\Python\\Main Problem Solving\\Python practice\\13 filleHandle\\dataFile\\file1.txt", "w") as file:
#     file.write("Hello, World! and Hello, Python!")

# open file and append
# file = open(r"L:\\Programming\\Python\\Main Problem Solving\\Python practice\\13 filleHandle\\dataFile\\file1.txt", "a")
# file.write("Hello, World! and Hello, Python!")
# file.close()

# # open file and with context manager
# with open(r"L:\\Programming\\Python\\Main Problem Solving\\Python practice\\13 filleHandle\\dataFile\\file1.txt", "a") as file:
#     file.write("Hello, World! and Hello, Python!")

# open file and binary mode
# file = open(r"L:\\Programming\\Python\\Main Problem Solving\\Python practice\\13 filleHandle\\dataFile\\file1.txt", "rb")
# print(file.read())
# file.close()

# # open file and with context manager
# with open(r"L:\\Programming\\Python\\Main Problem Solving\\Python practice\\13 filleHandle\\dataFile\\file1.txt", "rb") as file:
#     print(file.read())

# open file and read and write
file = open(r"L:\\Programming\\Python\\Main Problem Solving\\Python practice\\13 filleHandle\\dataFile\\file1.txt", "r+")
print(file.read())
# file cursor start from end
file.seek(0)
# this data not read because cursor is at the end we have to already print data
file.write("Hello, World! and Hello, Python!")
# right now show this data
file.flush()
file.close()

# open file and with context manager
# with open(r"L:\\Programming\\Python\\Main Problem Solving\\Python practice\\13 filleHandle\\dataFile\\file1.txt", "r+") as file:
#     print(file.read())
#     file.seek(0)
      # this data not read because cursor is at the end we have to already print data
#     file.write("Hello, World! and Hello, Python!")
      # right now show this data
#     file.flush()


