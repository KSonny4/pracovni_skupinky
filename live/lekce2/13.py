import random

barvy = ["kříže", "srdce", "piky", "káry"]
hodnoty = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q" , "K", "A"]




print( random.choice(hodnoty) + " "  + random.choice(barvy) )


nahodne_cislo1 = random.randint(0,len(barvy)-1)
nahodne_cislo2 = random.randint(0,len(hodnoty)-1)

print(hodnoty[nahodne_cislo2] + " " + barvy[nahodne_cislo1])

