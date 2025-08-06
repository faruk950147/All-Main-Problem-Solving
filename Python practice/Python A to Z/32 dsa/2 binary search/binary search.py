# lst = [1, 2, 3, 4, 5]
# lst in search item using binary search
# target = 3 search item

# def binary_search(lst, target):
#     left, right = 0, len(lst) - 1
#     while left <= right: 
#         mid = (left + right) // 2
#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# if __name__ == "__main__":
#     lst = [1, 2, 3, 4, 5]
#     print("Before search:", lst)
#     target = 3
#     print("After search:", binary_search(lst, target))


def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    for i in range(left, right + 1):
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print("Before search:", lst)
    target = 3
    print("After search:", binary_search(lst, target))