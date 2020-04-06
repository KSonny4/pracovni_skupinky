soubor=open("znamky.csv",encoding="utf=8")

radky = [radky for radky in soubor]
znamky=[x.replace("1","A").replace("2","B").replace("3","C").replace("4","D").replace("5","E") for x in radky[1:]]

soubor.close()

soubor1=open("znamky_nove.txt",mode = "w",encoding ="utf-8")

soubor1.write(radky[0]  + ("\n") )
[soubor1.write(radek + ("\n")) for radek in znamky[1:]]

soubor1.close()