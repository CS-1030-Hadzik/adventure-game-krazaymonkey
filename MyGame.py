"""
Adventure Game
Author: Tiffany Walther
Version: 2.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""

# TODO: Create a class called Player to represent the player in the game
from player import Player

# TODO: Commit and push your code with a message like:
#       REF player class added and game state flags implemented

def welcome_player():
# Welcome message and introduction
    print("Welcome to the Adventure Game!")
    print("Your journey begins here...")

#Move the forest description into a function called describe_area().
def describe_start_area():
    # Describe the starting area
    area1 = """
    You find yourself in a dark forest...
    You see three paths ahead:
        1. Take the left path into the dark woods.
        2. Take the center path towards the dark cave.
        3. Take the right path toward the mountain pass.
        4. Stay where you are.
        5. Turn and run (quit).
        Type 'i' to view your inventory.
    """
    print(area1)

def describe_second_area():
    pass

welcome_player()

# TODO: Replace the global variable player_name with a Player object
#       Example: player = Player("Scott")
player = Player()
player.get_name()

# Concantate strings to create a personalized message
# print("Welcome", playerName, "! Your journey begins now.")
# Use an f-string to display the same message in a more readable way
print(f"Welcome {player.name}! Your journey begins now.")

describe_start_area()

# TODO: Update all print statements that used player_name to use player.name

#while loop -> when we don't know the number of times to loop
#for loop -> when we know the number of times to loop
#do while (not in python) -> will execute at least once. condition is at the bottom

while True:
    # Ask the player for their first decision
    # decision = input("Do you wish to take the path? (yes, no, or run): ").lower()
    decision = input("What will you do? (1, 2, 3, 4, 5, i): ").lower()

    # Respond based on the player's decision
    if decision == "1":
        # TODO: In path 1, after picking up the lantern:
        # - Set player.has_lantern = True
        print(f"{player.name}, you step onto the left path and venture into the dark woods. ")
        player.add_to_inventory("a lantern")
    elif decision == "2":
        #if player has the lantern, they can enter the cave.
        if player.is_item_in_inventory("a lantern"):
            print(f"{player.name}, you enter the dark cave.")
        else:
            print("It's too dark to see in the cave.\n")
    elif decision == "3":
    # TODO: In path 2, after picking up the map:
    #       - Set player.has_map = True
        print(f"{player.name}, you step onto the right path and venture into the mountains. ")
        player.add_to_inventory("a map")
    elif decision == "4":
        print(f"{player.name}, you hesitate and stay where you are. ")
    # added in for fun
    elif decision == "5":
        print("You turn and run from the forest and end your adventure.\n Thanks for playing!")
        break
    #look at inventory
    elif decision == "i":
        print(player.inventory)
    else:
        print("Confused, you stand still, unsure of what to do.\n")

# TODO: (Optional Stretch) Add a check before certain choices
#       - Example: If player.has_lantern is False, prevent entering a cave
#       - Print a message like “It’s too dark to continue without a lantern.”
