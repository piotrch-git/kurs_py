lista = []
for i in range(10):
    lista.append(i ** 2)
print(lista)

lista_2 = [i ** 2 for i in range(10)]   # adekwatne list comprehension - wyrażenie listowe
print(lista_2)


###################
slownik = {}
for x in lista_2:
    slownik[x] = x ** 2

slownik = {x: x ** 2 for x in lista_2}  # adekwatne list comprehension
print(slownik)

###################
czary = print([int(input("Daj liczbę: ")) for i in range(3)])

print([x * y for x in range(5) for y in range(5)])
##############################

podzielne = []
for i in range(20):
    if i % 3 == 0 or i % 5 == 0:
        podzielne.append(i)

podzielne = [i for i in range(20) if i % 3 == 0 or i % 5 == 0]  # adekwatny fizzbuzz
print(podzielne)

