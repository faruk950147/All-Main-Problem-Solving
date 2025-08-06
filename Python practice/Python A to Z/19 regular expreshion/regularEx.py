import re

pattern = "hello"
text = "hello world"

match = re.search(pattern, text)
if match:
    print("Match found!")
else:
    print("No match found.")
