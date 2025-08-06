# __all__

name = "John"
def personal_info():
    return "I am from personal info function!"

def private_info():
    return "I am from private info function!"

def protected_info():
    return "I am from protected info function!"

def public_info():
    return "I am from public info function!"

def display_info():
    return "I am from display info function!"

# __all__ = ["name", "personal_info", "private_info", "protected_info", "public_info", "display_info"]

if __name__ == "__main__":
    print(name)
    print(personal_info())
    print(private_info())
    print(protected_info())
    print(public_info())
    print(display_info())
