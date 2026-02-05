"""
Adventure Game
Author: Tiffany Walther
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""

#Create an inventory system that the player can view
inventory = []

def add_to_inventory(item):
    inventory.append(item)
    print(f"You picked up {item}. It has been added to your inventory. ")

# Move your welcome message into a function called welcome_player().
def welcome_player():
    # Welcome message and introduction
    print("Welcome to the Adventure Game!")
    print("Your journey begins here...")

    # TODO uncomment for production
    # Ask for the player's name
    name = input("What is your name, adventurer? ")
    return name

#Move the forest description into a function called describe_area().
def describe_area1():
    # Describe the starting area
    area1 = """
    You find yourself in a dark forest...
    You see two paths ahead:
        1. Take the left path into the dark woods.
        2. Take the right path toward the mountain pass.
        3. Stay where you are.
        4. Turn and run.
        Type 'i' to view your inventory.
    """
    print(area1)

player_name = welcome_player()

# Concantate strings to create a personalized message
# print("Welcome", playerName, "! Your journey begins now.")
# Use an f-string to display the same message in a more readable way
print(f"Welcome {player_name}! Your journey begins now.")

describe_area1()

# Ask the player for their first decision
# decision = input("Do you wish to take the path? (yes, no, or run): ").lower()
decision = input("What will you do? (1, 2, 3, 4, i): ").lower()

# Respond based on the player's decision
if decision == "1":
    print(f"{player_name}, you step onto the left path and venture into the dark woods. ")
    add_to_inventory("a lantern")
elif decision == "2":
    print(f"{player_name}, you step onto the right path and venture into the mountains. ")
    add_to_inventory("a map")
elif decision == "3":
    print(f"{player_name}, you hesitate and stay where you are. ")
# added in for fun
elif decision == "4":
    print("You turn and run from the forest and end your adventure.")
#look at inventory
elif decision == "i":
    print(inventory)
else:
    print("Confused, you stand still, unsure of what to do.\n")