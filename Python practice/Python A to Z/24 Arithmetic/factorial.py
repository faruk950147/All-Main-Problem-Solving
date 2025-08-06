
num = int(input())
fact = 1
for i in range(1, num + 1):
    fact *= i
print(fact)

def find_fact(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact
print(find_fact(5))