# lst = [1, 2, 3, 4, 5]
# lst in search item using linear search
# target = 3 search item
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
    
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print("Before search:", lst)
    target = 3
    print("After search:", linear_search(lst, target))

# def linear_search(lst, target):
#     lst = len(lst)
#     i = 0
#     while i < lst:
#         if lst[i] == target:
#             return i
#         i += 1
#     return -1
    
# if __name__ == "__main__":
#     lst = [1, 2, 3, 4, 5]
#     print("Before search:", lst)
#     target = 3
#     print("After search:", linear_search(lst, target))