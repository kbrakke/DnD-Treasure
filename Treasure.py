__author__ = 'Kris'
import random, dice, Tables
from resources.data import *

"""
"""
class Treasure():
    def __init__(self, data):
        self.data = data
        if('-' in self.data["range"]):
            range_array = self.data["range"].split('-')
            self.low = int(range_array[0])
            self.high = int(range_array[1])
        else:
            self.low = int(self.data["range"])
            self.high = int(self.data["range"])
    def in_range(self, number):
        return (number in range(self.low, self.high+1))
    def roll_treasure(self):
        return "Unimplemented, please fix"
    def __str__(self):
        return str(self.roll_treasure())

class Coins(Treasure):
    def __init__(self, data):
        Treasure.__init__(self, data)
        self.coins = []
        for c in self.data["coins"]:
            split_die = c.split(';')
            self.coins.append([dice.dice(split_die[0]), split_die[1]])
    def roll_treasure(self):
        base = ""
        for c in self.coins:
            base += "{} {} ".format(str(int(c[0].roll())), c[1])
        return base

class magic_item(Treasure):
    def __init__(self, data):
        Treasure.__init__(self, data)
    def roll_treasure(self):
        return self.data["treasure"]

class object():
    def __init__(self, data):
        self.objects = gems_art
        die_num = data.split(";")
        self.die = die_num[0]
        self.num = die_num[1]
    def roll_treasure(self):
        rolls = dice.dice(self.die).roll()
        items = []
        for i in range(int(rolls)):
            items.append(random.choice(self.objects[self.num]))
        return ", ".join(items)+" ("+self.num+" gp each)"

class magic_items():
    def __init__(self, data):
        self.magic = Tables.magic_item_table()
        die_table = data.split(";")
        self.die = die_table[0]
        self.table = die_table[1]
    def roll_treasure(self):
        rolls = dice.dice(self.die).roll()
        items = []
        for i in range(int(rolls)):
            items.append(self.magic.generate_treasure(self.table))
        return ", ".join(items)

class hoard_treasure_line(Treasure):
    def __init__(self, data):
        Treasure.__init__(self, data)
        obj = data["objects"]
        if(obj == "None"):
            self.object = None
        else:
            self.object = object(obj)
        magic = data["Magic Items"]
        self.items = []
        if magic:
            for d in magic:
                self.items.append(magic_items(d))
    def roll_treasure(self):
        ret = "Gems or Art: "
        if self.object:
            ret += self.object.roll_treasure()
        ret += "\nMagic Items: "
        if self.items:
            for i in self.items:
                ret += i.roll_treasure()
        return ret








