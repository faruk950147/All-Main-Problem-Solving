# num1, num2 = list(map(int, input().split()))
# print("Before swapping:", num1, num2)
# num1, num2 = num2, num1
# print("After swapping:", num1, num2)

# # using third variable
# num1, num2 = list(map(int, input().split()))
# print("Before swapping:", num1, num2)
# temp = num1
# num1 = num2
# num2 = temp
# print("After swapping:", num1, num2)

# # without using third variable
# num1, num2 = list(map(int, input().split()))
# print("Before swapping:", num1, num2)
# num1 = num1 + num2
# num2 = num1 - num2
# num1 = num1 - num2
# print("After swapping:", num1, num2)

# a = 10 
# b = 20
# a, b = b, a  # swap a value of b and b value of a a = 20 b = 10
# print(a, b)

li = [1,2,3,4,5]
li[0], li[4] = li[4], li[0]
print(li)