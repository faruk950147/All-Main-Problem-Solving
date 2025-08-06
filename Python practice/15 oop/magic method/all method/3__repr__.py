# 🎯 3. __repr__(self)

# work: Official string representation (debugging friendly)
# Example:
class User:
    def __init__(self, name):
        self.name = name
    
    # work: Official string representation (debugging friendly) developer friendly
    def __repr__(self):
        return f"User object: {self.name}"

u = User("Omar")
print(u)  # Output: User object Omar

# Usage: Every class has this method by default.