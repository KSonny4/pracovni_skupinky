import sys

# Predpoklada male pismeno na zacatku -- sys.argv[1] == "velbloudHoniHada".
camel = sys.argv[1]
upper_indices = [0] + [i for i in range(len(camel)) if camel[i].isupper()] + [len(camel)]
snake = "_".join([camel[upper_indices[i]:upper_indices[i + 1]].lower() for i in range(len(upper_indices) - 1)])

print(snake)
