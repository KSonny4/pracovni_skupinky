#python3 kmax.py 5 6 1 3 8 4 7 2
import sys
kte = sys.argv[1]
seznam = sys.argv[2:]

cisla = [int(x) for x in seznam]
print(cisla)


novy_seznam = []


while len(cisla) > 0:

    minimum = cisla[0]
    for cislo in cisla:        
        if cislo < minimum:            
            minimum = cislo
    print(f"nove minimum: {minimum}")

    novy_seznam.append(minimum)
    cisla.remove(minimum)

print(f"novy seznam = {novy_seznam}")