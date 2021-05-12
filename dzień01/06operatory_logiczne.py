# and, or, not
print(f"{True and False}")
print(f"{True or False}")
print(f"{not True}")

#zadanie
liczba = int(input("podaj_liczbę: "))
nieparzysta = liczba % 2 != 0
podzielna = liczba % 3 == 0
większa = liczba > 10
siedem = liczba == 7
print(f"{nieparzysta and podzielna and większa or siedem}")  #ANDy mają większy priorytet niż ORy więc nie potrzeba nawiasów



