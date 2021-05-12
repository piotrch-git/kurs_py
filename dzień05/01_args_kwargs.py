#  '*' - unpacking operator

def fun(a,b, *args):  #*args to tupla z wszystkimi argumentami pozycyjnymi które nie zostały przypisane do żadnego innego argumentu
    print(f"{a = }")
    print(f"{b = }")
    print(f"{args = }")

fun(1,2)
fun(1,2,3,4,5,6)

def sumuj(*args): # funkcja do sumowania dowolne wielu argumentów
    wynik = 0
    for x in args:
        wynik += x
    return wynik
print(f"{sumuj(2,2,2)}")


######### to na marginesie
def fun2(a,b, *args):   # funkcja zawsze zwraca jedną warość. Ta wartość może być złożona (np tutaj zwraca tuple)
    return a - b, sum(args)

print(f"{fun2(10,7,2,2,2) = }")
############


tupla = (2,3,4,5,6)
lista = [30,50]
#print(sumuj(tupla))
print(sumuj(*tupla))  # to działa, bo * mówi: przekaż to jako osobne argumenty ('wypakuj' zawartość)
print(sumuj(*tupla, *lista))

print([10,20,30,40], sep="___")
print(*[10,20,30,40], sep="___") # funkcja print tutaj wypakowuje listę, więc wsadza pomiędzy ___

######
# fun(a=2)  #argument z kluczem
# fun(2, 3)  #argumenty pozycyjne

def argumenty_z_kluczem(a,b, *args, **kwargs): #key word argument - **kwargs przyjmuje nadprogramowe argumenty z kluczem (*args przyjmuje nadprogramowe argumenty pozycyjne)
# **kwargs to słownik (dict)
    print(f"{a = }")
    print(f"{b = }")
    print(f"{args = }")
    print(f"{kwargs = }")

argumenty_z_kluczem(b=1, a=2, c=10)
argumenty_z_kluczem(1,2,3,4,5, napis="ala", end="heh", sep="bla", liczba="123")

slownik = {'sep': '___'}
print(*tupla, **slownik)