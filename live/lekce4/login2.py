import sys
jmeno = sys.argv[1]
heslo = sys.argv[2]


def je_v_databazi(jmeno,heslo):
    spravne_jmeno = ["peta","verca"]
    spravne_heslo = ["python","sql"]

    for index in range(len(spravne_heslo)):               
        if jmeno == spravne_jmeno[index] and heslo == spravne_heslo[index]:
            return True
    
    return False

odpoved = je_v_databazi(jmeno,heslo)


if odpoved == True:
    print("Vitej uzivateli")
else:
    print("spatne")



def je_v_databazi_jine_funkce(jmeno,heslo):
    spravne_jmeno = ["peta","verca"]
    spravne_heslo = ["python","sql"]

    for index in range(len(spravne_heslo)):               
        if jmeno == spravne_jmeno[index] and heslo == spravne_heslo[index]:
            return "Vitej uzivateli"
    
    return "Sorry, spatnej login a heslo"

print(je_v_databazi_jine_funkce(jmeno,heslo))



def minimum(a,b):
    if a < b:
        return a
    else:
        return b

print(minimum(2,3))



    