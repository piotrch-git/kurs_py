#0. Napisz funkcję, która sprawdzi czy podana lista jest posortowana rosnąco.

#1. Napisz funkcję, która policzy n-tą liczbę Fibonacciego iteracyjnie (bez rekurencji)

#2. Napisz funkcję, która sprawdzi czy podana liczba jest liczbą doskonałą.
#https://pl.wikipedia.org/wiki/Liczba_doskona%C5%82a
#{\displaystyle 6=3+2+1.} Następną jest 28 ponieważ 28=14+7+4+2+1

#3. Napisz funkcję, która zwróci liczbę inwersji w podanej liście liczb.
#https://pl.wikipedia.org/wiki/Inwersja_(kombinatoryka)

#4. Napisz funkcję, która posortuje podaną listę algorytmem sortowania przez wybieranie
#https://pl.wikipedia.org/wiki/Sortowanie_przez_wybieranie

#5. Napisz funkcję, która posortuje podaną listę algorytmem sortowania bąbelkowego
#https://pl.wikipedia.org/wiki/Sortowanie_b%C4%85belkowe

#6. Napisz funkcję, która sprawdzi czy podany napis jest poprawnym wyrażeniem nawiasowym (wyjaśnienie niżej). Zakładamy, że napis zawiera tylko znaki '(' i ')'. (podobną rzecz robiliśmy w zadaniu 3 z funkcji)

#*7. Napisz funkcję, która posortuje podaną listę liczb za pomocą algorytmu quicksort (https://pl.wikipedia.org/wiki/Sortowanie_szybkie - w skrócie: wybieramy dowolny element(może być losowy) i tworzymy listę elementów mniejszych od niego i listę większych(można wykorzystać wyrażenia listowe), a następnie sortujemy obie algorytmem quicksort (rekurencja ;) ) i sklejamy wynik: mniejsze + wybrany element + większe)

#*8. Napisz funkcję, która sprawdzi czy podany napis jest wyrażeniem nawiasowym. Tym razem napis może zawierać dowolne nawiasy (tj. okrągłe '()', kwadratowe '[]', klamrowe '{}' oraz ostre '<>'). Oczywiście nawias zamykający zamyka tylko odpowiadający mu nawias otwierający, tzn. '[)' *nie* jest poprawnym wyrażeniem, ale '[(){<>}]' jest. (hint do zadania: https://pl.wikipedia.org/wiki/Stos_(informatyka) - może się przydać listowa metoda pop())

#WYRAŻENIA NAWIASOWE
#Wyrażenie nawiasowe definiujemy następująco:
#- pusty napis jest poprawnym wyrażeniem nawiasowym
#- jeżeli "A" i "B" są poprawnymi wyrażeniami nawiasowymi to napis "AB" też jest
#- jeżeli "A" jest poprawnym wyrażeniem nawiasowym to napis "(A)" też jest
#Oznacza to, że poprawnymi wyrażeniami są np. '()', '(())', '()()', '(()())()()'
#Przykładowe niepoprawne wyrażenia to: '(', '())', '((())))', '())((())'

#6
napis = input(f"podaj wyrażenie nawiasowe: ")

def sprawdzacz(napis):
    otwarte = 0
    zamkniete = 0
    for n in napis:
        if n == '(':
            otwarte += 1
        if n == ')':
            zamkniete += 1
    return otwarte == zamkniete
print(f"wyrażenie jest prawidlowe: {sprawdzacz(napis)}")

#4  ####### sortowanie przez wybieranie nie działa
lista=[]
n = None
while True:
    n = input('podaj liczbę lub "koniec": ')
    if n == 'koniec':
        break
    lista.append(int(n))
print(f"lista przed sortowaniem:{lista}")
def sort(lista):
    start = 1
    while start < len(lista):
        for n in range (start,len(lista)):
            if lista[n-1]>lista[n]:
                min = lista[n]
                imin = lista.index(min)
        temp = lista[start]
        lista[start]=min
        lista[imin]=temp
        start += 1
    return lista
print(f"lista po sortowaniu: {sort(lista)}")


#5  ####### działa - bąbelkowo
lista=[]
n = None
while True:
    n = input('podaj liczbę lub "koniec": ')
    if n == 'koniec':
        break
    lista.append(int(n))
print(f"lista przed sortowaniem:{lista}")
def sort(lista):
    n = 1
    while n < len(lista):
        if lista[n-1] > lista[n]:
            temp = lista[n]
            lista[n] = lista[n-1]
            lista[n-1] = temp
            n = 0
        n += 1
    return lista
print(f"lista po sortowaniu: {sort(lista)}")



#0 ################## Działa

def sort_check(a,b,c,d,e,f,g,h):
    lista = [a,b,c,d,e,f,g,h]
    for n in range (0,7):
        print(lista[n])
        print(lista[n+1])
        if lista[n] > lista[n+1]:
            return False
    return True

print(sort_check(0,0,0,0,0,1,0,12))

#1 ################# działa

def fib(n):  # 0 1 1 2 3 5 8 13 21 34 55 89
#najpierw przypadki brzegowe:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    i = 0
    f_a = 0
    f_b = 1
    while i < n-2:
        f_n = f_a + f_b
        f_a = f_b
        f_b = f_n
        i += 1
    return f_n

print(f"{fib(12)=}")

#2 ################# działa


def perfect(n):
    dzielnik = 1
    sum = 0
    while dzielnik < n:
        if n % dzielnik == 0:
            sum = sum + dzielnik
        dzielnik += 1
    if sum == n:
        return True
    else:
        return False

print(f"{perfect(28)=}")

#3  ####### działa
lista=[]
n = None
while True:
    n = input('podaj liczbę lub "koniec": ')
    if n == 'koniec':
        break
    lista.append(int(n))
print(lista)
def invers(lista):
    counter = 0
    for i in range(1,len(lista)):
        if lista[i-1] > lista[i]:
            counter += 1
    print(counter)
invers(lista)