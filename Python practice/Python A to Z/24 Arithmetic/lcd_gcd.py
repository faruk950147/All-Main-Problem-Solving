# # using gcd
# num1, num2 = list(map(int, input().split()))
# temp1, temp2 = num1, num2
# # GCD 
# while num2 != 0:
#     num1, num2 = num2, num1 % num2

# print(f"GCD: {num1} LCM: {(temp1 * temp2) // num1}")

import math
from functools import reduce

# GCD
def find_gcd(numbers):
    return reduce(math.gcd, numbers)

# LCM
def find_lcm(numbers):
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)
    return reduce(lcm, numbers)

nums = list(map(int, input("Enter numbers: ").split()))
print("GCD:", find_gcd(nums))    # ✅ Output: 5
print("LCM:", find_lcm(nums))    # ✅ Output: 525



# # GCD
# def find_gcd(*numbers):
#     return reduce(math.gcd, numbers)

# # LCM
# def find_lcm(*numbers):
#     def lcm(a, b):
#         return abs(a * b) // math.gcd(a, b)
#     return reduce(lcm, numbers)

# nums = list(map(int, input("Enter numbers: ").split()))

# print("GCD:", find_gcd(*nums))   # ✅ Output: 5
# print("LCM:", find_lcm(*nums))   # ✅ Output: 525
