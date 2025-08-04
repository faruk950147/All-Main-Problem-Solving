def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")
    
if __name__ == '__main__':
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    print_full_name(first, last)
    
firstName = "Faruk"
lastName = "Ahmed"
fullName = firstName + " " + lastName
print(fullName)
