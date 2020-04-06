from pprint import pprint

soubor = open("znamky.csv")
data = [radek for radek in soubor]
soubor.close()

pprint(f"tabulka {data}")

data_strip = [radek.strip() for radek in data]
pprint(f"tabulka strip {data_strip}")

prvni_radek = data_strip[0]
print(f" prvni radek {prvni_radek}")

znamky = [ radek.replace("1","A").replace("2","B").replace("3","C").replace("4","D").replace("5","F") for radek in data_strip[1:] ]
pprint(f"znamky {znamky}")


soubor1 = open("znamky_nove.csv", mode="w",encoding="utf-8")
soubor1.write(data_strip[0] + '\n') 
[ soubor1.write(znamka + '\n') for znamka in znamky ] 

soubor1.close()