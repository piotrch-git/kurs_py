#Tab - zaznaczone linijki przesuwa w prawo
#Shift + Tab - przesuwa w lewo
print("to się zawsze wypisze")
if 3 < 4:
    print("to się wypisze jak warunek jest prawdziwy")
    if 1==1:
        pass    #to nic nie robi. Umożliwia istnienie pustego bloku.
print("koniec")

x = int(input())
if x < 0:
    print("liczba mniejsza od zera")
else:
    print("liczba większa lub równa zero")

    if x < 0:
        print("liczba mniejsza od zera")
    elif x > 0:
        print("liczba większa od zera")
    else:
        print("liczba równa zero")

#zadanie
x = int(input("podaj rok urodzenia"))
rok = 2021
wiek = rok - x
if wiek >= 18:
    print("jestes pelnoletni")
else:
    print("nie jestes pelnoletni")

#zadanie2
y = int(input("podaj rok"))
if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
    print (" to jest rok przestępny")
else:
    print(" to nie jest rok przestępny")

#zadanie3

x = int(input("podaj 1 liczbę"))
y = int(input("podaj 2 liczbę"))
z = input("podaj operację: +, -, * lub /")

if z == "+":
    print(f"{x} + {y} = {x + y}")
elif z == "-":
    print(f"{x} - {y} = {x - y}")
elif z == "*":
    print(f"{x} * {y} = {x * y}")
elif z == "/":
    if y == 0:
        print ("nie dzielimy przez 0")
    else:
        print(f"{x} / {y} = {x / y}")
else:
    print("nieznane dzialanie")
#{koszt: .2f}
#print(f"{2 < 3 =}")

#zadanie4
x = int(input("podaj X: "))
y = int(input("podaj Y: "))
if x < 10 and y < 10:
    print("lewy dolny róg")
elif x > 10 and x < 10 and y < 90:
    print("dolna krawędź")
elif x > 90 and y < 10:
    print("prawy dolny róg")
elif x < 10 and y > 10 and y < 90:
    print("lewa krawedz")
elif x > 10 and x < 90 and y > 10 and y < 90:
    print("centrum")
elif x > 90 and y > 10 and y < 90:
    print("prawa krawedz")
elif x < 10 and y > 90:
    print("lewy górny róg")
elif x > 10 and x < 90 and y > 90:
    print("gorna krawedz")
elif x > 90 and y > 90:
    print("prawy górny róg")
else:
    print("poza planszą")



x = int(input("podaj X: "))
y = int(input("podaj Y: "))
if x < 10:
    if y < 10:
        print("dolny lewy róg")
    elif 10 < y < 90:
        print("lewa krawędź")
    elif y > 90:
        print("górny lewy róg")
elif 10 < x < 90:
    if y < 10:
        print("dolna krawędź")
    elif 10 < y < 90:
        print("centrum")
    elif y > 90:
        print("gorna krawedz")
elif x > 90:
    if y < 10:
        print("dolny prawy rog")
    elif 10 < y < 90:
        print("prawa krawedz")
    elif y > 90:
        print("gorny prawy rog")
else:
    print("poza planszą")