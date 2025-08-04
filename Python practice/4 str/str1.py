# str1 = "Hello World!"
# str2 = "Welcome to Python"
# str3 = """Hello World!"""
# str4 = """Hello World!"""
# print(str2)
# print(str3)
# print(str4)
# print(str1)
# print(str2)
# print(str1 + " " + str2) # string concatenation
# print(str1 * 3) # string repetition
# print(len(str1)) # string length
# first character
# print(str1[0]) # positive index
# # last character
# print(str1[-1]) # negative index
# # slice
# print(str1[0:5]) # positive index and 0 to 5
# step index 1 missing
# print(str1[0:5:2]) # positive index and 0 to 5 with step index 2
# print(str1[0:5:1]) # positive index and 0 to 5 with step index 1
# # reverse
# print(str1[::-1])
str1 = "Hello World"
print(str1.sort(reverse=True))
# print(str1[0:1])
# print(str1[:4]) # index 0 to 4
# print(str1[0:]) # index 1 to 3
# print(str1[6:]) # index 6 to end
# print(str1[6:10]) # index 6 to 9
# print(str1[6:10:2]) # index 6 to 9 step 2
# print(str1[::-1]) # reverse string
# print(str1[::2]) # step 2
# print(str1[:5] + "Python" + str1[6:]) # index 0 to 4 + "Python" + index 6 to end

# string methods
# print(str1.ljust(20, "*")) # left justify
# print(len(str1.rjust(20, "*"))) # right justify
# print(str1.center(20, "*")) # center justify
# print(str1.strip("*")) # strip
# # print(str1.lstrip("*"))
# # print(str1.rstrip("*"))
# print(str1.zfill(20))
# print(str1.replace("World", "Python"))
# print(str1.split(" "))
# print(str1.join(" "))   
# print(str1.find("World"))
# print(str1.rfind("World"))
# print(str1.index("World"))
# print(str1.count("o"))
# print(str1.startswith("Hello"))
# print(str1.endswith("!"))
# print(str1.upper())
# print(str1.lower())
# print(str1.title())
# print(str1.capitalize())
# print(str1.swapcase())
# print(str1.casefold())

# str to bytes
# print(str1.encode())

# # bytes to str
# print(str1.decode())

# expandtabs (default tab size is 8)
# print(str1.expandtabs(10))
# print(str1.format_map({"name": "World"}))
# print(str1.isalnum())
# print(str1.isalpha())
# print(str1.isdigit())
# print(str1.islower())
# print(str1.isupper())
# print(str1.istitle())
# print(str1.isnumeric())
# print(str1.isprintable())
# print(str1.isspace())
# str1 = "Hello World"
# print(str1.isidentifier())
# print(str1.iskeyword())
# # string format
# print("{} {}".format("Hello", "World"))
# print("{0} {1}".format("Hello", "World"))
# print("{1} {0}".format("Hello", "World"))
# print("{greeting} {name}".format(greeting="Hello", name="World"))
# print("{greeting} {name}".format(name="World", greeting="Hello"))
# print("{greeting} {name}".format(name="World", greeting="Hello"))
# print("{greeting} {name}".format(name="World", greeting="Hello"))
# f-string
# print(f"{str1} {str2}")
# print(f"{str1} {str2}".upper())
