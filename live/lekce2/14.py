import sys
#had_honi_velblouda
word = sys.argv[1]
print(word)

rozdelene = word.split('_')

print("rozdelene " + str(rozdelene))

# ['Had', 'Honi', 'Velblouda']
vebloud =  "".join([rozdelene[0]] + [slovo[0].upper() + slovo[1:] for slovo in rozdelene[1:]])
print("skoro velbloud " + str(vebloud))


final_velbloud = "".join(vebloud)
print("finalni velbloud " + str(final_velbloud))

# capitalize()
slovo = 'slovicko'
print("velke slovo " + str(slovo.capitalize()))

vebloud2 =  "".join([rozdelene[0]] + [slovo.capitalize() for slovo in rozdelene[1:]])
print("velbloud2 " + str(vebloud2))


#hadHoniVelblouda



