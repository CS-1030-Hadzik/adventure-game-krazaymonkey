# TODO: Create a class called Player to represent the player in the game
# TODO: Inside the Player class, define an __init__ method that:
#       - Takes a name parameter
#       - Initializes these attributes:
#         - self.name (string)
#         - self.inventory (empty list)
#         - self.health (set to 100)
#         - self.has_map (set to False)
#         - self.has_lantern (set to False)
class Player():
    def __init__(self):
        self.name = ""
        self.inventory = []
        self.health = 100
        # self.has_map = False // no longer needed due to item_in_inventory
        # self.has_lantern = False

    # TODO: Update your welcome_player() function to return a Player object
    #       Instead of returning just a name, create and return the Player
    # Move your welcome message into a function called welcome_player().
    def get_name(self):
        # TODO uncomment for production
        # Ask for the player's name
        self.name = input("What is your name, adventurer? ")

    # TODO: Update add_to_inventory() so it:
    #       - Accepts a Player object as a parameter
    #       - Appends the item to player.inventory
    #       - Prints a message confirming the item was picked up
    #Create an inventory system that the player can view
    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory. \n")

    def is_item_in_inventory(self, item):
        #item = lantern
        #look at inventory and check for a lantern
        if item in self.inventory:
            return True
        return False

