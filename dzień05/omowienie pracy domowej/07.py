
#*7. Napisz funkcję, która posortuje podaną listę liczb za pomocą algorytmu quicksort (https://pl.wikipedia.org/wiki/Sortowanie_szybkie - w skrócie: wybieramy dowolny element(może być losowy) i tworzymy listę elementów mniejszych od niego i listę większych(można wykorzystać wyrażenia listowe), a następnie sortujemy obie algorytmem quicksort (rekurencja ;) ) i sklejamy wynik: mniejsze + wybrany element + większe)
def quicksort(lista):
    if lista == []:
        return []
    wybrany = lista[0]
    mniejsze = [x for x in lista if x < wybrany]        # tutaj koszt liniowy
    rowne = [x for x in lista if x == wybrany]          # koszt liniowy
    wieksze = [x for x in lista if x > wybrany]         # koszt liniowy
    return quicksort(mniejsze) + rowne + quicksort(wieksze)

print(quicksort([5,1,8,44,2,0]))

