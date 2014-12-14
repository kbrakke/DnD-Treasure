__author__ = 'Kris'

class spell():
    def __init__(self, name, level):
        self.name = name
        self.level = level
    def __eq__(self, other):
        return str(self.name).__eq__(str(other.name))

spells = set()
#read in each spell
spells_dict = {}
f = open("Random Exploration - Spells.csv", 'r')
for line in f.readlines():
    (name, level) = line.split(',')
    spells_dict[name] = level
    s = spell(name, level)
    spells.add(s.name)

#write out the spells
f = open("SpellsList.csv", 'w')
for spell in spells:
    f.write("{},{}".format(spell, spells_dict[spell]))

