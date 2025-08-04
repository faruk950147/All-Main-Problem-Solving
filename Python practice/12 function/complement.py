# find complement of a number
# complement of a number is the number with all the bits inverted
# for example, the complement of 5 is 2
# 5 in binary is 101
# 2 in binary is 010

# bin() function returns a string object and [2:] is used to remove 0b from the string
# b = bin(5) # output: '0b101'
# Index:  0 1 2 3 4
# Value: '0' 'b' '1' '0' '1'
# use slice to remove 0b from the string index 0,1
# b = bin(5)[2:] # b = '101'
# print(b)
# a = int(b, 2) # a = 5
# print(a)


def FindComplement(num):
    binary = bin(num)[2:] # begin slice from index 2 to end [2:1:9]
    complement = "" 
    for bit in binary:
        if bit == "1":
            complement += "0"
        else:
            complement += "1"
    return int(complement, 2) # convert binary to decimal and 2 is base of binary
    
a = 1
print(FindComplement(a))
    
    