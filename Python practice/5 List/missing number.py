# n = int(input())
# arr = list(map(int, input().split()))

# for i in range(1, n + 1):
#     if i not in arr:
#         print(i)

def missing_number(arr):
    n = max(arr)
    for i in range(1, n + 1):
        if i not in arr:
            return i

print("Missing number:", missing_number([1, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: 2


def find_missing_number(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    return total - sum(arr)

numbers = [1, 2, 3, 5]  # 4 missing
print("Missing number:", find_missing_number(numbers))