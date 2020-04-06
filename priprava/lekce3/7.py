from pprint import pprint
# 7.a) Napište program, který vypíše pro první den kolik pasažérů jelo celkem směrem tam a kolik směrem zpět.

pasazeri = open("pasazeri.txt")
passengers = [p for p in pasazeri]
pprint(passengers)

passengers = [p.strip() for p in passengers]
pprint(passengers)

passengers = [p.split(" ") for p in passengers]
pprint(passengers)

dny = [[p.split(",") for p in passengers[x]] for x in range(len(passengers))]
pprint(dny)

dny0 = dny[0]
den1_tam = [int(dny0[x][0]) for x in range(len(dny0))]
den1_zpet = sum([int(dny[0][x][1]) for x in range(len(dny0))])
pprint(den1_tam)
pprint(den1_zpet)

# # 7.b) Nechť váš program vypisuje součty pasažérů ze celý týden, tedy kolik lidí za celý týden jelo směrem tam a kolik směrem zpět.
pasazeri = open("pasazeri.txt")
passengers = [p.strip() for p in pasazeri]
passengers = [p.split(" ") for p in passengers]
dny = [[p.split(",") for p in passengers[x]] for x in range(len(passengers))]
pasazeri.close()
tyden_tam = sum([sum([int(dny[y][x][0]) for x in range(len(dny[0]))]) for y in range(len(dny))])
tyden_zpet = sum([sum([int(dny[y][x][1]) for x in range(len(dny[0]))]) for y in range(len(dny))])
pprint(tyden_tam)
pprint(tyden_zpet)