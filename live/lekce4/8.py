# python3 usd.py czk 550
# python3 usd.py eur 21

import sys
mena = sys.argv[1]
castka = int(sys.argv[2])


if mena == "czk":
    vysledek = castka * 0.041
    print(f"{castka} CZK je {vysledek} USD")
elif mena == "eur":
    vysledek = castka * 1.1
    print(f"{castka} EUR je {vysledek} USD")
else:
    print("Sorry, neznam kurz pro tuhle menu")

