data = ['jméno příjmení  rodné číslo']
#'jménopříjmení_rodné_číslo'

tab = data[0].split('  ')
print(tab)

tab[1] = tab[1].replace(' ', '_')
print(tab)

tab[0] = '\t'.join(tab[0].split(' '))

tab = '\t'.join(tab)
print(tab)



#prvni_radek = [x[21].replace(' ','_') for x in data]

#print(prvni_radek)