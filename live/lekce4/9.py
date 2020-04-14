soubor = open("zustatky.txt", encoding='utf-8')
data = [float(x.strip()) for x in soubor]
soubor.close()
print(f"nactena data: {data}")

print("================")
#A
pocet = 0
for cislo in data:
    novy_zustatek = cislo*1.025
    pocet += 1
    if novy_zustatek > 0:
        print(f"{pocet} {novy_zustatek}")

print("================")

for poradove_cislo, cislo in enumerate(data):
    novy_zustatek = cislo*1.025
    if novy_zustatek > 0:
        print(f"{poradove_cislo+1} {novy_zustatek}")


