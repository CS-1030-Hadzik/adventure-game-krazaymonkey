#TODO: create a class called inventory to track different items in player's inventory
#TODO: Inside the inventory class, define 
#       - Create empty list for items
#       - max of 3 health potions
#       - add lantern, map, treasure, herbs
#       - check for required items for locations
import random

class Inventory():
    def __init__(self):
        self.required_items_inventory = []
        self.weapon = ["A sword"]
        self.potion_inventory = 3

    def display_inventory(self):
        print(f"Items: {self.required_items_inventory}")  
        print(f"Potions: {self.potion_inventory}")
        print(f"Weapon: {self.weapon}")


    def add_to_inventory(self, item):
        self.required_items_inventory.append(item)
        print(f"{item} has been added to your inventory. \n")

    def is_item_in_inventory(self, item):
        #item = lantern
        #look at inventory and check for a lantern
        if item in self.required_items_inventory:
            return True
        return False

    def have_health_potion(self):
        if self.potion_inventory > 0:
            return True
        return False
    
    def add_health_potion(self):
        if self.potion_inventory < 3:
            self.potion_inventory += 1
            print("You picked up a healing potion.")
        else:
            print("Your pockets are full.")
        return self.potion_inventory
    
    def use_health_potion(self):
        if self.potion_inventory > 0:
            healing_points = random.randint(60, 75)
            self.potion_inventory -= 1
            if self.potion_inventory <= 0:
                self.potion_inventory = 0
            return healing_points
        else:
            print("You don't have any potions.")
            return 0