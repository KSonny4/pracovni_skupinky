#10. Zkusme vyřešit problém losování karet tak, aby se nám nemohlo stát, že nám nějaká karta padne vícekrát, když by správně v balíčku měla být od každé karty pouze jedna.
#10.a) Ze souboru karty.txt si načtěte do seznamu kompletní balíček karet. Zadání je stejné jako v předchozí úložce, tedy vylosovat 4 karty z balíčku a vypsat je jako seznam spolu se součtem hodnot.

import random
karta = open('karty.txt', 'r', encoding='utf-8')

#10.b) Existuje vícero možných postupů, které vedou ke stejnému výsledku. Zde už můžete trochu zagooglit. Ve většině postupů se vám bude hodit příkaz, který umí odstranit prvek seznamu na zadaném indexu:.
#x = [1, 2, 3]
#>>> del x[0]
#>>> x
#[2, 3]
#Také se vám může hodit funkce shuffle() z modulu random, která umí náhodně zamíchat seznam.

import itertools, random

card_color = ['kříže', 'srdce', 'piky', 'káry']
card_number = ['2','3','4','5','6','7','8','9','J','Q','K','A']

deck = [[x, y] for y in card_number for x in card_color]

# jedna moznost
random.shuffle(deck)
cards = [[deck[i][0], deck[i][1]] for i in range(4)]
print(cards)

cards_with_changed_values = [card[1].replace("J","10").replace("Q","10").replace("K","10").replace("A","1") for card in cards]
print(cards_with_changed_values)
sum_cards = sum([int(x) for x in cards_with_changed_values])
print(sum_cards)


# https://docs.python.org/3/library/random.html#random.sample
print(random.sample(deck,4))




