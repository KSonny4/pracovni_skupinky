from pprint import pprint
soubor = open('pasazeri.txt','r',encoding='utf-8')
data = [radek.strip() for radek in soubor]
soubor.close()

pprint(data)

pasazeri = [radek.split(" ") for radek in data ]
pprint(f"pasazeri {pasazeri}")

prvni_den = pasazeri[0]
pprint(f"prvni_den {prvni_den}")

tam_prvni_den = sum([ int(hodnota.split(",")[0]) for hodnota in prvni_den ]) 
zpet_prvni_den = sum([ int(hodnota.split(",")[1]) for hodnota in prvni_den ]) 
pprint(f"tam_prvni_den {tam_prvni_den}")
pprint(f"zpet_prvni_den {zpet_prvni_den}")

#pprint([den for den in pasazeri])

tam = sum ([ sum([ int(hodnota.split(",")[0]) for hodnota in den ]) for den in pasazeri])
zpet = sum ([ sum([ int(hodnota.split(",")[1]) for hodnota in den ]) for den in pasazeri])
pprint(f"tam {tam}") 
pprint(f"zpet {zpet}") 
