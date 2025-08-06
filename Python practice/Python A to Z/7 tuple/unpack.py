tup1 = (1, 2, 3, 4, 5)
a, b, c, d, e = tup1
print(a)
print(b)
print(c)
print(d)
print(e)

def unpack_tuple(tup1):
    a, b, c, d, e = tup1
    return a, b, c, d, e

a, b, c, d, e = unpack_tuple(tup1)
print(a)
print(b)
print(c)
print(d)
print(e)
