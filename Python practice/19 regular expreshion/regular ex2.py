import re

pattern = "Bangladesh is our homeland"
text = "Bangladesh is our homeland"

match = re.search("o\w\w", text)
if match:
    print(match.group())
else:
    print("No match found.")

# match = re.search(pattern, text)
# if match:
#     print("Match found!")
# else:
#     print("No match found.")
