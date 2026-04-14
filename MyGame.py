"""
Adventure Game
Author: Tiffany Walther
Version: 5.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""

# TODO: Create a class called Player to represent the player in the game
from player import Player
from enemies import Enemy
from inventory import Inventory

def welcome_player():
# Welcome message and introduction
    print("Welcome to the Adventure Game!")
    print("Your journey begins here...")

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
def explore_dark_woods(player, forest_creature):
        print(f"{player.name}, you step onto the left path and venture into the dark woods. ")
        print("The woods seem to whisper as you pass.")
        print("You see something glimmering in a branch of a small tree.")
        turn = 0
        choice = ""

        forest_creature.forest_fight()
        #fight or run?
        while choice == "":
            if turn == 0:
                choice = input(f"{player.name} fight, heal, or run? ").lower()
                if choice == "run" or choice == "r":
                    break
                elif choice == "heal" or choice == "h":
                    player.health += inventory.use_health_potion()
                    if player.health > 100:
                        player.health = 100
                    print("You quickly drink a healing potion.")
                    print(f"Your health is now {player.health}\n")

                elif choice == "fight" or choice == "f":
                    #player's turn
                    print("Prepare to fight.\n")
                    player_damage = player.sword_attack()
                    if forest_creature.defense > player_damage:
                        player.health -= forest_creature.strength
                        print("You were hit by the creature.")
                        print(f"Your health is now {player.health}\n")
                    elif forest_creature.defense < player_damage:
                        forest_creature.health -= player_damage
                        print(f"{player.name} you raise your sword and attack!")
                        print("The creature shrieks as it's hit.")
                    else:
                        print("The creature blocked your attack.")

            else:
                #creature turn
                print("The creature attacks!")
                creature_damage = forest_creature.creature_attack()
                if player.defense >= creature_damage:
                    print("You blocked the creature's attack.")
                elif player.defense < creature_damage:
                    player.health -= creature_damage
                    print("You were hit by the creature.")
                    print(f"Your health is now {player.health}\n")

            if player.health < 1:
                death_by_creature(player)
                break
            #game break//perma death -> new game
            elif forest_creature.health < 1:
                print("The creature collapses from it's wounds dropping a health potion.")
                inventory.add_to_inventory("A lantern")
                inventory.add_health_potion()
                print("You return to the main path to choose again.")
                break
            
            choice = ""
            turn += 1
            if turn > 1:
                turn = 0

# TODO: Create a function called explore_cave(player)
#       - If player.has_lantern: allow entry and add "treasure"
#       - Else: warn that it's too dark
def explore_cave(player):
    if inventory.is_item_in_inventory("A lantern"):
        print(f"{player.name}, you enter the dark cave.")
        print("Lantern light bounces off the wet walls around you.")
        print("You see a glimmer of gold as you round a corner.")

        #cave_creature(Enemy)

        inventory.add_to_inventory("A treasure chest")
        print("You return to the main path to choose again.")
    else:
        print("It's too dark to see in the cave.\n")
        print("The looming darkness pushes you back to the main path.")
        player.health -= 10
        print(f"Your health is now {player.health}\n")


# TODO: Create a function called explore_mountain_pass(player)
#       - Print area description
#       - Add "map" to inventory if not already collected
def explore_mountain_pass(player):
    print(f"{player.name}, you step onto the right path and venture into the mountains. ")
    print("The wind howls as you climb the steep, rocky slope.")
    print("You see something flapping in the wind, caught on a small tree.")
    
    #mountain_creature(Enemy)
    
    inventory.add_to_inventory("A map")
    print("You return to the main path to choose again.")

# TODO: Create a function called explore_hidden_valley(player)
#       - If player.has_map: allow entry and add "rare herbs"
#       - Else: warn that player can't find the valley
def explore_hidden_valley(player):
    if (inventory.is_item_in_inventory("A map") and inventory.is_item_in_inventory("A treasure chest")):
        print(f"{player.name} you find your way to the hidden valley.")
        print("Rolling hills covered in wildflowers sway in a gentle breeze.")
        print("A distinct patch of green catches your eye.")
        inventory.add_to_inventory("Rare herbs")
    else:
        print("You're missing the required items to find the hidden valley.")
        print("Hungry and lost you return to the main path.")
        player.health -= 10
        print(f"Your health is now {player.health}\n")

# TODO: Create a function stay_still(player)
#       - Subtract 10 health when the player stays still
def stay_still(player):
    player.health -= 10
    print("The darkness of the forest pushes on your mind.")
    print(f"Your health is now {player.health}\n")

# TODO: Create win conditions
# requires rare herbs and treasure. Tresure is required to get rare herbs
def check_win(player):
    if inventory.is_item_in_inventory("Rare herbs"):
        print(f"Congratulations, {player.name}, you have won the game!")
        print("The light is now shining brightly through the trees, ligting the path home.")
        return True
    else:
        return False

# TODO: create lose conditions
# player health = 0, death
def check_lose(player):
    if player.health <= 0:
        print(f"{player.name}, you have succumbed to hunger and died.")
        print("The trees will accept your remains into their forest.")
        return True
    else:
        return False
    
def death_by_creature(player):
    if player.health <= 0:
        print(f"{player.name} your wounds are too great.")
        print("You have died")
        exit()

welcome_player()

# TODO: Replace the global variable player_name with a Player object
player = Player()
player.get_name()

# Concantate strings to create a personalized message
print(f"Welcome {player.name}! Your journey begins now.")

inventory = Inventory()
forest_creature = Enemy()
cave_creature = Enemy()
mountain_creature = Enemy()

describe_start_area()

while True:
    # Ask the player for their first decision
    decision = input("What will you do? (1, 2, 3, 4, 5, q, i): ").lower()

    # Respond based on the player's decision
    if decision == "1": #dark woods
        explore_dark_woods(player, forest_creature)

    elif decision == "2": #dark cave
        explore_cave(player, cave_creature)

    elif decision == "3": #mountain path
        explore_mountain_pass(player, mountain_creature)

    elif decision == "4": # hidden valley
        explore_hidden_valley(player)

    elif decision == "5": 
        print(f"{player.name}, you hesitate and stay where you are. ")
        print("The path looms ahead with an overwhelming presence.")
        stay_still(player)

    elif decision == "q": #quit
        print("You turn and run from the forest ending your adventure.\n Thanks for playing!")
        break

    #look at inventory
    elif decision == "i":
        print(player.inventory)
    else: #wrong input
        print("Confused, you stand still, unsure of what to do.\n Please chose from the above options.")

    if check_win(player):
        break

    if check_lose(player):
        break