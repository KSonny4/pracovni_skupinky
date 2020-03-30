# 8
import sys
import math

print("Nacetli jsme prvni cislo: " + sys.argv[1])

vysledek_zaokrouhlovani1 = math.floor(float(sys.argv[1])+0.5)
print("zaokrouhleno " + str(vysledek_zaokrouhlovani1))

# https://realpython.com/python-f-strings/
print(f"zaokrouhleno {vysledek_zaokrouhlovani1}")