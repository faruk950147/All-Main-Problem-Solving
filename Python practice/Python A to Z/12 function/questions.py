"""
if input 2 512 
2*2 = 4
4*2 = 8
8*2 = 16
16*2 = 32
32*2 = 64
64*2 = 128
128*2 = 256
256*2 = 512
result = 512
count = 9
"""

# inputNum = input("Enter a number: ")
# newNum = inputNum.split()
# num1, num2 = int(newNum[0]), int(newNum[1])
# count = 0
# while True:
#     num1 *= 2
#     count += 1
#     if num1 == num2:
#         break
# print(count)

def countNum(num1, num2):
    count = 0
    while True:
        num1 *= 2
        count += 1
        if num1 == num2:
            break
    return count

print(countNum(2, 512))

