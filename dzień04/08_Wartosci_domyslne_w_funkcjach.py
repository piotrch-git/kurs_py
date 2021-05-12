def fun (a,b,c=0):  #argumenty z wartościami domyślnymi muszą występować po argumentach bez wartości domyślnych
# c ma wartość domyślną 0 jeżeli nie zostanie podane przy wywołaniu funkcji
    print(f"{a=}")
    print(f"{b=}")
    print(f"{c=}")

fun(2,5,7)
fun(1,2)

def foo(A,B=0,C=0):
    print(f"{A= }")
    print(f"{B= }")
    print(f"{C= }")
#foo(C=15, 99) # nie zadziała bo argumenty z kluczami muszą nastąpić po argumentach pozycyjnych
foo(99, C=15)

#podchwytliwe:
def bar(lista=[]):  # WAŻNE !!!!  Wartości domyślne są tworzone w momencie definiowania funkcji i (raczej) nie chcemy jako wartości ustawiać niczego mutowalnego
#każde kolejne wykonanie funkcji będzie nadpisywało wartość domyślną !!!

    lista.append(123)
    print(lista)
x = [1, 2]
bar(x)
bar()
bar()

#np taka pułapka:
def wypisz(napis=input("podaj napis: ")):
    print(f"{napis=}")

print("teraz wypisujemy")
wypisz()
wypisz("ala ma kota")
wypisz()

# to jest fix:

def wypisz(napis=None):
    if napis is None:
        napis = input("podaj napis")
    print(napis)

print("teraz wypisujemy")
wypisz()
wypisz("ala ma kota")
wypisz()