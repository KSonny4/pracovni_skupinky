# 8
import sys
import math

print(math.floor(float((sys.argv[1]))+0.5))

print(int(cislo+0.5))



# 14

import sys
word = sys.argv[1]
text = word.split('_')
capital = [ str(cap[0]) + cap[1:]  for cap in text]
answer = ''.join(capital)
print(answer)

import sys
word = sys.argv[1]
text = word.split('_')
capital = [cap.capitalize() for cap in text]
answer = ''.join(capital)
print(answer)

# 15