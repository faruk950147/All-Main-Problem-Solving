list1 = [1, 2, 3, 4, 5]
# squares = list(map(lambda value: value * value, list1))
# print(squares)


def filter(list1, callback):
    result = []
    for i in list1:
        if callback(i, list1):
            result.append(i)
    return result

def even(value, array):
    return value % 2 == 0

def odd(value, array):
    return value % 2 != 0

print(filter(list1, even))
print(filter(list1, odd))


def filter(list1, callback):
    result = []
    for i in range(len(list1)):
        if callback(list1[i], i, list1):
            result.append(list1[i])
    return result

def even(value, index, array):
    return value % 2 == 0

def odd(value, index, array):
    return value % 2 != 0

print(filter(list1, even))
print(filter(list1, odd))

# print(filter(list1, lambda value: value % 2 == 0))
# print(filter(list1, lambda value: value % 2 != 0))