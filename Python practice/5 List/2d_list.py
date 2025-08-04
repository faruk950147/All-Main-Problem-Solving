list1 = [
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        [10,11,12],
        [13,14,15],
        [16,17,18]
    ]
]
print(list1)
city  = [
    ['Dhaka','Chittagong','Khulna'],
    ['Rajshahi','Barisal','Sylhet']
    ]
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[0][0])
# print(list1[0][1])
# print(list1[0][2])
for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j], end=" ")
    print()

# for i in list1:
#     for j in i:
#         print(j)




list2 = [10,11,12,13,14,15,16,17,18,19]
print(list2[len(list2) - 1])
print(list2[-1])
