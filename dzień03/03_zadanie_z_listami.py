lista = [2,3,4,3,5,1]

print(f"{2 in lista=}") # in odpowiada na pytanie czy taki element znajduje się w liście

indeks = 0
for i in range(1, len(lista)):  # nie 'in lista' bo ma iterować po indeksach, a nie po wartościach
    if lista[i] > lista[indeks]:
        indeks = i

lista[indeks] = -1000
print(lista)


############################################
#zadanie 6
print("zadanie6")

lista = [3,3,4,3,5,11,2]

i_min = 0
i_max = 0
for i in range(1, len(lista)):  # nie 'in lista' bo ma iterować po indeksach, a nie po wartościach
    if lista[i] > lista[indeks]:
        i_max = i

    if lista[i] < lista[indeks]:
        i_min = i

print(f"{i_min=}")
print(f"{i_max=}")

# podmiana z użycem zmiennej pomocniczej_

tmp = lista[i_max]  # zmienna pomocnicza
lista[i_max] = lista[i_min]
lista[i_min] = tmp

#podmiana z użyciem przypisania tuplowego (lepsze, bardziej pythonowe)
lista[i_min], lista[i_max] = lista[i_max], lista[i_min]

print(lista)
#########################################################

print(lista.index(max(lista)))
print(lista.index(min(lista)))

####################################################

lista = [10,20,30]
for i, v in enumerate(lista):   #enumerate zwraca pary (licznik, element lista) co powoduje przypisanie licznika do i, a elementu do v
    print(i, v)