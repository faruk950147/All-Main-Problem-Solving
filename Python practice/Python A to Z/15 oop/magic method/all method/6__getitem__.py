# 🎯 6. __getitem__(self, key)

# work: Access object like a dictionary
# Example:
class User:
    def __init__(self, name):
        self.name = name
    
    def __getitem__(self, key):
        return self.name[key]

u = User("Omar")
# Access object like a dictionary
print(u.name) # Output: Omar
print(u[0:]) # Output: Omar
print(u[0:2]) # Output: Om
print(u[:]) # Output: Omar
print(u[0])  # Output: O
print(u[1:3])  # Output: ma
print(u[1])  # Output: m
print(u[-1])  # Output: r

# Usage: Access object like a dictionary
