n = int(input("Enter a number: "))
total = 0
while n > 0:
    digit = n % 10
    n //=10
    
    total += digit**2
    #total += digit*digit
print(total)