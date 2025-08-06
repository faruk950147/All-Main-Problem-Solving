
list2 = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]
print(list2[0][1][1])  # Output: 6

for i in range(len(list2)): # Block level
    for j in range(len(list2[i])): # Row level
        for k in range(len(list2[i][j])): # Column level
            print(list2[i][j][k], end=" ")
        print()
# for i in list1:
#     for j in i:
#         for k in j:
#             print(k, end=" ")
#         print()