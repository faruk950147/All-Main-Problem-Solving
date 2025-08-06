# from functools import reduce

list1 = [1, 2, 3, 4]
# sum_value = reduce(lambda prev, curr: prev + curr, list1, 0)

# print(sum_value)  # Output: 10

def reduce(list1, callback, initial):
    result = initial
    for i in list1:
        result = callback(result, i)
    return result

def sum_value(prev, curr):
    return prev + curr

sum_value = reduce(list1, sum_value, 0)
print(sum_value)  # Output: 10


def reduce(list1, callback, initial):
    result = initial
    for i in range(len(list1)):
        result = callback(result, list1[i], i, list1)
    return result

def sum_value(prev, curr, index, list1):
    return prev + curr

sum_value = reduce(list1, sum_value, 0)
print(sum_value)  # Output: 10

# sum_value = reduce(list1, lambda prev, curr, index, array: prev + curr, 0)
# print(sum_value)  # Output: 10
