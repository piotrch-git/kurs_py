def fun(x,y,z=2,*args):
    return x+y+z+args[0]
print(fun(2,2,2,1,2,3,4))

def sumuj(*args):
    wynik = 0
    for x in args:
        wynik += x
    return wynik

tupla = (1,2,3)
#print(sumuj(tupla))  to nie zadziala, tuplę trzeba rozpakować:
print(sumuj(*tupla))

print(1,2,3,sep="_")
print([1,2,3],sep="_")
print(*[1,2,3],sep="_") #teraz z * print dostaje 3 argumenty wiec dodaje _


def fun1(text):
    print(text)
def fun2(myFunction, arg1=""):
    print("Pierwszy print")
    myFunction(arg1)
    print("Drugi print")
print("START")
fun2(fun1, "Tekst do funkcji wewnetrznej")
print("KONIEC")


#dobre cwiczenie na zagnieżdżanie

def wybierz(f, lista):
    wynik = []
    for x in lista:
        if f(x):
            wynik.append(x)
    return wynik

def czy_podzelna_przez_2(x):
    return x % 2 == 0

lista_wej = [1,2,3,4]

print(wybierz(czy_podzelna_przez_2,lista_wej))




def czy_podzielna2(z):
    return z % 2 == 0
def wynikowa(f,lista):
    wynik = []
    for x in lista:
        if f(x):
            wynik.append(x)
    return wynik

lista_wej = [1,2,3,4,5,6,7,8]
print(wynikowa(czy_podzielna2,lista_wej))


def czy_podzielna(liczba,dzielnik2):
    return liczba % dzielnik2 == 0

def wywolywana(f, lista_liczb,dzielnik):
    wynik = []
    for i in lista_liczb:
        if f(i,dzielnik):
            wynik.append(i)
    return wynik
lista = [1,2,3,4,5,6,7,8,9,10]
print(wywolywana(czy_podzielna,lista,10))


#### funkcja zwracająca listę będą wynikiem funkcji f() wykonanej dla wszystkich elementow
def zaaplikuj(f,lista):
    #wynik = []
    #for x in lista:
    #    wynik.append(f(x))
    #return wynik
    return [f(x) for x in lista]
def dodaj10(x):
    return x + 10

lista = [1,2,3]
print(zaaplikuj(dodaj10,lista))

print("filter")
"""to jest docstring,  
multilinowy z potrojnym cudzyslowiem. To nie jest komentarz bo interpreter go czyta"""


#filter zwraca te wartosci z listy dla ktorych funkcja zwraca true

def podzielne2(x):
    return x % 2 == 0
print(list(filter(podzielne2,[1,2,3,4])))

#map zwraca wszystkie wyniki z funkcji z wszystkimi argumentami z listy

def potegowanie(x):
    return x ** 2
print(list(map(potegowanie,[1,2,3,4,5])))

#sprytny sposob na zmiane stringa na liste intow za pomoca funkcji map:  (int to jest po prostu funkcja konwertujaca)
napis = "1 2 3 4 5 6"
lista_intow = list(map(int,napis.split()))
print (lista_intow)

#definicja i wywolanie funkcji w jednym:
print(f"{(lambda x: x % 3 == 0)(21) =}")

#skrocona wersja wypisywania podzelnych przez 2 z listy, bez wczesniejszej definicji funkcji
for x in filter(lambda x: x % 2 == 0, [1,2,3,4,5,6]):
    print(x)