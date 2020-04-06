import random

card_color = ["krize","piky","srdce","kary"]
card_number = ["2","3","4","5","6","7","8","9","J","Q","K","A"]

# vylosovat 4 nahodne karty

# random.randint --> vrati nahodne cislo
# random.choice --> vybere ze seznamu nahodnej prvek
# random.shuffle --> zamicha seznam

# seznam = [1,2,3,4,5]
# random.shuffle(seznam)
# print(seznam)

# a)
#picked_cards = [ random.choice(card_color) + " " + random.choice(card_number) for i in range(4) ]
picked_cards = [ [random.choice(card_color), random.choice(card_number)] for i in range(4) ]
print(picked_cards)


# b)
 # J,Q,K --> 10 ... A --> 1
hodnoty = [ card[1] for card in picked_cards ]
print(f"hodnoty: {hodnoty}")

nahrazeni_pismenek = [ cislo_karty.replace("J","10").replace("Q","10").replace("K","10").replace("A","1") for cislo_karty in hodnoty ]

print(f"nahrazeni_pismenek {nahrazeni_pismenek}")

# secist jejich hodnoty a vypsat soucet

soucet = sum([ int(cislo) for cislo in nahrazeni_pismenek ])
print(soucet)
