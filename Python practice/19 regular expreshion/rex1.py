import re

# Email validation pattern (with + support)
pattern = r'^[\w\.\+\-]+@[\w\.-]+\.\w+$'

# mail.txt file
with open(r"L:\\Programming\\Python\\Main Problem Solving\\Python practice\\19 regular expreshion\\mail.txt", 'r') as file:
    lines = file.readlines()

print("Valid Emails:")
for email in lines:
    email = email.strip("\n")  # remove new line
    if re.match(pattern, email):
        print(f"{email}")

print("\nInvalid Emails:")
for email in lines:
    email = email.strip("\n")
    if not re.match(pattern, email):
        print(f"{email}")
