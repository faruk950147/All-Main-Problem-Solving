# 🎯 1. __init__(self, ...)

# work: Object creating Run (Constructor)
# Example:

# class User:
#     def __init__(self, name):
#         self.name = name

# u = User("Omar")
# print(u.name)  # Output: Omar

# Usage: Every class has this method by default.


# 🎯 2. __str__(self)

# work: Human-readable text when print(object)
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self):
#         return f"User object: {self.name}"

# u = User("Omar")
# print(u)  # Output: User object Omar

# Usage: EvLogging, Debugging


# 🎯 3. __repr__(self)

# work: Official string representation (debugging friendly)
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __repr__(self):
#         return f"User object: {self.name}"

# u = User("Omar")
# print(u)  # Output: User object Omar

# Usage: EvLogging, Debugging


# 🎯 4. __call__(self, ...)

# work: Make object callable (like function) that can be called like a function
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __call__(self):
#         return f"User object: {self.name}"

# u = User("Omar")
# print(u())  # Output: User object Omar

# Usage: Callable objects


# 🎯 5. __len__(self)

# work: Return length of object
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __len__(self):
#         return len(self.name)

# u = User("Omar")
# print(len(u))  # Output: 4

# Usage: Length of object


# 🎯 6. __getitem__(self, key)

# work: Access object like a dictionary
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __getitem__(self, key):
#         return self.name[key]

# u = User("Omar")
# print(u[0])  # Output: O

# Usage: Access object like a dictionary


# 🎯 7. __setitem__(self, key, value)

# work: Set value of object like a dictionary
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __setitem__(self, key, value):
#         self.name[key] = value

# u = User("Omar")
# u[0] = "A"
# print(u.name)  # Output: Omar

# Usage: Set value of object like a dictionary


# 🎯 8. __delitem__(self, key)

# work: Delete value of object like a dictionary
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __delitem__(self, key):
#         del self.name[key]

# u = User("Omar")
# del u[0]
# print(u.name)  # Output: Omar

# Usage: Delete value of object like a dictionary


# 🎯 9. __iter__(self)

# work: Make object iterable (like list)
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __iter__(self):
#         return iter(self.name)

# u = User("Omar")
# for i in u:
#     print(i)  # Output: O m a r

# Usage: Make object iterable (like list)


# 🎯 10. __next__(self)

# work: Return next item of object
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __next__(self):
#         return self.name

# u = User("Omar")
# print(next(u))  # Output: O

# Usage: Return next item of object


# 🎯 11. __contains__(self, item)

# work: Check if item is in object
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __contains__(self, item):
#         return item in self.name

# u = User("Omar")
# print("O" in u)  # Output: True

# Usage: Check if item is in object


# 🎯 12. __eq__(self, other)

# work: Check if object is equal to other object
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __eq__(self, other):
#         return self.name == other.name

# u1 = User("Omar")
# u2 = User("Omar")
# print(u1 == u2)  # Output: True

# Usage: Check if object is equal to other object


# 🎯 13. __ne__(self, other)

# work: Check if object is not equal to other object
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __ne__(self, other):
#         return self.name != other.name

# u1 = User("Omar")
# u2 = User("Omar")
# print(u1 != u2)  # Output: False

# Usage: Check if object is not equal to other object


# 🎯 14. __lt__(self, other)

# work: Check if object is less than other object
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __lt__(self, other):
#         return self.name < other.name

# u1 = User("Omar")
# u2 = User("Omar")
# print(u1 < u2)  # Output: False

# Usage: Check if object is less than other object


# 🎯 15. __le__(self, other)

# work: Check if object is less than or equal to other object
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __le__(self, other):
#         return self.name <= other.name

# u1 = User("Omar")
# u2 = User("Omar")
# print(u1 <= u2)  # Output: True

# Usage: Check if object is less than or equal to other object


# 🎯 16. __gt__(self, other)

# work: Check if object is greater than other object
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __gt__(self, other):
#         return self.name > other.name

# u1 = User("Omar")
# u2 = User("Omar")
# print(u1 > u2)  # Output: False

# Usage: Check if object is greater than other object


# 🎯 17. __ge__(self, other)

# work: Check if object is greater than or equal to other object
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __ge__(self, other):
#         return self.name >= other.name

# u1 = User("Omar")
# u2 = User("Omar")
# print(u1 >= u2)  # Output: True

# Usage: Check if object is greater than or equal to other object


# 🎯 18. __add__(self, other)

# work: Add two objects
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __add__(self, other):
#         return self.name + other.name

# u1 = User("Omar")
# u2 = User("Omar")
# print(u1 + u2)  # Output: OmarOmar

# Usage: Add two objects


# 🎯 19. __sub__(self, other)

# work: Subtract two objects
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __sub__(self, other):
#         return self.name - other.name

# u1 = User("Omar")
# u2 = User("Omar")
# print(u1 - u2)  # Output: OmarOmar

# Usage: Subtract two objects


# 🎯 20. __mul__(self, other)

# work: Multiply two objects
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __mul__(self, other):
#         return self.name * other.name

# u1 = User("Omar")
# u2 = User("Omar")
# print(u1 * u2)  # Output: OmarOmar

# Usage: Multiply two objects


# 🎯 21. __truediv__(self, other)

# work: Divide two objects
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __truediv__(self, other):
#         return self.name / other.name

# u1 = User("Omar")
# u2 = User("Omar")
# print(u1 / u2)  # Output: OmarOmar

# Usage: Divide two objects


# 🎯 22. __floordiv__(self, other)

# work: Floor divide two objects
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __floordiv__(self, other):
#         return self.name // other.name

# u1 = User("Omar")
# u2 = User("Omar")
# print(u1 // u2)  # Output: OmarOmar

# Usage: Floor divide two objects


# 🎯 23. __mod__(self, other)

# work: Modulo two objects
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __mod__(self, other):
#         return self.name % other.name

# u1 = User("Omar")
# u2 = User("Omar")
# print(u1 % u2)  # Output: OmarOmar

# Usage: Modulo two objects


# 🎯 24. __pow__(self, other)

# work: Power two objects
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __pow__(self, other):
#         return self.name ** other.name

# u1 = User("Omar")
# u2 = User("Omar")
# print(u1 ** u2)  # Output: OmarOmar

# Usage: Power two objects


# 🎯 25. __len__(self)

# work: Return length of object
# Example:
# class User:
#     def __init__(self, name):
#         self.name = name
    
#     def __len__(self):
#         return len(self.name)

# u = User("Omar")
# print(len(u))  # Output: 4

# Usage: Return length of object

