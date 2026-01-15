"""
Adventure Game
Author: Tiffany Walther
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""

# Welcome message and introduction
print("Welcome to the Adventure Game!")
print("Your journey begins here...")

# TODO uncomment for production
# Ask for the player's name
player_name = input("What is your name, adventurer? ")

# Concantate strings to create a personalized message
# print("Welcome", playerName + "! Your journey begins now.")
# Use an f-string to display the same message in a more readable way
print(f"Welcome {player_name}! Your journey begins now.")

# Describe the starting area
starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
"""
print(starting_area)

# Ask the player for their first decision
decision = input("Do you wish to take the path? (yes, no, or run): ").lower()

# Respond based on the player's decision
if decision == "yes":
    print(f"Brave choice, {player_name}! You step onto the path and venture forward. \n")
elif decision == "no":
    print(player_name + ", you decide to wait. Perhaps courage will find you later. \n") # Concatenation example
# added in for fun
elif decision == "run":
    print("You turn and run from the forest and end your adventure.\n")

else:
    print("Confused, you stand still, unsure of what to do.\n")