# def vowelAndConsonant(str1):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for i in range(len(str1)):
#         if str1[i] in vowels:
#             count += 1
#     return count

# print(vowelAndConsonant("Hello World"))


# def consonantAndVowel(str1):
#     consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
#     count = 0
#     for i in range(len(str1)):
#         if str1[i] in consonant:
#             count += 1
#     return count

# print(consonantAndVowel("Hello World"))

def countVowelAndConsonant(str1):
    vowels = "aeiouAEIOU"
    consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for i in str1:
        if i in vowels:
            count += 1
            print(f"vowel {i} count {count}")
        elif i in consonant:
            count += 1
            print(f"consonant {i} count {count}")
        else:
            continue
    return count

print(countVowelAndConsonant("Hello World"))