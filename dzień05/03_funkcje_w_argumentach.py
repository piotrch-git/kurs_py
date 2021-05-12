def fun():
    print("asdf")

x = fun #przypisujemy alias do funkcji
x() #to samo co wywołanie fun()
fun()

def wykonaj(f,x):   #przyjmuję funkcje f, argument x i wykonuje f(x)
    print("uwaga wywołuję f")
    f(x) #wypisz_arg(20)

def wypisz_arg(x):
    print("Argument to", x)

wykonaj(wypisz_arg, 20)

wykonaj(print, "Ala ma kota")

## Zadanie: napisz funkcję wybierz(f, lista), która zwróci listę elementów z 'lista', dla których f() zwraca True.
# Przykłady:
# wybierz(czy podzielne_przez_2, [1,2,3,4,5,6])  -> to ma zwrócić [2,4,6]
# wybierz(czy podzielne_przez_3, [1,2,3,4,5,6])  -> to ma zwrócić [3,6]

def wybierz(f, lista):
    wynik = []
    for x in lista:
        if f(x):
            wynik.append(x)
    return wynik

def czy_podzielne_przez_2(x):
    return x % 2 == 0

def czy_podzielne_przez_3(x):
    return x % 3 == 0


def wybierz2(lista):
    wynik = []
    for x in lista:
        if czy_podzielne_przez_2(x):
            wynik.append(x)
    return wynik

lista = [1,2,3,4,5,6,8,12]
print(wybierz2(lista))
print(f"{wybierz(czy_podzielne_przez_2, lista) = }")
print(f"{wybierz(czy_podzielne_przez_3, lista) = }")

