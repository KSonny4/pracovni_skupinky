import csv 

#soubor = open("soubor.txt", encoding='utf8')
#chroustani = [x for x in soubor]
#print(chroustani)
#soubor.close()

with open("soubor.txt", "r") as soubor:
    csv_soubor = csv.reader(soubor, delimiter=' ', quotechar='|')
    for radek in csv_soubor:
        print(radek)
    
    

# tady uz je soubor zavreny