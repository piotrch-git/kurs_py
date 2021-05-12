
#1. Napisz funkcję, która policzy n-tą liczbę Fibonacciego iteracyjnie (bez rekurencji)
# to jest iteracyjnie (szybko!!)
#tu jest gorsza złożoność pamięciowa i dobra złożoność czasowa

def fib(n):
    lista = [0,1]
    while len(lista) <= n:
        lista.append(lista[-1] + lista [-2])
    return lista[n]

#podobnie napisałem w p. domowej:
#tu jest dużo lepsza złożoność pamięciowa (tylko 3 zmienne a nie cała lista) i taka sama jak wyżej złożoność czasowa:

def fib2(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return a

print(f"{fib(10000) = }")
print(f"{fib2(10000) = }")