# def collision(list1, list2):
    # return [value for value in list1 if value in list2]
    # return list(set(list1) & set(list2))
    # return list(set(list1).intersection(set(list2)))
    # for i in list1:
    #     if i in list2:
    #         return True
    # return False
    # for i in list1:
    #     for j in list2:
    #         if i == j:
    #             return True
    # return False
#     for i in range(len(list1)):
#         for j in range(len(list2)):
#             if list1[i] == list2[j]:
#                 return True
#     return False
    
# print(collision([1,2,3,4,5], [4,5,6,7,8]))

def collision(rect1, rect2):
    # rect1 and rect2 are dictionaries or objects with x, y, width, height
    if (rect1['x'] < rect2['x'] + rect2['width'] and
        rect1['x'] + rect1['width'] > rect2['x'] and
        rect1['y'] < rect2['y'] + rect2['height'] and
        rect1['y'] + rect1['height'] > rect2['y']):
        return True
    else:
        return False
print(collision({'x': 1, 'y': 1, 'width': 10, 'height': 10}, {'x': 5, 'y': 5, 'width': 10, 'height': 10}))