
#### Zad: Napisz funkcję zaaplikuj(f, lista), która zwróci listę będącą wynikami funkcji f() wywołanej dla wszystkich elementów listy
# [a, b, b]  -> [f(a), f(b), f(c)]
#zaaplikuj(dodaj10, [1,2,3,4]) == [11,12,13,14]

def zaaplikuj(f, lista):
    wynik = []
    for x in lista:
        wynik.append(f(x))
    return wynik
    # return [f(x) for x in lista]      #listowo

def dodaj10(x):
    return x + 10

print(zaaplikuj(dodaj10, [1,2,3]))