#TODO: Create a class for enemies to fight
# one enemy for 3 main locations. can run away or fight
    #stick creature for forest
    #goblin for cave
    #rock golem for mountain

#init health, strenght, defense
#drops health potion, area item
import random

class Enemy():
    def __init__(self):
        self.name = ""
        self.health = 50
        self.slap = 0
        #defense is player.strenght vs enemy.defense, higher number wins
        self.defense = 10
        #health potion

    def forest_fight(self):
        print("\nThe branches of the small tree sway in the breeze as you approach.")
        print("As you get closer, you see two orange eyes between the leaves.")
        print("The small tree shakes and stands, dirt raining from the lower branchs.\n")


    def cave_fight(self):
        print("\nYou see a small chest, gold spilling out in a small pile.")
        print("A skittering sound bounces off the walls around you.")
        print("A small, fleshy creature jumps in your path and shrieks, raising a stone club.\n")


    def mountain_fight(self):
        print("\nA small pile of rocks near the tree shifts as you approach.")
        print("The ground rumbles as the pile of rocks moves again, getting taller.")
        print("The rock creature turns to you, obsidian eyes angry, and roars.\n")

    def creature_attack(self):
        self.slap = random.randint(10, 14)
        return self.slap
