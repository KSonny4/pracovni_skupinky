import sys

velbloud = sys.argv[1]
print("nactene slovo: " + str(velbloud))

#velbloud = velbloudHoniHada
# velbloud Honi Hada


#seznam_slov = ["a","b","c", "A", "C", "s"]
#slov = [cislo_pismena for cislo_pismena, pismeno in enumerate(seznam_slov) if pismeno.isupper()]
#print(slov)


#velbloud = velbloudHoniHada
#velbloud Honi Hada

lokace_velka_pismena = [cislo_pismena for cislo_pismena,pismeno in enumerate(velbloud) if pismeno.isupper()]

print("lokace_velka_pismena: " + str(lokace_velka_pismena))

# lokace: [0, 8, 12, 16, 18, 25]
lokace =           [0]    + lokace_velka_pismena  + [len(velbloud)]

print(lokace_velka_pismena)
print("lokace: " + str(lokace))

#velbloudHoniHadaNaZahrade
print("slovo1 : " + velbloud[0:8])
print("slovo2 : " + velbloud[8:12])

xka = [ x for x in range(0,len(lokace)-1) ]
print("xka: " + str(xka))
roz = [velbloud[ 0  : 8 ]]

#                                                    [0, 1, 2, 3, 4]
rozsek = [ velbloud[lokace[x]:lokace[x+1]] for x in range(0,len(lokace)-1) ]
#rozsek = [ velbloud[lokace[0]:lokace[0+1]] for x in range(0,len(lokace)-1) ]


print(rozsek)

spojeno = '_'.join(rozsek).lower()

print("vitezny snake: " + str(spojeno))



super_velbloud = "tohleJeHad"

slovo = "vyhra" if "A".islower() else "prohra"
print(slovo)

vysledek = [pismeno for pismeno in super_velbloud]
print(vysledek)

vysledek1 = "".join(["_" + pismeno.lower() if pismeno.isupper() else pismeno for pismeno in super_velbloud])
print(vysledek1)