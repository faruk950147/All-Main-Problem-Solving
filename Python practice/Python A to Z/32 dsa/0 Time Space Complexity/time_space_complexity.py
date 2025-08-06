# Time Complexity:
# Time Complexity is the number of fundamental operations performed by an algorithm 
# as a function of the input size (n), not the actual runtime in seconds.
# It is a measure of efficiency.

# Common Time Complexities (in increasing order of growth):
# O(1)      → Constant time
# O(log n)  → Logarithmic time
# O(n)      → Linear time
# O(n log n)→ Linearithmic time
# O(n^2)    → Quadratic time
# O(2^n)    → Exponential time
# O(n!)     → Factorial time

# Note: Runtime (in seconds) is not Time Complexity 
# because it's not expressed as a function of input size.


# Space Complexity:
# Space Complexity is the amount of memory (auxiliary space) used by an algorithm 
# as a function of the input size (n), not the actual memory in MB/GB.
# It includes space for input, output, and auxiliary variables.

# Common Space Complexities:
# O(1)      → Constant space
# O(log n)  → Logarithmic space
# O(n)      → Linear space
# O(n log n)→ Linearithmic space
# O(n^2)    → Quadratic space
# O(2^n)    → Exponential space
# O(n!)     → Factorial space

# Note: Memory usage shown in tools or OS is not Space Complexity 
# because it's not expressed as a function of input size.

# Example 1
# Time Complexity: O(1)
# Space Complexity: O(1)
# number_first = 10
# number_second = 20
# result = number_first + number_second
# print(result)


# # Example 2
# # Time Complexity: O(n)
# # Space Complexity: O(1)
# n = int(input())
# result = n * (n + 1) // 2
# print(result)

# # Example 3
# # Time Complexity: O(n)
# # Space Complexity: O(n)
# n = int(input())
# result = 0
# # result = [i for i in range(1, n + 1)]
# # print(result)
# for i in range(1, n + 1):
#     result += i
# print(result)

# n = int(input())
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

n = 100
even = [False] * (n + 1)
# for i in range(0, n + 1, 2):
#     if even[i]:
#         continue
#     for j in range(i * 2, n + 1, i + 2):
#         even[j] = True
# print(even)

for i in range(2, n + 1, 2):
    even[i] = True
print(even)

