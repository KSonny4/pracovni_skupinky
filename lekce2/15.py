import sys
word = sys.argv[1]

pos = [i for i, e in enumerate (word+'A') if e.isupper()]
parts = [word[pos[j]:pos[j+1]] for j in range(len(pos)-1)]
answer = ('_'.join(parts)).lower()
print(answer)


word = sys.argv[1]
upper_indices = [0] + [i for i in range(len(word)) if word[i].isupper()] + [len(word)]
print(upper_indices)
snake = "_".join([word[upper_indices[i]:upper_indices[i + 1]].lower() for i in range(len(upper_indices) - 1)])
print(snake)