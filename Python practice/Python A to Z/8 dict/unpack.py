dict1 = {'a': 1, 'b': 2, 'c': 3}
a, b, c = dict1.values()
print(a)
print(b)
print(c)

def unpack_dict(dict1):
    a, b, c = dict1.values()
    return a, b, c

a, b, c = unpack_dict(dict1)
print(a)
print(b)
print(c)
    