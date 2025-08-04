set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1.add(6)
set1.remove(1)
set1.discard(2)
set1.pop()

print(set1)

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

print(set1.issubset(set2))
print(set1.issuperset(set2))

print(set1.isdisjoint(set2))