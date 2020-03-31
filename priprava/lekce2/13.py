import random
card_color = ['kříže', 'srdce', 'piky', 'káry']
card_number = [str(list(range(2,10))), 'J', 'Q', 'K', 'A']
print((random.choice(card_number))+' ' +(random.choice(card_color)))