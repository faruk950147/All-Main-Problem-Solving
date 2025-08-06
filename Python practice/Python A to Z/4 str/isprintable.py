# isprintable() # it checks only printable
def isprintable1(word):
    return word.isprintable()
print(isprintable1("Hello")) # True because it contains only printable
print(isprintable1("Hello\n")) # False because it contains special character
print(isprintable1("Hello\t")) # False because it contains special character
print(isprintable1("Hello\r")) # False because it contains special character
print(isprintable1("Hello\b")) # False because it contains special character
print(isprintable1("Hello\f")) # False because it contains special character

