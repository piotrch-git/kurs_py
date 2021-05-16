import json
obiekt = {"bool":True, "int":5, "float":3.14, "lista":[10, 'ala', None], "slownik": {}}
napis = json.dumps(obiekt)
print(napis)
print(type(napis))

x = json.loads(napis)
print(x)
print(type(x))
x["bool"] = False
print(x)

with open("costam.json", 'w') as plik:  #otwieramy nowy plik jsonowy
    json.dump(x, plik)  #zapisujemy x w 'plik'

napis = json.dumps(x)
print(napis)

# json mapping:
# dict -> object
# list, tuple -> array
# str -> string
# int, fload.. -> number
# ...
