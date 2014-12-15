__author__ = 'Kris'

import Tables
TT = Tables.individual_treasure_table()
MiT = Tables.magic_item_table()
#for i in range(1, 100):
#    print TT.generate_treasure(2)
for i in range(1,10):
    print MiT.generate_treasure("A")
    print MiT.generate_treasure("B")
    print MiT.generate_treasure("C")
    print MiT.generate_treasure("D")
    print MiT.generate_treasure("E")
    print MiT.generate_treasure("F")
    print MiT.generate_treasure("G")
    print MiT.generate_treasure("H")
    print MiT.generate_treasure("I")