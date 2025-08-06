# num = int(input())
# fib_prev, fib_next = 0, 1
# for i in range(num):
#     fib_prev, fib_next = fib_next, fib_prev + fib_next
# print(f"{num}th term of Fibbnacci series is {fib_next}")

def fib_find(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib_prev, fib_next = 0, 1
    for _ in range(1, n + 1):
        fib_prev, fib_next = fib_next, fib_prev + fib_next
    return fib_next

print(fib_find(5))