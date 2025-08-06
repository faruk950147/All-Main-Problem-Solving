# str1 = "I Love Python Programming"

# str2 = str1.replace("Python", "Java")

# print(str1)  # I Love Python Programming
# print(str2)  # I Love Java Programming
# print()

# def remove_space(s):
#     new_str = ''
#     for i in range(len(s)):
#         if s[i] != ' ':
#             new_str += s[i]
#     return new_str


# text = input("Enter a string with spaces: ")

# result = remove_space(text)

# print("Without spaces:", result)


# def remove_space(s):
#     return s.replace(' ', '')

# text = input("Enter a string with spaces: ")
# result = remove_space(text)
# print("Without spaces:", result)


# str1 = "I Love Python Programming"
# del str1
# print(str1


# word = input("Enter a word: ")

# for i in range(0, len(word) // 2):
#     if word[i] == word[len(word) - i - 1]:
#         continue  
#     else:
#         print("Not Palindrome")
#         break
# else:
#     # for loop 
#     print("Palindrome")
    
# word = input("Enter a word: ")
# is_palindrome = True  

# for i in range(0, len(word) // 2):
#     if word[i] != word[len(word) - i - 1]:
#         is_palindrome = False
#         break
        
# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# def palindrome(word):
#     new_word = word[::-1]
#     if word == new_word:
#         return True
#     else:
#         return False
# def is_palindrome(word):
#     for i in range(len(word) // 2):
#         if word[i] != word[-(i + 1)]:
#             return False
#     return True

# def is_palindrome(word):
#     for i in range(len(word) // 2):
#         if word[i] != word[len(word) - i - 1]:
#             return False
#     return True

# word = input("Enter a word or sentence: ")

# if is_palindrome(word):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# def is_palindrome(word):
#     return word == word[::-1]



    
# word = input("Enter a word ")
# new_word = word[::-1]
# if word == new_word:
#     print("is palindrome")
# else:
#     print("is not palindrome")

word = input("Enter a word: ")
if word == word[::-1]:
    print(f"{word} is Palindrome")
else:
    print(f"{word} is Not Palindrome")


# vowels = 'aeiou'
# str1 = input().casefold()
# count = {}.fromkeys(vowels, 0)
# print(count)



# str1 = input()
# r=''
# for i in range(str1):
#     r=i+r
# print(r)

# str1 = input()

