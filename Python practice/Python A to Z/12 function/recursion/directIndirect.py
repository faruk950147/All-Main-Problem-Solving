# Direct Recursion
# When a function calls itself directly
# Indirect Recursion
# When a function calls another function which calls the first function
# Recursion is a function that calls itself again and again
# Base Case is the condition that stops the recursion
# Recursive Case is the condition that calls the function again
# By default, Python has a limit on the number of recursive calls it can make (recursion limit) 1000

# Direct Recursion
def recursion(n):
    if n == 0:
        return
    print("Hello")
    recursion(n - 1)

recursion(2)

# Indirect Recursion
def recursion2(n):
    if n == 0:
        return
    print("Hello")
    recursion(n - 1)

recursion2(2)

