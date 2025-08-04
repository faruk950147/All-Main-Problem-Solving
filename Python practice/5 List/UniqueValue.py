def duplicate_remove_with_if(lst):
    li = []
    for i in lst:
        if lst.count(i) == 1:
            li.append(i)
    return li
print(duplicate_remove_with_if([1,2,2,3,3,4,5,5,5,6,6,6,7,7,7,7]))

def duplicate_remove_with_set(lst):
    return list(set(lst))
print(duplicate_remove_with_set([1,2,2,3,3,4,5,5,5,6,6,6,7,7,7,7]))

def duplicate_remove_with_count(lst):
    li = []
    for i in range(0, len(lst)):
        if lst[:i].count(lst[i]) == 0:
            li.append((i))
    return li
print(duplicate_remove_with_count([1,2,2,3,3,4,5,5,5,6,6,6,7,7,7,7]))

# def unique_with_if(lst):
#     li = []
#     # for i in range(len(lst)):
#     #     if lst[i] not in li:
#     #         li.append((lst[i]))
#     # return li
#     for i in lst:
#         if i not in li:
#             li.append(i)
#     return li
# print(unique_with_if([1,2,3,3,4,4]))

# def unique_with_count(lst):
#     li = []
#     for i in range(0, len(lst)):
#         if lst[:i].count(lst[i]) == 0:
#             li.append((i))
#     return li
# print(unique_with_count([1,2,3,3,4,4]))

# def unique_with_set(lst):
#     return list(set(lst))
# print('**************',unique_with_set([1,2,3,3,4,4]))

# given two lists find the common elements
list1 = [2, 3, 4, 5, 5, 6, 7]
list2 = [5, 6, 7, 8, 9, 5, 10]

# common elements 
common = []


# for item in list1:
#     if item in list2 and item not in common:
#         common.append(item)

# # increasing order 
# common.sort()
# for i in list1:
#     if i in list2:
#         if i not in common:
#             common.append(i)

# print(common)

# li = [1,2,3,4]
# li[1:3] = [8,9]
# print(li)
# print(2**3**2)
li2 = [1,2,3]
print(li2[3:])
print(li2[:3])
print(li2[:])


