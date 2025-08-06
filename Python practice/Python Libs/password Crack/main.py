import itertools
import string
from pikepdf import PasswordError
import pikepdf

# password = string.ascii_letters + string.digits + string.punctuation
# for i in range(1, 5):
#     for j in itertools.product(password, repeat=i):
#         # join j tuple into string
#         word = ''.join(j)
#         # password warehouse
#         with open("warehouse.txt", "a") as f:
#             try:
#                 f.write(word + "\n")
#                 print(f"Password Generated Successfully: {word}")
#             except Exception as e:
#                 print("Exception", str(e))

# Ensure the PDF is password protected
# pdfPath = r"sample.pdf"

# try:
#     with pikepdf.open(pdfPath) as pdf:
#         print("PDF is not password protected")
# except PasswordError:
#     print("PDF is password protected")
# except Exception as e:
#     print("Exception", str(e))


with open("warehouse.txt", "r") as f:
    count = 0
    for password in f:
        password = password.strip()
        count += 1
        try:
            pikepdf.open("sample.pdf", password=password)
            print(f"Password Found: {password}")
            break
        except Exception as e:
            print(f"{count} : {password} : Password Not Found")


