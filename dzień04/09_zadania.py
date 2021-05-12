# znaki są warte 0. Każdy inny jest tyle w ilu parach nawiasow sie znajduje
#napis = 'ala ma <kota> a <kot <ma a>le>'
#         000000001111000001111122221110
#opcjonalne 2 argumenty dla zmiany nawiasow ostrych na inne znaki

def licznik(napis,znak1='<',znak2='>'):
    licznik = 0
    cena = 0
    for znak in napis:
        if znak == znak1:
            cena += 1
        elif znak == znak2:
            cena -= 1
        else:
            licznik += cena
    return(licznik)

print(licznik("[a]la [[ma]] <<kota>> a kot ma ale","[","]"))


#Zad funkcja licząca silnię - implementacja iteracyjna

def silnia(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i              #!!!!!!!!!! taki myk
    return wynik

for i in range(10):
    print(f"silnia({i}) = {silnia(i)}")

#funkcja licząca silnię - implementacja rekurencyjna (bez fora, tylko funkcja wykonuje samą siebie)  !!!!!
def silnia2(n):
    if n == 0:
        return 1
    return n * silnia(n-1)

for i in range(10):
    print(f"silnia({i}) = {silnia2(i)}")


## Zad napisz funkcję fin(n) generującą n-tą liczbę fibonachiego

def fib(n):
#najpierw przypadki brzegowe:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)      # to jest OK ale nie optymalnie, wiele wykonań fib jest dublowanych
# To dowód że podejście rekurencyjne nie zawsze jest najlepsze. Tutaj lepiej iteracyjnie.

print(f"{fib(5) = }")

