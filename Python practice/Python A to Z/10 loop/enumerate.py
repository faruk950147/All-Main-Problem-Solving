# enumerate method is used to get index of iterable object
# li = ["a", "b", "c", "d", "e"]
# for i in enumerate(li):
#     print(i) #return tuple

# enumerate method is used to get index of iterable object and value
li = ["a", "b", "c", "d", "e"]
for i, j in enumerate(li):
    print(i, j) # return index and value
    print(type(i)) # type of index int