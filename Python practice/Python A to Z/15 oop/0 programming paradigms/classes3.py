
#=============== Same memory location==============
# s1=2
# print(s1)
# print(id(s1))
# s1=2
# print(s1)
# print(id(s1))
# s=2
# print(s)
# print(id(s))
# s1=2
# print(s1)
# print(id(s1))

#=============== Different memory location==============
s1=2
print(s1)
print(id(s1))
s1=3
print(s1)
print(id(s1))

s=2
print(s)
print(id(s))
s=3
print(s)
print(id(s))