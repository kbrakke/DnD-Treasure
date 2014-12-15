__author__ = 'Kris'
import Tables
from resources.data import *

TT = Tables.individual_treasure_table()
MiT = Tables.magic_item_table()
HT = Tables.hoard_treasures(Hoard_Teir_1)
for i in range(10):
    print HT.generate_treasure()
    print
#for i in range(1, 100):
#    print TT.generate_treasure(2)
#for i in range(1,10):
#    print MiT.generate_treasure("A")
#    print MiT.generate_treasure("B")
#    print MiT.generate_treasure("C")
#    print MiT.generate_treasure("D")
#    print MiT.generate_treasure("E")
#    print MiT.generate_treasure("F")
#    print MiT.generate_treasure("G")
#    print MiT.generate_treasure("H")
#    print MiT.generate_treasure("I")