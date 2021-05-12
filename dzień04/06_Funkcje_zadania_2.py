from time import time

# zad 1 # Tak jest nieoptymalnie
def czy_jest_pierwsza(n):
    dzielniki=[]
    for i in range (1, n+1):
        if n % i == 0:
            dzielniki.append(i)
    if len(dzielniki) == 2:
        return True
    return False

print(czy_jest_pierwsza(10))

#Lepiej:
# Pomysł #1
def czy_jest_pierwsza_2(n):
    licznik = 0
    for i in range(1, n+1):
        if n % i == 0:
            licznik += 1
            if licznik > 2: # żeby nie znajdował bez sensu wszyskich dzielników, ale to nadal może długo czekać na 3ci dzielnik
                break
    return licznik == 2

#jeszcze Lepiej:
# Pomysł #2

def czy_jest_pierwsza_3(n):
    if n == 1:
        return False    # corner case dla 1ki która nie jest l. pierwszą
    for i in range(2, n):   # Wyłączamy 1 i n z przedziału bo one na pewno nie są wynikami
        if n % i == 0:
            return False # jeżeli liczba dzieli się przez cokolwiek z przedziału [2, n) to na pewno nie jest pierwsza
        return True

przed = time()  # liczba  sekund od północy 1.01.1970
print(czy_jest_pierwsza_3(1000000007))
po = time()
print(f"zajęło to {po-przed} sekund")       #spawdzić dlaczego to się wykonuje tak szybko, powinno być ponad minuta


#jeszcze Lepiej:
# Pomysł #3

def czy_jest_pierwsza_4(n):
    if n == 1:
        return False    # corner case dla 1ki która nie jest l. pierwszą
    for i in range(2, int(n ** 0.5)):   # range musi dostać inta, a pierwiastek będzie floatem. To jest najbardziej optymalny sposób - wystarczy szukać l. pierwszych do pierwiasta n bo dzielniki chodzą parami.
        if n % i == 0:
            return False
        return True

przed = time()  # liczba  sekund od północy 1.01.1970
print(czy_jest_pierwsza_4(1000000007))
po = time()
print(f"zajęło to {po-przed} sekund")

