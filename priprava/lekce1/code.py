# odkaz na dokumentaci na list comprehensions - chroustani seznamu
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

#úkol 10 - delky = [136, 105, 82]

delky = [136, 105, 82]
trvani = [str([x // 60, x % 60]) for x in delky]
trvani = [str(x // 60) + ":" + str(x % 60) for x in delky]

#########################

nazvy = [
  'Někdo to rád horké, extended edition', 
  'Adéla ještě nevečeřela',
  'Kulový blesk'
]
delky = [136, 105, 82]


# z
[[str(delka//60) + ":" + str(delka%60)] for delka in delky]

# na
[str(delka//60) + ":" + str(delka%60) for delka in delky]

###########################
# ukol 6

#seznam vestavenych funkci z dokumentace Pythonu https://docs.python.org/3/library/functions.html
# https://thehelloworldprogram.com/python/python-string-methods/

jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']
pocty_pismen = [len(x) for x in jmena]
pismena_velkym = [x.upper() for x in jmena]
zenska_jmena = [x + 'a' for x in jmena]
email_adresy = [x.lower() + '@email.cz' for x in jmena]



#############################

hlasy = [ 
  [78774, 43179, 225111, 144799, 242854],
  [91062, 22451, 17475, 53391, 46450],
  [179186, 216499, 4493, 156305, 61222],
  [9619, 53476, 926, 64737, 34566],
  [66904, 85730, 27271, 12964, 38041],
  [118755, 1929, 30426, 25178, 31952],
  [64467, 40993, 81181, 39392, 4335],
  [11221, 97970, 26179, 98539, 112578],
  [171064, 7638, 8752, 96666, 39738],
  [74235, 101680, 18920, 45904, 1922],
  [39309, 1505, 10531, 30458, 40228],
  [131584, 1812, 241122, 22267, 99326],
  [194133, 39985, 200997, 28229, 20780],
  [66188, 51607, 15977, 177272, 17664]
]



#12.a) Kolik získal každý kandidát hlasů v celé ČR?

# co sloupec to kandidat
# nulty sloupec
[radek[0] for radek in hlasy]
# prvni sloupec
[radek[1] for radek in hlasy]

# a tak dal.. ten potrebujeme secist


sum( [radek[0] for radek in hlasy])
#1296501
sum( [radek[1] for radek in hlasy])
#766454
sum( [radek[2] for radek in hlasy])
#909361
sum( [radek[3] for radek in hlasy])
#996101
sum( [radek[4] for radek in hlasy])
#791656
#Neboli:

# jedine co se nam meni jsou cisla pro prvky v seznamu, potrebujeme
# si je nejak vygenerovat
[i for i in [0,1,2,3,4]]

#to je pracne, muzeme pouzit funkci range()

[i for i in range(4)]
[i for i in range(0,4)]

kandidati = [sum([radek[i] for radek in hlasy]) for i in [0,1,2,3,4]]
#[1296501, 766454, 909361, 996101, 791656]



#############################


#12.b) Který kandidát vyhrál první kolo voleb?

#>>> igor, radim, ondrej, vladan, augustin
#(1296501, 791656, 996101, 909361, 766454)
kandidati


max(kandidati)
#1296501

# pripadne
kandidati.index(max(kandidati))
#1296501

#############################

# 12.c) Ve kterých krajích byla nejvyšší a nejnižší volební účast

Praha =sum(hlasy[0])
J_k= sum(hlasy[1])
J_m_k= sum(hlasy[2])
K_k = sum(hlasy[3]) # atd.

# mozno takhle nebo kraje = [sum(hlasy[i]) for i in range(len(hlasy))]

kraje = [sum(kraje) for kraje in hlasy]
maximum = kraje.index(max(kraje))
minimum = kraje.index(min(kraje))

#############################

#12.d) Vytvořte tabulku, která ukazuje který kandidát vyhrál v kterém kraji.
# pro kazdy radek
[radek for radek in hlasy]

#najdu maximum ze radku
[max(radek) for radek in hlasy]

#[242854, 91062, 216499, 64737, 85730, 118755, 81181, 112578, 171064, 101680, 40228, 241122, 200997, 177272]

jmena = ['igor', 'augustin', 'vladan', 'ondrej', ' radim']

# pro kazdy radek si najdu maximum a to si ulozim do listu
vsechny_pozice = [kraj.index(max(kraj)) for kraj in hlasy]
vsechny_pozice


[jmena[pozice] for pozice in vsechny_pozice]
#[' radim', 'igor', 'augustin', 'ondrej', 'augustin', 'igor', 'vladan', ' radim', 'igor', 'augustin', ' radim', 'vladan', 'vladan', 'ondrej']




kraje = [
  ['Hlavní město Praha', '1 280 508'],
  ['Jihočeský kraj', '638 782'],
  ['Jihomoravský kraj', '1 178 812'],
  ['Karlovarský kraj', '296 749'],
  ['Kraj Vysočina', '508 952'],
  ['Královéhradecký kraj', '550 804'],
  ['Liberecký kraj', '440 636'],
  ['Moravskoslezský kraj', '1 209 879'],
  ['Olomoucký kraj', '633 925'],
  ['Pardubický kraj', '517 087'],
  ['Plzeňský kraj', '578 629'],
  ['Středočeský kraj', '1 338 982'],
  ['Ústecký kraj', '821 377'],
  ['Zlínský kraj', '583 698']
]

[[ kraje[index][0] , jmena[vsechny_pozice[index]]] for index in range(14)]

#############################


# 12.e) Využijte tabulku počtů obyvatel v krajích a vytvořte tabulku podobnou té z tohoto cvičení, která místo čísel bude obsahovat kolik procent hlasů získal každý kandidát v daném kraji.

[ round(kandidat / sum(hlasy[0]) ,2) for kandidat in hlasy[0] ]
[ round(kandidat / sum(hlasy[1]) ,2) for kandidat in hlasy[1] ]
[ round(kandidat / sum(hlasy[2]) ,2) for kandidat in hlasy[2] ]

#ukazka enumerate
list1 = ["eat","sleep","repeat"] 
[[cislo_prvku, prvek] for cislo_prvku, prvek in enumerate(list1)]


# bez enumerate
[ [round(kandidat/sum(kraj)*100,2) for kandidat in kraj] for kraj 
in hlasy]

# Enumerate
[[ round(kandidat / sum(hlasy[cislo_kraje]) * 100, 2) for kandidat in kraj]
 for cislo_kraje, kraj in enumerate(hlasy)]




#12.f) Vytvořte seznam pravdivostních hodnot, který bude říkat ve kterých krajích překročila voleb
# split() je stejne jako split(" ")
kraje2 = [[x[0] , int (''.join(x[1].split()))] for x in kraje]
kraje2 = [[x[0] , int(x[1].replace(" ", "")) ] for x in kraje]
kraje2
#[['Hlavní město Praha', 1280508], ['Jihočeský kraj', 638782], ['Jihomoravský kraj', 1178812], ['Karlovarský kraj', 296749], ['Kraj Vysočina', 508952], ['Královéhradecký kraj', 550804], ['Liberecký kraj', 440636], ['Moravskoslezský kraj', 1209879], ['Olomoucký kraj', 633925], ['Pardubický kraj', 517087], ['Plzeňský kraj', 578629], ['Středočeský kraj', 1338982], ['Ústecký kraj', 821377], ['Zlínský kraj', 583698]]
hlasy_celkem = [sum (x) for x in hlasy]
hlasy_celkem

#[734717, 230829, 617705, 163324, 230910, 208240, 230368, 346487, 323858, 242661, 122031, 496111, 484124, 328708]
volici = [x[1] for x in kraje2]
volici
#[1280508, 638782, 1178812, 296749, 508952, 550804, 440636, 1209879, 633925, 517087, 578629, 1338982, 821377, 583698]

#round(hlasy_celkem[0]/ volici[0] * 100,2)
57.38

[(hlasy_celkem[cislo_kraje] / volici[cislo_kraje] * 100)> 50  for cislo_kraje in range (0,14)]
#[True, False, True, True, False, False, True, False, True, False, False, False, True, True]


###########################
# ukol 6 v povinnem ukolu


seznam = [1,2,3,4,5]
[x for x in seznam] # [1,2,3,4,5]
[[x] for x in seznam] # [[1],[2],[3],[4],[5]]
[[x,x+1] for x in seznam] # [[1,2],[2,3],[3,4],[4,5],[5,6]]


#############################


#chroustani chroustani

cisilka = [["prvni RaDeK", 1, 2, 3, 4],
           ["DRuHy radek", 5, 6, 7, 8],
           ["TRETi RADEK", 9 ,10, 11, 12],
           ["CtvRTy Radek", 13, 14, 15, 16]]


sloupec1 = [sloupec[1] for sloupec in cisilka]

print([ [ sum(radek[1:]) , radek[0].upper() ] for radek in cisilka])


#############################
# scitani sloupcu a radku
cisla = [[1,1,1,1],
        [2,2,2,2],
        [3,3,3,3],
        [4,4,4,4]]


#pripadne jde takhle [sum(cisla[i]) for i in range(len(cisla)) ]
soucet_radky =       [sum(radek) for radek in cisla]
soucet_sloupce = [sum([cisla[i][j] for i in range(len(cisla))]) for j in range(len(cisla[0]))]


##############################
# dalsi zajimavy priklad

matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)

