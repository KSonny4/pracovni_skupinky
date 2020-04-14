#seznam = [3,4,5,10,9,14]
seznam = [3,4,5,14,10]
print(f"puvodni seznam {seznam}")
print(f" serazeny {sorted(seznam)}")

serazeny = sorted(seznam)
if serazeny == seznam:
    print("byl vzestupne")
else:
    print("nebyl vzestupne")

# nejvyssi = 0
# for polozka in seznam:
#     if polozka > nejvyssi:
#         nejvyssi = polozka
#     else:
#         print("neni vzestupny")
#         exit()

# print("je vzestupny")

seznam = [3,4,5,14,10]

for i in range(len(seznam) - 1):
    if seznam[i] < seznam[i + 1]:
        print(f"{seznam[i]} {seznam[i+1]}")
        print("True")        
    else:
        print("False")
        exit(0)
        
