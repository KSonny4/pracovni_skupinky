import sys
jmeno = sys.argv[1]
heslo = sys.argv[2]
spravne_jmeno = ["peta","verca"]
spravne_heslo = ["python","sql"]


for index in range(len(spravne_heslo)):
    
    print(f"uzivatel: {spravne_jmeno[index]} heslo: {spravne_heslo[index]}")
    
    if jmeno == spravne_jmeno[index] and heslo == spravne_heslo[index]:
        print("Je v databazi")
        exit()

print("Neni v databazi")
    