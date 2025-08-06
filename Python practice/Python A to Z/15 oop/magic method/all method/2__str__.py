# 🎯 2. __str__(self)

# work: Human-readable text when print(object)
# Example:
class User:
    def __init__(self, name):
        self.name = name
    
    # work: Human-readable text when print(object) user friendly
    def __str__(self):
        return f"User object: {self.name}"

u = User("Omar")
print(u)  # Output: User object Omar

# Usage: Every class has this method by default.
