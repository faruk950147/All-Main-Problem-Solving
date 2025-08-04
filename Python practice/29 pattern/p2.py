# rows = int(input("Enter number of rows: "))
# # upper part of the diamond
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * (2 * i - 1))
    
# # lower part of the diamond
# for i in range(rows, 0, -1):
#     print(" " * (rows - i) + "*" * (2 * i - 1))


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            print("X", end=' ')
        else:
            print("O", end=' ')
    print()