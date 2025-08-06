list1 = [2, 3, 4, 5, 5, 6, 7]
list2 = [5, 6, 7, 8, 9, 5]

# common elements 
common = []


for item in list1:
    if item in list2 and item not in common:
        common.append(item)

# # increasing order 
common.sort()
# for i in list1:
#     if i in list2:
#         if i not in common:
#             common.append(i)

# print(common)

list1 = [2, 3, 4, 5, 5, 6, 7]
list2 = [5, 6, 7, 8, 9, 5]

common = sorted(list(set(list1) & set(list2)))

print(common)
