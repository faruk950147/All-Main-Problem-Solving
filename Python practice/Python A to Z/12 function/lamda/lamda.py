# syntax
# lambda arguments: expression
# sum = lambda x, y: x + y
# print(sum(5, 3))
# even = lambda x: x % 2 == 0
# print(even(5))

# largeOfthree = lambda x, y, z: x if x > y and x > z else y if y > x and y > z else z
# print(largeOfthree(5, 3, 1))

# square = lambda x: x * x
# print(square(5))
# sortedData = lambda data: sorted(data)
# print(sortedData([5, 3, 1]))

# people = [['John', 'Doe', '25', 'M'], ['Jane', 'Smith', '22', 'F']]
# sortedData = lambda data: sorted(data)
# print(sortedData([5, 3, 1]))

# people = [['John', 'Doe', '25', 'M'], ['Jane', 'Smith', '22', 'F']]
# sortedData = lambda data: sorted(data)
# print(sortedData([5, 3, 1]))

# from ast import arguments


# people = [['John', 'Doe', '25', 'M'], ['Jane', 'Smith', '22', 'F']]
# Syntax arguments: expression
# arguments is receive data
# expression is a return value
# arguments is data
# expression is sorted(data, key=lambda person: int(person[2]))
# sorted_people = lambda data: sorted(data, key=lambda person: int(person[2]))
# print(sorted_people(people))

# def strsorted(data):
#     return sorted(data, key=lambda person: int(person[2]))
# print(strsorted([['John', 'Doe', '25', 'M'], ['Jane', 'Smith', '22', 'F']]))    

# Using Lambda with the sorted() Function:

def secondWord(name):
    return name.split()[1] # name of the second word

data = ['Sharma Rohit', 'Kohli Virat', 'Tendulkar Sachin', 
        'Raina Suresh', 'Gill Shubman', 'Kishan Ishan']

# key secondWord function
print(sorted(data, key=secondWord))


