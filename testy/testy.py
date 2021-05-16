def fib(n):
    lista = [0,1]
    while len(lista) < n:
        lista.append(lista [-1] + lista [-2])
    print(lista)

fib(100)


def calc(*args):
    sum=0
    for i in args:
        sum += i
    return sum

print(calc(1,2,3))


