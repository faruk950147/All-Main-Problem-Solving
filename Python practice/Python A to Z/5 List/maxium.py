# numbers = list(map(int, input().split()))
# maximum = numbers[0]

# for num in numbers:
#     if num > maximum:
#         maximum = num

# print(maximum)

# for num in range(len(numbers)):
#     if numbers[num] > maximum:
#         maximum = numbers[num]

# print(maximum)


def find_max(numbers):
    return max(numbers)

print(find_max([1, 2, 3, 4, 5]))

