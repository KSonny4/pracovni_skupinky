import requests
import json
import sys
#python3 5b.py 01 12

den = sys.argv[1]
mesic = sys.argv[2]

address = 'http://svatky.adresa.info/json?date=' + den + mesic

request = requests.get(address)

print(f'request {request.text}')

#chroustani_textu = [x for x in request.text]
#print( chroustani_textu)

names = json.loads(request.text)

print([x['name'] for x in names])