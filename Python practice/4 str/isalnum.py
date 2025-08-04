def isalnum1(word):
    return word.isalnum()

print(isalnum1("HelloWorld")) # True because it contains only alphabets
print(isalnum1("Hello World")) # False because it contains space
print(isalnum1("Hello World 123")) # False because it contains space and numbers
print(isalnum1("HelloWorld123!")) # False because it contains special character
print(isalnum1("HelloWorld123")) # True because it contains only alphabets and numbers

# isalpha() # it checks only alphabets
def isalpha1(word):
    return word.isalpha()
print(isalpha1("HelloWorld")) # True because it contains only alphabets
print(isalpha1("Hello World")) # False because it contains space
print(isalpha1("Hello World 123")) # False because it contains space and numbers
print(isalpha1("HelloWorld123!")) # False because it contains special character
print(isalpha1("HelloWorld123")) # False because it contains numbers
# isdigit() # it checks only digits
def isdigit1(word):
    return word.isdigit()
print(isdigit1("123")) # True because it contains only digits
print(isdigit1("123!")) # False because it contains special character
print(isdigit1("123Hello")) # False because it contains alphabets
# islower() # it checks only lowercase
def islower1(word):
    return word.islower()
print(islower1("hello")) # True because it contains only lowercase
print(islower1("Hello")) # False because it contains uppercase
print(islower1("hello123")) # True because it contains only lowercase and numbers
# isupper() # it checks only uppercase
def isupper1(word):
    return word.isupper()
print(isupper1("HELLO")) # True because it contains only uppercase
print(isupper1("Hello")) # False because it contains lowercase
print(isupper1("HELLO123")) # True because it contains only uppercase and numbers
# istitle() # it checks only title
def istitle1(word):
    return word.istitle()
print(istitle1("Hello")) # True because it contains only title
print(istitle1("hello")) # False because it contains lowercase
print(istitle1("Hello123")) # True because it contains only title and numbers
# isnumeric() # it checks only numeric
def isnumeric1(word):
    return word.isnumeric()
print(isnumeric1("123")) # True because it contains only numeric
print(isnumeric1("123!")) # False because it contains special character
print(isnumeric1("123Hello")) # False because it contains alphabets
# isdecimal() # it checks only decimal
def isdecimal1(word):
    return word.isdecimal()
print(isdecimal1("123")) # True because it contains only decimal
print(isdecimal1("123!")) # False because it contains special character
print(isdecimal1("123Hello")) # False because it contains alphabets
# isidentifier() # it checks only identifier
def isidentifier1(word):
    return word.isidentifier()
print(isidentifier1("Hello")) # True because it contains only identifier
print(isidentifier1("Hello123")) # True because it contains only identifier and numbers
print(isidentifier1("Hello_123")) # True because it contains only identifier and numbers
print(isidentifier1("Hello-123")) # False because it contains special character
print(isidentifier1("Hello 123")) # False because it contains space
# isprintable() # it checks only printable
def isprintable1(word):
    return word.isprintable()
print(isprintable1("Hello")) # True because it contains only printable
print(isprintable1("Hello\n")) # False because it contains special character
print(isprintable1("Hello\t")) # False because it contains special character
print(isprintable1("Hello\r")) # False because it contains special character
print(isprintable1("Hello\b")) # False because it contains special character
print(isprintable1("Hello\f")) # False because it contains special character
# isspace() # it checks only space
def isspace1(word):
    return word.isspace()
print(isspace1(" ")) # True because it contains only space
print(isspace1("\n")) # False because it contains special character
print(isspace1("\t")) # False because it contains special character
print(isspace1("\r")) # False because it contains special character
print(isspace1("\b")) # False because it contains special character
print(isspace1("\f")) # False because it contains special character
