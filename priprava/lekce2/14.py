import sys
word = sys.argv[1]
text = word.split('_')
capital1 = [text[0]] + [cap.capitalize() for cap in text[1:]]
capital2 = [text[0]] + [str(cap[0].upper()) + cap[1:] for cap in text[1:]]
answer1 = ''.join(capital1)
answer2 = ''.join(capital2)
print(answer1)
print(answer2)