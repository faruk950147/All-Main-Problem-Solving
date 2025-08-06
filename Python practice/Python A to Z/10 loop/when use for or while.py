# when you know starting point and ending point then use for loop
# when you iterable object then use for loop

# for loop
# for i in range(10):
#     print(i)

# # while loop
# i = 0
# while i < 10:
#     print(i)
#     i += 1

# list1 = [1,2,3,4,5,6,7,8,9,10]
# for i in list1:
#     print(i)

# # while loop
# i = 0
# while i < len(list1):
#     print(list1[i])
#     i += 1


# when you don't know the number of iterations then use while loop

# while True:
#     print("Hello World")

# while True:
#     print("Hello World")
#     break

stop = int(input("Enter a number to stop quit 0: "))
while True:
    if stop == 0:
        break
    num = int(input("Enter a number: "))
    print(num)
        
    