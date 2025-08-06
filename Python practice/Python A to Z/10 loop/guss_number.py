import random
# number = random.randint(1, 10)
# guess = int(input("Guess the number between 1 and 10: "))
# while guess != number:
#     if guess < number:
#         print("Too low")
#     else:
#         print("Too high")
#     guess = int(input("Guess again: "))
# print("You guessed it!")


# limit = random.randint(1, 10)
# low, high = 1, 10
# attempts = 0
# while True:
#     print(f"Guess the number between {low} and {high}")
#     inputNum = int(input("Enter your guess: "))
#     print(f"Input number: {inputNum}")
#     attempts += 1
#     if inputNum == limit:
#         print(f"You guessed it! in {attempts} attempts")
#         break
#     elif inputNum < limit:
#         low = inputNum + 1
#     else:
#         high = inputNum - 1

limit = random.randint(1, 10)
attempts = 0
low, high = 1, 10
while True:
    print(f"Guess the number between {low} and {high}")
    inputNum = (low + high) // 2
    print(f"Input number: {inputNum}")
    attempts += 1
    if inputNum == limit:
        print(f"You guessed it! in {attempts} attempts")
        break
    elif inputNum < limit:
        low = inputNum + 1
    else:
        high = inputNum - 1