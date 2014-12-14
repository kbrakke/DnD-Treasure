__author__ = 'Kris'

import Tables
TT = Tables.individual_treasure_table()
for i in range(1, 100):
    print TT.generate_treasure(2)