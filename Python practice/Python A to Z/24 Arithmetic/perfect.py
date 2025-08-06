num = int(input())  
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print("Perfect")
else:
    print("Not Perfect")

def perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False
    
num = int(input())
if perfect(num):
    print("Perfect")
else:
    print("Not Perfect")
