# def fib_find(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     fib_x, fib_y = 0, 1
#     for _ in range(2, n + 1):
#         fib_x, fib_y = fib_y, fib_x + fib_y
#     return fib_y
#
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

# print(fibonacci(5))
#
#
# n = int(input())
# a, b = 0, 1
# for i in range(n):
#     a, b = b, a + b
#     print(b)
#
n = int(input("Fibonacci series nth : "))
a, b = 0, 1
for _ in range(1,n+1):
    a, b = b, a + b
    print(f"{n}-th Fibonacci number: {b}")
