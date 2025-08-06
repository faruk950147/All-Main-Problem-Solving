def simple(a, b, callback):
    if callback == add:
        print("Addition")
        return callback(a, b)
    elif callback == sub:
        print("Subtraction")
        return callback(b, a)
    elif callback == mul:
        print("Multiplication")
        return callback(a, b)
    elif callback == div:
        print("Division")
        return callback(a, b)
    else:
        print("Invalid callback")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

if __name__ == "__main__":
    print(simple(10, 20, add))
    print(simple(10, 20, sub))
    print(simple(10, 20, mul))
    print(simple(10, 20, div))