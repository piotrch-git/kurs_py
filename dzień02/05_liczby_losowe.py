#import tak:

#import math
#print(math.pi)

#albo tak:
#from math import pi
#print(pi)

from random import randint
x = randint(1, 6)
print(f"rzut kostką: {x}")


#zadanie
print(f"zadanie - zgadywanka wylosowanej liczby")

liczba = randint (1, 1000000)
print(f"wylosowano {liczba}")

los = 0
while los != liczba:
    los = int(input("zgadnij liczbę"))
    if los > liczba:
        print("za dużo, próbuj dalej")
    elif los < liczba:                      #lepszy elif niż drugi if bo ify się zawsze sprawdzają a elif się nie sprawdza jeżeli pierwszy if przejdzie
        print("za mało, próbuj dalej")
print("brawo!")


# 2gi sposób rozwiązania

wylosowana = randint(1,10)
while True:
    zgadnieta = int(input("zganij liczbę: "))
    if zgadnieta == wylosowana:
        break
    if zgadnieta > wylosowana:
        print("za dużo!")
    else:
        print("za mało!")
print("hura")
