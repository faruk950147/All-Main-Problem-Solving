# same variable name same memory location stored. and must be same data type.and same value
# defrent variable name defrent memory location stored./

# a = 10
# print(a)
# print(type(a))
# output
# 10
# <class 'int'>

# b = float(a)
# print(b)
# print(type(b))
# output
# 10.0
# <class 'float'>

# complex1 = 1+2j
# print(complex1)
# print(type(complex1))
# output
# (1+2j)
# <class 'complex'>

# c = int(b)
# print(c)
# print(type(c))
# output
# 10
# <class 'int'>

# d = complex(a)
# print(d)
# print(type(d))
# output
# (10+0j)
# <class 'complex'>

# e = complex(b)
# print(e)
# print(type(e))
# output
# (10+0j)
# <class 'complex'>

# f = complex(a, b)
# print(f)
# print(type(f))
# output
# (10+10j)
# <class 'complex'>

# # Type Conversion
# list1 = [1, 2, 3, 4, 5]
# tuple1 = tuple(list1)
# print(tuple1)
# print(type(tuple1))
# output
# (1, 2, 3, 4, 5)
# <class 'tuple'>
# set1 = set(list1)
# print(set1)
# print(type(set1))
# output
# {1, 2, 3, 4, 5}
# <class 'set'>
# frozenset1 = frozenset(list1)
# print(frozenset1)
# print(type(frozenset1))
# output
# frozenset({1, 2, 3, 4, 5})
# <class 'frozenset'>
# str1 = str(list1)
# print(str1)
# print(type(str1))
# output
# [1, 2, 3, 4, 5]
# <class 'str'>

# bool1 = bool(list1)
# print(bool1)
# print(type(bool1))
# output
# True
# <class 'bool'>
# none1 = None
# print(none1)
# print(type(none1))
# output
# None
# <class 'NoneType'>

# int1 = int(none1)
# print(int1)
# print(type(int1))
# output
# 0
# <class 'int'>

# float1 = float(none1)
# print(float1)
# print(type(float1))
# output
# 0.0
# <class 'float'>

# complex1 = complex(none1)
# print(complex1)
# print(type(complex1))
# output
# 0j
# <class 'complex'>
# dict1 = dict(list1)
# print(dict1)
# print(type(dict1))  
# output
# {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
# <class 'dict'>

# # Type Conversion
# list2 = list(tuple1)
# print(list2)
# print(type(list2))
# output
# [1, 2, 3, 4, 5]
# <class 'list'>
# set2 = set(tuple1)
# print(set2)
# print(type(set2))
# output
# {1, 2, 3, 4, 5}
# <class 'set'>
# frozenset2 = frozenset(tuple1)
# print(frozenset2)
# print(type(frozenset2))
# output
# frozenset({1, 2, 3, 4, 5})
# <class 'frozenset'>
# str2 = str(tuple1)
# print(str2)
# print(type(str2))
# output
# (1, 2, 3, 4, 5)
# <class 'str'>
# output
# (1, 2, 3, 4, 5)
# <class 'str'>

# bool2 = bool(tuple1)
# print(bool2)
# print(type(bool2))
# output
# True
# <class 'bool'>
# none2 = None
# print(none2)
# print(type(none2))
# output
# None
# <class 'NoneType'>

# int2 = int(none2)
# print(int2)
# print(type(int2))
# output
# 0
# <class 'int'>
# float2 = float(none2)
# print(float2)
# print(type(float2))
# output
# 0.0
# <class 'float'>

# complex2 = complex(none2)
# print(complex2)
# print(type(complex2))
# output
# 0j
# <class 'complex'>
# dict2 = dict(tuple1)
# print(dict2)
# print(type(dict2))
# output
# {1: 2, 2: 3, 3: 4, 4: 5}
# <class 'dict'>
