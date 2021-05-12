#3. Napisz funkcję, która zwróci liczbę inwersji w podanej liście liczb.
#https://pl.wikipedia.org/wiki/Inwersja_(kombinatoryka)

#Zrobiłem tak, ale to jest źle bo inwersje nie muszą być obok siebie (tutaj liczy 2 a są 3 inwersje)
def invers(lista):
    counter = 0
    for i in range(1,len(lista)):
        if lista[i-1] > lista[i]:
            counter += 1
    print(counter)

print(invers([3,2,1]))

# Tak jest ok:

def inwersja(lista):
    licznik = 0
    for i in range(len(lista)): # nie 'in lista' bo etedy by nie brał ostatniego elementu
        for j in range(i + 1,len(lista)):
            if lista[i] > lista[j]:
                licznik += 1
    return licznik

print(inwersja([3,2,1]))
