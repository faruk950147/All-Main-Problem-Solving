set1 = {'a', 'b'}
a, b = set1
print(a)
print(b)

def unpack_set(set1):
    a, b = set1
    return a, b

a, b = unpack_set(set1)
print(a)
print(b)