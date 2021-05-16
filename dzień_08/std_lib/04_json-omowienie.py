#omowienie:
import json

try:
    with open("pracownicy.json") as plik:       #tutaj otwieramy tylko do odczytu
        lista = json.load(plik)
except FileNotFoundError:
    lista = []

operacja = input("co robimy d/w")
if operacja == "d":
    pracownik = {}
    pracownik['imie'] = input("Imię: ")
    pracownik['nazwisko'] = input("Nazwisko: ")
    pracownik['rok_uro'] = input("Rok urodzenia: ")
    pracownik['pensja'] = input("Pensja: ")

    #słownik dodajemy do listy wczytanej na początku programu
    lista.append(pracownik)

    with open("pracownicy.json", "w") as plik:
        json.dump(lista, plik)

elif operacja == "w":

    for i, p in enumerate(lista, 1):
        print(f"[{i}] - {p['imie']} {p['nazwisko']}, rok urodzenia: {p['rok_uro']}, pensja: {p['pensja']} PLN")