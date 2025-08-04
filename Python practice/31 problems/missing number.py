# def missing_number(li):
#     n = len(li) + 1
#     total = n * (n + 1) // 2
#     return total - sum(li)

# print(missing_number([1, 2, 3, 5]))

# def missing_number2(li):
#     for i in range(1, len(li) + 1):
#         if i not in li:
#             return i

# print(missing_number2([1, 2, 3, 5]))

# def missing_number3(li):
#     li.sort()
#     for i in range(len(li)):
#         if li[i] != i + 1:
#             return i + 1

# print(missing_number3([1, 2, 3, 5]))

