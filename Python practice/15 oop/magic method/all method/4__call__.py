# 🎯 4. __call__(self, ...)

# work: Make object callable (like function) that can be called like a function
# Example:
class User:
    def __init__(self, name):
        self.name = name
    
    # work: Make object callable (like function) that can be called like a function
    def __call__(self):
        return f"User object: {self.name}"

u = User("Omar")
print(u())  # Output: User object Omar

# Usage: Callable objects
