# Range przyjmuje tylko wartości całkowite (bez floatów!)
# zakres w rangu jest lewostronnie zamknięty i lewostronnie otwarty  (0,10) - to liczy od 0 do 9. 

lista = [10, 20, 30, 1, 2, 3]
for element in lista:
    print(element)

for x in lista[:3]: # od początku do trzeciego włącznie
    print(x)

# range nie jest listą
x = range(10)
print (x)
print(type(x))
print(list(range(3, 10, 2))) # od 3 do 10 co 2


#zadanie #3
dodatnie = 0
ujemne = 0
lista = [1, 3, -4, -1, 0]
for x in lista:
    if x > 0:
        dodatnie += 1
    elif x < 0:
        ujemne += 1

print(f"ilość licz dodatnich: {dodatnie}")
print(f"ilość licz ujemnych: {ujemne}")

#zadanie
#podejście 1:

for x in range (1, 101):
    if (x % 3 == 0) and (x % 5 == 0):
        print("HopsasaTralala")
    elif x % 3 == 0:
        print("Hopsasa")
    elif x % 5 == 0:
        print("Tralala")
    else:
        print (x)

# podejście 2, bardziej optymalne:
#dodatkowy warunek: przy podzielnych przez 7 wypisz Buu

print ("lepsze podejście")
for i in range (1, 101):
    if i % 3 == 0:
        print("Hopsasa", end="")
    if i % 5 == 0:
        print("Tralala", end="")
    if i % 7 == 0:
        print("Buu", end="")

    if i % 3 != 0 and i % 5 != 0 and i % 7 == 0:
        print(i, end="")
    print()


# podejście 3, jeszcze bardziej optymalne:

print ("lepsze podejście")
for i in range (1, 101):
    czy_cos_wypisalismy = False
    if i % 3 == 0:
        print("Hopsasa", end="")
        czy_cos_wypisalismy = True
    if i % 5 == 0:
        print("Tralala", end="")
        czy_cos_wypisalismy = True
    if i % 7 == 0:
        print("Buu", end="")
        czy_cos_wypisalismy = True

    if not czy_cos_wypisalismy:
        print(i, end="")

    print()

