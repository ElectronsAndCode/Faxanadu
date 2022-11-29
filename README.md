# Faxanadu
Password generator and decoder for NES Faxanadu

This project is a barebones password codec for the NES game Faxanadu.  To create a password, call encode with the following parameters:

1. Starting town (0-7)  The town furthest from start whose priest you have visited
2. title (0-15) The latest title (level) conferred on you
3. elfring (0 or 1)  Do you have the Ring of Elf?
4. rubyring (0 or 1)  Do you have the Ruby Ring?
5. dworfring (0 or 1)  Do you have the Ring of Dworf?
6. demonring (0 or 1)  Do you have the Demons Ring?
7. elixir (0 or 1)  Do you have an elixir?
8. magicrod (0 or 1)  Do you have the rod that increases magic power?
9. pendant (0 or 1)  Do you have the rod that nerfs your sword?
10. blackonyx (0 or 1) Do you have the Black Onyx shield?
11. events (A list of accomplished feats).  Each value should be 0 or 1.
   - (unknown)
   - (unknown)
   - Pushed rock
   - Killed Dworf
   - Killed Rock Vaulter
   - Activated Third Spring
   - Activated Second Spring
   - Activated First Spring
12. weapon (0 to 3 or None)  Equipped weapon
   - 0 Hand dagger
   - 1 Long sword
   - 2 Giant blade
   - 3 Dragon slayer
13. armor (0 to 3 or None)  Equipped armor
   - 0 Leather armor
   - 1 Studded mail
   - 2 Full plate
   - 3 Battle suit
14. shield (0 to 3 or None)  Equipped shield
   - 0 Small shield
   - 1 Large shield
   - 2 Magic shield
   - 3 Battle helmet
15. magic (0 to 4 or None)  Equipped magic
   - 0 Deluge
   - 1 Fire
   - 2 Thunder
   - 3 Death
   - 4 Tilte
16. item (0 to 31 or None)  Readied item
   - 0 Ring of Elf (cannot be used)
   - 1 Ruby Ring (cannot be used)
   - 2 Ring of Dworf (cannot be used)
   - 3 Demons Ring (cannot be used)
   - 4 Ace Key
   - 5 King Key
   - 6 Queen Key
   - 7 Jack Key
   - 8 Joker Key
   - 9 Mattock
   - 10 Rod (cannot be used)
   - 11 Crystal (cannot be used)
   - 12 Lamp (cannot be used)
   - 13 Hour Glass
   - 14 Book (cannot be used)
   - 15 Wing Boots
   - 16 Red Potion
   - 17 Black Potion (cannot be used)
   - 18 Elixir (cannot be used as an item)
   - 19 Pendant (cannot be used)
   - 20 Black Onyx (cannot be used)
   - 21 Fire Crystal (cannot be used)
   - 22-31 are not defined
17. weapons  List of weapons
   - List is up to 4 integers between 0 and 3.  See equipped weapon for values
18. armors  List of armors
   - List is up to 4 integers between 0 and 3.  See equipped armor for values
19. shields  List of shields
   - List is up to 4 integers between 0 and 3.  See equipped shield for values
20. magics  List of magics
   - List is up to 4 integers between 0 and 4.  See equipped magic for values
21. items List of items
   - List is up to 8 integers between 0 and 31.  See equipped item for values

Example:
```
print encode(
             0,   # Starting town
             15,  # Lord
	     1,   # Elf
	     1,   # Ruby
	     1,   # Dworf
	     1,   # Demons
	     1,   # Elixir
	     1,   # Rod
	     0,   # No pendant
	     1,   # Black Onyx
	     [0,0,1,0,1,1,1,1], # Pushed rock, killed rock vaulter, opened all springs
	     3, # Dragon Slayer
	     3, # Battle Suit
	     3, # Battle Helmet
	     4, # Tilte
	     None, # No item
	     [0,1,2], # Three weaker swords
	     [0,1,2], # Three weaker armors
	     [0,1,2], # Three weaker shields
	     [0,1,2,3], # 4 previous magics
	     [6,7,16]) # Queen key, Jack key, Red potion
```

A given password may also be decoded by calling decode(password_string, descriptive_tag).

Example:
```
decode("tqz8Mv?9zsZjMaAqI0yTg", "Black Onyx")
```
