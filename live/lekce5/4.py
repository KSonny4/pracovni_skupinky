import json
import requests


people = requests.get('http://api.kodim.cz/python-data/people')

# mel bych dostat 200, cili uspech https://cs.wikipedia.org/wiki/Stavov%C3%A9_k%C3%B3dy_HTTP
print(f"HTTP kod odpoved {people}")

people_dict = json.loads(people.text)
print(f"prvni radek: {people_dict[0]}")

# a)
#people_chroustani = len([x for x in people_dict])
people_count = len(people_dict)
print(f"dostali jsme {people_count} lidi ")

# b)

person = people_dict[0]
print(f"osoba 1 {person}")

# moje advanced reseni
#person_info = person.keys()
#print(f"informace ktere mame o osobach {person_info}")



print(f"informace ktere mame o osobach {[x for x in people_dict[1]]}")

#c 

# 1. reseni
muzi = 0
zeny = 0
treti_pohlavi = 0
for x in people_dict:
    if x['gender'] == 'Male':
        muzi += 1
    elif x['gender'] == 'Female':
        # z = z + 1
        zeny += 1
    else:
        treti_pohlavi += 1

print(f"muzi {muzi} zeny {zeny} treti pohlavi {treti_pohlavi}")


# 2. reseni
men = [x for x in people_dict if x['gender'] == 'Male']
women = [x for x in people_dict  if x['gender'] == 'Female']

print(f"men {len(men)} women {len(women)}")

# 3. reseni
gender = [osoba['gender'] for osoba in people_dict]

print(gender.count('Female'))
print(gender.count('Male'))


# 4.reseni
pohlavi = [x["gender"] for x in people_dict]
print("Pocet zen je " + str(pohlavi.count("Female")) + " Pocet muzu je " + str(pohlavi.count("Male")))
print(f"Pocet zen je {pohlavi.count('Female')} Pocet muzu je {pohlavi.count('Male')} ")

a = pohlavi.count('Female')
b = pohlavi.count('Male')
print("Pocet zen je {} Pocet muzu je {}".format(a, b))
