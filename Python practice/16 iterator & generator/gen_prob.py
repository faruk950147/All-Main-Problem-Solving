# 1.normal way 1-n
# 2 recursive way technique
# 3 list comprehension
# 4 generator way technique

# 1.normal way 1-n
for i in range(1, 11):
    print(i)

# 2.recursive way 1-n
def recursive(n):
    if n == 1:
        return 1
    else:
        return n + recursive(n - 1)

print(recursive(10))

# 3 list comprehension way 1-n
print([i for i in range(1, 11)])


# 4 generator way 1-n
def generator(n):
    for i in range(1, n + 1):
        yield i

for i in generator(10):
    print(i)

# 5 generator expression way 1-n
print(sum(i for i in range(1, 11)))

# 6 generator expression way 1-n
print(sum(i for i in range(1, 11)))


def getFibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for i in getFibonacci(10):
    print(i)  
    
def getFibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

for i in getFibonacci(10):
    print(i)    

def getFactorial(n):
    if n == 1:
        return 1
    else:
        return n * getFactorial(n - 1)

print(getFactorial(10))

def getFactorial(n):
    if n == 1:
        return 1
    else:
        return n * getFactorial(n - 1)

print(getFactorial(10))

def getEven(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

print(list(getEven(10)))

def gen_even_sum(n):
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += i
    yield sum

print(list(gen_even_sum(10)))

def gen_sum(n):
    sum = 0
    for i in range(n):
        sum += i
    yield sum

print(list(gen_sum(10)))