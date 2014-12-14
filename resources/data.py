__author__ = 'Kris'

individual_treasure = [
[ {"range" : "1-30"  , "coins" : ["5d6;cp"]},
  {"range" : "31-60" , "coins" : ["4d6;sp"]},
  {"range" : "61-70" , "coins" : ["3d6;ep"]},
  {"range" : "71-95" , "coins" : ["3d6;gp"]},
  {"range" : "96-100", "coins" : ["1d6;pp"]}
],
[ {"range" : "1-30"  , "coins" : ["4d6x100;cp" , "1d6x10;ep" ]},
  {"range" : "31-60" , "coins" : ["6d6x10;sp"  , "2d6x10;gp" ]},
  {"range" : "61-70" , "coins" : ["3d6x10;ep"  , "2d6x10;gp" ]},
  {"range" : "71-95" , "coins" : ["4d6x10;gp"]},
  {"range" : "96-100", "coins" : ["2d6x10;gp"  , "3d6x1;pp"   ]}
],
[ {"range" : "1-20"  , "coins" : ["4d6x100;sp" , "1d6x100;gp"]},
  {"range" : "21-35" , "coins" : ["1d6x100;ep" , "1d6x100;gp"]},
  {"range" : "36-75" , "coins" : ["2d6x100;gp" , "1d6x10;pp" ]},
  {"range" : "76-100", "coins" : ["2d6x100;gp" , "2d6x10;pp" ]}
],
[ {"range" : "1-15"  , "coins" : ["2d6x1000;ep", "8d6x100;gp"]},
  {"range" : "16-55" , "coins" : ["1d6x1000;gp", "1d6x100;pp"]},
  {"range" : "56-100", "coins" : ["1d6x1000;gp", "2d6x100;pp"]}
]
]

gemstones = {
    "10"  : ["Azurite","Banded agate","Blue quartz","Eye Agate","Hematite","Lapis Lazuli",
             "Malachite","Moss Agate","Obsidian","Rhodochrosite","Tiger Eye","Turquoise"],
    "50"  : ["Bloodstone","Carnelian","Chalcedony","Chrysoprase","Citrine",
             "Jasper","Moonstone","Onyx","Quartz","Sardonyx","Star Rose Quartz"],
    "100" : ["Amber","Amethyst","Chrysoberyl","Coral","Garnet","Jade","Jet","Pearl","Spinel","Tourmaline"],
    "500" : ["Alexandrite","Aquamarrine","Black Perl","Blue Spinel","Peridot","Topaz"],
    "1000": ["Black Opal","Blue Sapphire","Emerald","Fire Opal","Opal","Star Ruby","Star Sapphire","Yellow Sapphire"],
    "5000": ["Black Sapphire","Diamond","Jacinth","Ruby"]
}

art = {
    "25"  : ["Silver ewer","Carved bone statuette","Small gold bracelet","Cloth-of-gold vestments",
             "Black velvet mask stitched with silver thread","Chopper chalice with silver filigree",
             "Pair of engraved bone dice","Small mirror set in a painted wooden frame",
             "Embroidered silk handkerchief","Gold locket with a painted portrait inside"],
    "250" : ["Gold ring set with bloodstones","Carved ivory statuette","Large gold bracelet",
             "Silver necklace with a gemstone pendant","Bronze crown","Silk robe with gold embroidery",
             "Large well-made tapestry","Brass mug with jade inlay","Box of turquoise animal figurine",
             "Gold bird cage with electrum filigree"],
    "750" : ["Silver chalice set with moonstones","Silver-plated steel longsword with jet set in hilt",
             "Carved harp of exotic wood with ivory inlay and zircon gems","Small gold idol",
             "Gold dragon comb set with red garnets as eyes","Silver and gold brooch,"
             "Bottle stopper cork embossed with gold leaf and set with amethysts","Painted gold war mask",
             "Ceremonial electrum dagger with a black pearl in the pommel",
             "Obsidian statuette with gold fittings and inlays"],
    "2500": ["Fine gold chain set with a fire opal","Old masterpiece painting","Platinum bracelet set with a sapphire",
             "Embroidered silk and velvet mantle set with numerous moonstones","Embroidered glove set with jewel chips",
             "Jeweled anklet","Gold music box","Gold circlet set with four aquamarines",
             "A necklace string of small pink perls","Eye patch with a mock eye set in blue sapphire and moonstone"],
    "7500": ["Jeweled gold crown","Jeweled platinum ring","Small gold statuette set with rubies",
             "Gold cup set with emeralds","Gold jewelry box with platinum filigree","Painted gold child's sarcophagus",
             "Jade game board with solid gold playing pieces","Bejeweled ivory drinking horn with gold filigree"]
}

A = [
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
]

B = [
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
]

C = [
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
]

D = [
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
]

E = [
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
    {"range" : "1-50", "treasure" : "Potion of Healing"},
]

F = [

]

G = [

]

H = [

]

I = [
    
]