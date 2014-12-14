__author__ = 'Kris'
import random, re

class dice():
    def __init__(self, die):
        die_regex = re.compile("(\d+)d(\d+)(?:x)?(\d+)?")
        die_groups = die_regex.search(die)
        self.num_dice = int(die_groups.group(1))
        self.dice_size = int(die_groups.group(2))
        if(die_groups.group(3) == None):
            self.multiplier = 1
        else:
            self.multiplier = int(die_groups.group(3))
    def roll(self):
        sum = 0
        for i in range(self.num_dice):
            sum += random.randint(1,self.dice_size)
        return str((sum*self.multiplier))
    def __str__(self):
        return str(self.roll())