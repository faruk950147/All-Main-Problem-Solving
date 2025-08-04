import re
# Basic email validation pattern
# pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# advance email validation pattern
# pattern = r'^[\w\.\+\-]+@[\w\.-]+\.\w+$'


emails = [
    "john.doe@example.com",
    "jane_doe123@gmail.com",
    "admin007@yahoo.co.uk",
    "student.cmt@ttti.edu.bd",
    "omar.cse99@gmail.com",
    "my.email+project2025@domain.io",   # <-- this will fail in this regex
    "user@.com",       # invalid
    "@gmail.com",      # invalid
    "user@gmail",      # invalid
    "user@com.",       # invalid
    "user@@gmail.com"  # invalid
]

# for email in emails:
#     if re.match(pattern, email):
#         print(f"{email} is a valid email.")
#     else:
#         print(f"{email} is an invalid email.")

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False
    
validate_email(emails)

