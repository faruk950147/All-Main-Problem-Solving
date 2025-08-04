# def replace(str1, callback):
#     result = ""
#     for i in str1:
#         result += callback(i)
#     return result


def replace(str1, callback):
    result = ""
    for i in range(len(str1)):
        result += callback(str1[i], i, str1)
    return result


print(replace("Hello World", lambda x, i, str1: x.upper()))
print(replace("Hello World", lambda x, i, str1: x.lower()))
print(replace("Hello World", lambda x, i, str1: x if x != " " else ""))
print(replace("Hello World", lambda x, i, str1: x if x != "l" else ""))
print(replace("Hello World", lambda x, i, str1: x if x != "l" else "L"))
print(replace("Hello World", lambda x, i, str1: x if x != "l" else "L"))

    
    
    