# def removeDuplicateFromList(list1):
#     return list(set(list1))


def removeDuplicateFromList(list1):
    li = []
    for index, element in enumerate(list1):
        if element not in li:
            li.append(element)
    return li

print(removeDuplicateFromList([1,2,3,4,5,5,6,7,8,9,9]))

def removeDuplicateFromList2(list1):
    li = []
    for index, element in enumerate(list1):
        if element not in list1[:index]:
            li.append(element)
    return li

print(removeDuplicateFromList2([1,2,2,3,4,5,5,6,7,8,9,9]))