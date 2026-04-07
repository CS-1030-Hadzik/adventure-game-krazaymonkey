"""
Adventure Game
Author: Tiffany Walther
Version: 3.5
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""

# TODO: Update the main while loop
#       - Replace large decision blocks with function calls


# TODO: Create a class called Player to represent the player in the game
from player import Player

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
        4. Search for the hidden valley.
        5. Stay where you are.
        q. Turn and run (quit).
        Type 'i' to view your inventory.
    """
    print(area1)

# TODO: Create a function called explore_dark_woods(player)
#       - Print area description
#       - Add "lantern" to inventory if not already collected
def explore_dark_woods(player):
        # TODO: In path 1, after picking up the lantern:
        # - Set player.has_lantern = True
        print(f"{player.name}, you step onto the left path and venture into the dark woods. ")
        print("The woods seem to whisper as you pass.")
        print("You see something glimmering near the base of a tree.")
        player.add_to_inventory("A lantern")

# TODO: Create a function called explore_cave(player)
#       - If player.has_lantern: allow entry and add "treasure"
#       - Else: warn that it's too dark
def explore_cave(player):
    # TODO: In the cave choice:
    # - If player.has_lantern is True: allow entry and add "treasure" to inventory
    # - Else: display a message that it’s too dark
    if player.is_item_in_inventory("a lantern"):
        print(f"{player.name}, you enter the dark cave.")
        print("Lantern light bounces off the wet walls around you.")
        print("You see a gold reflection around the next corner.")
        player.add_to_inventory("A treasure chest")
    else:
        print("It's too dark to see in the cave.\n")

# TODO: Create a function called explore_mountain_pass(player)
#       - Print area description
#       - Add "map" to inventory if not already collected
def explore_mountain_pass(player):
    # TODO: In path 2, after picking up the map:
    #       - Set player.has_map = True
    print(f"{player.name}, you step onto the right path and venture into the mountains. ")
    print("The wind howls as you climb the steep, rocky, slope.")
    print("You see something flapping in the wind, caught on a small tree.")
    player.add_to_inventory("a map")

# TODO: Create a function called explore_hidden_valley(player)
#       - If player.has_map: allow entry and add "rare herbs"
#       - Else: warn that player can't find the valley
def explore_hidden_valley(player):
    # TODO: Add a new menu option for "Search for a hidden valley"
    # TODO: In the valley choice:
    #       - If player.has_map is True: allow entry and add "rare herbs" to inventory
    #       - Else: display a message that you can’t find the valley
    if (player.is_item_in_inventory("a map") and player.is_item_in_inventory("a treasure chest")):
        print(f"{player.name} you enter the hidden valley.")
        player.add_to_inventory("rare herbs")
    else:
        print("You're missing the required items to find the hidden valley.\n")

def stay_still(player):
    pass

welcome_player()

# TODO: Replace the global variable player_name with a Player object
player = Player()
player.get_name()

# Concantate strings to create a personalized message
print(f"Welcome {player.name}! Your journey begins now.")

describe_start_area()

#while loop -> when we don't know the number of times to loop
#for loop -> when we know the number of times to loop
#do while (not in python) -> will execute at least once. condition is at the bottom

while True:
    # Ask the player for their first decision
    # decision = input("Do you wish to take the path? (yes, no, or run): ").lower()
    decision = input("What will you do? (1, 2, 3, 4, 5, q, i): ").lower()

    # Respond based on the player's decision
    if decision == "1": #dark woods
        explore_dark_woods(player)

    elif decision == "2": #dark cave
        explore_cave(player)

    elif decision == "3": #mountain path
        explore_mountain_pass(player)

    elif decision == "4": # hidden valley
        explore_hidden_valley(player)

    elif decision == "5": #wrong input
        print(f"{player.name}, you hesitate and stay where you are. ")

    # added in for fun
    elif decision == "q": #quit
        print("You turn and run from the forest and end your adventure.\n Thanks for playing!")
        break

    #look at inventory
    elif decision == "i":
        print(player.inventory)
    else:
        print("Confused, you stand still, unsure of what to do.\n")
