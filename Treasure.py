__author__ = 'Kris'
import random, dice, json
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
    def __init__(self):
        self.objects = gems_art
    def roll_treasure(self, die, size):
        rolls = dice.dice(die).roll()
        items = random.sample(self.objects[size], rolls)
        return "".join(items, ", ")





