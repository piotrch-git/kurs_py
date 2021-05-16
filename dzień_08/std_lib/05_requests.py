from urllib.request import urlopen
import json

with urlopen("http://api.nbp.pl/api/cenyzlota?format=json") as plik:
    obiekt = json.loads(plik.read())

print(obiekt)
slownik = obiekt[0]
print(f"cena złota na dzień {slownik['data']} wynosi {slownik['cena']} PLN/g")


#zadanie
city = "warsaw"

with urlopen(f"https://www.metaweather.com/api/location/search/?query={city}") as plik:
    obiekt = json.loads(plik.read())
    a = (obiekt[0])
    woeid = (a['woeid'])
    print(woeid)

with urlopen(f"https://www.metaweather.com/api/location/{woeid}/") as plik:
    obiekt = json.loads(plik.read())
    print(obiekt)

    weather = (obiekt['consolidated_weather'])
    print(f"{weather[0]['applicable_date']},max temp: {weather[0]['max_temp']}")
    print(f"{weather[1]['applicable_date']},max temp: {weather[1]['max_temp']}")
    print(f"{weather[2]['applicable_date']},max temp: {weather[2]['max_temp']}")
    print(f"{weather[3]['applicable_date']},max temp: {weather[3]['max_temp']}")
    print(f"{weather[4]['applicable_date']},max temp: {weather[4]['max_temp']}")

#omówienie

lokacja = input("podaj lokację: ")
with urlopen(f"https://www.metaweather.com/api/location/search/?query={lokacja}") as plik:
    lista = json.loads(plik.read())
print(lista)
woeid = lista[0]['woeid']
print(woeid)

with urlopen(f"https://www.metaweather.com/api/location/{woeid}/") as plik:
    slownik = json.loads(plik.read())

for prognoza in slownik['consolidated_weather']:
    print(f"{prognoza['applicable_date']}: temp = {prognoza['the_temp']:.1f}")

