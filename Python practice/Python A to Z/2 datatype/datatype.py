# Python Data Type
# Data type is the type of data stored in a variable.
# same variable name same memory location stored. and must be same data type.and same value
# defrent variable name defrent memory location stored./

# Python has 6 happiness data types.

        # 1. Numeric Type
        
        # Numeric type is used to store numeric values.
        
        # int, float, complex
        
        # int is used to store integer values.
        
        # ex: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
a = 10
print(a)
# output
# 10
                
        # float is used to store floating point values.
        
        # ex: 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10
b = 10.10
print(b)
# output
# 10.1
        
        # complex is used to store complex numbers.
        
        # ex: 1+2j, 2+3j, 3+4j, 4+5j, 5+6j, 6+7j, 7+8j, 8+9j, 9+10j, 10+11j
c = 10+11j
print(c)
# output
# (10+11j)
        
        
        

        # 2. Sequence Type
        
        # Sequence type is used to store sequence values.
        
        # str, list, tuple
        
        # str is used to store string values.
                
        # ex: "Hello World!"
d = "Hello World!"
print(d)
# output
# Hello World!
        
        # list is used to store list values.
        
        # ex: [1, 2, 3, 4, 5]
e = [1, 2, 3, 4, 5]
print(e)
# output
# [1, 2, 3, 4, 5]
# output
# [1, 2, 3, 4, 5]
        
        # tuple is used to store tuple values.
        
        # ex: (1, 2, 3, 4, 5)
f = (1, 2, 3, 4, 5)
print(f)
# output
# (1, 2, 3, 4, 5)
        # 3. Mapping Type
        
        # Mapping type is used to store mapping values.
        
        # dict
        
        # dict is used to store dictionary values.
        
        # ex: {"name": "John", "age": 30, "city": "New York"}
g = {"name": "John", "age": 30, "city": "New York"}
print(g)
# output
# {"name": "John", "age": 30, "city": "New York"}
        # 4. Set Type
        
        # Set type is used to store set values.

        # set, frozenset
        
        # set is used to store set values.
        
        # ex: {1, 2, 3, 4, 5}
h = {1, 2, 3, 4, 5}
print(h)
# output
# {1, 2, 3, 4, 5}
        
        # frozenset is used to store frozenset values.
        
        # ex: frozenset({1, 2, 3, 4, 5})
i = frozenset({1, 2, 3, 4, 5})
print(i)
# output
# frozenset({1, 2, 3, 4, 5})

        # 5. Boolean Type
        
        # Boolean type is used to store boolean values.
            
        # bool
        
        # bool is used to store boolean values.
        
        # ex: True, False
i = True
print(i)
# output
# True
        # 6. None Type
        
        # None type is used to store None values.
        
        # None is used to store None values.  

        # ex: None          
j = None
print(j)
# output
# None

# check data type  isinstance()

# print(isinstance(a, int))
# output
# True  
# print(isinstance(b, float))
# output
# True
# print(isinstance(c, complex))
# output
# True
# print(isinstance(d, str))
# output
# True
# print(isinstance(e, list))
# output
# True
# print(isinstance(f, tuple))
# output
# True
# print(isinstance(g, dict))
# output
# True
# print(isinstance(h, set))
# output
# True
# print(isinstance(i, frozenset))
# output
# True
# print(isinstance(j, bool))
# output
# True
# print(isinstance(j, NoneType))
# output
# True

