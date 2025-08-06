# list1 = [2, 3, 4, 5, 5, 6]
# list2 = [4, 6, 7, 8, 8]

# combined = list1 + list2

# unique_values = []

# for item in combined:
#     if combined.count(item) == 1 and item not in unique_values:
#         unique_values.append(item)

# unique_values.sort()

# print(unique_values)

list1 = [2, 3, 4, 5, 5, 6]
list2 = [4, 6, 7, 8, 8]

combined = list1 + list2
freq = {}

for item in combined:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

unique_values = sorted([item for item in freq if freq[item] == 1])

print(unique_values)

# list1 = [2, 3, 4, 5, 5, 6]
# list2 = [4, 6, 7, 8, 8]

# combined = list1 + list2

# unique_values = sorted({x for x in combined if combined.count(x) == 1})

# print(unique_values)
