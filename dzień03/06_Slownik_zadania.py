
#Zadanie10 zliczanie liczy wystepowań znaków w napisie
napis = input("podaj napis: ")
wystapienia = {}
for litera in napis:
    if litera in wystapienia:
        wystapienia[litera] += 1 # litera już była w słowniku
    else:
        wystapienia[litera] = 1 # to jest pierwsze wystąpienie litery
print(wystapienia)



####################################
# Zadanie : sklep

produkty= {"marchewki":10, "kapusta":10, "jabłka":30}

print (f"dostępne są: ")
for produkt, cena in produkty.items():
    print(produkt,cena)
print()

towar = input("podaj towar").lower() #lower żeby działał bez wzglądu na wielkosc liter

if towar not in produkty:
    print("nie ma takiego produktu")
else:
    waga = float(input("podaj wagę"))
    naleznosc = produkty[towar] * waga
    print(f"należność: {naleznosc:.2f}")