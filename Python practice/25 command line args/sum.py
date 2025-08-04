import sys

if len(sys.argv) != 3:
    print("Usage: python sum.py <number1> <number2>")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[2])

print("Sum:", a + b)