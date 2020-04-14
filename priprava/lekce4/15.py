#https://stackoverflow.com/questions/11964450/python-order-a-list-of-numbers-without-built-in-sort-min-max-function
#https://en.wikipedia.org/wiki/Bogosort
#https://github.com/gustavo-depaula/stalin-sort


import sys

cislo = int(sys.argv[1])
data = sys.argv[2:]
data_list = [int(x) for x in data]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print(new_list[-cislo])