# Zad. Napisz funkcję czy_podzielna(), która zwróci informację True/False czy n jest podzielne przez k

#def czy_podzielna(n,k):
#    if n % k == 0:
#        return True
#    return False

#print(czy_podzielna(4,3))

# Tak lepiej !!!!!!!!!!!!!!  :
def czy_podzielna(n,k):
    return n % k == 0
if czy_podzielna(10,2):
    print("jest podzielne")


#Zad. Napisz funkcję suma cyfr(x), która zwróci sumę cyft liczby x

def suma_cyfr(n):
    suma = 0
    while n > 0:  # chba tak nie jestem pewien
        suma += n % 10
        n //= 10  # to samo co n = n // 10
    return suma

print(suma_cyfr(123))


#Zad - zliczanie ile razy trzeba dodać wszystkie cyfry w liczbie żeby dostać wynik jednocyfrowy (z pracy domowej)

def ile_razy_suma_cyfr(n):
    licznik = 0
    while n > 9:
        n = suma_cyfr(n)
        print(n)
        licznik += 1
    return licznik
print(ile_razy_suma_cyfr(1234567))


#Zad - napisz funkcję dzielniki(n) która wypisze wszystkie dzielniki liczby całkowitej n
def dzielniki(n):
    dzielniki=[]
    for i in range (1, n+1):
        if n % i == 0:
            dzielniki.append(i)
    return dzielniki

print(dzielniki(6))


# Lepiej tak, za pomocą wyrażenia listowego:

def dzielniki_2(n):
    return [i for i in range(1, n+1) if n % i == 0]

print(dzielniki_2(6))