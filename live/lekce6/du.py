soubor = open("vstup.txt", "r", encoding="utf-8")

#data = [row.strip() for row in soubor]


psenice = []
jecmen = []


data = []
for row in soubor:
    print(row)
    print(type(row))

soubor.close()


seznam_cisel = [x for x in range(10)]
print(seznam_cisel)


seznam_cisel2 = []
for x in range(10):
    seznam_cisel2.append(x)
print(seznam_cisel2)


slova = ["AHOJ","cus","NAZDAR"]

velka_slova = [x for x in slova if x.isupper()]


