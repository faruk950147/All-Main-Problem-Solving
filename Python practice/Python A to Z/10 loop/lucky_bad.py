import random
# def lucky_bad():
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print("Lucky Bad")
#         elif i % 3 == 0:
#             print("Lucky")
#         elif i % 5 == 0:
#             print("Bad")
#         else:
#             print(i)

# lucky_bad()
# def lucky_bad(number):
#     if number % 2 == 0:
#         return "Lucky"
#     else:
#         return "Bad"
# print(lucky_bad(7))  # Output: Bad

def lucky_day(participants):
    if participants:
        lucky = random.choice(participants)
        return f"Lucky Day is: {lucky}"
    else:
        return "The day is not lucky"

print(lucky_day(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]))
