def mutable(word, callback):
    result = ""
    for i in range(len(word)):
        result += callback(word[i], i, word)
    return result

print(mutable("Hello World", lambda x, i, word: x.upper()))
print(mutable("Hello World", lambda x, i, word: x.lower()))
print(mutable("Hello World", lambda x, i, word: x if x != " " else ""))
print(mutable("Hello World", lambda x, i, word: x if x != "l" else ""))
print(mutable("Hello World", lambda x, i, word: x if x != "l" else "L"))
print(mutable("Hello World", lambda x, i, word: x if x != "l" else "L"))
print(mutable("Hello World", lambda x, i, word: x if x != "l" else "L"))
print(mutable("Hello World", lambda x, i, word: x if x != "l" else "L"))
print(mutable("Hello World", lambda x, i, word: x if x != "l" else "L"))


def mutable(word, callback):
    result = ""
    for i in word:
        result += callback(i)
    return result
    
    
    
    