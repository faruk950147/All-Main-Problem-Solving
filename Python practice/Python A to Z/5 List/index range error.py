my_list = [10, 20, 30]
index = len(my_list) - 1 # -1 because list index start from 0

if index < len(my_list):
    print(my_list[index])
else:
    print("Index out of range")


# try:
#     print(my_list[index])
# except IndexError:
#     print("Invalid index! Please check list size.")
