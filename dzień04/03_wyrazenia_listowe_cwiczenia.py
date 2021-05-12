#zadanie 13

#1
lista = [i / 10 for i in range(10)]
print(lista)

#2
zbior = {(i, i ** 2, i ** 3) for i in range(-10, 11)}
print(zbior)


#3
napisy = {"ala", "ma", "kota", "sedes", "kajak"}
slownik = {napis: len(napis) for napis in napisy} # dla każdego napisu ze zbioru wstawiamy do słownika parę napis-jedo długość
print(slownik)

#wariant z user inputem, ale to jest czarna magia z walrus operatorem
slownik = {(napis := input("daj napis: ")): len(napis) for _ in range(5)}
print(slownik)