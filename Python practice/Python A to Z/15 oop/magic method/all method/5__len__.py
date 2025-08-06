# 🎯 5. __len__(self)

# work: Return length of object
# Example:
class User:
    def __init__(self, name):
        self.name = name
    
    def __len__(self):
        return len(self.name)

u = User("Omar")
print(len(u))  # Output: 4

# Usage: Return length of object
