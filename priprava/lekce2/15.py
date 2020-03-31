import sys

# Predpoklada male pismeno na zacatku -- sys.argv[1] == "velbloudHoniHada".
camel = sys.argv[1]
upper_indices = [0] + [i for i in range(len(camel)) if camel[i].isupper()] + [len(camel)]
snake = "_".join([camel[upper_indices[i]:upper_indices[i + 1]]for i in range(len(upper_indices) - 1)]).lower() 
print(snake)


pos = [i for i, e in enumerate (camel+'A') if e.isupper()]
parts = [camel[pos[j]:pos[j+1]] for j in range(len(pos)-1)]
answer = ('_'.join(parts)).lower()
print(answer)


s = 'velbloudHoniHada'
print([c for c in s])
result = "".join(["_" +c.lower() if c.isupper() else c for c in s])
print(result)


s = 'velbloudHoniHada'
print([c for c in s])
result = "".join([[c,"_" +c.lower()][c.isupper()] for c in s])
print(result)
