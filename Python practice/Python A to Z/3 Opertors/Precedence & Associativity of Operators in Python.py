# Precedence & Associativity of Operators in Python
# rules that rule is follow BODMAS
# BODMAS = Bracket, Order, Division, Multiplication, Addition, Subtraction
# Associativity is left to right

# evaluate the expression
# **  exponential
# *   multiplication
# /   division
# +   addition
# -   subtraction
# +x  positive
# -x  negative
# ~x  bitwise NOT
# ()  brackets  

# 1. Brackets ( ) # first priority
# 2. Exponentiation ** # second priority
# 3. Multiplication *, Division /, Floor Division //, Modulus % # third priority but priority level is same
# 4. Addition +, Subtraction - # fourth priority but priority level is same


# a = 2 + 3 * 5
# print(a)
# a = (2 + 3) * 5
# print(a)

# associativity priority level is same 
# left to right 2 + 3 + 4 + 5

# b = 2 + 3 + 4 - 5
# print(b)

# # associativity priority level is same 
# # right to left 2 + 3 + 4 - 5

# b = 2 + 3 + 4 - 5
# print(b)

# c = 2 * 3 // 5
# print(c)

d = 2 * 3 + 5
print(d)