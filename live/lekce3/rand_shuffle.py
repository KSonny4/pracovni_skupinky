import random
seznam = [1,2,3,4,5,6]
random.shuffle(seznam)

#print(seznam)


x = ["kral","eso","dama"]
print(x)

# vyberu prvek
prvek1 = random.choice(x)
print(prvek1)

# najdu kde je prvek v listu x
index_prvek1 = x.index(prvek1)

# vymazu prvek v listu x na pozici index_prvek1
del x[index_prvek1]

print(x)