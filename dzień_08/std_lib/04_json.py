#zadanie

import json
while True:

    with open("baza.json") as plik:
        obiekt = json.load(plik)

    inp = input("co chcesz zrobić? d/w")
    pracownik = []

    if inp == "d":
        pracownik.append(input("Imię: "))
        pracownik.append(input("Nazwisko: "))
        pracownik.append(input("data urodzenia: "))
        pracownik.append(input("Pensja: "))

        obiekt.append(pracownik)

        with open("baza.json", 'w') as plik:
            json.dump(obiekt, plik)

    elif inp == "w":
        with open("baza.json") as plik:
            obiekt = json.load(plik)
        for i in obiekt:
            print(i)

