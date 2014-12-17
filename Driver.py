__author__ = 'Kris'
import Tables
from resources.data import *

TT = Tables.individual_treasure_table()
MiT = Tables.magic_item_table()
HT1 = Tables.hoard_treasures(Hoard_Teir_1)
HT2 = Tables.hoard_treasures(Hoard_Teir_2)
HT3 = Tables.hoard_treasures(Hoard_Teir_3)
HT4 = Tables.hoard_treasures(Hoard_Teir_4)
#for i in range(10):
#    print HT1.generate_treasure()
#    print
#for i in range(10):
#    print HT2.generate_treasure()
#    print
#for i in range(10):
#    print HT3.generate_treasure()
#    print
for i in range(10):
    print HT4.generate_treasure()
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