import random

# participants = ["Omar", "Sadia", "Rafi", "Tushar", "Mehedi", "Tanvir"]

# winner = random.choice(participants)

# print("🏆 The Winner is:", winner)
# This code randomly selects a winner from a list of participants and prints the winner's name.
# You can modify the participants list to include any names you want.
# To run this code, simply execute it in a Python environment.
# Make sure to have the random module available, which is part of Python's standard library.    


participants = ["Omar", "Sadia", "Rafi", "Tushar", "Mehedi", "Tanvir"]

winners = random.sample(participants, 3) # random.sample() used to select a random sample of a specified size from a list.

print("🏆 The Winners are:", winners)
