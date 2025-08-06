numbers = list(map(int, input().split()))
positive = 0
negative = 0
for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
print(positive, negative)

if positive > 0:
    print("Positive")
elif negative > 0:
    print("Negative")
else:
    print("Zero")