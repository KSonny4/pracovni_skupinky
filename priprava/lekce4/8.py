import sys

EUR_to_CZK = 26.79 # 1 USD == 26.79 kc
CZK_to_EUR = 0.037 # 1 EUR == 0.037 CZK
mena = sys.argv[1]
cislo = sys.argv[2]

if mena == 'czk':
    vypocet = float(cislo)*CZK_to_EUR
    print(f"{cislo} {mena} je {vypocet} eur")
elif mena == 'eur':
    vypocet = float(cislo)*EUR_to_CZK 
    print(f"{cislo} {mena} je {vypocet} czk")

else:
    print("NEZNAM MENU!")