import sys
import random
kolikastenna = int(sys.argv[1])
pocet_hodu = int(sys.argv[2])


seznam_nahodnych_cisel = [ random.randint(1,kolikastenna) for x in range(pocet_hodu) ] 

print(seznam_nahodnych_cisel)



