# slice method is used to get a part of string
# slice(start, stop, step)
str1 = "Hello World"
print(len(str1))
# 0 to 5 positive index
# print(str1[0:5]) # Hello by default step is 1
# # 0 to 5 positive index with step 1 and it's default value
# print(str1[0:5:1]) # Hello by default step is 1
# # 0 to 5 with step 2 positive index
# print(str1[0:5:2]) # Hlo step is 2
# missing start end step
# print(str1[:]) # missing all step output Hello World
# print(str1[::]) # missing all step output Hello World
# print(str1[::1]) # missing all step 1 output Hello World
# print(str1[::2]) # missing all step 2 output Hlo
# missing start step
# print(str1[:5]) # missing step output Hello
# print(str1[:5:1]) # missing step 1 output Hello
# print(str1[:5:2]) # missing step 2 output Hlo
# # missing end step
# print(str1[5:]) # missing step output World
# print(str1[5:1]) # when start is greater than end it return empty string
# print(str1[5:2]) # when start is greater than end it return empty string

# negative index
print(str1[-6:-1]) # World
print(str1[-6:-1:1]) # World
print(str1[-6:-1:2]) # Wrd
print(str1[-6:-1:3]) # Wl
print(str1[-6:-1:4]) # W
print(str1[-6:-1:5]) # 
# missing start step
print(str1[-6:]) # World
print(str1[-6:1]) # when start is greater than end it return empty string
print(str1[-6:2]) # when start is greater than end it return empty string
# missing end step
print(str1[:-1]) # missing step output Hello World
print(str1[:-1:1]) # missing step 1 output Hello World
print(str1[:-1:2]) # missing step 2 output Hlo
