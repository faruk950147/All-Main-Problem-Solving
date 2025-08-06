# Recursion is a function that calls itself again and again
# Base Case is the condition that stops the recursion
# Recursive Case is the condition that calls the function again
# By default, Python has a limit on the number of recursive calls it can make (recursion limit) 1000
def recursive_sum(n):
    if n == 1: # Base Case
        return 1
    return n + recursive_sum(n - 1) # Recursive Case
print(recursive_sum(5))

def recursive_factorial(n):
    if n == 1: # Base Case
        return 1
    return n * recursive_factorial(n - 1) # Recursive Case
print(recursive_factorial(5))

def sayHello(n):
    if n == 0: # Base Case
        return
    print("Hello")
    sayHello(n - 1) # Recursive Case
sayHello(5)