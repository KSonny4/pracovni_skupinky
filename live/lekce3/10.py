import random
from pprint import pprint 
soubor = open("karty.txt","r")
deck = [card for card in soubor]
soubor.close()


# print("zaprasene " + str(deck))
# print("zaprasene {}".format(deck))
pprint(f"zaprasene: {deck}")

deck_strip = [card.strip() for card in deck]
pprint(f"odprasene: {deck_strip}")


# zamichat a vybrat hodnoty
random.shuffle(deck_strip)

pprint(f"zamichano: {deck_strip}")

vybrane_karty = deck_strip[:4]

pprint(f"vybrane karty: {vybrane_karty}")


# secist hodnoty karet
# kluk dáma král --> 10 ; eso --> 1

rozdeleni = [ karta.split() for karta in vybrane_karty]
pprint(f"karty rozdelene: {rozdeleni}")

nahrazeni = [int(card[0].replace("kluk","10").replace("dáma","10").replace("král","10").replace("eso","1")) for card in rozdeleni]
pprint(f"nahrazeni {nahrazeni}")


soucet = sum(nahrazeni)
print(f"soucet {soucet}")
