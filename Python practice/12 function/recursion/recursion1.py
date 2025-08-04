# Recursion is a function that calls itself again and again
# Base Case is the condition that stops the recursion
# Recursive Case is the condition that calls the function again
# By default, Python has a limit on the number of recursive calls it can make (recursion limit) 1000
import sys
print(sys.getrecursionlimit())
i = 0
def demo():
    global i
    i += 1
    print("Hello", i)
    demo()



# def default_recursion_limit():
#     return sys.getrecursionlimit()
# print(default_recursion_limit())

# sys.setrecursionlimit(10000)
# def recursive_sum(n):
#     if n == 1:
#         return 1
#     return n + recursive_sum(n - 1)
# print(recursive_sum(5))

