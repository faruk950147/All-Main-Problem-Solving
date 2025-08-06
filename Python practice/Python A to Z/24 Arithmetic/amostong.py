n = int(input("Enter numbers : "))
original = n
sum = 0
while n > 0:
    digit = n % 10
    sum += digit**3
    n //= 10
if original == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
# nums = int(input("Enter a number: "))
# total = 0
# digits = []
# original = nums  
# while nums > 0:
#     digit = nums % 10
#     digits.append(digit)
#     total += digit
#     nums = nums // 10

# print("Digits:", digits)
# print("Sum of digits:", total)

# if total == original:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")


# import math

# def is_armstrong(n: int) -> bool:
#     if n < 10:
#         return True  
    
#     order = len(str(n))
#     power_sum = sum(int(digit) ** order for digit in str(n))
    
#     return power_sum == n


# def is_armstrong(n):
#     if n == 0:
#         return True
#     order = int(math.log10(n)) + 1

#     temp = n
#     sum = 0
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** order
#         if sum > n:
#             return False
#         temp //= 10

#     return sum == n

# num = int(input("Enter a number: "))
# if is_armstrong(num):
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")


# def is_armstrong(n):
#     digits = [int(d) for d in str(n)]
#     power = len(digits)
#     total = sum(d ** power for d in digits)
#     return total == n

# num = int(input("Enter a number: "))
# if is_armstrong(num):
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is not an Armstrong number")


# def is_armstrong(n):
#     digits = [int(d) for d in str(n)]
#     power = len(digits)
#     total = sum(d ** power for d in digits)
#     return total == n

# print("Armstrong numbers from 1 to 99999:")
# for i in range(1, 100000):
#     if is_armstrong(i):
#         print(i)

