import random

def lottery_system(participants):
    if not participants:
        return False
    print(f"Total participants: {len(participants)} ")
    winner = random.choice(participants)
    print(f"Winner: {winner}")

names = ["Rahim", "Karim", "Selina", "Tania", "Rafi"]
lottery_system(names)
#
# participants = ["Rahim", "Karim", "Selina", "Tania", "Rafi"]
#
# if participants:
#     print(f"Total participants: {len(participants)}")
#     winner = random.choice(participants)
#     print(f"Winner: {winner}")
# else:
#     print("No participants found!")
