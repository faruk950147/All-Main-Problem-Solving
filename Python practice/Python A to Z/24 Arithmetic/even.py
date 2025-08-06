# num = int(input())
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# num = list(map(int, input().split()))
# for i in num:
#     if i % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# if you want to use it in a function just even 
def even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def odd(num):
    if num % 2 != 0:
        return True
    else:
        return False

def even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even"
    else:
        return f"{num} is Odd"

# # if you want to use it in a loop 
# for i in range(1, 11):
#     print(even_odd(i))
    
# # if you want to use it in a list 
# li = [1,2,3,4,5,6,7,8,9,10]
# for i in li:
#     print(even_odd(i))
    
# # if you want to use it in a tuple 
# tup = (1,2,3,4,5,6,7,8,9,10)
# for i in tup:
#     print(even_odd(i))
    
# if you want to use it in a dictionary 
dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
for i in dict1:
    print(even_odd(dict1[i]))