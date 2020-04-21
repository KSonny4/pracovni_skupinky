#http://svatky.adresa.info/json

import requests
import json

adress = 'http://svatky.adresa.info/json'

request = requests.get(adress)
print(request.text)

odpoved = json.loads(request.text)
print(f" json loads: {odpoved}")

print(f" json nulty prvek: {odpoved[0]}")

print(f" json nulty prvek jmeno: {odpoved[0]['name']}")

print("=====================")

response = requests.get("http://svatky.adresa.info/json")
print(response)
svatek = json.loads(response.text)

#Kdo ma dnes svatek
jmeno = [x['name'] for x in svatek]
print(jmeno)
print("Svatek ma dnes: " + str(jmeno))


5b