#chcemy żeby to zwróciło 1 za pierwszym razem, 2 za drugim i 3 za trzecim
def gen():
    yield 1             #jeżeli w funkcji jest co najmniej jeden 'yield' to ta funkcja zwraca generator
    yield 2
    yield 3

g = gen()
it = iter(g)
print(next(it))
print(next(it))
print(next(it))

def counter(n):
    for i in range(n):
        yield i

for i in counter(5):
    print(f"{i =}")


#zadanie:

def vowels(napis):
    for i in napis:
        if i.lower() in 'aeiouy':
            yield i


for i in vowels("ala ma kota"):
    print(i)

#Zadanie: napisz generator który będzie zwracał (yield) kolejne liczby pierwsze




def czy_jest_pierwsza(n):
    if n == 1:
        return False    # corner case dla 1ki która nie jest l. pierwszą
    for i in range(2, int(n ** 0.5) + 1):   # range musi dostać inta, a pierwiastek będzie floatem. To jest najbardziej optymalny sposób - wystarczy szukać l. pierwszych do pierwiasta n bo dzielniki chodzą parami.
        if n % i == 0:
            return False
    return True




def pierwsze():
    i = 1
    while True:
        if czy_jest_pierwsza(i):
            yield i
        i+= 1

for i, p in enumerate(pierwsze(), 1):   #enumerate to generator par: 1- element z iterowalnego zbioru, 2-licznik
    print(i, p)