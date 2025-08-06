# # str1 = input("Enter your string: ")
# # vowels = "aeiouAEIOU"

# # for i in range(len(str1)):
# #     if str1[i] in vowels:
# #         str1 = str1.replace(str1[i], "")  # replace vowels with empty string

# # print("String without vowels:", str1)

# # for i in str1:
# #     if i in vowels:
# #         str1 = str1.replace(i, "")  # replace vowels with empty string

# # print("String without vowels:", str1)

# while True:
#     print("If you want to exit press 'q': ")
#     if input() == 'q':
#         break
#     else:
#         str1 = input("Enter your string: ")
#         vowels = "aeiouAEIOU"

#         # for i in range(len(str1)):
#         #     if str1[i] in vowels:
#         #         str1 = str1.replace(str1[i], "")  # replace vowels with empty string

#         # print("String without vowels:", str1)
#         for i in str1:
#             if i in vowels:
#                 str1 = str1.replace(i, "")  # replace vowels with empty string

#         print("String without vowels:", str1)

# str1 = input("Enter your string: ")
# char = input("Enter your character: ")
# print(str1.count(char))
while True:
    str1 = input("Enter your string: ")
    print("If you want to exit press 'q': ")
    if input() == 'q':
        break
    else:
        char = input("Enter your character: ")
        print(str1.count(char))
