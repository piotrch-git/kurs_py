#Zadanie 2  # działa ok, DO zrozumienia PRZEANALIZOWANIA
def liczba_wystapien(napis):
    wystapienia = {}
    for litera in napis:
        if litera in wystapienia:
            wystapienia[litera] += 1
        else:
            wystapienia[litera] = 1
    return wystapienia

def wiecej_niz(napis, n):
    w = liczba_wystapien(napis)
    zbior = set()
    for klucz, wartosc in w.items():
        if wartosc > n:
            zbior.add(klucz)
    return zbior

# to samo w formie listowej
def wiecej_niz2(napis,n):
    return {k for k, v in liczba_wystapien(napis).items() if v > n}

print(wiecej_niz("ala ma kota a kot ma ale", 1))

