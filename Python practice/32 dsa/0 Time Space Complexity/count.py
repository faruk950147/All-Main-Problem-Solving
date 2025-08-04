# exponential
# Time Complexity: O(2^n)
# Space Complexity: O(1)
# Exponential 
    # 2**n = 2^0 + 2^1 + 2^2 + ... + 2^(n-1)
    
# multiplication
    # 2*n = 2^0 + 2^1 + 2^2 + ... + 2^(n-1)

# n = int(input())
# count = 0
# # Time Complexity: O(n)
# # Space Complexity: O(1)
# for i in range(1, n + 1):
#     count += 1
# print(count)


# Example 2 square root
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# n = int(input())
# count = 0
# for i in range(n):
#     for j in range(n):
#         count += 1
# print(count)

# Example 3 

n = int(input())
count = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            count += 1
print(count)