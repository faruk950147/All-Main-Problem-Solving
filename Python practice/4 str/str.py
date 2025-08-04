import sys

if __name__ == '__main__':
    print(sys.getsizeof("Hello World!"))

    str1 = "Hello World!"
    str2 = "Hello World!"

    print(id(str1))
    print(id(str2))
    print(sys.getsizeof(str1))
