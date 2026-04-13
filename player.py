# TODO: Create a class called Player to represent the player in the game
# TODO: Inside the Player class, define an __init__ method that:
#       - Takes a name parameter
#       - Initializes these attributes:
#         - self.name (string)
#         - self.inventory (empty list)
#         - self.health (set to 100)
#         - self.has_map (set to False)
#         - self.has_lantern (set to False)
import random

class Player():
    def __init__(self):
        self.name = ""
        self.inventory = ["A sword"]
        self.health = 100
        self.sword = 0

    # TODO: Update your welcome_player() function to return a Player object
    #       Instead of returning just a name, create and return the Player
    def get_name(self):
        self.name = input("What is your name, adventurer? ")

    # TODO: Update add_to_inventory() so it:
    #       - Accepts a Player object as a parameter
    #       - Appends the item to player.inventory
    #       - Prints a message confirming the item was picked up
    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory. \n")

    def is_item_in_inventory(self, item):
        #item = lantern
        #look at inventory and check for a lantern
        if item in self.inventory:
            return True
        return False

    def sword_attack(self):
        self.sword = random.randint(1, 15)
        return self.sword
