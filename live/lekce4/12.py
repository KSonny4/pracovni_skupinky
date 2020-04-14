import sys
znamky = sys.argv[1:]
znamky = [int(x) for x in znamky]
print(f"znamky {znamky}")

for znamka in [1,2,3,4,5]:
    pocet = znamky.count(znamka)
    if pocet > 0:
        print(f"znamka {znamka}: {pocet}")

jednicky = 0
dvojky = 0
for znamka in znamky:

    ...

    if znamka == 1:
        jednicky += 1
    if znamka == 2:
        dvojky += 1

print(f"jednicky: {jednicky}, dvojky: {dvojky}")