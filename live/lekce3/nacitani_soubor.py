soubor = open("znamky.csv")
data = [radek for radek in soubor]
print(f"data: {data}")
soubor.close()


data2 =  [radek for radek in soubor]
print(f"data2: {data2}")