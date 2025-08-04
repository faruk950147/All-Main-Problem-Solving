
# # find the sum of all digits of a number
# n = int(input("Enter a number: "))
# total = 0
# while n > 0:
#     digit = n % 10
#     n //=10
#     total += digit
# print(total)



# find the sum of last 3 digits of a number
# nums = int(input("Enter a number with at least 3 digits: "))
# count = 0
# total = 0

# while nums > 0 and count < 3:
#     digit = nums % 10
#     nums = nums // 10
#     total += digit
#     count += 1

# print("Total of last 3 digits:", total)
# print(f"Digits of last 3 digits: {digit}")
# print(f"Count of last 3 digits: {count}")

nums = 146
count = 0
total = 0
digits = []

while nums > 0 and count < 3:
    digit = nums % 10
    digits.append(digit)
    nums = nums // 10
    total += digit
    count += 1

print("Total of last 3 digits:", total)
print(f"Digits of last 3 digits: {digits}")
print(f"Count of last 3 digits: {count}")
