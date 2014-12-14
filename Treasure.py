__author__ = 'Kris'
import random, dice, json

"""
This file details all the different types treasure that you can find in a dungeons and dragons game
You can find
Coins - die, multiplier, type
Goods:
    Art - die, multiplier, name (description)
    Gems - die, multiplier, name
Items:
    Mundane:
        Alchemical - Value, Name, Descripion, quantity (die)
        Armor - Value, Name, Weight, Description
        Weapons:
            Simple Melee - Name, Value, Damage, Type, Weight, Properties
            Simple Ranged - Name, Value, Damage, Type, Weight, Properties
            Martial Melee - Name, Value, Damage, Type, Weight, Properties
            Martial Ranged - Name, Value, Damage, Type, Weight, Properties
    Minor/Medium/Major:
        Armor:
            Generated Armor - Name, Value, Weight, Description
            Specific Armor
        Weapons:
            Generated Weapons:
                Generated Melee - Name, Value, Damage, Type, Weight, Properties
                Generated Ranged - Name, Value, Damage, Type, Weight, Properties
            Sepecific Weapons - Name, Value, Damage, Type, Weight, Properties
        Potions - Name, Value, Description, Quantity
        Rings - Name, Value, Description
        Rods - Name, Value, Description
        Staff - Name, Value, Description
        Wand - Name, Value, Description
        Wonderous Item - Name, Value, Description
"""

"""
json description of items

coin {die : Die, multiplier : Int, denomination : String}
art {die : Die, Multiplier : Int, Denomination : String, Descriptions : [String]}

"""
class Treasure():
    def __init__(self, data):
        self.data = data
        range_array = self.data["range"].split('-')
        self.low = int(range_array[0])
        self.high = int(range_array[1])
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

class Goods(Treasure):
    def __init__(self, range_low, range_high, die, multiplier, value, description_list):
        self.range_low = range_low
        self.range_high = range_high
        self.die = die
        self.multiplier = multiplier
        self.value = value
        self.description_list = description_list
    def roll_treasure(self):
        return "{} {} {}".format(random.choice(self.description_list),
                                 str(int(self.die.roll()) * int(self.multiplier)),
                                 self.value)

class Null_Treasure(Treasure):
    def __init__(self, range_low, range_high):
        Treasure.__init__(range_low, range_high)
    def roll_treasure(self):
        return "None"

class NVD_Treasure(Treasure):
    def __init__(self, range_low, range_high, name, value, description):
        Treasure.__init__(range_low, range_high)
        self.name = name
        self.value = value
        self.description = description
    def roll_treasure(self):
        return "{}\n{}\n{}".format(self.name, self.value, self.description)

class Table_Treasure(Treasure):
    def __init__(self, range_low, range_high, table):
        Treasure.__init__(self, range_low, range_high)
        self.table = table
    def roll_treasure(self):
        roll = random.randint(1, 100)
        for entry in self.table:
            if entry.in_range(roll):
                return str(entry.roll_treasure())

class Multi_Treasure(Treasure):
    def __init__(self, range_low, range_high, die, treasure):
        Treasure.__init__(range_low, range_high)
        self.die = die
        self.treasure = treasure
    def roll_treasure(self):
        treasure_set = []
        for i in range(0, int(self.die.roll())):
            treasure_set.append(self.treasure.roll_treasure())

class Weapon_Treasure(Treasure):
    def __init__(self, range_low, range_high, name, value, damage, type, weight, properties):
        Treasure.__init__(range_low, range_high)
        self.name = name
        self.value = value
        self.damage = damage
        self.type = type
        self.weight = weight
        self.properties = properties
    def roll_treasure(self):
        return "{}\n{}   {}\n{} {}\n{}".format(self.name, self.value, self.weight, self.damage, self.type, self.properties)

class Descriptive_Treasure(Treasure):
    def __init__(self, range_low, range_high, name, value, weight, description):
        Treasure.__init__(range_low, range_high)
        self.name = name
        self.value = value
        self.weight = weight
        self.description = description
    def roll_treasure(self):
        return "{}\n{}   {}\n{}".format(self.name, self.value, self.weight, self.description)

class Generated_Weapon_Treasure(Treasure):
    def __init__(self, range_low, range_high, weapon_generator):
        Treasure.__init__(range_low, range_high)
        self.weapon_generator = weapon_generator
    def roll_treasure(self):
        return self.weapon_generator.roll_item()





