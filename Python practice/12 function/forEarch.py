list1 = [1, 2, 3, 4, 5]

# def forEach(list1,callback):
#     for i in list1:
#         callback(i, list1)

# def printValue(value,array):
#     print(f"Value: {value} Array: {array}")

def forEach(arr,callback):
    for i in range(len(arr)):
        callback(arr[i], i, arr)
        

def printValue(value,index,array):
    print(f"Value: {value} Index: {index} Array: {array}")

forEach(list1, printValue)

# forEach(list1, lambda value,index,array: print(f"Value: {value} Index: {index} Array: {array}"))


















