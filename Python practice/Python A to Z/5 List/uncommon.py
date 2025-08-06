list1 = [2, 3, 4, 5, 5, 6, 7]
list2 = [5, 6, 7, 8, 9, 5]

set1 = set(list1)
set2 = set(list2)

uncommon = sorted((set1 - set2) | (set2 - set1))

print(uncommon)

list1 = [2, 3, 4, 5, 5, 6, 7]
list2 = [5, 6, 7, 8, 9, 5]

uncommon = []

for item in list1:
    if item not in list2 and item not in uncommon:
        uncommon.append(item)

for item in list2:
    if item not in list1 and item not in uncommon:
        uncommon.append(item)

uncommon.sort()

print(uncommon)
