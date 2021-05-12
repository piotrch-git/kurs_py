#zbiór (set) - nieuporządkowana kolekcja elementów o szybkim czasie wstawienia/usunięcia/sprawdzenia czy element istnieje
#zbiór przechowuje tylko unikalne element (bez powtórzeń), i w zupełnie losowej kolejności
zbior = {1, 2, 3, 3, 3}
print(type(zbior))
print(zbior)
pusty = set() # nie można inaczej tworzyć pustego zbioru, bo '{}' tworzy pusty slownik
print(pusty)

podzielne = set()
for i in range(20):
    if i % 2 == 0:
        podzielne.add(i)    # a nie append tak jak w listach.
print(podzielne)

print(f"{6 in podzielne=}")
podzielne.remove(6)
print(f"{6 in podzielne=}")
print(podzielne)

print(len(set("ala ma kota")))  # ile różnych znaków jest w napisie 'ala ma kota, bo to jest zbiór

A = {1,2,3,4}
B = {3,4,5,6}
print(f"{A=}")
print(f"{B=}")
print(f"{A | B=}") # suma zbiorów - wszystkie elementy z A i B
print(f"{A - B=}") # różnica rbiorów - wszystko z A co nie należy do B
print(f"{A & B=}") # iloczyn zbiorów - część wspólna z A i B
print(f"{A ^ B=}") # różnica symetryczna - elementy z A i B oprócz części wspólnej
print(f"{A - B | B - A=}") # to samo co A ^ B
print(f"{A.issuperset({1,3})=}")

#zadanie11
podane = set()
while True:
    napis = input("podaj liczbę lub 'stop': ")
    if napis == "koniec":
        break
    liczba = int(napis)
    podane.add(liczba)

print(podane)
print(len(podane))

#parzyste = set()
#for i in range(101):
#    if i % 2 == 0:
#        parzyste.add(i)

# Bardziej optymalne tworzenie listy parzystych iczb:  !!!!!!!!!!!!!!!!!!
parzyste = set(range(0, 101, 2))  # Range jest iterowalne więc można zrobić zbiór bezpośrednio
print(parzyste)

print(f"{podane & parzyste=}")
print(f"{len(podane & parzyste)=}")