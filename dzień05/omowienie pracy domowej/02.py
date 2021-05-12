#2. Napisz funkcję, która sprawdzi czy podana liczba jest liczbą doskonałą.
#https://pl.wikipedia.org/wiki/Liczba_doskona%C5%82a
#{\displaystyle 6=3+2+1.} Następną jest 28 ponieważ 28=14+7+4+2+1

def doskonala(n):
    suma=0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma == n
print(f"{doskonala(6) = }")