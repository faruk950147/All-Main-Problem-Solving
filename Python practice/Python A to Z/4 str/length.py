
# _ is a throwaway variable
# _ don't care variable
# _ is ignored variable
# _ is used to throw away the value


str1 = "Hello World!"
length = 0

while True:
    try:
        _ = str1[length]
        length += 1
    except IndexError:
        break

print(length)

# for ch in str1:
#     length += 1

# print(length)

# for _ in str1:
#     length += 1

# print(length)