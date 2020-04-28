data = open("studenti.txt","r", encoding='utf-8')

students = [row for row in data]

data.close()

#print(students)

print("--------------------")

prvni_radek = students[0]


split1 = [row.strip().split('\t') for row in students][1:]
#print(split1)

nova_tabulka = []

for row in split1:
    vek = 2020 - int('19'+row[2][:2])
    #print(vek)
    row.append(str(vek))


print(split1)

#print("=======================================")


prvni_radek = students[0].split()

#print(prvni_radek)

jmeno = prvni_radek[0]
prijmeni = prvni_radek[1]
rodne_cislo = prvni_radek[2] + " " +prvni_radek[3]

#print(f"{jmeno} {prijmeni} {rodne_cislo} ")
list_of_dictionaries = []
for row in split1:
    dictionary = {jmeno:row[0], prijmeni:row[1], rodne_cislo:row[2]}
    list_of_dictionaries.append(dictionary)


#print("//////////////////////")

#print(list_of_dictionaries)