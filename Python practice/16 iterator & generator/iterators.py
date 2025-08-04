# =======================================
# 1. Iterable
# =======================================

# Iterable object: A list is an iterable because we can iterate over it
numbers = [1, 2, 3, 4, 5]

# Iteration using for loop (this is the process of iteration)
print("Example of Iterable and Iteration (using for loop):")
for num in numbers:
    print(num)


# =======================================
# 2. Iterator
# =======================================

# We can convert an iterable into an iterator using iter()
numbers = [1, 2, 3, 4, 5]
iterable = iter(numbers)  # now it's an iterator object

print("\nExample of Iterator (using next()):")
print(next(iterable))  # Output: 1
print(next(iterable))  # Output: 2
print(next(iterable))  # Output: 3
print(next(iterable))  # Output: 4
print(next(iterable))  # Output: 5
# print(next(iterable))  # This will raise StopIteration


# =======================================
# 3. Iteration (manual using index)
# =======================================

# Iteration is the process of going through the elements one by one
numbers = [1, 2, 3, 4, 5]

print("\nExample of Iteration using index:")
for i in range(len(numbers)):
    print(numbers[i])  # accessing elements one by one using index
