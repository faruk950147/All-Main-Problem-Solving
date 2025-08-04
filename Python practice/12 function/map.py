list1 = [1, 2, 3, 4, 5]
# squares = list(map(lambda value: value * value, list1))
# print(squares)

def map(list1, callback):
    result = []
    for i in list1:
        result.append(callback(i, list1))
    return result

def square(value, array):
    return value * value

def cube(value, array):
    return value * value * value

squares = map(list1, square)
print(squares)

cubes = map(list1, cube)
print(cubes)

def map(list1, callback):
    result = []
    for i in range(len(list1)):
        result.append(callback(list1[i], i, list1))
    return result

def square(value, index, array):
    return value * value

def cube(value, index, array):
    return value * value * value

squares = map(list1, square)
print(squares)

cubes = map(list1, cube)
print(cubes)



squares = map(list1, lambda value, index, array: value * value)
print(squares)
