def funkcja_hello():        #definicja funkcji bez argumentów
    print("Hello world!")
funkcja_hello()         #wywołanie funkcji

def daj_4():
    print("Uwaga, zwracam 4!")
    return 4    #return zwraca wartość z funkcji i kończy jej działanie
    print("zwróciłem")  # to się nigdy nie wykona bo jest za returnem

x = daj_4()
print(x)

def funkcja_z_argumentem(x):
    #wewnątrz funkcji 'x' traktujemy jako zdefiniowany
    print(f"Dostałem argument {x}")

funkcja_z_argumentem(12)
funkcja_z_argumentem("qwertz")

def funkcja_z_dwoma_argumentami(x, y):
    print(f"Dostałem argumenty {x=}, {y=}")
funkcja_z_dwoma_argumentami(3, "abc")

funkcja_z_dwoma_argumentami([i ** 2 for i in range(10)], {})


def zmieniacz_listy(x):     #ta funkcja dodaje wartość do przekazanej listy
    x.append(1111111111111111111)

lista = []
zmieniacz_listy(lista)
print(lista)

#########################
#zadanie - funkcja liczaca wartość bezwzględną

def wartosc_bezwzgledna(x):
    if x < 0:
        return -x
    return x            #else nie jest potrzebny bo return zawsze kończy funkcję

print(f"{wartosc_bezwzgledna(-7)=}")

############
def f(x):
    return 2 * x + 3
print(f"{f(3)=}")
