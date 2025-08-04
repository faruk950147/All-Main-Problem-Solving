import math
x1, y1, x2, y2 = map(float, input().split())
# print(f"{((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5:.2f}")
print(f"{math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2):.2f}")

list2 = [10,11,12,13,14,15,16,17,18,19]
print(list2[len(list2) - 1])
print(list2[-1])