# Spojeni dvou listu

listone = [1,2,3]
listtwo = [4,5,6]

joinedlist = listone + listtwo


listone = [1,2,3]
listtwo = [4,5,6]
mergedlist = []
mergedlist.extend(listone)
mergedlist.extend(listtwo)


seznam = [1,2,3,4,5]
[x for x in seznam] # [1,2,3,4,5]
[[x] for x in seznam] # [[1],[2],[3],[4],[5]]
[[x,x+1] for x in seznam] # [[1,2],[2,3],[3,4],[4,5],[5,6]]



#############################

# pouziti int()

listlist = ["1",'2',3, 3.14]

# pokud bych chtel zachovat desetinne cisla, musel bych u posledniho
# prvku listlist pouzit float()
list_cisel = [int(cislo) for cislo in listlist]


#############################






#chroustani chroustani

cisilka = [["prvni RaDeK", 1, 2, 3, 4],
           ["DRuHy radek", 5, 6, 7, 8],
           ["TRETi RADEK", 9 ,10, 11, 12],
           ["CtvRTy Radek", 13, 14, 15, 16]]


sloupec1 = [sloupec[1] for sloupec in cisilka]

print([ [ sum(radek[1:]) , radek[0].upper() ] for radek in cisilka])


#############################

cisla = [[1,1,1,1],
        [2,2,2,2],
        [3,3,3,3],
        [4,4,4,4]]


#              [sum(cisla[i]) for i in range(len(cisla)) ]
soucet_radky = [sum(radek) for radek in cisla]

soucet_sloupce = [sum([cisla[i][j] for i in range(len(cisla))]) for j in range(len(cisla[0]))]


#############################

matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)


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
igor =  sum( [igor[0] for igor in hlasy])
augustin = sum( [igor[0] for augustin in hlasy])
vladan = sum( [vladan[2] for vladan in hlasy])
ondrej = sum( [ondrej[3] for ondrej in hlasy])
radim = sum( [radim[4] for radim in hlasy])

kandidati = [sum([radek[i] for radek in hlasy]) for i in [0,1,2,3,4]]


12.b) Který kandidát vyhrál první kolo voleb
#>>> igor, radim, ondrej, vladan, augustin
#(1296501, 791656, 996101, 909361, 766454)
max(igor, radim, ondrej, vladan, augustin)


1296501
12.c) Ve kterých krajích byla nejvyšší a nejnižší volební účast
>>> Praha =sum(hlasy[0])
>>> J_k= sum(hlasy[1])
>>> J_m_k= sum(hlasy[2])
>>> K_k = sum(hlasy[3]) # atd.
12.d) Vytvořte tabulku, která ukazuje který kandidát vyhrál v kterém kraji.
>>> [max(kandidat) for kandidat in hlasy]
[242854, 91062, 216499, 64737, 85730, 118755, 81181, 112578, 171064, 101680, 40228, 241122, 200997, 177272]
>>> jmena = ['igor', 'augustin', 'vladan', 'ondrej', ' radim']
>>> pozice = [kraj.index(max(kraj)) for kraj in hlasy]
>>> [jmena [p] for p in pozice]
[' radim', 'igor', 'augustin', 'ondrej', 'augustin', 'igor', 'vladan', ' radim', 'igor', 'augustin', ' radim', 'vladan', 'vladan', 'ondrej']
12.e) Využijte tabulku počtů obyvatel v krajích a vytvořte tabulku podobnou té z tohoto cvičení, která místo čísel bude obsahovat kolik procent hlasů získal každý kandidát v daném kraji.
>>> [[x[0], int(''.join(x[1].split()))] for x in kraje]
[['Hlavní město Praha', 1280508], ['Jihočeský kraj', 638782], ['Jihomoravský kraj', 1178812], ['Karlovarský kraj', 296749], ['Kraj Vysočina', 508952], ['Královéhradecký kraj', 550804], ['Liberecký kraj', 440636], ['Moravskoslezský kraj', 1209879], ['Olomoucký kraj', 633925], ['Pardubický kraj', 517087], ['Plzeňský kraj', 578629], ['Středočeský kraj', 1338982], ['Ústecký kraj', 821377], ['Zlínský kraj', 583698]]
>>> soucty = [sum (x) for x in hlasy]
>>> soucty
[734717, 230829, 617705, 163324, 230910, 208240, 230368, 346487, 323858, 242661, 122031, 496111, 484124, 328708]
>>> volici = [x[1] for x in kraje]
>>> volici
['1 280 508', '638 782', '1 178 812', '296 749', '508 952', '550 804', '440 636', '1 209 879', '633 925', '517 087', '578 629', '1 338 982', '821 377', '583 698']
>>> [soucty[cislo_kraje]/volici[cislo_kraje] for cislo_kraje in range(0,14)]
>>> kraj = hlasy[0]
>>> kraj
[78774, 43179, 225111, 144799, 242854]
>>> kraj[0] / sum(kraj) * 100
10.721679231595296
>>> kraj[1] / sum(kraj) * 100
5.876956705779232
>>> kraj[2] / sum(kraj) * 100
30.63914405138305 # atd.
12.f) Vytvořte seznam pravdivostních hodnot, který bude říkat ve kterých krajích překročila voleb
>>> kraje = [[x[0] , int (''.join(x[1].split()))] for x in kraje]
>>> kraje
[['Hlavní město Praha', 1280508], ['Jihočeský kraj', 638782], ['Jihomoravský kraj', 1178812], ['Karlovarský kraj', 296749], ['Kraj Vysočina', 508952], ['Královéhradecký kraj', 550804], ['Liberecký kraj', 440636], ['Moravskoslezský kraj', 1209879], ['Olomoucký kraj', 633925], ['Pardubický kraj', 517087], ['Plzeňský kraj', 578629], ['Středočeský kraj', 1338982], ['Ústecký kraj', 821377], ['Zlínský kraj', 583698]]
>>> hlasy_celkem = [sum (x) for x in hlasy]
>>> hlasy_celkem
[734717, 230829, 617705, 163324, 230910, 208240, 230368, 346487, 323858, 242661, 122031, 496111, 484124, 328708]
>>> volici = [x[1] for x in kraje]
>>> volici
[1280508, 638782, 1178812, 296749, 508952, 550804, 440636, 1209879, 633925, 517087, 578629, 1338982, 821377, 583698]
>>> round(hlasy_celkem[0]/ volici[0] * 100,2)
57.38
>>> [round(hlasy_celkem[0]/ volici[0] * 100,2) for cislo_kraje in range (0,14)
... ]
[57.38, 57.38, 57.38, 57.38, 57.38, 57.38, 57.38, 57.38, 57.38, 57.38, 57.38, 57.38, 57.38, 57.38]
>>> [(hlasy_celkem[cislo_kraje]/ volici[cislo_kraje] * 100)> 50  for cislo_kraje in range (0,14)]
[True, False, True, True, False, False, True, False, True, False, False, False, True, True]
