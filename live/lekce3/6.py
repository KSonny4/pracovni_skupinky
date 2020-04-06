import random

hody = [random.randint(0,6) for i in range(4)]

print(hody)

soubor = open("hody.txt", "w", encoding="utf-8")

seznam = ','.join([str(x) for x in hody])

# [soubor.write(prvek) for prvek in seznam]

soubor.write(seznam + '\n')


soubor.close()

# 5,4,1,2,3,