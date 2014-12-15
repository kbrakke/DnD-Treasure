__author__ = 'Kris'
import Parsers, random, json, Treasure, dice
from resources.data import *

d100 = dice.dice("1d100")
class Table():
    def __init__(self, treasure_list):
        self.treasure_list = treasure_list
    def generate_treasure(self):
        treasure_string = ""
        for k,v in self.treasure_list:
            treasure_string = treasure_string+("-"*10)+str(k)+("-"*10)+"\n"
            treasure_string = treasure_string+str(v.roll_treasure)+"\n"
        return treasure_string
    def __str__(self):
        return str(self.generate_treasure())

class tier_table():
    def __init__(self, coins_list):
        self.lines = []
        for c in coins_list:
            self.lines.append(Treasure.Coins(c))
    def generate_treasure(self):
        roll = d100.roll()
        for c in self.lines:
            if c.in_range(int(roll)):
                return c.roll_treasure()
    def __str__(self):
        return self.generate_treasure()

class individual_treasure_table():
    def __init__(self):
        self.tiers = []
        for t in individual_treasure:
            self.tiers.append(tier_table(t))
    def generate_treasure(self, teir):
        return self.tiers[teir-1].generate_treasure()
    def __str__(self):
        return self.tiers(0).generate_treasure()

class magic_item_table():
    def __init__(self):
        self.tables = {"A" : [], "B" : [], "C" : [], "D" : [], "E" : [], "F" : [], "G" : [] , "H" : [], "I" : []}
        for i in A:
            self.tables["A"].append(Treasure.magic_item(i))
        for i in B:
            self.tables["B"].append(Treasure.magic_item(i))
        for i in C:
            self.tables["C"].append(Treasure.magic_item(i))
        for i in D:
            self.tables["D"].append(Treasure.magic_item(i))
        for i in E:
            self.tables["E"].append(Treasure.magic_item(i))
        for i in F:
            self.tables["F"].append(Treasure.magic_item(i))
        for i in G:
            self.tables["G"].append(Treasure.magic_item(i))
        for i in H:
            self.tables["H"].append(Treasure.magic_item(i))
        for i in I:
            self.tables["I"].append(Treasure.magic_item(i))
    def generate_treasure(self, table):
        roll = d100.roll()
        for i in self.tables[table]:
            if(i.in_range(int(roll))):
                return i.roll_treasure()
    def __str__(self):
        return self.generate_treasure("A")

class hoard_treasures():
    def __init__(self, hoard):
        self.coins = Treasure.Coins(hoard["coins"])
        self.hoards = []
        for t in hoard["treasure"]:
            self.hoards.append(Treasure.hoard_treasure_line(t))

    def generate_treasure(self):
        roll = d100.roll()
        ret = "Coins: "+self.coins.roll_treasure()+"\n"
        for h in self.hoards:
            if(h.in_range(int(roll))):
                ret += h.roll_treasure()
        return ret








