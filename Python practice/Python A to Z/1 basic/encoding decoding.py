# encoding decoding

# encoding is the process of converting a string into a sequence of bytes
# decoding is the process of converting a sequence of bytes into a string

a = "Hello, World!"
encoded = a.encode()
print("encoded", encoded)
# output
# encoded b'Hello, World!'

decoded = encoded.decode()
print("decoded", decoded)
# output
# decoded Hello, World!

# encoded = a.encode("utf-8")
# print(encoded)
# output
# encoded b'Hello, World!'

# decoded = encoded.decode("utf-8")
# print(decoded)
# output
# decoded Hello, World!'
# output
# decoded Hello, World!'