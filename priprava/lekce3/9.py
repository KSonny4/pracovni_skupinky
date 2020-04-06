import random
# 9a)
card_color = ['kříže', 'srdce', 'piky', 'káry']
card_number = ['2','3','4','5','6','7','8','9','J','Q','K','A']
cards = [ [random.choice(card_color) , random.choice(card_number)] for i in range(4)]
print(cards)

# 9b) Dále k tomuto seznamu vypište součet hodnot všech vylosovaných karet. Položme hodnotu karet J, Q a K rovnu deseti a eso rovnu jedné.
cards_with_changed_values = [card[1].replace("J","10").replace("Q","10").replace("K","10").replace("A","1") for card in cards]
print(cards_with_changed_values)
sum_cards = sum([int(x) for x in cards_with_changed_values])
print(sum_cards)    