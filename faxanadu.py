xlat = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,?"

titles = [ "Novice", "Aspirant", "Battler", "Fighter", 
           "Adept", "Chevalier", "Veteran", "Warrior",
           "Swordsman", "Hero", "Soldier", "Myrmidon",
           "Champion", "Superhero", "Paladin", "Lord" ]

weapons = [ "Hand Dagger", "Long Sword", "Giant Blade", "Dragon Slayer" ]

armors = [ "Leather Armor", "Studded Mail", "Full Plate", "Battle Suit" ]

shields = [ "Small Shield", "Large Shield", "Magic Shield", "Battle Helmet" ]

magics = [ "Deluge", "Fire", "Thunder", "Death", "Tilte" ]

items = [ "Ring of Elf", "Ruby Ring", "Ring of Dworf", "Demons Ring", "Ace Key", "King Key", "Queen Key", "Jack Key",
          "Joker Key", "Mattock", "Rod", "Crystal", "Lamp", "Hour Glass", "Book", "Wing Boots",
          "Red Potion", "Black Potion", "Elixir", "Pendant", "Black Onix", "Fire Crystal", "it22", "it23",
          "it24", "it25", "it26", "it27", "it28", "it29", "it30", "it31" ]

powerups = [ "Elf Ring", "Ruby Ring", "Dworf Ring", "Demon's Ring", "Elixir", "Magical Rod", "Pendant", "Black Onyx" ]

events = [ "ev0", "ev1", "Pushed Rock", "Killed Dworf (T)", "Killed Rock Vaulter", "Third Spring", "Second Spring", "First Spring" ]

def cksum(bits):
    cs = 0
    while len(bits) >= 8:
        cs = cs + int(bits[0:8], 2)
        bits = bits[8:]
    if len(bits) > 0:
        bits = bits + "0000000"
        cs = cs + int(bits[0:8], 2)
    return cs & 0xff

def base64dec(passwd):
    mx = [ xlat.index(x) for x in passwd]
    mxb = [ "{:06b}".format(x) for x in mx]
    mxs = ''.join(mxb)
    return mxs

def base64enc(bits):
    enc = ""
    while len(bits) > 0:
        enc = enc + xlat[ int(bits[0:6],2) ]
        bits = bits[6:]
    return enc

def declist(bits, title, names, cbits, lbits):
    eexist = bits[0:cbits]
    bits = bits[cbits:]

    print title,

    eeval = int(eexist,2)
    if eeval == 0:
        print "None"
        return bits

    for x in xrange(eeval):
        print names[int(bits[0:lbits],2)],
        eexist = eexist + bits[0:lbits]
        bits = bits[lbits:]

    print eexist

    return bits

def decode(passwd, cmt):
    mxs = base64dec(passwd)
    print mxs, passwd

    if not cksum(mxs) == 0:
        print "Checksum fails"
        return

    cs = mxs[0:8]
    mxs = mxs[8:]
    print "Checksum: ", int(cs,2), cs

    nd = mxs[0:5]
    mxs = mxs[5:]
    print "Digits:   ", int(nd,2), nd
    if not int(nd,2) == len(passwd):
        print "Wrong number of digits"
        return

    town = mxs[0:3]
    mxs = mxs[3:]
    print "Town:     ", int(town,2), town

    title = mxs[0:4]
    mxs = mxs[4:]
    print "Title:    ", titles[ int(title, 2) ], title

    pbits = mxs[0:8]
    mxs = mxs[8:]

    print "Powerups: ",
    for i in xrange(8):
        if pbits[i] == "1":
            print powerups[i],
    print pbits

    evbits = mxs[0:8]
    mxs = mxs[8:]

    print "Events:   ",
    for i in xrange(8):
        if evbits[i] == "1":
            print events[i],
    print evbits

    mxs = declist( mxs, "Weapon:   ", weapons, 1, 2)
    mxs = declist( mxs, "Armor:    ", armors, 1, 2)
    mxs = declist( mxs, "Shield:   ", shields, 1, 2)
    mxs = declist( mxs, "Magic:    ", magics, 1, 3)
    mxs = declist( mxs, "Item:     ", items, 1, 5)

    mxs = declist( mxs, "Weapons:  ", weapons, 3, 2)
    mxs = declist( mxs, "Armors:   ", armors, 3, 2)
    mxs = declist( mxs, "Shields:  ", shields, 3, 2)
    mxs = declist( mxs, "Magics:   ", magics, 3, 3)
    mxs = declist( mxs, "Items:    ", items, 4, 5)

    print "Zeroes:   ", mxs

    print cmt
    print


def flag(v):
    if v:
        return "1"
    return "0"

def eslot(item, lbits):
    if item is None:
        return "0"
    return mklist([item], 1, lbits)

def mklist(ilist, cbits, lbits):
    cfmt = "{{:0{:d}b}}".format(cbits)
    lfmt = "{{:0{:d}b}}".format(lbits)
    lst = cfmt.format(len(ilist))
    for x in ilist:
        lst = lst + lfmt.format(x)
    return lst

def encode(town, title, elfring, rubyring, dworfring, demonring, elixir, magicrod, pendant, blackonyx, events, weapon, armor, shield, magic, item, weapons, armors, shields, magics, items):
    bits = "0000000000000"

    bits = bits + "{:03b}".format(town)
    bits = bits + "{:04b}".format(title)

    bits = bits + flag(elfring)
    bits = bits + flag(rubyring)
    bits = bits + flag(dworfring)
    bits = bits + flag(demonring)
    bits = bits + flag(elixir)
    bits = bits + flag(magicrod)
    bits = bits + flag(pendant)
    bits = bits + flag(blackonyx)

    for x in events:
        bits = bits + flag(x)

    bits = bits + eslot(weapon, 2)
    bits = bits + eslot(armor, 2)
    bits = bits + eslot(shield, 2)
    bits = bits + eslot(magic, 3)
    bits = bits + eslot(item, 5)

    bits = bits + mklist(weapons, 3, 2)
    bits = bits + mklist(armors, 3, 2)
    bits = bits + mklist(shields, 3, 2)
    bits = bits + mklist(magics, 3, 3)
    bits = bits + mklist(items, 4, 5)

    while not (len(bits) % 6) == 0:
        bits = bits + "0"

    bits = bits[0:8] + "{:05b}".format( len( bits) / 6 ) + bits[13:]

    c = -cksum( bits ) & 0xff
    bits = "{:08b}".format( c ) + bits[8:]

    return base64enc(bits)

import sys
if len(sys.argv) > 1:
    decode( sys.argv[1], "Command Line" )
    sys.exit(0)

#decode("o1EIAAQAAA", "0 nothing eq: <> Leather <> <> ElfRing")
#decode("l1kIAAQEAAA", "0 nothing Dagger eq: <> Leather <> <> ElfRing")
#decode("F1kIAAQEAIA", "0 nothing Dagger Deluge eq: <> Leather <> <> ElfRing")
#decode("SWEIAARGBAAA", "0 RedPotion Dagger eq: <> Leather <> Deluge ElfRing")
#decode("UmEIAARAgAGA", "0 nothing RedPotion Dagger eq: <> Leather <> Deluge ElfRing")
#decode("FlkIAAkAAIA", "0 nothing Deluge eq: Dagger Leather <> <> ElfRing")
#decode("hlkIAAkQAAA", "0 nothing eq: Dagger Leather <> Deluge ElfRing")
#decode("RWEIAAkQAAE4", "0 nothing JKey eq: Dagger Leather <> Deluge ElfRing")
#decode("RWEIAAkROAAA", "0 JKey eq: Dagger Leather <> Deluge ElfRing")
#decode("MWkIAAkROAAMA", "0 JKey RedPotion eq: Dagger Leather <> Deluge ElfRing")
#decode("AXEIAAkROAAUIA", "0 JKey RedPotion RedPotion eq: Dagger Leather <> Deluge ElfRing")
#decode("8XEYAAkROAAUIA", "1 JKey RedPotion RedPotion eq: Dagger Leather <> Deluge ElfRing")
#decode("6HEYAAkROAAcIQ", "1 JKey RedPotion RedPotion RedPotion eq: Dagger Leather <> Deluge ElfRing")
#decode("0HkYAAkROAAkIQg", "1 JKey RedPotion RedPotion RedPotion RedPotion eq: Dagger Leather <> Deluge ElfRing")
#decode("gIEYAAkROAAsIQhA", "1 JKey RedPotion RedPotion RedPotion RedPotion RedPotion eq: Dagger Leather <> Deluge ElfRing")
#decode("bokYAAkROAA0IQhCA", "1 JKey RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion eq: Dagger Leather <> Deluge ElfRing")
#decode("TpEYAAkROAA8IQhCEA", "1 JKey RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion eq: Dagger Leather <> Deluge ElfRing")
#decode("vpkYAAkROABEIQhCEIA", "1 JKey RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion eq: Dagger Leather <> Deluge ElfRing")
#decode("vpkYAAkRgABEIQhCEDg", "1 RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion JKey eq: Dagger Leather <> Deluge ElfRing")
#decode("tJkYAAkRgAQRCEIQhA4", "1 RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion JKey SShld eq: Dagger Leather <> Deluge ElfRing")
#decode("xZkYAAkkYAARCEIQhA4", "1 RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion JKey eq: Dagger Leather SShld Deluge ElfRing")
#decode("tZkoAAkkYAARCEIQhA4", "2 RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion JKey eq: Dagger Leather SShld Deluge ElfRing")
#decode("pZk4AAkkTgARCEIQhCA", "3 JKey RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion eq: Dagger Leather SShld Deluge ElfRing")
#decode("pZk4AAkkYAARCEIQhA4", "3 RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion JKey eq: Dagger Leather SShld Deluge ElfRing")
#decode("ypE4AQkkAAIhCEIQgk", "3 nothing RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion Mattock eq: Dagger Leather SShld Deluge ElfRing")
#decode("upFIAQkkAAIhCEIQgk", "4 nothing RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion RedPotion Mattock eq: Dagger Leather SShld Deluge ElfRing")
#decode("14FYAQkkADBYQhBI", "5 nothing RedPotion RedPotion RedPotion RedPotion Mattock MShield eq: Dagger Leather SShld Deluge ElfRing")
#decode("14FYAQk0ACBYQhBI", "5 RedPotion RedPotion RedPotion RedPotion RedPotion Mattock SShield eq: Dagger Leather MShld Deluge ElfRing")
#decode("DXpYAAk0YFBAcIQ", "5 RedPotion RedPotion RedPotion RedPotion SShield LSword eq: Dagger Leather MShld Deluge ElfRing")

#encode(town, title, elfring, rubyring, dworfring, demonring, elixir, magicrod, pendant, blackonyx, events, weapon, armor, shield, magic, item, weapons, armors, shields, magics, items):
#print encode(1, 0, 1, 0, 0, 0, 0, 0, 0, 0, [0,0,0,0,0,0,0,0], None, 0, None, None, None, [], [], [], [], [])

#decode("05j?0v?,GMxmNAUzMeA", "Starting Town")
#decode("uJH?0v?,GMxmNAUyNA", "Martial Arts")
#decode("j4n?8A?,GMxmNAUxO", "First town")
#decode("fon?8Q?,GMxmNAUxS", "Killed Dworf")
#decode("zoL?8Q?,GMxmNAUw", "Forepaw")
#decode("Bor?cB?,GMxmNAUxM", "First Spring")
#decode("upL?cJ?,GMxmNAUyM8", "Defeated Rock Dropper")
#decode("pqL?8L?,GMxmNAU0NCEA", "Second spring")
#decode("5qL?cP?,GMxmNAU0NCEA", "Third spring")
#decode("l4r8Av?,GMxmNAUxM", "Pushed Rock")
#decode("8Jv8Av?9mMxmNAVDacw", "Third town")
#decode("8pv8Iv?9mMxmNAVDOdo", "Pendant")
#decode("RbT8Iv?9mMxmNAVHO2EDJO", "Fourth Town")
#decode("tqz8Mv?9zsZjMaAqI0yTg", "Black Onyx")
#decode("8a3,Mv?9mMxmNAVFaZJzg", "Dworf Ring")
#decode("mr7,Mv?9mMxmNAVIaZJzvgU", "Sixth Town")
#decode("Rbf?cv?9mMxmNAjHaZJzvK", "Seventh Town")
#print encode(0, 15, 1, 1, 1, 1, 1, 1, 0, 1, [0,0,1,0,1,1,1,1], 3, 3, 3, 4, None, [0,1,2], [0,1,2], [0,1,2], [0,1,2,3], [6,7,16])
#decode("tpL?0??,GMxmNAUyNA", "PW")
