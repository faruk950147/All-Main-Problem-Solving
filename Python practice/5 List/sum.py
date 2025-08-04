# n = int(input())
# li = []
# total = 0 

# for i in range(n):
#     e = int(input())
#     li.append(e)
#     total += li[i]
# # using looping for sum
# print("Sum using loop:", total)
# # using sum function 
# print("Sum using sum:", sum(li))

# def sum_of_list(li):
#     total = 0
#     for i in li:
#         total += i
#     return total

# print(sum_of_list([1,2,3,4,5]))

# def sum_of_list2(li):
#     total = 0
#     for i in range(len(li)):
#         total += li[i]
#     return total

# print(sum_of_list2([1,2,3,4,5]))

# def sum_of_list(li):
#   return sum(li)

# print(sum_of_list([1,2,3,4,5]))



# given a list find the sum of all elements greater than or equal to the current element
# numbers = [2, 4, 6, 10, 1]

# result = []

# for i in range(len(numbers)):
#     sum_value = 0
#     for j in range(i, len(numbers)):
#         if numbers[j] >= numbers[i]:
#             sum_value += numbers[j]
#     result.append(sum_value)

# print(result)


# find the sum of all elements greater than or equal to the current element
# li = [2, 4, 6, 10, 1]

# result = [] 
# for i in li:
#     total = 0
#     for j in li:
#         if j >= i:
#             total+=j
#     result.append(total)
# print(result)

